def validate_data(df):
    errors = []

    if 'Quantity' not in df.columns or 'Price' not in df.columns:
        errors.append("Missing required columns")

    if (df['Quantity'] < 0).any():
        errors.append("Quantity cannot be negative")

    if (df['Price'] < 0).any():
        errors.append("Price cannot be negative")

    return errors
