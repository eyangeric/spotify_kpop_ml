CREATE TABLE importances (
    ID serial PRIMARY KEY,
    Model_Train_ID INTEGER,
    Feature_ID INTEGER,
    Feature_Importance FLOAT,
    Permutation_Importance FLOAT,
    CONSTRAINT fk_ml_model_train
    FOREIGN KEY(Model_Train_ID) 
    REFERENCES ml_models_evaluation(Model_Train_ID),
    CONSTRAINT fk_feature
    FOREIGN KEY(Feature_ID) 
    REFERENCES features(ID)
);