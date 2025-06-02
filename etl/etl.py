import os
import pandas as pd
from pymongo import MongoClient

MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME", "root")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "password")
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_DB   = os.getenv("MONGO_DB", "healthcare")

uri = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:27017/"
client = MongoClient(uri)
db = client[MONGO_DB]
collection = db["patients"]

file_path = "/app/data/healthcare_dataset-20250506.csv"
df = pd.read_csv(file_path, sep=";")

df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

null_counts = df.isnull().sum()
print("Null counts per column:")
print(null_counts)

df["date_of_admission"] = pd.to_datetime(
    df["date_of_admission"], dayfirst=True, errors="coerce"
)
df["discharge_date"] = pd.to_datetime(
    df["discharge_date"], dayfirst=True, errors="coerce"
)


df.fillna("", inplace=True)

documents = df.to_dict(orient="records")
collection.insert_many(documents)

print(f"{len(documents)} documents inserted into MongoDB.")
