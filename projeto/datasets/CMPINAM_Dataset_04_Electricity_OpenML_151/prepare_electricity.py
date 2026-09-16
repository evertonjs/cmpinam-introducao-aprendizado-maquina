"""Prepara o dataset Electricity (OpenML 151) para uso em CMPINAM."""

from io import StringIO
from pathlib import Path
import json
import urllib.request

import pandas as pd
from scipy.io import arff


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT
DOWNLOAD_URL = "https://openml.org/data/v1/download/2419/electricity.arff"
TRAIN_ROWS = 36_240  # 755 dias completos, com 48 períodos por dia

RENAME_COLUMNS = {
    "date": "date_normalized",
    "day": "day",
    "nswprice": "nsw_price_normalized",
    "nswdemand": "nsw_demand_normalized",
    "vicprice": "vic_price_normalized",
    "vicdemand": "vic_demand_normalized",
    "transfer": "transfer_normalized",
    "class": "nsw_price_class",
}


def load_source() -> pd.DataFrame:
    with urllib.request.urlopen(DOWNLOAD_URL) as response:
        arff_text = response.read().decode("utf-8")
    raw, _ = arff.loadarff(StringIO(arff_text))
    source = pd.DataFrame(raw)
    source["day"] = source["day"].str.decode("utf-8")
    source["class"] = source["class"].str.decode("utf-8")
    return source


def class_summary(frame: pd.DataFrame) -> dict:
    counts = frame["nsw_price_class"].value_counts().sort_index()
    return {
        "rows": int(len(frame)),
        "down": int(counts.get("down", 0)),
        "up": int(counts.get("up", 0)),
        "down_rate": round(
            float((frame["nsw_price_class"] == "down").mean()), 6
        ),
        "up_rate": round(float((frame["nsw_price_class"] == "up").mean()), 6),
    }


def main() -> None:
    source = load_source()
    curated = source.rename(columns=RENAME_COLUMNS).copy()

    curated["day"] = "day_" + curated["day"].astype(str)
    curated["period_index"] = (source["period"] * 47).round().astype(int) + 1
    curated = curated.drop(columns=["period"])
    curated["nsw_price_class"] = curated["nsw_price_class"].str.lower()

    ordered_columns = [
        "date_normalized",
        "day",
        "period_index",
        "nsw_price_normalized",
        "nsw_demand_normalized",
        "vic_price_normalized",
        "vic_demand_normalized",
        "transfer_normalized",
        "nsw_price_class",
    ]
    curated = curated[ordered_columns]

    train = curated.iloc[:TRAIN_ROWS].reset_index(drop=True)
    test = curated.iloc[TRAIN_ROWS:].reset_index(drop=True)

    train.to_csv(OUTPUT / "electricity_train.csv", index=False, encoding="utf-8")
    test.to_csv(OUTPUT / "electricity_test.csv", index=False, encoding="utf-8")

    date_decreases = int((source["date"].diff() < 0).sum())
    metadata = {
        "dataset": "Electricity",
        "openml_dataset_id": 151,
        "source_url": "https://www.openml.org/d/151",
        "download_url": DOWNLOAD_URL,
        "source_file": "electricity.arff",
        "source_rows": int(len(source)),
        "source_columns_including_target": int(source.shape[1]),
        "source_exact_duplicate_rows": int(source.duplicated().sum()),
        "curated_rows": int(len(curated)),
        "curated_columns_including_target": int(curated.shape[1]),
        "target": "nsw_price_class",
        "split": {
            "method": "sequential holdout by original ARFF row order",
            "train_rows": int(len(train)),
            "test_rows": int(len(test)),
            "train_complete_days": int(len(train) / 48),
            "test_complete_days": int(len(test) / 48),
            "shuffle": False,
            "stratified": False,
        },
        "full": class_summary(curated),
        "train": class_summary(train),
        "test": class_summary(test),
        "missing_values": int(curated.isna().sum().sum()),
        "normalized_date_decreases_in_original_order": date_decreases,
        "date_note": (
            "A sequência das linhas foi preservada. O atributo de data normalizado "
            "possui cinco reduções e não permite reconstruir datas civis com segurança."
        ),
        "license": "Public (as listed by OpenML)",
        "openml_file_id": 2419,
        "openml_md5": "8ca97867d960ae029ae3a9ac2c923d34",
    }
    (OUTPUT / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
