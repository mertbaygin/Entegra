from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('db.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/products", methods=["GET", "POST"])
def product():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cur = cursor.execute("SELECT * FROM product")
        products = [
            dict(name=row[0], productCode=row[1], quantity=row[2])
            for row in cursor.fetchall()
        ]
        if products is not None:
            return jsonify(products)

    if request.method == "POST":
        new_name = request.form["name"]
        new_code = request.form["productCode"]
        new_quan = request.form["quantity"]
        sql = """INSERT INTO product (name, productCode, quantity) VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (new_name, new_code, new_quan))
        conn.commit()
        return "successfully"


@app.route("/products/<string:name>", methods=["GET", "PUT", "DELETE"])
def single_book(name):
    conn = db_connection()
    cursor = conn.cursor()
    products = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM product WHERE name=?", (name,))
        rows = cursor.fetchall()
        for r in rows:
            products = r
        if products is not None:
            return jsonify(products), 200
        else:
            return "Something wrong"

    if request.method == "PUT":
        sql = """UPDATE product
                SET name=?,
                    productCode=?,
                    quantity=?
                WHERE name=? """

        name = request.form["name"]
        productCode = request.form["productCode"]
        quantity = request.form["quantity"]
        updated_product = {
            "name": name,
            "productCode": productCode,
            "quantity": quantity,
        }
        conn.execute(sql, (name, productCode, quantity))
        conn.commit()
        return jsonify(updated_product)

    if request.method == "DELETE":
        sql = """ DELETE FROM product WHERE name=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The product has been deleted"


if __name__ == '__main__':
    app.run(debug=True)
