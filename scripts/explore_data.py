import pandas as pd


INPUT_FILE = "data/expression.csv"


def main():
    df = pd.read_csv(INPUT_FILE)

    print("Dataset overview")
    print("================")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst five genes:")
    print(df[["gene_id", "gene_name"]].head())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nExpression summary:")
    print(df[["control_1", "control_2", "treated_1", "treated_2"]].describe())


if __name__ == "__main__":
    main()