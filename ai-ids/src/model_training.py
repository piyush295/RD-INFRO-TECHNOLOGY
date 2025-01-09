def split_data(data, test_size=0.2):
    from sklearn.model_selection import train_test_split
    return train_test_split(data, test_size=test_size, random_state=42)

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import classification_report
    y_pred = model.predict(X_test)
    return classification_report(y_test, y_pred)

def main():
    import pandas as pd
    from anomaly_detection import AnomalyDetector
    from data_preprocessing import load_and_preprocess_data

    data = load_and_preprocess_data('data/processed/processed_data.csv')
    X = data.drop('label', axis=1)
    y = data['label']

    X_train, X_test, y_train, y_test = split_data(X, test_size=0.2)

    model = AnomalyDetector()
    trained_model = train_model(model, X_train, y_train)

    evaluation_report = evaluate_model(trained_model, X_test, y_test)
    print(evaluation_report)

if __name__ == "__main__":
    main()