#!/usr/bin/env python3
"""Baixa o HTRU2 original e recria a curadoria CMPINAM de forma determinística."""

from __future__ import annotations

import io
import json
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


SOURCE_URL = "https://archive.ics.uci.edu/static/public/372/htru2.zip"
RANDOM_SEED = 42
TEST_SIZE = 0.20

COLUMNS = [
    "mean_integrated_profile",
    "std_integrated_profile",
    "excess_kurtosis_integrated_profile",
    "skewness_integrated_profile",
    "mean_dm_snr_curve",
    "std_dm_snr_curve",
    "excess_kurtosis_dm_snr_curve",
    "skewness_dm_snr_curve",
    "is_pulsar",
]


def load_source() -> pd.DataFrame:
    with urllib.request.urlopen(SOURCE_URL, timeout=120) as response:
        archive_bytes = response.read()
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
        with archive.open("HTRU_2.csv") as source:
            return pd.read_csv(source, header=None, names=COLUMNS)


def main() -> None:
    output_dir = Path(__file__).resolve().parent
    data = load_source()

    train, test = train_test_split(
        data,
        test_size=TEST_SIZE,
        random_state=RANDOM_SEED,
        stratify=data["is_pulsar"],
        shuffle=True,
    )
    train = train.reset_index(drop=True)
    test = test.reset_index(drop=True)

    train.to_csv(output_dir / "train.csv", index=False)
    test.to_csv(output_dir / "test.csv", index=False)

    split_info = {
        "source_url": SOURCE_URL,
        "source_instances": int(len(data)),
        "source_features": 8,
        "target": "is_pulsar",
        "test_size": TEST_SIZE,
        "random_seed": RANDOM_SEED,
        "stratified_by": "is_pulsar",
        "train_rows": int(len(train)),
        "test_rows": int(len(test)),
        "train_class_counts": {
            str(k): int(v) for k, v in train["is_pulsar"].value_counts().sort_index().items()
        },
        "test_class_counts": {
            str(k): int(v) for k, v in test["is_pulsar"].value_counts().sort_index().items()
        },
    }
    (output_dir / "split_info.json").write_text(
        json.dumps(split_info, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
