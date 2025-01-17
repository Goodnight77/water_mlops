import mlflow

import dagshub


mlflow.set_tracking_uri("https://dagshub.com/Goodnight77/water_mlops.mlflow")
dagshub.init(repo_owner='Goodnight77', repo_name='water_mlops', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)