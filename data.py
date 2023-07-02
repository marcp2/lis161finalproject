import sqlite3

db_path = "database.db"

def connect_to_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def read_restaurants_by_location(location):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM restaurants WHERE location = ?'
    value = location
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

def read_restaurant_by_id(id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM restaurants WHERE id = ?'
    value = id
    results = cur.execute(query,(value,)).fetchone()
    conn.close()
    return results

def insert_restaurant(restaurant_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO restaurants (location, name, price, review, rating, payment_method, url) VALUES (?,?,?,?,?,?,?)'
    values = (restaurant_data['location'], restaurant_data['name'],
              restaurant_data['price'], restaurant_data['review'],
              restaurant_data['rating'], restaurant_data['payment_method'], 
              restaurant_data['url'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

def update_restaurant(restaurant_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE restaurants SET location=?, name=?, price=?, review=?, rating=?, payment_method=?, url=? WHERE id=?"
    values = (restaurant_data['location'], restaurant_data['name'],
              restaurant_data['price'], restaurant_data['review'],
              restaurant_data['rating'], restaurant_data['payment_method'],
              restaurant_data['url'], restaurant_data['restaurant_id'])  # Update the key here
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_restaurant(restaurant_id):
    con, cur = connect_to_db(db_path)
    query = "DELETE FROM restaurants WHERE id=?"
    values = (restaurant_id,)
    cur.execute(query, values)
    con.commit()
    con.close()

def search_restaurants(query):
    conn, cur = connect_to_db(db_path)
    sql_query = "SELECT * FROM restaurants WHERE location LIKE ? OR name LIKE ?"
    value = "%{}%".format(query)
    results = cur.execute(sql_query, (value, value)).fetchall()
    conn.close()
    return results
