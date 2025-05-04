import sys
import os

import pandas as pd

from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass

from src.components.vectorizer import C_Vectorizer
from src.components.recommender import recommend

@dataclass
class DataIngestionConfig():
    raw_data_path: str=os.path.join("artifact","raw.csv")
    transformed_data_path: str=os.path.join("artifact","transformed_df.csv")
    
class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Data ingestion is in progress...")
        try:
            df=pd.read_csv("notebook\\data\\1_dataset.csv")
            logging.info("Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Merging the genre and overview")
            df_movies = df.copy()
            df_movies['tag'] = df_movies['genre'].str.cat(df_movies['overview'].astype(str),sep=',')
            
            logging.info("Dropping the unnecessary columns...")
            columns_to_drop= ['id','original_language','popularity','release_date',
                                         'vote_average','vote_count', 'genre','overview']
            df_movies = df_movies.drop(columns=columns_to_drop, axis=1)
            
            df_movies.to_csv(self.ingestion_config.transformed_data_path,index=False,header=True)
            logging.info("data's are stored in artifact directory succesfully")
            
            return self.ingestion_config.raw_data_path, self.ingestion_config.transformed_data_path
        
        except Exception as e:
            raise CustomException(e,sys)
            
        

