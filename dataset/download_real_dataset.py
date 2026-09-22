"""
Download the SMS Spam Collection dataset from UCI.
"""

import os
import urllib.request
import zipfile

DATASET_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
OUTPUT_DIR = os.path.dirname(__file__)
ZIP_PATH = os.path.join(OUTPUT_DIR, "smsspamcollection.zip")
CSV_PATH = os.path.join(OUTPUT_DIR, "spam.csv")


def download_and_extract():
    print(f"Downloading dataset from {DATASET_URL}...")
    urllib.request.urlretrieve(DATASET_URL, ZIP_PATH)
    print(f"Downloaded zip to {ZIP_PATH}")

    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(OUTPUT_DIR)
    print("Extracted archive")

    # The archive contains SMSSpamCollection, convert to CSV format
    raw_path = os.path.join(OUTPUT_DIR, "SMSSpamCollection")
    if not os.path.exists(raw_path):
        raise FileNotFoundError("Expected SMSSpamCollection file inside the archive")

    with open(raw_path, "r", encoding="utf-8") as raw_file, open(CSV_PATH, "w", encoding="utf-8") as csv_file:
        csv_file.write("label,message\n")
        for line in raw_file:
            label, text = line.strip().split("\t", 1)
            text = text.replace(",", " ")
            csv_file.write(f"{label},{text}\n")

    print(f"Created CSV dataset at {CSV_PATH}")


if __name__ == "__main__":
    download_and_extract()
