from flask import Flask
from flask import request

# Import Clients
from clients.data_parser import DataParser
from clients.sql_client import SQLClient

import sys
import json
import os
from threading import Thread

# Setup flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./uploads"

isUploading = False

@app.route("/api/update_course_data", methods=["POST"])
def update_course_data():
    if 'file' not in request.files:
        return '{success: false}'

    file = request.files['file']
    if file.filename == '':
        return '{success: false}'
    elif file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], "data." + file.filename.rsplit('.', 1)[1].lower()))
        Thread(target = update_db, args=(file.filename, )).start()
        return '{success: true}'


@app.route("/api/all_courses", methods=["GET"])
def all_courses():
    sql_client = SQLClient()
    output = sql_client.get_all_courses()
    sql_client.close()

    return output

# Helper Functions

# Confirms that file is of the right type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv', 'json', 'html'}

# Updates the contents of the db
def update_db(filename):
    sql_client = SQLClient()
    sql_client.drop_tables()
    sql_client.create_tables()
    parser = DataParser("uploads/data." + filename.rsplit('.', 1)[1].lower())
    print(parser)
    sql = SQLClient()
    parser.dump_to_db(sql)

# Functions for verifying and parsing GET/POST parameters
def get_filtered_courses_parameters():
    info = request.args.get('info')
    collisions = request.args.get('collisions')
    autofill = request.args.get('autofill')
    lecture_day = request.args.get('lecture_day')
    seminar_lab_day = request.args.get('seminar_lab_day')
    exam_day = request.args.get('exam_day')
    level = request.args.get('level')
    credit = request.args.get('credit')
    prof = request.args.get('prof')

    if info is not None:
        info = info.lower() in ["true", ]

    if collisions is not None:
        collisions = collisions.lower() in ["true", ]
   
    if autofill is not None:
        autofill = autofill.split(",")
        autofill = {int(a) for a in autofill}

    if lecture_day is not None:
        lecture_day = lecture_day.split(",")
        lecture_day = [lecture.split("-") for lecture in lecture_day]

    if seminar_lab_day is not None:
        seminar_lab_day = seminar_lab_day.split(",")
        seminar_lab_day = [seminar.split("-") for seminar in seminar_lab_day]

    if exam_day is not None:
        exam_day = exam_day.split(",")

    if level is not None:
        level = level.split(",")
        level = {int(a) for a in level}

    if credit is not None:
        credit = credit.split(",")

    if prof is not None:
        prof = str(prof)

    return (info, collisions, autofill, lecture_day, seminar_lab_day, exam_day, level, credit, prof)

# Start dev server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
