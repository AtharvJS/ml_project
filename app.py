import re
from flask import Flask, request, render_template
import numpy as np
import pandas as pd 
from pyngrok import ngrok
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application

# Route for home page

@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
  if request.method == 'GET':
    return render_template('home.html')
  else:
    data = CustomData(
      gender = request.form.get('gender'),
      race_ethnicity = request.form.get('ethnicity'),
      parental_level_of_education = request.form.get('parental_level_of_education'),
      lunch = request.form.get('lunch'),
      test_preparation_course = request.form.get('test_preparation_course'),
      reading_score = float(request.form.get('reading_score')),
      writing_score = float(request.form.get('writing_score'))
    )

    pred_df = data.get_data_as_frame()
    print(pred_df)

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    return render_template('home.html', results=results[0])



# Running the application-----------------

ngrok.kill()

# ngrok config add-authtoken 2vwL8EbHp1aYcIM114zdpCnLmot_84CbCwPwWq28TZT2rkKsC     

public_url = ngrok.connect(5000)
print(f" * Public URL: {public_url}")
if __name__ == '__main__':
  app.run()


