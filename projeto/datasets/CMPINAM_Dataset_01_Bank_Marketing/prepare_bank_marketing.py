"""Prepara o Bank Marketing para uso didático em CMPINAM.

Fonte: UCI Machine Learning Repository, dataset 222.
Estratégia: versão completa enriquecida, remoção de duplicatas exatas,
exclusão de duration e divisão estratificada 80/20.
"""

from pathlib import Path
from io import BytesIO
import json
import urllib.request
import zipfile

import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT
DOWNLOAD_URL = "https://archive.ics.uci.edu/static/public/222/bank%2Bmarketing.zip"
RANDOM_STATE = 42
TEST_SIZE = 0.20

RENAME_COLUMNS = {
    "emp.var.rate": "emp_var_rate",
    "cons.price.idx": "cons_price_idx",
    "cons.conf.idx": "cons_conf_idx",
    "euribor3m": "euribor_3m",
    "nr.employed": "nr_employed",
    "y": "subscribed",
}


def class_summary(frame: pd.DataFrame) -> dict:
    counts = frame["subscribed"].value_counts().sort_index()
    return {
        "rows": int(len(frame)),
        "no": int(counts.get("no", 0)),
        "yes": int(counts.get("yes", 0)),
        "yes_rate": round(float((frame["subscribed"] == "yes").mean()), 6),
    }


def load_source() -> pd.DataFrame:
    """Baixa e lê bank-additional-full.csv a partir do pacote oficial."""
    with urllib.request.urlopen(DOWNLOAD_URL) as response:
        outer_bytes = response.read()
    with zipfile.ZipFile(BytesIO(outer_bytes)) as outer:
        additional_bytes = outer.read("bank-additional.zip")
    with zipfile.ZipFile(BytesIO(additional_bytes)) as additional:
        csv_bytes = additional.read("bank-additional/bank-additional-full.csv")
    return pd.read_csv(BytesIO(csv_bytes), sep=";")


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)

    source = load_source()
    duplicate_rows = int(source.duplicated().sum())

    curated = (
        source.drop_duplicates()
        .drop(columns=["duration"])
        .rename(columns=RENAME_COLUMNS)
        .reset_index(drop=True)
    )

    features = curated.drop(columns=["subscribed"])
    groups = pd.util.hash_pandas_object(features, index=False).astype(str)
    splitter = StratifiedGroupKFold(
        n_splits=5,
        shuffle=True,
        random_state=RANDOM_STATE,
    )
    train_index, test_index = next(
        splitter.split(features, curated["subscribed"], groups)
    )
    train = curated.iloc[train_index]
    test = curated.iloc[test_index]
    train = train.reset_index(drop=True)
    test = test.reset_index(drop=True)

    train_path = OUTPUT / "bank_marketing_train.csv"
    test_path = OUTPUT / "bank_marketing_test.csv"
    train.to_csv(train_path, index=False, encoding="utf-8")
    test.to_csv(test_path, index=False, encoding="utf-8")

    metadata = {
        "dataset": "Bank Marketing",
        "source_url": "https://archive.ics.uci.edu/dataset/222/bank+marketing",
        "source_file": "bank-additional-full.csv",
        "source_rows": int(len(source)),
        "source_columns_including_target": int(source.shape[1]),
        "exact_duplicate_rows_removed": duplicate_rows,
        "excluded_columns": {
            "duration": (
                "A duração só é conhecida após a ligação e deve ser excluída "
                "de um modelo realista de decisão pré-contato."
            )
        },
        "curated_rows": int(len(curated)),
        "curated_columns_including_target": int(curated.shape[1]),
        "target": "subscribed",
        "split": {
            "method": "stratified group holdout using one of five folds",
            "train_fraction": 0.80,
            "test_fraction": TEST_SIZE,
            "random_state": RANDOM_STATE,
            "stratification_column": "subscribed",
            "grouping": "hash of all feature columns after excluding duration",
        },
        "full": class_summary(curated),
        "train": class_summary(train),
        "test": class_summary(test),
        "semantic_missing_values": "unknown",
        "license": "CC BY 4.0",
        "doi": "10.24432/C5K306",
    }
    (OUTPUT / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
