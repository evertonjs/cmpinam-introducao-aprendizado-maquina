"""Prepara o Rice (Cammeo and Osmancik) para uso em CMPINAM."""

from io import BytesIO, StringIO
from pathlib import Path
import json
import urllib.request
import zipfile

import pandas as pd
from scipy.io import arff
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT
DOWNLOAD_URL = (
    "https://archive.ics.uci.edu/static/public/545/"
    "rice%2Bcammeo%2Band%2Bosmancik.zip"
)
RANDOM_STATE = 42
TEST_SIZE = 0.20

RENAME_COLUMNS = {
    "Area": "area",
    "Perimeter": "perimeter",
    "Major_Axis_Length": "major_axis_length",
    "Minor_Axis_Length": "minor_axis_length",
    "Eccentricity": "eccentricity",
    "Convex_Area": "convex_area",
    "Extent": "extent",
    "Class": "variety",
}


def load_source() -> pd.DataFrame:
    with urllib.request.urlopen(DOWNLOAD_URL) as response:
        archive_bytes = response.read()
    with zipfile.ZipFile(BytesIO(archive_bytes)) as archive:
        arff_bytes = archive.read("Rice_Cammeo_Osmancik.arff")
    raw, _ = arff.loadarff(StringIO(arff_bytes.decode("utf-8")))
    source = pd.DataFrame(raw)
    source["Class"] = source["Class"].str.decode("utf-8")
    return source


def class_summary(frame: pd.DataFrame) -> dict:
    counts = frame["variety"].value_counts().sort_index()
    return {
        "rows": int(len(frame)),
        "cammeo": int(counts.get("cammeo", 0)),
        "osmancik": int(counts.get("osmancik", 0)),
        "cammeo_rate": round(float((frame["variety"] == "cammeo").mean()), 6),
        "osmancik_rate": round(
            float((frame["variety"] == "osmancik").mean()), 6
        ),
    }


def main() -> None:
    source = load_source()
    curated = source.rename(columns=RENAME_COLUMNS).copy()
    curated["area"] = curated["area"].astype(int)
    curated["convex_area"] = curated["convex_area"].astype(int)
    continuous_columns = [
        "perimeter",
        "major_axis_length",
        "minor_axis_length",
        "eccentricity",
        "extent",
    ]
    curated[continuous_columns] = curated[continuous_columns].round(6)
    curated["variety"] = curated["variety"].str.lower()

    train, test = train_test_split(
        curated,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=curated["variety"],
    )
    train = train.reset_index(drop=True)
    test = test.reset_index(drop=True)

    train.to_csv(OUTPUT / "rice_train.csv", index=False, encoding="utf-8")
    test.to_csv(OUTPUT / "rice_test.csv", index=False, encoding="utf-8")

    metadata = {
        "dataset": "Rice (Cammeo and Osmancik)",
        "source_url": (
            "https://archive.ics.uci.edu/dataset/545/"
            "rice+cammeo+and+osmancik"
        ),
        "source_file": "Rice_Cammeo_Osmancik.arff",
        "source_rows": int(len(source)),
        "source_columns_including_target": int(source.shape[1]),
        "source_exact_duplicate_rows": int(source.duplicated().sum()),
        "curated_rows": int(len(curated)),
        "curated_columns_including_target": int(curated.shape[1]),
        "target": "variety",
        "split": {
            "method": "random stratified holdout",
            "train_fraction": 0.80,
            "test_fraction": TEST_SIZE,
            "random_state": RANDOM_STATE,
            "stratification_column": "variety",
        },
        "full": class_summary(curated),
        "train": class_summary(train),
        "test": class_summary(test),
        "missing_values": int(curated.isna().sum().sum()),
        "license": "CC BY 4.0",
        "doi": "10.24432/C5MW4Z",
    }
    (OUTPUT / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
