from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '10.4.13.36'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'satdata'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        log_time = details['log']
        _ID = details['id']
        orbit = details['or']
        sendfrom = details['send']
        location = details['loc']
        
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        #sql = "INSERT INTO image VALUES (%s)"

        #cur.execute("INSERT INTO messages(message) VALUES ('%s')",(firstName))
        #cur.execute("INSERT INTO messages(message) VALUES ('testdata1')")
        #    cur.execute("INSERT INTO song (title) VALUES ('%s')" %(i,))
        cur.execute("INSERT INTO satdata(messages) VALUES ('%s','%s','%s','%s','%s')" %(log_time,_ID,orbit,sendfrom,location))


        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('web1.html')


@app.route('/', methods=['GET', 'POST'])
def index1():
    if request.method == "POST":
        details = request.form
        log_time = details['log']
        _ID = details['id']
        orbit = details['or']
        sendfrom = details['send']
        location = details['loc']
        
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        #sql = "INSERT INTO image VALUES (%s)"

        #cur.execute("INSERT INTO messages(message) VALUES ('%s')",(firstName))
        #cur.execute("INSERT INTO messages(message) VALUES ('testdata1')")
        #    cur.execute("INSERT INTO song (title) VALUES ('%s')" %(i,))
        cur.execute("INSERT INTO satdata(messages) VALUES ('%s','%s','%s','%s','%s')" %(log_time,_ID,orbit,sendfrom,location))


        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('web1.html')

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
