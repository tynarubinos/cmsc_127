# DBSoria

This is a Python application called DBSoria. It allows you to manage inventory items by providing functionalities to add, delete, edit, and view items. The application utilizes the Flask framework for the web interface and MySQL for the database.

### Requirements

Make sure you have the following requirements installed on your system:

- Python
- Pip
- Flask (Install with `pip install Flask`)
- MySQL

### Installation

To install the necessary libraries, run the following command:

```
pip install flask mysql-connector-python
```

This will install Flask and the MySQL Connector Python library, which are required for running the application.

### Usage

1. Clone or download the DBSoria repository to your local machine.

2. Make sure you have MySQL installed and running. Set up the necessary database and tables using the provided SQL script (`inventory.sql`).

3. Open a terminal or command prompt and navigate to the directory where you have cloned or downloaded the repository.

4. Run the following command to start the application:

   ```
   python app.py
   ```

   This will start the Flask development server.

5. Open your web browser and enter the following URL:

   ```
   http://localhost:5000
   ```

   The DBSoria application will be accessible through this URL.

6. You can now use the application to add, delete, edit, and view items in the inventory.

Feel free to explore and customize the application according to your needs.

**Note:** Remember to configure the database connection settings in the `app.py` file to match your MySQL database credentials.
