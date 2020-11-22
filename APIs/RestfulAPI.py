import os
from datetime import timedelta

from flask import Flask, request, redirect, session,g
from flask_cors import cross_origin

from Core.Code_Core import Code_Core
from Core.SQLite_Core import SQLite_Core

app = Flask(__name__)

app.secret_key = os.urandom(16)
app.permanent_session_lifetime = timedelta(days=1)

FileSQL = SQLite_Core(r'../Test_Source/File.db', Table_Name='File')
AccountSQL = SQLite_Core(r'../Test_Source/Account.db', Table_Name='Account')

Code_Generate = Code_Core()

'''
全部資料：GET + 名稱
特定資料：GET + 名稱 + id
新增一筆資料：POST + 名稱
修改特定資料：PUT + 名稱 + id
刪除特定資料：DELETE + 名稱 + id
'''


#捕抓例外路徑
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return f'Path : {path} no exist'


@app.route(r'/', methods=['GET', 'POST'])
@cross_origin()
def Main_Page():
    return "Main"


@app.route(r'/Login', methods=['GET', 'POST'])
@cross_origin()
def Login():
    if request.method == "POST":
        print(request.form.get('Email'))
        print(request.form.get('Password'))
        print(request.form.get('Verification_Code'))
    return redirect('http://127.0.0.1:5000/', 302)


@app.route(r'/Logout', methods=['GET'])
@cross_origin()
def Logout():
    session['login_state'] = False
    if request.method == "POST":
        print(request.form.get('Email'))
        print(request.form.get('Password'))
        print(request.form.get('Verification_Code'))
    return redirect('http://127.0.0.1:5000/', 302)


@app.route(r'/Register', methods=['GET', 'POST'])
@cross_origin()
def Register():
    if request.method == "POST":
        print(request.form.get('Email'))
        print(request.form.get('Password'))
        print(request.form.get('ConfirmPassword'))
    return redirect('http://127.0.0.1:5000/Login', 302)


@app.route(r'/Forgot_Password', methods=['GET', 'POST'])
@cross_origin()
def Forgot_Password():
    if request.method == "POST":
        print(request.form.get('Email'))
    return redirect('http://127.0.0.1:5000/Verification_Code', 302)


@app.route(r'/Verification_Code', methods=['GET', 'POST'])
@cross_origin()
def Verification_Code():
    if request.method == "POST":
        print(request.form.get('Verification_Code'))
    return redirect('http://127.0.0.1:5000/Login', 302)


@app.route(r'/Generate_CodeImage', methods=['GET', 'POST'])
@cross_origin()
def Code_Image():
    Image_Base64 = Code_Generate.Generate.Generate_Base64_Image(False)
    print(Image_Base64[0])
    return Image_Base64[1]


if __name__ == "__main__":
    app.run(debug=True)
