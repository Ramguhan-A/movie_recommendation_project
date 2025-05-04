import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.vectorizer import C_Vectorizer
from src.exception import CustomException
import sys

class RecommendationPipeline:
    def __init__(self):
        self.ingestor = DataIngestion()
        self.vectorizer = C_Vectorizer()

    def run_pipeline(self):
        
        try:
                
            raw_data_path,transformed_data_path=self.ingestor.initiate_data_ingestion()
            
            vectorized_data,_ = self.vectorizer.initiate_count_vectorizer(transformed_data_path)
            
            similarity_matrix = self.vectorizer.similarity_prediction(vectorized_data)
            
            df_movies = pd.read_csv(transformed_data_path)
            
            return df_movies,similarity_matrix
        
        except Exception as e:
            raise CustomException(e,sys)
    