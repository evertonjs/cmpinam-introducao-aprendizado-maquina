"""Prepara o Online Shoppers Purchasing Intention para CMPINAM."""

from io import BytesIO
from pathlib import Path
import json
import urllib.request
import zipfile

import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT
DOWNLOAD_URL = (
    "https://archive.ics.uci.edu/static/public/468/"
    "online%2Bshoppers%2Bpurchasing%2Bintention%2Bdataset.zip"
)
RANDOM_STATE = 42

RENAME_COLUMNS = {
    "Administrative": "administrative_pages",
    "Administrative_Duration": "administrative_duration",
    "Informational": "informational_pages",
    "Informational_Duration": "informational_duration",
    "ProductRelated": "product_related_pages",
    "ProductRelated_Duration": "product_related_duration",
    "BounceRates": "bounce_rate",
    "ExitRates": "exit_rate",
    "PageValues": "page_value",
    "SpecialDay": "special_day",
    "Month": "month",
    "OperatingSystems": "operating_system",
    "Browser": "browser",
    "Region": "region",
    "TrafficType": "traffic_type",
    "VisitorType": "visitor_type",
    "Weekend": "weekend",
    "Revenue": "purchase",
}

MONTHS = {
    "Feb": "feb",
    "Mar": "mar",
    "May": "may",
    "June": "jun",
    "Jul": "jul",
    "Aug": "aug",
    "Sep": "sep",
    "Oct": "oct",
    "Nov": "nov",
    "Dec": "dec",
}

VISITOR_TYPES = {
    "New_Visitor": "new",
    "Returning_Visitor": "returning",
    "Other": "other",
}


def load_source() -> pd.DataFrame:
    with urllib.request.urlopen(DOWNLOAD_URL) as response:
        archive_bytes = response.read()
    with zipfile.ZipFile(BytesIO(archive_bytes)) as archive:
        csv_bytes = archive.read("online_shoppers_intention.csv")
    return pd.read_csv(BytesIO(csv_bytes))


def class_summary(frame: pd.DataFrame) -> dict:
    counts = frame["purchase"].value_counts().sort_index()
    return {
        "rows": int(len(frame)),
        "no": int(counts.get("no", 0)),
        "yes": int(counts.get("yes", 0)),
        "yes_rate": round(float((frame["purchase"] == "yes").mean()), 6),
    }


def main() -> None:
    source = load_source()
    curated = source.rename(columns=RENAME_COLUMNS).copy()

    curated["month"] = curated["month"].map(MONTHS)
    curated["visitor_type"] = curated["visitor_type"].map(VISITOR_TYPES)
    curated["weekend"] = curated["weekend"].map({True: "yes", False: "no"})
    curated["purchase"] = curated["purchase"].map({True: "yes", False: "no"})

    for column, prefix in {
        "operating_system": "os",
        "browser": "browser",
        "region": "region",
        "traffic_type": "traffic",
    }.items():
        curated[column] = prefix + "_" + curated[column].astype(str)

    features = curated.drop(columns=["purchase"])
    groups = pd.util.hash_pandas_object(features, index=False).astype(str)
    splitter = StratifiedGroupKFold(
        n_splits=5,
        shuffle=True,
        random_state=RANDOM_STATE,
    )
    train_index, test_index = next(
        splitter.split(features, curated["purchase"], groups)
    )
    train = curated.iloc[train_index].reset_index(drop=True)
    test = curated.iloc[test_index].reset_index(drop=True)

    train.to_csv(OUTPUT / "online_shoppers_train.csv", index=False, encoding="utf-8")
    test.to_csv(OUTPUT / "online_shoppers_test.csv", index=False, encoding="utf-8")

    metadata = {
        "dataset": "Online Shoppers Purchasing Intention Dataset",
        "source_url": (
            "https://archive.ics.uci.edu/dataset/468/"
            "online+shoppers+purchasing+intention+dataset"
        ),
        "source_file": "online_shoppers_intention.csv",
        "source_rows": int(len(source)),
        "source_columns_including_target": int(source.shape[1]),
        "source_exact_duplicate_rows": int(source.duplicated().sum()),
        "duplicate_policy": (
            "Mantidas: a documentação informa que cada sessão pertence a um "
            "usuário diferente. Perfis idênticos foram mantidos no mesmo conjunto."
        ),
        "curated_rows": int(len(curated)),
        "curated_columns_including_target": int(curated.shape[1]),
        "target": "purchase",
        "split": {
            "method": "stratified group holdout using one of five folds",
            "train_fraction_approximate": 0.80,
            "test_fraction_approximate": 0.20,
            "random_state": RANDOM_STATE,
            "stratification_column": "purchase",
            "grouping": "hash of all feature columns",
        },
        "full": class_summary(curated),
        "train": class_summary(train),
        "test": class_summary(test),
        "missing_values": 0,
        "license": "CC BY 4.0",
        "doi": "10.24432/C5F88Q",
    }
    (OUTPUT / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
