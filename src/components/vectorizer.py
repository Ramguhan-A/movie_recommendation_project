import os
import sys

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object

@dataclass
class TransformationConfig:
     c_vectorized_data_path: str = os.path.join("artifact","C_vectorized.pkl")
     similarity_obj_path: str = os.path.join("artifact","similarity.pkl") 
     
class C_Vectorizer:
    def __init__ (self):
        self.prediction_config = TransformationConfig()
        self.count_vectorizer = CountVectorizer(max_features=10000,stop_words="english")
        
    def initiate_count_vectorizer(self,data_path):
        
        try:
            df = pd.read_csv(data_path)
            logging.info("Reading the data file to vectorize...")

            transform_column = "tag"
            
            if transform_column not in df.columns:
                raise KeyError(f"Column '{transform_column}' not found in the DataFrame.")
            
            vectorized_data = self.count_vectorizer.fit_transform(df[transform_column].values.astype('U')).toarray()
            logging.info("vectorization done...")
            
            save_object(
                file_path = self.prediction_config.c_vectorized_data_path,
                obj= self.count_vectorizer
            )
            
            return(vectorized_data,self.prediction_config.c_vectorized_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def similarity_prediction(self,data):
        try:
            logging.info("Cosine similarity metrics...")
            similarity_obj = cosine_similarity(data)
            return similarity_obj
        
        except Exception as e:
            raise CustomException(e,sys)   
        
        
            
        
        
        