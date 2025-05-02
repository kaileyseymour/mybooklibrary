# this file contains the class for a book
import sqlite3
from sqlite3 import Error

class Book:
    def __init__(self):
        pass
    
    # get all books
    def get_books(self,connection):
        cursor = connection.cursor()
        sql = "SELECT * FROM `books`"
        cursor.execute(sql)
        output = cursor.fetchall()
        return list(output)

    # get book by ID
    def get_book_by_id(self, connection, id):
        cursor = connection.cursor()
        sql = "SELECT * FROM `books` WHERE `id`={}".format(id)
        cursor.execute(sql)
        output = cursor.fetchall()
        return output

    # create new book
    def create_new_book(self, connection, title, author, isbn, length, average_rating):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO 'books' (title,author,isbn,length,average_rating) VALUES ('{}','{}','{}','{}','{}');".format(title, author, isbn, length, average_rating))
        connection.commit()
        output = cursor.fetchall()
        return output

    # delete book
    def delete_book(self, connection, id):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM 'books' WHERE 'id'='{}';".format(id))
        connection.commit()
        output = cursor.fetchall()
        return output
        
