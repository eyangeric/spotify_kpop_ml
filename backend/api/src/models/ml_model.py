class ML_MODEL:
    def __init__(self, ml_model, features_scaler):
        self.ml_model = ml_model
        self.features_scaler = features_scaler

        def predict_outcome(self, features):
            scaled_features = self.features_scaler.transform(features)
            outcome = self.ml_model.predict(scaled_features)
            return outcome