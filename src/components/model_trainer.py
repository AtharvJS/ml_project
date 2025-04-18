import os 
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import(
  AdaBoostClassifier,
  AdaBoostRegressor,
  GradientBoostingRegressor,
  RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging 
from src.utils import save_object
from src.utils import evaluate_model

@dataclass
class ModelTrainerConfig:
  trained_model_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
  def __init__(self):
    self.model_trainer_config = ModelTrainerConfig()

  def initiate_model_trainer(self, train_arr, test_arr):
    try:
      logging.info('Spliting training and testing input data')
      X_train, y_train, X_test, y_test = (
        train_arr[:,:-1],
        train_arr[:,-1],
        test_arr[:,:-1],
        test_arr[:,-1]
      )
      models = {
        'Random Forest' : RandomForestRegressor(),
        'Decision Tree' : DecisionTreeRegressor(),
        'Gradient Boost' : GradientBoostingRegressor(),
        'Linear Regression' : LinearRegression(),
        'K-Neighbors Classifier' : KNeighborsRegressor(),
        'XGBClassifier' : XGBRegressor(),
        'Catboosting Classifier' : CatBoostRegressor(verbose=False),
        'AdaBoost Classifier' : AdaBoostRegressor()
      }

      params={
        'Decision Tree':{
          'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
        },
        'Random Forest':{
          'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
          'n_estimators':[8,16,32,64,128,256]
        },
        'Gradient Boost':{
          'learning_rate':[.1,.01,.05,.001],
          'subsample':[.6,.7,.75,.8,.85,.9],
          'n_estimators':[8,16,32,64,128,256]
        },
        'Linear Regression':{},
        'K-Neighbors Classifier':{
          'n_neighbors':[5,7,9,11]
        },
        'XGBClassifier':{
          'learning_rate':[.1,.01,.05,.001],
          'n_estimators':[8,16,32,64,128,256]
        },
        'Catboosting Classifier':{
          'depth':[6,8,10],
          'learning_rate':[.01,.05,.1],
          'iterations':[30,50,100]
        },
        'AdaBoost Classifier':{
          'learning_rate':[.1,.01,.05,.001],
          'n_estimators':[8,16,32,64,128,256]
        }
      }

      model_report:dict=evaluate_model(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models, param=params)
  
      # To get best model score from dictionary
      best_model_score = max(sorted(model_report.values()))

      # To get best model name from dictionary
      best_model_name = list(model_report.keys())[
        list(model_report.values()).index(best_model_score)
      ]

      best_model = models[best_model_name]

      if best_model_score < 0.6:
        raise CustomException('No best model found')
      logging.info('Best model found on both training and testing dataset')

      save_object(
        file_path = self.model_trainer_config.trained_model_file_path,
        obj = best_model
      )

      predicted = best_model.predict(X_test)

      r2_square = r2_score(y_test, predicted)
      return r2_square



    except Exception as e:
      raise CustomException(e,sys)































































