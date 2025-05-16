from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from sqlite3 import Error
from Book import Book

conn = sqlite3.connect("mybooks.db", check_same_thread=False)
app = Flask(__name__)
CORS(app)
book_instance = Book()

# get all books
@app.route("/books", methods=["GET"])
def getAllBooks():
    try:
        books = book_instance.get_books(conn)
        return jsonify(books)
    except Exception as e:
        return jsonify({"message":str(e)})

# get single book by ISBN
@app.route("/books/<isbn>", methods=["GET"])
def getBookByISBN(isbn):
    try:
        book = book_instance.get_book_by_isbn(conn, isbn)
        return jsonify(book)
    except Exception as e:
        return jsonify({"message":"Invalid Book ISBN"})

# create a new book
@app.route("/books/create")
def createBook():
    try:
        # created = book_instance.create_new_book(conn, "Normal People", "Sally Rooney", "1984822179", "273", "3.8")
        created = ""
        return jsonify({"created":created})
    except Exception as e:
        return jsonify({"message":str(e)})
    
# delete a book
@app.route("/books/delete/<id>")
def deleteBook(id):
    try:
        deleted = book_instance.delete_book(conn, id)
        # deleted = ""
        return jsonify({"deleted":deleted})
    except Exception as e:
        return jsonify({"message":str(e)})

if __name__ == '__main__':
   app.run()