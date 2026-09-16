#!/usr/bin/env python3
"""Prepara a versão didática do Adult a partir dos arquivos oficiais da UCI."""

from pathlib import Path
import json
import io
import urllib.request
import zipfile
import pandas as pd

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source_raw"
DOWNLOAD_URL = "https://archive.ics.uci.edu/static/public/2/adult.zip"

SOURCE_COLUMNS = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "hours_per_week", "native_country",
    "income",
]

OUTPUT_COLUMNS = [
    "age", "workclass", "education", "marital_status", "occupation",
    "relationship", "race", "sex", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income_over_50k",
]


def ensure_source() -> None:
    """Baixa a cópia oficial somente quando os arquivos brutos não existem."""
    if (SOURCE / "adult.data").exists() and (SOURCE / "adult.test").exists():
        return
    SOURCE.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(DOWNLOAD_URL) as response:
        payload = response.read()
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        archive.extract("adult.data", SOURCE)
        archive.extract("adult.test", SOURCE)


def read_source(path: Path, *, test: bool = False) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        names=SOURCE_COLUMNS,
        skiprows=1 if test else 0,
        skipinitialspace=True,
        na_values="?",
    )
    if test:
        df["income"] = df["income"].str.rstrip(".")
    df["income_over_50k"] = df["income"].map({"<=50K": 0, ">50K": 1})
    if df["income_over_50k"].isna().any():
        raise ValueError(f"Rótulo inesperado em {path}")
    return df[OUTPUT_COLUMNS]


def main() -> None:
    ensure_source()
    train = read_source(SOURCE / "adult.data")
    test = read_source(SOURCE / "adult.test", test=True)
    train.to_csv(ROOT / "train.csv", index=False)
    test.to_csv(ROOT / "test.csv", index=False)

    info = {
        "dataset": "Adult (Census Income)",
        "source": "https://archive.ics.uci.edu/dataset/2/adult",
        "source_doi": "https://doi.org/10.24432/C5XW20",
        "split_strategy": "Divisao oficial da UCI preservada: adult.data / adult.test",
        "random_seed": None,
        "target": "income_over_50k",
        "target_mapping": {"<=50K": 0, ">50K": 1},
        "train_rows": len(train),
        "test_rows": len(test),
        "predictor_columns": 12,
        "excluded_source_columns": {
            "fnlwgt": "Peso amostral do censo; nao e uma caracteristica pessoal comum para predicao.",
            "education_num": "Codificacao ordinal redundante com education.",
        },
        "missing_values": {
            "train": train.isna().sum()[lambda s: s > 0].to_dict(),
            "test": test.isna().sum()[lambda s: s > 0].to_dict(),
        },
        "class_counts": {
            "train": train["income_over_50k"].value_counts().sort_index().to_dict(),
            "test": test["income_over_50k"].value_counts().sort_index().to_dict(),
        },
    }
    (ROOT / "split_info.json").write_text(
        json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
