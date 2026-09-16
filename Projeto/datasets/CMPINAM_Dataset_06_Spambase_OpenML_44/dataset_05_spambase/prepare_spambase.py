"""Prepara o dataset Spambase (OpenML 44 / UCI 94) para CMPINAM."""

from io import StringIO
from pathlib import Path
import json
import urllib.request

import pandas as pd
from scipy.io import arff
from sklearn.model_selection import StratifiedGroupKFold


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT
DOWNLOAD_URL = "https://openml.org/data/v1/download/44/spambase.arff"
RANDOM_STATE = 42

RENAME_COLUMNS = {
    "char_freq_%3B": "char_freq_semicolon",
    "char_freq_%28": "char_freq_left_parenthesis",
    "char_freq_%5B": "char_freq_left_bracket",
    "char_freq_%21": "char_freq_exclamation",
    "char_freq_%24": "char_freq_dollar",
    "char_freq_%23": "char_freq_hash",
    "class": "is_spam",
}


def load_source() -> pd.DataFrame:
    with urllib.request.urlopen(DOWNLOAD_URL) as response:
        arff_text = response.read().decode("utf-8")
    raw, _ = arff.loadarff(StringIO(arff_text))
    source = pd.DataFrame(raw)
    source["class"] = source["class"].str.decode("utf-8")
    return source


def class_summary(frame: pd.DataFrame) -> dict:
    counts = frame["is_spam"].value_counts().sort_index()
    return {
        "rows": int(len(frame)),
        "no": int(counts.get("no", 0)),
        "yes": int(counts.get("yes", 0)),
        "spam_rate": round(float((frame["is_spam"] == "yes").mean()), 6),
    }


def main() -> None:
    source = load_source()
    curated = source.rename(columns=RENAME_COLUMNS).copy()
    curated["is_spam"] = curated["is_spam"].map({"0": "no", "1": "yes"})

    features = curated.drop(columns=["is_spam"])
    groups = pd.util.hash_pandas_object(features, index=False).astype(str)
    splitter = StratifiedGroupKFold(
        n_splits=5,
        shuffle=True,
        random_state=RANDOM_STATE,
    )
    train_index, test_index = next(
        splitter.split(features, curated["is_spam"], groups)
    )
    train = curated.iloc[train_index].reset_index(drop=True)
    test = curated.iloc[test_index].reset_index(drop=True)

    train.to_csv(OUTPUT / "spambase_train.csv", index=False, encoding="utf-8")
    test.to_csv(OUTPUT / "spambase_test.csv", index=False, encoding="utf-8")

    grouped = source.groupby(
        [column for column in source if column != "class"], dropna=False
    )["class"].nunique()
    metadata = {
        "dataset": "Spambase",
        "openml_dataset_id": 44,
        "uci_dataset_id": 94,
        "source_urls": {
            "openml": "https://www.openml.org/d/44",
            "uci": "https://archive.ics.uci.edu/dataset/94/spambase",
        },
        "download_url": DOWNLOAD_URL,
        "source_file": "spambase.arff",
        "source_rows": int(len(source)),
        "source_features": 57,
        "source_exact_duplicate_rows": int(source.duplicated().sum()),
        "source_duplicate_feature_vectors": int(
            source.drop(columns=["class"]).duplicated().sum()
        ),
        "feature_profiles_with_conflicting_labels": int((grouped > 1).sum()),
        "duplicate_policy": (
            "Todos os registros foram mantidos. Perfis de atributos idênticos "
            "foram mantidos no mesmo lado da divisão."
        ),
        "source_order_note": (
            "O ARFF está ordenado por classe: 1813 spams seguidos por 2788 não spams."
        ),
        "curated_rows": int(len(curated)),
        "curated_columns_including_target": int(curated.shape[1]),
        "target": "is_spam",
        "split": {
            "method": "stratified group holdout using one of five folds",
            "train_fraction_approximate": 0.80,
            "test_fraction_approximate": 0.20,
            "random_state": RANDOM_STATE,
            "stratification_column": "is_spam",
            "grouping": "hash of all 57 feature columns",
        },
        "full": class_summary(curated),
        "train": class_summary(train),
        "test": class_summary(test),
        "missing_values_in_openml_arff": int(curated.isna().sum().sum()),
        "license": "CC BY 4.0 according to the current UCI repository page",
        "uci_doi": "10.24432/C53G6X",
        "openml_file_id": 44,
        "openml_md5": "d9ace01aeac3461e326a8e1b2d53fd84",
    }
    (OUTPUT / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
