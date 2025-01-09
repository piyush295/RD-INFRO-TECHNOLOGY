def log(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def load_data(filepath):
    """Loads data from a specified file path."""
    import pandas as pd
    return pd.read_csv(filepath)