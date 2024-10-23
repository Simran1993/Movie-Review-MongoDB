from flask import Flask, render_template, request, redirect, url_for
import requests
from bson import ObjectId
from models.db import get_db

app = Flask(__name__)
db = get_db()
reviews_collection = db['reviews']

# Replace with your own API key from OMDb or TMDb
API_KEY = 'b24150c3'
MOVIE_API_URL = f'http://www.omdbapi.com/?i=tt3896198&apikey={API_KEY}'

# Home Route - Fetch movies from API and show existing reviews
@app.route('/')
def index():
    search_query = request.args.get('query', 'Avengers')  # Default search
    response = requests.get(f'{MOVIE_API_URL}&s={search_query}')
    movies = response.json().get('Search', [])  # Fetch movie results from API

    # Fetch reviews from MongoDB
    reviews = list(reviews_collection.find())
    
    return render_template('index.html', movies=movies, reviews=reviews)

# Route to add a new review
@app.route('/add_review', methods=['POST'])
def add_review():
    movie_id = request.form.get('movie_id')
    review_text = request.form.get('review')
    rating = request.form.get('rating')
    
    # Insert new review into MongoDB
    reviews_collection.insert_one({
        'movie_id': movie_id,
        'review': review_text,
        'rating': int(rating)
    })
    
    return redirect(url_for('index'))

# Route to update an existing review
@app.route('/update_review/<review_id>', methods=['POST'])
def update_review(review_id):
    new_review = request.form.get('review')
    new_rating = request.form.get('rating')
    
    # Update the review in the database
    reviews_collection.update_one(
        {'_id': ObjectId(review_id)},
        {'$set': {'review': new_review, 'rating': int(new_rating)}}
    )
    
    return redirect(url_for('index'))

# Route to delete a review
@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    # Remove review from MongoDB
    reviews_collection.delete_one({'_id': ObjectId(review_id)})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
