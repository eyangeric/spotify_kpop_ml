CREATE TABLE ml_models_evaluation (
    Model_Train_ID serial PRIMARY KEY,
    ML_Model_ID INTEGER,
    Hyperparameters VARCHAR,
    Log_Loss FLOAT,
    DZ_Precision FLOAT,
    DZ_Accuracy FLOAT,
    EY_Precision FLOAT,
    EY_Accuracy FLOAT,
    EY_DZ_Precision FLOAT,
    EY_DZ_Accuracy FLOAT,
    Overall_Accuracy FLOAT,
    CONSTRAINT fk_ml_model 
    FOREIGN KEY(ML_Model_ID) 
    REFERENCES ml_models(ID)
);