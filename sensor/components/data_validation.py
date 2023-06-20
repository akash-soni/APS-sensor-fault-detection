from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.config_entity import DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from sensor.utils.main_utils import read_yaml_file
from sensor.exception import SensorException
from sensor.logger import logging
import pandas as pd
import os, sys

class DataValidation:

    def __init__(self, data_ingestion_artifact:DataIngestionArtifact, data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            
        except Exception as e:
            raise SensorException(e, sys)


    def validate_number_of_columns(self)->bool:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        

    def is_numerical_column_exist(self)->bool:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        """
        we create a static method as it will read the file directly
        """
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e,sys)

    def detect_dataset_drift(self):
        pass

    def initiate_data_validation(self)->DataIngestionArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # reading data
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)



        except Exception as e:
            raise SensorException(e,sys)
     