import pandas as pd

def export_to_csv(rows):
    df = pd.DataFrame(rows)
    csv = df.to_csv(index=False)
    return csv, df