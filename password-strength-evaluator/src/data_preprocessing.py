def clean_data(data):
    # Implement data cleaning logic here
    cleaned_data = data.dropna()  # Example: dropping missing values
    return cleaned_data

def split_data(data, test_size=0.2):
    from sklearn.model_selection import train_test_split
    train_data, test_data = train_test_split(data, test_size=test_size)
    return train_data, test_data