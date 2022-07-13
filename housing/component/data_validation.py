


from multiprocessing.sharedctypes import RawArray
from tkinter import E

from evidently import dashboard
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity   import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import pandas as pd
import sys , os
import json




class dataValidation:
    



    def __init__(self, data_validation_config:DataValidationConfig,
        data_ingestion_artifact : DataIngestionArtifact):

        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise HousingException(e,sys) from e


    def get_train_and_test_df(self):
        try:
           train_df =  pd.read_csv(self.data_ingestion_artifact.train_file_path)
           test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
           return train_df , test_df
        except Exception as e:

           
            raise HousingException(e,sys) from e


    
    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking if training and test file are available")
            is_train_file_exist = False
            is_test_file_exist  = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path


            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)


            is_available = is_test_file_exist and is_train_file_exist

            logging.info(f"Is Train and test file exist ? -> {is_available}")


            if not is_available:
                training_file =self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                message = f"Training file:{training_file} or testing file : {testing_file}"\
                    "is not present"
               
                raise Exception(message)
            return is_available

        except Exception as e:
            raise HousingException(e,sys) from e


    def validate_dataset_schema(self)->bool:
        try:

            validation_status = True




            #validation_status = True
            return validation_status
           
        except Exception as e:
            raise HousingException(e,sys) from e 

    def get_and_save_data_drift_report(self):

        try:
            profile = Profile(sections=[DataDriftProfileSection()])


            train_df , test_df = self.get_train_and_test_df()

            profile.calculate(train_df, test_df)
            profile.json()

            report = json.loads(profile.json())
            
            with open(self.data_validation_config.report_file_path, "w") as report_file:
                json.dump(report, report_file, indent=6)


        except Exception as e:
            raise HousingException(e,sys) from e


       


    def save_data_drift_report_page(self):
        try:

            dashboard = Dashboard(tabs=[DataDriftTab()])

            train_df , test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df, test_df)
            dashboard.save(self.data_validation_config.report_page_file_path)
            



        except Exception as e:
            raise HousingException(e,sys) from e









    def is_data_drift_found(self)->bool:
        try:

            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            return True
        except Exception as e:
            raise HousingException(e,sys) from e

    
    def initiate_data_validation(self):
        try:

            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()
            
        except Exception as e:
            raise HousingException(e,sys) from e


    
     
   