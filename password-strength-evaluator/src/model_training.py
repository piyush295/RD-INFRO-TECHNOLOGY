def train_model(training_data):
    """
    Trains a machine learning model using the provided training data.
    
    Parameters:
    training_data (DataFrame): The data used for training the model.
    
    Returns:
    model: The trained machine learning model.
    """
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    import joblib

    # Split the data into features and target
    X = training_data.drop('target', axis=1)
    y = training_data['target']

    # Split the dataset into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestClassifier()

    # Train the model
    model.fit(X_train, y_train)

    # Validate the model
    predictions = model.predict(X_val)
    accuracy = accuracy_score(y_val, predictions)
    print(f"Model accuracy: {accuracy:.2f}")

    return model

def save_model(model, filename):
    """
    Saves the trained model to a file.
    
    Parameters:
    model: The trained machine learning model.
    filename (str): The name of the file to save the model to.
    """
    joblib.dump(model, filename)