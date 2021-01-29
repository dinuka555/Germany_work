from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '10.4.13.36'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        #lastName = details['lname']
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        cur.execute("INSERT INTO messages(message) VALUES (%s)",(firstName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('web1.html')

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
