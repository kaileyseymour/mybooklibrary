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
        output = cursor.fetchall()
        return list(output)

    # get book by ISBN
    def get_book_by_isbn(self, connection, isbn):
        cursor = connection.cursor()
        sql = "SELECT * FROM `mybooks` WHERE `isbn`={}".format(isbn)
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
