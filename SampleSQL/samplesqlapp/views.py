from django.shortcuts import render
import mysql.connector as connector
from django.template.defaultfilters import register
import datetime


def index(request):

    # create_database()
    # product_categories()
    # products()

    mydb = connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="toko"
    )

    sql = "SELECT a.id, a.name, GROUP_CONCAT(b.name) FROM product_categories a JOIN products b " \
          "WHERE b.category_id = a.id GROUP BY b.category_id"

    mycursor = mydb.cursor()
    mycursor.execute(sql)

    result = mycursor.fetchall()
    id = []
    categories = []
    names = []

    for r in result:
        id.append(r[0])
        categories.append(r[1])
        names.append(", ".join(r[2].split(',')))

    data = zip(id, categories, names)

    return render(request, 'index.html', {"database": data})


def create_database():

    mydb = connector.connect(
        host="127.0.0.1",
        user="root",
        passwd=""
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE toko")


def product_categories():

    mydb = connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="toko"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE product_categories ( id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY , "
                     "name VARCHAR(255) NOT NULL , created_date VARCHAR(19) NOT NULL )")

    val = [
        ('1', 'Peralatan Mandi', datetime.datetime.now().strftime("%Y-%m-%d %X")),
        ('2', 'Minuman Kemasan', datetime.datetime.now().strftime("%Y-%m-%d %X")),
        ('3', 'Produk Susu', datetime.datetime.now().strftime("%Y-%m-%d %X"))
    ]

    sql = "INSERT INTO product_categories (id, name, created_date) VALUES (%s, %s, %s)"

    mycursor.executemany(sql, val)
    mydb.commit()


def products():
    mydb = connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="toko"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE products ( id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY , "
                     "name VARCHAR(255) NOT NULL , category_id INT(11) NOT NULL , created_date VARCHAR(19) NOT NULL , "
                     "FOREIGN KEY (category_id) REFERENCES product_categories(id) )")

    val = [
        ('1', 'Sabun Wangi', '1', datetime.datetime.now().strftime("%Y-%m-%d %X")),
        ('2', 'Minuman Cola', '2', datetime.datetime.now().strftime("%Y-%m-%d %X")),
        ('3', 'Prenagen Gold', '3', datetime.datetime.now().strftime("%Y-%m-%d %X")),
        ('4', 'Aqua', '2', datetime.datetime.now().strftime("%Y-%m-%d %X")),
        ('5', 'Teh Botol', '2', datetime.datetime.now().strftime("%Y-%m-%d %X")),
        ('6', 'Shampoo', '1', datetime.datetime.now().strftime("%Y-%m-%d %X"))
    ]

    sql = "INSERT INTO products (id, name, category_id, created_date) VALUES (%s, %s, %s, %s)"

    mycursor.executemany(sql, val)
    mydb.commit()


@register.filter(name='zip')
def zip_lists(a, b, c):
    return zip(a, b, c)