from housing.pipeline.pipeline import Pipeline 
from housing.exception import HousingException
from housing.config.configuration import Configuration
from housing.logger import logging
import os , sys


def main():

    try:

        # pipeline = Pipeline()

        # pipeline.run_pipeline()

       data_validation_config = Configuration().get_data_validation_config
       print(data_validation_config)

    except Exception as e:

        logging.error(f"{e}")


    if __name__=="__main__":
      main()

    
