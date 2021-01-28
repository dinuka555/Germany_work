from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '10.4.13.36'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ' '
app.config['MYSQL_DB'] = 'satdata'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        location = details['UK']
        orbit = details['59.7']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO satdata(location, orbit) VALUES (%s, %s)", (location, orbit))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return "Hello from Python!"


if __name__ == '__main__':
    app.run()
