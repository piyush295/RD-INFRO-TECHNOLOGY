class AnomalyDetector:
    def __init__(self, model):
        self.model = model

    def fit(self, X):
        self.model.fit(X)

    def predict(self, X):
        predictions = self.model.predict(X)
        return predictions

    def get_anomalies(self, X):
        predictions = self.predict(X)
        anomalies = X[predictions == -1]  # Assuming -1 indicates an anomaly
        return anomalies