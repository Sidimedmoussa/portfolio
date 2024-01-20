from flask import Flask, render_template, request, redirect, url_for

from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'portfolio'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)




app = Flask(__name__)

@app.route("/homme")
def index():
    conn = mysql.connect()
    cursor =conn.cursor()

    cursor.execute("SELECT * FROM project")
    projects_data = cursor.fetchall()

    cursor.execute("SELECT * FROM skills")
    skils_data = cursor.fetchall()

    conn.close()
    return render_template("index.html",skils_data =skils_data,projects_data=projects_data)

@app.route("/contact_form",methods=["POST","GET"])
def contact_me():
    if request.method == 'POST':
        name  = request.form.get('name')
        email = request.form.get('email')
        msg   = request.form.get("message")

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO contact (name, email,message) VALUES (%s,%s,%s)",(name,email,msg))
       
        conn.commit()
        conn.close()
    
    return redirect("/homme")
    
app.run(debug=True,port=5001)