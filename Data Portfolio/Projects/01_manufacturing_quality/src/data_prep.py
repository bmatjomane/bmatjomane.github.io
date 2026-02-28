from pathlib import Path
import pandas as pd

RAW = Path(__file__).resolve().parents[1] / "data" / "raw"
PROCESSED = Path(__file__).resolve().parents[1] / "data" / "processed"

def load_raw_csv(filename: str) -> pd.DataFrame:
    path = RAW / filename
    return pd.read_csv(path)

def save_processed(df: pd.DataFrame, filename: str) -> None:
    PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED / filename, index=False)