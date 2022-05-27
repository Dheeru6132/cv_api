from flask import Flask, request
import mysql.connector
import datetime

application=Flask(__name__)
app = application
jd=mysql.connector.connect(
        host='cv-portal.cc4euyfhpe3u.us-east-1.rds.amazonaws.com',
        user='admin',
        password='Dheeru6132',
        database='registration'
    )
mycursor = jd.cursor()
data_status = {"responseStatus": 0, "results": ""}
@application.route('/postpermission',methods=['POST','GET'])
def addpermission():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        sl_no = request.form['sl_no']
        name = request.form['name']
        action = request.form['action']
        permission = request.form['permission']
        mycursor.execute("insert into permission_list values(%s,%s,%s,%s)", (sl_no, name, action, permission))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status

@app.route('/getpermission',methods=['POST','GET'])
def getpermission():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from permission_list")
        jd= mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"] = jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status

@app.route('/postprofessional',methods=['POST','GET'])
def addprofessional():
    global data_status
    if request.method == 'POST':
        data_status={"responseStatus":0,"results":""}
        employee_id = request.form['employee_id']
        qualification = request.form['qualification']
        passing_year = request.form['passing_year']
        marks = request.form['marks']
        created = request.form['created']
        modified = datetime.datetime.now()
        mycursor.execute("insert into professional values(%s,%s,%s,%s,%s,%s,%s)",(None,employee_id,qualification,passing_year,marks,created,modified))
        jd.commit()
        data_status["responseStatus"]=1
        data_status["results"]="success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status

@app.route('/getprofessional',methods=['POST','GET'])
def getprofessional():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from professional")
        jd=mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"]=jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status

@app.route('/result',methods=['POST','GET'])
def result():
    global data_status
    if request.method=='POST':
        data_status = {"responseStatus": 0, "results": ""}
        Id=request.form['Id']
        name=request.form['name']
        husband_or_father_name=request.form['husband_or_father_name']
        DOB=request.form['DOB']
        mobile_no=request.form['mobile_no']
        address=request.form['address']
        state=request.form['state']
        city=request.form['city']
        education_qualification=request.form['education_qualification']
        no_of_sons=request.form['no_of_sons']
        no_of_daughters=request.form['no_of_daughters']
        email_id=request.form['email_id']
        alternate_mobile_no=request.form['alternate_mobile_no']
        field_options=request.form['field_options']
        qualification=request.form['qualification']
        percent=request.form['percent']
        passing_year=request.form['passing_year']
        school=request.form['school']
        designation=request.form['designation']
        From=request.form['From']
        to=request.form['to']
        subject_class=request.form['subject_class']
        duration=request.form['duration']
        date=request.form['date']
        description=request.form['description']
        attachment=request.form['attachment']
        mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Id,name,husband_or_father_name,DOB,mobile_no,address,state,city,education_qualification,no_of_sons,no_of_daughters,email_id,alternate_mobile_no,field_options,qualification,percent,passing_year,school,designation,From,to,subject_class,duration,date,description,attachment))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status

@app.route('/postformstep',methods=['POST','GET'])
def addformstep():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        id = request.form['id']
        name = request.form['step_name']
        mycursor.execute("insert into form_step values(%s,%s)",(id,name))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status

@app.route('/getformstep',methods=['POST','GET'])
def getformstep():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from form_step")
        jd=mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"]=jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status

@app.route('/postemployee',methods=['POST','GET'])
def addemployeedetails():
    global data_status
    if request.method == 'POST':
        data_status = {"responseStatus": 0, "results": ""}
        id = request.form['id']
        name = request.form['name']
        gender = request.form['gender']
        dob = request.form['dob']
        hire_date = request.form['hire_date']
        salary = request.form['salary']
        department = request.form['department']
        address = request.form['address']
        mycursor.execute("insert into employee_details values(%s,%s,%s,%s,%s,%s,%s,%s)", (id, name, gender, dob, hire_date, salary, department, address))
        jd.commit()
        data_status["responseStatus"] = 1
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status

@app.route('/getemployee',methods=['POST','GET'])
def getemployeedetails():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from employee_details")
        jd=mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"]=jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status

@app.route('/postexam',methods=['POST','GET'])
def addexam():
    global data_status
    if request.method == 'POST':
        data_status={"responseStatus":0,"results":""}
        id = request.form['id']
        name = request.form['name']
        subject_name=request.form['subject_name']
        date = request.form['date']
        time = request.form['time']
        mycursor.execute("insert into exam_request values(%s,%s,%s,%s,%s)", (id, name, subject_name, date, time))
        jd.commit()
        data_status["responseStatus"]=1
        data_status["results"]="success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status

@app.route('/getcv',methods=['POST','GET'])
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

@app.route('/meeting',methods=['POST','GET'])
def meeting():
    global data_status
    if request.method == 'POST':
        data_status={"responseStatus":0,"results":""}
        id = request.form['id']
        name = request.form['name']
        date= request.form['date']
        time= request.form['time']
        mycursor.execute("insert into meeting_request values(%s,%s,%s,%s)",(id,name,date,time))
        dj.commit()
        data_status["responseStatus"]=1
        data_status["results"]="success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Required fields are missing"
        return data_status

@app.route('/getskill',methods=['POST','GET'])
def getskill():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from skill_list")
        jd=mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"]=jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status

@app.route('/getuser',methods=['POST','GET'])
def getuser():
    global data_status
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from user")
        jd=mycursor.fetchall()
        data_status["responseStatus"] = 1
        data_status["details"]=jd
        data_status["results"] = "success"
        return data_status
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status

if __name__=="__main__":
    app.run(debug=True)
