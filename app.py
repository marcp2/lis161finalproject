from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stores/<location>') 
def stores(location):
    restaurants_list = read_restaurants_by_location(location)
    return render_template("stores.html", location=location, restaurants=restaurants_list) 

@app.route('/stores/<int:restaurant_id>')
def restaurant(restaurant_id):
    restaurant= read_restaurant_by_id(restaurant_id)
    return render_template("restaurant.html",restaurant=restaurant) 

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processed', methods=['POST'])
def processing():
    restaurant_data = {
        "location": request.form['location'],
        "name": request.form['location_name'],
        "price": request.form['location_price'],
        "review": request.form['location_review'],
        "rating": request.form['location_rating'],
        "payment_method": request.form['payment_method'],  # Update the key here
        "url": request.form['location_url']
    }
    insert_restaurant(restaurant_data)
    return redirect(url_for('stores', location=request.form['location']))

@app.route('/modify', methods=['post'])
def modify():
    if request.form["modify"] == "EDIT":
        restaurant_id = request.form["restaurant_id"] 
        restaurant = read_restaurant_by_id(restaurant_id)
        return render_template('update.html', restaurant=restaurant)
    elif request.form["modify"] == "DELETE":
        restaurant_id =request.form["restaurant_id"]
        restaurant = read_restaurant_by_id(restaurant_id)
        delete_restaurant(restaurant_id)
        return redirect(url_for("stores", location=restaurant['location']))

@app.route('/update', methods=['post'])
def update():
    restaurant_data = {
        "restaurant_id": request.form["restaurant_id"],  # Update the key here
        "location": request.form['restaurant_location'],
        "name": request.form['restaurant_name'],
        "price": request.form['restaurant_price'],
        "review": request.form['restaurant_review'],
        "rating": request.form['restaurant_rating'],
        "payment_method": request.form['restaurant_payment_method'],
        "url": request.form['restaurant_url']
    }
    update_restaurant(restaurant_data)
    return redirect(url_for('restaurant', restaurant_id=request.form['restaurant_id']))

@app.route('/search', methods=['get'])
def search():
    query = request.args.get('query', '')
    results = search_restaurants(query)
    return render_template('search.html', query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
