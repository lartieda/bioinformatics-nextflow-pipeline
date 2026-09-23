import pandas as pd

from scripts.analyze import calculate_fold_change


def test_fold_change_calculation():
    df = pd.DataFrame(
        {
            "gene_id": ["GENE001", "GENE002"],
            "gene_name": ["TP53", "BRCA1"],
            "control_mean": [100.0, 50.0],
            "treated_mean": [200.0, 25.0],
        }
    )

    result = calculate_fold_change(df)

    assert result.loc[0, "fold_change"] == 2.0
    assert result.loc[1, "fold_change"] == 0.5



def test_fold_change_does_not_modify_input():
    df = pd.DataFrame(
        {
            "gene_id": ["GENE001"],
            "gene_name": ["TP53"],
            "control_mean": [100.0],
            "treated_mean": [200.0],
        }
    )

    original_columns = df.columns.tolist()

    calculate_fold_change(df)

    assert df.columns.tolist() == original_columns
    assert "fold_change" not in df.columns