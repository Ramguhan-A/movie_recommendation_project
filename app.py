from flask import Flask,request,render_template
from src.pipeline.predict_pipeline import RecommendationPipeline

app = Flask(__name__)

pipeline = RecommendationPipeline()
df_movies, similarity_matrix = pipeline.run_pipeline()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recommend',methods = ["GET","POST"])
def recommend_movies():
    movie_name = request.form['movie']
    try:
        index = df_movies[df_movies['title']==movie_name].index[0]
        distance = sorted(list(enumerate(similarity_matrix[index])),reverse=True,key = lambda vec:vec[1])
        recommendations = [df_movies.iloc[i[0]].title for i in distance[1:6]]
        return render_template("index.html",movie=movie_name,recommendations=recommendations)
    except:
        return render_template("index.html",error="Movies not found. Please try again later..")
    
if __name__ == "__main__":
    app.run(debug=True)
