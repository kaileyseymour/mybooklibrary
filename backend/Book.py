# this file contains the class for a book
import sqlite3
import json
from sqlite3 import Error

class Book:
    def __init__(self):
        pass
    
    # get all books
    def get_books(self,connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM mybooks")
        return cursor.fetchall()
        
        # rows = cursor.fetchall()
        # columns = [column[0] for column in cursor.description]
        # output = []
        # for row in rows:
        #     row_dict = {columns[i]: row[i] for i in range(len(columns))}
        #     output.append(row_dict)
        # return json.dumps(output)

    def handle_fetch():
        print('fetching all')
        db = get_db_connection()
        cur = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute('SELECT * FROM guitars;')
        guitar_data = cur.fetchall()
        cur.close()
        db.close()
        return jsonify(guitar_data)

    # get book by ID
    def get_book_by_id(self, connection, id):
        cursor = connection.cursor()
        sql = "SELECT * FROM `mybooks` WHERE `id`={}".format(id)
        cursor.execute(sql)
        output = cursor.fetchall()
        return output

    # create new book
    def create_new_book(self, connection, cover, title, author, isbn, my_rating, average_rating, publisher, length, published, dateRead, bookshelves, exclusiveShelf, myReview):
        cursor = connection.cursor()
        cover, 
        cursor.execute("INSERT INTO 'mybooks' (cover, title, author, isbn, my rating, average rating, publisher, number of pages, year published, date read, bookshelves, exclusive shelf, my review) VALUES ('{}','{}','{}','{}','{}');".format(cover, title, author, isbn, my_rating, average_rating, publisher, length, published, dateRead, bookshelves, exclusiveShelf, myReview))
        connection.commit()
        output = cursor.fetchall()
        return output

    # delete book
    def delete_book(self, connection, id):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM 'mybooks' WHERE 'id'='{}';".format(id))
        connection.commit()
        output = cursor.fetchall()
        return output
        
