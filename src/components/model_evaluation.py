import os
import sys
import mlflow
import pickle
import numpy as np
import mlflow.sklearn
from urllib.parse import urlparse
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from src.utils.utils import load_object

class ModelEvaluation:
    def __init__(self):
        pass
    
    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        r2 = r2_score(actual,pred)
        mae = mean_absolute_error(actual,pred)
        return rmse,r2,mae
    
    def initiate_model_evaluation(self,train_array,test_array):
        try:
            X_test,y_test = (test_array[:,:-1],test_array[:,-1])
            
            model_path = os.path.join("Artifacts","Model.pkl")
            model = load_object(model_path)
            with mlflow.start_run():
                predicted_qualities = model.predict(X_test)
                
                (rmse,mae,r2) = self.eval_metrics(y_test,predicted_qualities)
                
                mlflow.log_metric("rmse",rmse)
                mlflow.log_metric("mae",mae)
                mlflow.log_metric("r2",r2)
                
                mlflow.sklearn.log_model(model,"model")
                
        except Exception as e:
            raise e
        
                
    