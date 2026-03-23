import pandas as pd
import numpy as np

def process_data(file_path):
    df = pd.read_csv(file_path)

    # Clean data
    df.dropna(inplace=True)

    # KPI Calculation
    df['Total'] = df['Quantity'] * df['Price']

    # Aggregation
    summary = {
        "total_sales": float(np.sum(df['Total'])),
        "average_sales": float(np.mean(df['Total'])),
        "total_orders": int(len(df))
    }

    return df, summary
