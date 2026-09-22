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
