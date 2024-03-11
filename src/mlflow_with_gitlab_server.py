import mlflow
from mlflow import MlflowClient
import os

#token = 'glpat-xs7YZSxymiciPyDoXqP8'
#uri = 'https://gitlab.com/api/v4/projects/55563514/ml/mlflow'
#os.environ['MLFLOW_TRACKING_TOKEN'] = token
#os.environ['MLFLOW_TRACKING_URI'] = uri


class Mlflow_client_gitlab_server:
    def __init__(self,token,uri,register_model_name):
        self.token = token
        self.uri = uri
        self.register_model_name = register_model_name
        os.environ['MLFLOW_TRACKING_TOKEN'] = self.token
        os.environ['MLFLOW_TRACKING_URI'] = self.uri
        self.client = MlflowClient()
    
    def create_empty_register_model(self):
        self.client.create_registered_model(self.register_model_name)
    def delete_register_model(self):
        self.client.delete_registered_model(name=self.register_model_name)
    def Fetch_Register_model(self):
        Model = self.client.get_registered_model(name=self.register_model_name)
        return Model
    def Create_model_version(self,version,tags,description):
        self.client.create_model_version(name=self.register_model_name,source="",tags=tags,description=description)
    def Update_register_model(self,new_description):
        self.client.update_registered_model(name=self.register_model_name,description=new_description)
    def Update_model_version(self,new_description,new_version):
        self.client.update_model_version(name=self.register_model_name,version=new_version,description=new_description)

