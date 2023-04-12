from flask import Flask,render_template,request
import mysql.connector as con

conn=con.connect(user="root",password="",host="localhost",port="3306",database="sco")
cur=conn.cursor()
cur.execute("SELECT * FROM flask")
a=cur.fetchall()
print(a)



app=Flask(__name__)
@app.route("/")
def main():
    return render_template('main.html')

@app.route("/details",methods=["post"])
def delt():
    name=request.form.get("name")
    msg=request.form.get("message")
    email=request.form.get("email")
    cur.execute(f"insert into flask values('{name}','{email}','{msg}')")
    conn.commit()

    return name






app.run(debug=True)



