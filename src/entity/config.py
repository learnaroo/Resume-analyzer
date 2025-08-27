from src.exceptions import CustomException
from src.logger import logging
from src.constants import *
import sys

class ConfigEntity:
    def __init__(self):
        self.output_dir = OUTPUT_DIR
        self.data_dir = DATA_DIR
        self.open_api_key = OPENAI_API_KEY
        self.open_api_model = OPENAI_API_MODEL
        
        
class TextExtracterConfig:
    def __init__(self,config:ConfigEntity):
        try:
            self.output_dir =config.output_dir
            self.data_dir = config.data_dir
        except Exception as e:
            raise CustomException(e,sys)
        
        
class EvaluatorConfig:
    def __init__(self,config:ConfigEntity):
        try:
          self.open_api_key = config.open_api_key
          self.open_api_model = config.open_api_model
        except Exception as e:
            raise CustomException(e,sys)
        