import pandas as pd


def test_fold_change_calculation():
    df = pd.DataFrame(
        {
            "gene_id": ["GENE001", "GENE002"],
            "gene_name": ["TP53", "BRCA1"],
            "control_mean": [100.0, 50.0],
            "treated_mean": [200.0, 25.0],
        }
    )

    df["fold_change"] = df["treated_mean"] / df["control_mean"]

    assert df.loc[0, "fold_change"] == 2.0
    assert df.loc[1, "fold_change"] == 0.5
