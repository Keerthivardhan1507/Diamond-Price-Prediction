from src.components.data_ingestion import DataIngestion

from src.components.data_transformation import DataTransformation

from src.components.model_evaluation import ModelEvaluation

from src.components.model_trainer import ModelTrainer

obj = DataIngestion()
train_data_path,test_data_path = obj.initiate_data_ingestion()

data_transformation_obj = DataTransformation()
train_arr,test_arr = data_transformation_obj.initiate_data_transformation(train_data_path,test_data_path)

model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_trainer_config(train_arr,test_arr)

model_eval_obj = ModelEvaluation()
model_eval_obj.initiate_model_evaluation(train_arr,test_arr)

