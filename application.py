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


@application.route('/postpermission', methods=['POST', 'GET'])
def addpermission():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        sl_no = request.json['sl_no']
        name = request.json['name']
        action = request.json['action']
        permission = request.json['permission']
        mycursor.execute("insert into permission_list values(%s,%s,%s,%s)", (sl_no, name, action, permission))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status


@application.route('/getpermission', methods=['POST', 'GET'])
def getpermission():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from permission_list")
        jd = mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"] = jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status


@application.route('/postprofessional', methods=['POST', 'GET'])
def addprofessional():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        employee_id = request.json['employee_id']
        qualification = request.json['qualification']
        passing_year = request.json['passing_year']
        marks = request.json['marks']
        created = request.json['created']
        modified = datetime.datetime.now()
        mycursor.execute("insert into professional values(%s,%s,%s,%s,%s,%s,%s)", (None, employee_id, qualification, passing_year, marks, created, modified))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status


@application.route('/getprofessional', methods=['POST', 'GET'])
def getprofessional():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from professional")
        jd = mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"] = jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status


@application.route('/register', methods=['POST', 'GET'])
def register():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        Id = request.json['Id']
        name = request.json['name']
        husband_or_father_name = request.json['husband_or_father_name']
        DOB = request.json['DOB']
        mobile_no = request.json['mobile_no']
        address = request.json['address']
        state = request.json['state']
        city = request.json['city']
        education_qualification = request.json['education_qualification']
        no_of_sons = request.json['no_of_sons']
        no_of_daughters = request.json['no_of_daughters']
        email_id = request.json['email_id']
        alternate_mobile_no = request.json['alternate_mobile_no']
        field_options = request.json['field_options']
        qualification = request.json['qualification']
        percent = request.json['percent']
        passing_year = request.json['passing_year']
        school = request.json['school']
        designation = request.json['designation']
        From = request.json['From']
        to = request.json['to']
        subject_class = request.json['subject_class']
        duration = request.json['duration']
        date = request.json['date']
        description = request.json['description']
        attachment = request.json['attachment']
        mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Id, name, husband_or_father_name, DOB, mobile_no, address, state, city, education_qualification, no_of_sons, no_of_daughters, email_id, alternate_mobile_no, field_options, qualification, percent, passing_year, school, designation, From, to, subject_class, duration, date, description, attachment))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status


@application.route('/postformstep', methods=['POST', 'GET'])
def addformstep():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        id = request.json['id']
        name = request.json['step_name']
        mycursor.execute("insert into form_step values(%s,%s)", (id, name))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status


@application.route('/getformstep', methods=['POST', 'GET'])
def getformstep():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from form_step")
        jd = mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"] = jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status


@application.route('/postemployee', methods=['POST', 'GET'])
def addemployeedetails():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        id = request.json['id']
        name = request.json['name']
        gender = request.json['gender']
        dob = request.json['dob']
        hire_date = request.json['hire_date']
        salary = request.json['salary']
        department = request.json['department']
        address = request.json['address']
        mycursor.execute("insert into employee_details values(%s,%s,%s,%s,%s,%s,%s,%s)", (id, name, gender, dob, hire_date, salary, department, address))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status


@application.route('/getemployee', methods=['POST', 'GET'])
def getemployeedetails():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from employee_details")
        jd = mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"] = jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status


@application.route('/postexam', methods=['POST', 'GET'])
def addexam():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        id = request.json['id']
        name = request.json['name']
        subject_name = request.json['subject_name']
        date = request.json['date']
        time = request.json['time']
        mycursor.execute("insert into exam_request values(%s,%s,%s,%s,%s)", (id, name, subject_name, date, time))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status


@application.route('/getcv', methods=['POST', 'GET'])
def getcv():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from cvform_field")
        jd = mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"] = jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status


@application.route('/meeting', methods=['POST', 'GET'])
def meeting():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        id = request.json['id']
        name = request.json['name']
        date = request.json['date']
        time = request.json['time']
        mycursor.execute("insert into meeting_request values(%s,%s,%s,%s)", (id, name, date, time))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status


@application.route('/getskill', methods=['POST', 'GET'])
def getskill():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from skill_list")
        jd = mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"] = jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status


@application.route('/getuser', methods=['POST', 'GET'])
def getuser():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from user")
        jd = mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"] = jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status
  

@application.route('/postevent', methods=['POST', 'GET'])
def event():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        title = request.json['title']
        event = request.json['event']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        mycursor.execute("insert into event values(%s,%s,%s,%s,%s)",(None, title, event, start_date, end_date))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status

    
@application.route('/getevent', methods=['POST', 'GET'])
def getevent():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from event")
        jd = mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"] = jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status


if __name__ == "__main__":
    #application.run(debug=True)
    application.run(host='0.0.0.0', port=8080)
