import os
import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging

def recommend(movie_name,sim,vec_data):
    try:
        logging.info(f"Lets recommend the movies...based on {movie_name}")
        df_movies = pd.read_csv("artifact\\transformed_df.csv")
        index = df_movies[df_movies['title']==movie_name].index[0]
        distance = sorted(list(enumerate(sim[index])),reverse=True,key = lambda vec:vec[1])
        for i in distance[1:6]:
            rec = df_movies.iloc[i[0]].title
            print(rec)
            logging.info(f"Recommendation are {rec}")
        
    except Exception as e:
        raise CustomException(e,sys)