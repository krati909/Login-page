from django.db import connection
from django.shortcuts import render


def start(request):
    return render(request, "login.html")
def register(request):
    return render(request, "signup.html")


def signup(request):
    name = request.GET['name']
    email = request.GET['email']
    password = request.GET['psw']
    mobile_no = request.GET['mobile_no']
    data = {"name":name, "email": email, "password": password, "mobile_no": mobile_no}
    cursor = connection.cursor()

    try:
    # to insert the data into database
        query = "insert into users(name,email,password,mobile_no) values (%s,%s,%s,%s)"
        value = (name,email, password, mobile_no)
        cursor.execute(query, value)
        return render(request, "sucessful_login_in.html", data)
    except:

        return render(request, "signup.html",)




def login(request):
    email = request.GET['email']
    password = request.GET['psw']
    cursor = connection.cursor()
    # to fetch the data from database
    query = "select * from users where email='" + email + "'"
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
        return render(request, "signup.html")
    if row[3]== password:
        data = {"email": row[2], "password": row[3], "mobile_no" :row[4]}
        return render(request, "sucessful_login_in.html", data)
    else:
        return render(request, "login.html")

def operation(request):
    return render(request, "operation.html")

def calculate(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    ope = request.GET['ope']
    if ope=="add":
        ans=num1+num2
        data={"ans":ans}
    elif ope== "sub":
        ans=num1-num2
        data={"ans":ans}
    elif ope=="mul":
        ans=num1*num2
        data={"ans":ans}
    else :
        ans=num1/num2
        data={"ans":ans}
    return render(request, "answer.html",data)