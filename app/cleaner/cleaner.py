import pandas as pd
import os
import json


def clean_scraped_data(file_path="output.json"):
    with open(file_path,"r") as f:
        data=json.load(f)


    df=pd.DataFrame(data)
    df.drop_duplicates(subset=["url"], inplace=True)
    df.dropna(subset=["title", "url"], inplace=True)
    df["title"] = df["title"].str.strip().str.title()
    df.to_csv("data/processed/cleaned_articles.csv", index=False)
    return df
if __name__ == "__main__":
    df = clean_scraped_data()
    print(df.head())             # Shows first 5 rows
    print(df.shape)              # (rows, columns)
    print(df.columns)            # Column names




