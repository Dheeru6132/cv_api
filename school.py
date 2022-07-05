from flask import Flask, request
import mysql.connector
import datetime
import json

application = Flask(__name__)
app = application
jd = mysql.connector.connect(
    host='portalcv.cc4euyfhpe3u.us-east-1.rds.amazonaws.com',
    user='admin',
    password='dj756132',
    database='portalcv'
)
mycursor = jd.cursor()
data_status = {"responseStatus": 0, "results": ""}


@application.route('/forschool', methods=['POST', 'GET'])
def forschool():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        reason = request.json['reason']
        date = datetime.datetime.now()
        time = datetime.datetime.now()
        mycursor.execute("insert into temporary_school values(%s,%s,%s,%s,%s)", (firstname, lastname, reason, date, time))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status


if __name__ == "__main__":
    #application.run(debug=True)
    application.run(host='0.0.0.0', port=8080)
