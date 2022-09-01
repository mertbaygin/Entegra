from Product_Service.ProductList.Products import Product
import sqlite3


class DB:
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    def createTable(self):
        self.cursor.execute('''CREATE TABLE product (
        name text,
        productCode text,
        quantity long)''')

    def addDataToProduct(self):
        self.createTable()
        x = Product()
        y = x.getProducts()
        for i in range(5):
            name = y[i].get('name')
            code = y[i].get('productCode')
            quan = y[i].get('quantity')
            self.cursor.execute('''INSERT INTO product (name,productCode,quantity) VALUES (?,?,?)''', (name, code, quan))
        self.conn.commit()

    def dataPrint(self):
        for row in self.cursor.execute('''SELECT * FROM product'''):
            print(row)
