import sys
from botocore.exceptions import NoCredentialsError, ClientError

from Chest_Disease.cloud_storage.s3_ops import S3Operation
from Chest_Disease.entity.config_entity import ModelPusherConfig
from Chest_Disease.exception import XRayException
from Chest_Disease.logger import logging
from Chest_Disease.constant.training_pipeline import *

class ModelPusher:
    def __init__(self,model_pusher_config: ModelPusherConfig):

        self.model_pusher_config = model_pusher_config
        self.s3 = S3Operation()


    
    def initiate_model_pusher(self):

        """
        Method Name :   initiate_model_pusher

        Description :   This method initiates model pusher. 
        
        Output      :    Model pusher artifact 
        """
        logging.info("Entered initiate_model_pusher method of Modelpusher class")
        try:
            # Uploading the best model to s3 bucket
            self.s3.upload_file(
                "model/model.pt",
                "model.pt",
                "chest-disease",
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")


        except Exception as e:
            raise e