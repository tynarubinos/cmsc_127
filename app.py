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
                 id):
        self.product_code = product_code
        self.category_id = category_id
        self.name = name
        self.date_acquired = date_acquired
        self.expiration_date = expiration_date
        self.quantity = quantity
        self.cost = cost
        self.storage_location = storage_location
        self.id = id
        
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
        supplier_id = int(request.form["supplier_id"])

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
        cursor.execute("UPDATE product SET product_code=%s, category_id=%s, name=%s, date_acquired=%s, expiration_date=%s, quantity=%s, cost=%s, storage_location=%s, id=%s WHERE product_code=%s", 
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
class Supplier:
    def __init__(self, 
                 id, 
                 name,
                 address,
                 contact_number):
        self.id = id
        self.name = name
        self.address = address
        self.contact_number = contact_number
        
# Fetch all suppliers from the database
@app.route("/supplier")
def supplier():
    cursor.execute("SELECT * FROM supplier")
    rows = cursor.fetchall()

    # Create Supplier item for each row
    supplier_list = []
    for row in rows:
        item = Supplier(row[0], row[1], row[2], row[3])
        supplier_list.append(item)

    # Render template with inventory data
    return render_template("supplier.html", supplier=supplier_list)
########## OK

# Add new suppliers
@app.route("/add_supplier", methods=["GET", "POST"])
def add_supplier():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        address = request.form["address"]
        contact_number = request.form["contact_number"]

        # Insert the new supplier into the database
        cursor.execute("INSERT INTO supplier (id, name, address, contact_number) VALUES (%s, %s, %s, %s)", 
                       (id, name, address, contact_number))
        db.commit()

        return redirect("/supplier")
    else:
        return render_template("add_supplier.html")
#################### OK

# Edit suppliers
@app.route("/edit_supplier/<int:id>", methods=["GET", "POST"])
def edit_supplier(id):
    if request.method == "POST":
        updated_id = request.form["id"]
        name = request.form["name"]
        address = request.form["address"]
        contact_number = request.form["contact_number"]

        # Update the supplier in the database
        cursor.execute("UPDATE supplier SET id=%s, name=%s, address=%s, contact_number=%s WHERE id=%s", 
                       (id, name, address, contact_number, id))
        db.commit()

        return redirect("/supplier")
    else:
        cursor.execute("SELECT * FROM supplier WHERE id = %s", (id,))
        row = cursor.fetchone()
        item = Supplier(row[0], row[1], row[2], row[3])

        return render_template("edit_supplier.html", item=item)
######### OK     

# Delete a supplier from the supplier table
@app.route("/delete_supplier/<int:id>")
def delete_supplier(id):
    # Delete supplier from the database
    cursor.execute("DELETE FROM supplier WHERE id = %s", (id,))
    db.commit()

    return redirect("/supplier")
######### OK

######################
# Categories
######################
class Category:
    def __init__(self, 
                 id, 
                 name):
        self.id = id
        self.name = name
        
# Fetch all categories from the database
@app.route("/category")
def category():
    cursor.execute("SELECT * FROM category")
    rows = cursor.fetchall()

    # Create Category item for each row
    category_list = []
    for row in rows:
        item = Category(row[0], row[1])
        category_list.append(item)

    # Render template with inventory data
    return render_template("category.html", category=category_list)

# Add new category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        id = int(request.form["id"])
        name = request.form["name"]

        # Insert the new category into the database
        cursor.execute("INSERT INTO category (id, name) VALUES (%s, %s)", (id, name,))
        db.commit()

        return redirect("/category")
    else:
        return render_template("add_category.html")

#################### OK

# Edit category
@app.route("/edit_category/<int:id>", methods=["GET", "POST"])
def edit_category(id):
    if request.method == "POST":
        updated_id = request.form["id"]
        name = request.form["name"]

        # Update the category in the database
        cursor.execute("UPDATE category SET id=%s, name=%s WHERE id=%s",
                       (updated_id, name, id))
        db.commit()

        return redirect("/category")
    else:
        cursor.execute("SELECT * FROM category WHERE id = %s", (id,))
        row = cursor.fetchone()
        item = Category(row[0], row[1])

        return render_template("edit_category.html", item=item)
    
# Delete a category from the category table
@app.route("/delete_category/<int:id>")
def delete_category(id):
    # Delete the category from the database
    cursor.execute("DELETE FROM category WHERE id = %s", (id,))
    db.commit()

    return redirect("/category")
######### OK

if __name__ == "__main__":
    app.run(debug=True)