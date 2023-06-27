from flask import Flask, render_template, request, redirect
import mysql.connector


app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="dbsorya_db",
    password="123456"
)

# Create a cursor to interact with the database
cursor = db.cursor()

# Homepage 
@app.route("/")
def home():
    # Render home
    return render_template("home.html")

######################
# Products
######################

# Define the data model
class ProductItem:
    def __init__(self, 
                 product_code, 
                 category_id, 
                 name, 
                 date_acquired, 
                 expiration_date, 
                 quantity, 
                 cost, 
                 storage_location, 
                 supplier_id):
        self.product_code = product_code
        self.category_id = category_id
        self.name = name
        self.date_acquired = date_acquired
        self.expiration_date = expiration_date
        self.quantity = quantity
        self.cost = cost
        self.storage_location = storage_location
        self.supplier_id = supplier_id
        
# Fetch all products from the database
@app.route("/product")
def product():
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()

    # Create Product objects for each row
    product_list = []
    for row in rows:
        item = ProductItem(row[0], row[1], row[2], row[3],
                       row[4], row[5], row[6], row[7],
                       row[8])
        product_list.append(item)

    # Render template with inventory data
    return render_template("product.html", product=product_list)

# Add new product to the inventory
@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product_code = request.form["product_code"]
        category_id = request.form["category_id"]
        name = request.form["name"]
        date_acquired = request.form["date_acquired"]
        expiration_date = request.form["expiration_date"]
        quantity = int(request.form["quantity"])
        cost = float(request.form["cost"])
        storage_location = request.form["storage_location"]
        supplier_id = request.form["supplier_id"]

        # Insert the new item into the database
        cursor.execute("INSERT INTO product (product_code, category_id, name, date_acquired, expiration_date, quantity, cost, storage_location, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       (product_code, category_id, name, date_acquired, 
                        expiration_date, quantity, cost, storage_location, supplier_id))
        db.commit()

        return redirect("/product")
    else:
        return render_template("add_product.html")
#################### OK

# Edit an existing product item in the table
@app.route("/edit_product/<string:product_code>", methods=["GET", "POST"])
def edit_product(product_code):
    if request.method == "POST":
        product_code = request.form["product_code"]
        category_id = request.form["category_id"]
        name = request.form["name"]
        date_acquired = request.form["date_acquired"]
        expiration_date = request.form["expiration_date"]
        quantity = int(request.form["quantity"])
        cost = float(request.form["cost"])
        storage_location = request.form["storage_location"]
        supplier_id = request.form["supplier_id"]

        # Update the item in the database
        cursor.execute("UPDATE product SET product_code=%s, category_id=%s, name=%s, date_acquired=%s, expiration_date=%s, quantity=%s, cost=%s, storage_location=%s, supplier_id=%s WHERE product_code=%s", 
                       (product_code, category_id, name, date_acquired, expiration_date, quantity, cost, storage_location, supplier_id, product_code))
        db.commit()

        return redirect("/product")
    else:
        cursor.execute("SELECT * FROM product WHERE product_code = %s", (product_code,))
        row = cursor.fetchone()
        item = ProductItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

        return render_template("edit_product.html", item=item)
############ OK

# Delete an item from the product table
@app.route("/delete_product/<string:product_code>")
def delete_product(product_code):
    # Delete product from the database
    cursor.execute("DELETE FROM product WHERE product_code = %s", (product_code,))
    db.commit()

    return redirect("/product")
############ OK

######################
# Suppliers
######################

######################
# Categories
######################


if __name__ == "__main__":
    app.run(debug=True)