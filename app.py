from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="dbsorya_db"
)

# Create a cursor to interact with the database
cursor = db.cursor()

# Define the data model
class InventoryItem:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

# Home page to display all inventory items
@app.route("/")
def home():
    # Fetch all items from the database
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()

    # Create InventoryItem objects for each row
    inventory_items = []
    for row in rows:
        item = InventoryItem(row[0], row[1], row[2], row[3])
        inventory_items.append(item)

    # Render the template with the inventory data
    return render_template("home.html", inventory=inventory_items)

# Add new item to the inventory
@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        name = request.form["name"]
        quantity = int(request.form["quantity"])
        price = float(request.form["price"])

        # Insert the new item into the database
        cursor.execute("INSERT INTO inventory (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
        db.commit()

        return redirect("/")
    else:
        return render_template("add.html")

# Edit an existing item in the inventory
@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    if request.method == "POST":
        name = request.form["name"]
        quantity = int(request.form["quantity"])
        price = float(request.form["price"])

        # Update the item in the database
        cursor.execute("UPDATE inventory SET name=%s, quantity=%s, price=%s WHERE id=%s", (name, quantity, price, item_id))
        db.commit()

        return redirect("/")
    else:
        # Fetch the item from the database
        cursor.execute("SELECT * FROM inventory WHERE id = %s", (item_id,))
        row = cursor.fetchone()
        item = InventoryItem(row[0], row[1], row[2], row[3])

        return render_template("edit.html", item=item)

# Delete an item from the inventory
@app.route("/delete/<int:item_id>")
def delete_item(item_id):
    # Delete the item from the database
    cursor.execute("DELETE FROM inventory WHERE id = %s", (item_id,))
    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)