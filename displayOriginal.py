from flask import Flask, request, jsonify
from flask import render_template
from flask import request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def enterRow():
    conn = sqlite3.connect('userInfo.db')
    
    cursor = conn.cursor()

    table ="""CREATE TABLE IF NOT EXISTS USER(id INT, mInc int, mExp int);"""
    cursor.execute(table)

    #cursor.execute('''INSERT INTO USER VALUES ('4', 'Arnav', 'Aidan')''') 
    #cursor.execute('''INSERT INTO USER VALUES ('5', 'Inor', 'Billy')''') 
    #cursor.execute('''INSERT INTO USER VALUES ('6', 'Sean', 'Joseph')''')

    print("Data Inserted in the table: ") 
    data=cursor.execute('''SELECT * FROM USER''') 
    for row in data: 
        print(row)

    conn.commit()
    # conn.close()




enterRow()


@app.route("/", methods = ["POST"])
def info():
    
    if request.method == 'POST':
        con = sqlite3.connect('userId.db')
        try:
            # mInc = request.form['mInc']     
            # mExp = request.form['mExp']
            json = request.get_json()
            mInc = json['mInc']
            mExp = json['mExp']
            
            print('cursor')
            cur = con.cursor()
            print('execute')
            cur.execute("INSERT INTO USER (id, mInc, mExp) VALUES (5," + str(mInc) + ", " + str(mExp) + ",?)")
            print('commit')
            con.commit()
            print('done')
            return jsonify({'msg': "Record Successfully Added To Database"})
        except:
            con.rollback()
            print('ERROR')
        
        finally:
            con.close()
            
    return {
        "status": 500,
        "msg": "oops"
    }
            
            