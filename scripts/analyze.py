import pandas as pd


INPUT_FILE = "preprocessed_expression.csv"
OUTPUT_FILE = "differential_expression.csv"


def calculate_fold_change(df):
    df = df.copy()
    df["fold_change"] = df["treated_mean"] / df["control_mean"]
    return df


def main():
    df = pd.read_csv(INPUT_FILE)

    df = calculate_fold_change(df)

    results = df[
        [
            "gene_id",
            "gene_name",
            "control_mean",
            "treated_mean",
            "fold_change",
        ]
    ].sort_values("fold_change", ascending=False)

    results.to_csv(OUTPUT_FILE, index=False)

    print("Analysis completed successfully.")
    print(f"Results written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()