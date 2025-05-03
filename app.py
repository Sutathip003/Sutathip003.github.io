from flask import Flask, request, render_template, redirect
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__) 
file_path = "D:\\MySQL_connection\\Mysql_connectrion.txt"

# Open homepage ("/")
@app.route("/", methods=["GET"])
def home():
    print("Entry the page")
    return render_template("index.html")
    

# Fill data on main page
@app.route("/submit_bp", methods=["POST"])
def submit_bp():
    systolic = request.form["systolic"]
    diastolic = request.form["diastolic"]
    pulse = request.form["pulse"]
    note = request.form["note"]
    recorded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Store data to MySQL

    conn_info = {}
    try:
        # Open MySQL connection file
    
        with open(file_path, "r") as file:
            for line in file:
                if "=" in line :
                    key, value = line.strip().split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"')
                    conn_info[key] = value
                
    # Connect to MySQL
        db = mysql.connector.connect(
            host = conn_info["host"],
            user = conn_info["user"],
            password = conn_info["password"],
            database = conn_info["database"]
        )
    
        if db.is_connected():
            print("Successfully connected to MySQL!")
  
        else:
            print("Failed to connect to MySQL.")

        cursor = db.cursor()
    
        # Insert into database
        sql = "INSERT INTO bp_tracker (Date, Systolic, Diastolic, Pulse, Note) VALUES (%s, %s, %s, %s, %s) "
        val = (recorded_at, systolic, diastolic, pulse,note,)
        cursor.execute(sql, val)
        db.commit()

        cursor.close()
        db.close()

        print("Commit successful")

        return redirect("/")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return "Database Error: {e}", 500