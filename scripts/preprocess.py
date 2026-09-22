import pandas as pd


INPUT_FILE = "expression.csv"
OUTPUT_FILE = "preprocessed_expression.csv"


def main():
    df = pd.read_csv(INPUT_FILE)

    required_columns = [
        "gene_id",
        "gene_name",
        "control_1",
        "control_2",
        "treated_1",
        "treated_2",
    ]

    missing_columns = [
        column for column in required_columns if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df[required_columns].isnull().any().any():
        raise ValueError("Input data contains missing values.")

    df["control_mean"] = df[["control_1", "control_2"]].mean(axis=1)
    df["treated_mean"] = df[["treated_1", "treated_2"]].mean(axis=1)

    results = df[
        [
            "gene_id",
            "gene_name",
            "control_mean",
            "treated_mean",
        ]
    ]

    results.to_csv(OUTPUT_FILE, index=False)

    print("Preprocessing completed successfully.")
    print(f"Results written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()