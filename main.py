# from fastapi import FastAPI
# import uvicorn
# from pydantic import BaseModel
# import json
# from fastapi import Request
#
#
# app = FastAPI()
#
# f = open("students.json", mode="r", encoding="utf-8")
# studentxx = json.load(f)
#
#
# def save_file():
#     g = open('students.json', 'a+')
#     json.dump(obj=studentxx, fp=g)
#     g.close()
#
#
# class Students(BaseModel):
#     name: str
#     student_id: str
#     score: float
#
#
# @app.post("/input-student/")
# def input_student(student: Students):
#     studentxx.append(student)
#     # save_file()
#     return studentxx
#
#
# @app.get("/print-student/")
# def print_student(student_code: str):
#     for stud in studentxx:
#         if stud["student_id"] == student_code:
#             return stud
#     return {"Error": "Not student"}


# @app.put("/repair-student/")
# def repair_student(student_code: str, student: Students):
#     for stud in studentxx:
#         if stud["student_id"] == student_code:
#             student.name = stud["name"]
#             student.student_id = stud["student_id"]
#             student.score = stud["score"]
#             return stud
#
# @app.get("/get-student/{student_id}")
# def get_student(student_id: int):
#     return students[student_id]
#
#
# @app.get("/get-by-name/{student_id}")
# def get_student(student_id: int, name: str):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"Data": "Not found"}
#


# uvicorn.run(app, host='127.0.0.1', port=5000)
import mysql


import mysql.connector

mydb = mysql.connector.connect(
    port="6633",
    user="root",
    password="dangduong020309"
)
# code = 'CREATE SCHEMA `TEST11`;'
#
# mycursor = mydb.cursor()
# mycursor.execute(code)
print(mydb)