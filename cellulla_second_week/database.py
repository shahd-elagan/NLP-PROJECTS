import pandas as pd
import os

DB_FILE = "user_database.csv"


def save_to_db(text, label):

    new_row = pd.DataFrame({
        "input_text": [text],
        "classification": [label]
    })

    if os.path.exists(DB_FILE):
        df = pd.read_csv(DB_FILE)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row

    df.to_csv(DB_FILE, index=False)


def load_db():

    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    else:
        return pd.DataFrame(columns=["input_text", "classification"])