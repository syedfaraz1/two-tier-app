from flask import Flask, render_template, request
import mysql.connector
import os
import time

app = Flask(__name__)

# Wait until MySQL starts
time.sleep(10)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "mysql"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", "password"),
    database=os.getenv("DB_NAME", "messagesdb")
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
id INT AUTO_INCREMENT PRIMARY KEY,
message VARCHAR(255)
)
""")

db.commit()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        msg = request.form["message"]

        cursor.execute(
            "INSERT INTO messages(message) VALUES(%s)",
            (msg,)
        )

        db.commit()

    cursor.execute("SELECT * FROM messages")
    data = cursor.fetchall()

    return render_template("index.html", messages=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
