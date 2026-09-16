#!/usr/bin/env python3
"""Baseline reprodutível e auditoria descritiva por grupos."""

from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, average_precision_score, f1_score, log_loss,
    precision_score, recall_score, roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parent
TARGET = "income_over_50k"
SENSITIVE = ["race", "sex"]


def group_audit(y_true, y_pred, group):
    rows = []
    frame = pd.DataFrame({"y": y_true, "pred": y_pred, "group": group}).dropna()
    for value, part in frame.groupby("group", observed=True):
        y = part["y"].to_numpy()
        pred = part["pred"].to_numpy()
        positives = y == 1
        negatives = y == 0
        rows.append({
            "group": str(value),
            "rows": int(len(part)),
            "positive_prediction_rate": float(pred.mean()),
            "recall": float((pred[positives] == 1).mean()) if positives.any() else None,
            "false_positive_rate": float((pred[negatives] == 1).mean()) if negatives.any() else None,
        })
    return rows


def main():
    train = pd.read_csv(ROOT / "train.csv")
    test = pd.read_csv(ROOT / "test.csv")

    # race e sex ficam disponíveis para auditoria, mas não entram no modelo.
    features = [c for c in train.columns if c not in [TARGET, *SENSITIVE]]
    numeric = train[features].select_dtypes(include="number").columns.tolist()
    categorical = [c for c in features if c not in numeric]

    prep = ColumnTransformer([
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
        ]), numeric),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]), categorical),
    ])
    model = Pipeline([
        ("preprocess", prep),
        ("classifier", LogisticRegression(max_iter=3000, random_state=42)),
    ])
    model.fit(train[features], train[TARGET])
    proba = model.predict_proba(test[features])[:, 1]
    pred = (proba >= 0.5).astype(int)
    y = test[TARGET].to_numpy()

    results = {
        "model": "LogisticRegression + imputacao + padronizacao + one-hot",
        "excluded_from_model": SENSITIVE,
        "threshold": 0.5,
        "metrics": {
            "accuracy": accuracy_score(y, pred),
            "precision": precision_score(y, pred, zero_division=0),
            "recall": recall_score(y, pred, zero_division=0),
            "f1": f1_score(y, pred, zero_division=0),
            "roc_auc": roc_auc_score(y, proba),
            "pr_auc": average_precision_score(y, proba),
            "log_loss": log_loss(y, proba),
        },
        "group_audit": {
            col: group_audit(y, pred, test[col].to_numpy()) for col in SENSITIVE
        },
    }
    (ROOT / "baseline_results.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
