import os
from re import L
import sys
from typing_extensions import dataclass_transform
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

@dataclass 
class DataIngestionConfig:
  train_data_path: str = os.path.join('artifacts', 'train.csv')
  test_data_path: str = os.path.join('artifacts', 'test.csv')
  raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
  def __init__(self):
    self.ingestion_config = DataIngestionConfig()

  def initiate_data_ingestion(self):
    logging.info('Entered the data ingestion method or component')
    try:
      df = pd.read_csv('/content/drive/MyDrive/Data Science - End-to-end Project/environment/ml_project/notebooks/student_performance.csv')
      logging.info('Exported or read the dataset in dataframe')

      df.rename(columns={'race/ethnicity':'race_ethnicity','parental level of education':'parental_level_of_education','test preparation course':'test_preparation_course','math score':'math_score','reading score':'reading_score','writing score':'writing_score'},inplace=True)

      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

      df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

      logging.info('Train-Test split initiated')
      train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)
     
      train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
      
      test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

      logging.info('Data Ingestion completed')

      return(
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path
      )
    except Exception as e:
      raise CustomException(e,sys)

if __name__ == '__main__':
  obj = DataIngestion()
  train_data, test_data = obj.initiate_data_ingestion() 
  
  data_transformation = DataTransformation()
  train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

  modeltrainer = ModelTrainer()

  print(modeltrainer.initiate_model_trainer(train_arr, test_arr))






















