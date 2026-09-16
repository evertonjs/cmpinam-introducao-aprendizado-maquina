#!/usr/bin/env python3
"""Baseline simples para a divisão fornecida, sem usar o conjunto de teste no ajuste."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    classification_report,
    log_loss,
    roc_auc_score,
)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


DATA_DIR = Path(__file__).resolve().parent
TARGET = "is_pulsar"

train = pd.read_csv(DATA_DIR / "train.csv")
test = pd.read_csv(DATA_DIR / "test.csv")

X_train = train.drop(columns=TARGET)
y_train = train[TARGET]
X_test = test.drop(columns=TARGET)
y_test = test[TARGET]

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=3000, random_state=42),
)
model.fit(X_train, y_train)

probability = model.predict_proba(X_test)[:, 1]
prediction = (probability >= 0.5).astype(int)

print(f"Log loss: {log_loss(y_test, probability):.4f}")
print(f"ROC-AUC: {roc_auc_score(y_test, probability):.4f}")
print(f"PR-AUC: {average_precision_score(y_test, probability):.4f}")
print(f"Acurácia: {accuracy_score(y_test, prediction):.4f}")
print(classification_report(y_test, prediction, target_names=["não pulsar", "pulsar"]))
