from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="change_this_strong_password",
        database="exampledb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return  f"<h1>On persnonoitu nyt ja tässä sinulle kellonaika, jonka saat päivitettyä sivua päivittämällä {result[0]}</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
