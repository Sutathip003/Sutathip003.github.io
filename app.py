from flask import Flask, request, render_template, redirect
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)

# Open homepage ("/")
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Fill data on main page
@app.route("/submit_bp", methods=["POST"])
def submit_bp():

    # Get data from form
    # recorded_at = datetime.strptime(date, "%Y-%m-%dT%H:%M")  
    systolic = request.form["systolic"]
    diastolic = request.form["diastolic"]
    pulse = request.form["pulse"]
    note = request.form["note"]

    recorded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Store data to MySQL
    password_Str = request.form["db_password"]

    try:
    # Connect to MySQL
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password_Str,
        database="health_tracker"  
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
        return "Database Error", 500






