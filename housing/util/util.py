from housing.exception import HousingException
import os , sys
import yaml

def read_yaml_file(file_path:str)->dict:
    """
    Lecture du fichier yaml et retourne un dictionnaire en sortie.
    file_path:str 
    
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
