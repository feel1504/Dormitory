import re
from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import *
from django.http import HttpResponse
# Create your views here.
def denglu(request):
    return render(request,'index.html')

def zhuce(request):
    return render(request,'zhuce.html')

def login(request):
    user_name = request.POST.get("username")
    user_password = request.POST.get("password")
    names = Myuser.objects.filter(username=user_name)
    error_msg = '用户名或密码不正确'
    if len(names) == 1:
        if names[0].username == user_name and names[0].password == user_password and re.match("[\u4e00-\u9fa5]+",user_name):
            pay_am = Student.objects.filter(sname__contains=user_name).values("waijian__pay__pay_amount","waijian__pay__yongshuiliang","waijian__pay__yongdianliang")
            content = {"content":pay_am,"user":user_name}
            print(content)
            return render(request,"qiantai.html",content)
        elif names[0].username == user_name and names[0].password == user_password:
            response = redirect("/student/1")
            response.set_cookie("user",user_name)
            return response
        else:
            return render(request,'index.html',{'error_msg':error_msg})
    else:
        return render(request,'index.html',{'error_msg':error_msg})

def register(request):
    user_name = request.POST.get('username')
    user_password = request.POST.get('password')
    user_repassword = request.POST.get('repassword')
    if not user_password or not user_repassword or not user_name:
        error_msg = '密码或用户名不能为空'
    elif user_password != user_repassword:
        error_msg = '密码不一致'
    elif Myuser.objects.filter(username=user_name):
        error_msg = '用户名已存在'
    else:
        user = Myuser()
        user.username = user_name
        user.password = user_password
        try:
            user.save()
            return render(request,'index.html')
        except:
            return render(request,'zhuce.html')
    return render(request,'zhuce.html',{"error_msg":error_msg})

def add_student(request):
    sno = request.POST.get('sno')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    dept = request.POST.get('dept')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    stype = request.POST.get('type')
    intime = request.POST.get('intime')
    outtime = request.POST.get('outtime')
    user = Student()
    user.sno = sno
    user.sname = name
    user.ssex = sex
    user.sage = age
    user.sdept = dept
    user.smajor = major
    user.sgrade = grade
    user.stype = stype
    user.sintime = intime
    user.souttime = outtime
    try:
        user.save()
    except Exception as a:
        print(a)
    return redirect('/student/1')

def list_student(request,ye):
    all_student = Student.objects.all()
    student_page = Paginator(all_student,2)
    pages = student_page.page(int(ye))
    username = request.COOKIES['user']
    content = {"all":pages,'user':username}
    return render(request,'houtai.html',content)

def edit_student(request,id):
    sid = int(id)
    student = Student.objects.filter(id=sid)
    student = student[0]
    sno = request.POST.get('sno')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    dept = request.POST.get('dept')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    stype = request.POST.get('type')
    intime = request.POST.get('intime')
    outtime = request.POST.get('outtime')

    student.sno = sno
    student.sname = name
    student.ssex = sex
    student.sage = age
    student.sdept = dept
    student.smajor = major
    student.sgrade = grade
    student.stype = stype
    student.sintime = intime
    student.souttime = outtime
    try:
        student.save()
    except Exception as a:
        print(a)
    return redirect("/student/1")

def del_student(request,id):
    sid = int(id)
    student = Student.objects.filter(id=sid)
    try:
        student.delete()
    except:
        pass
    return redirect('/student/1')

#--------------------------------------------------------

def list_emp(request,ye):
    all_emp = Admin.objects.all()
    emp_page = Paginator(all_emp,2)
    pages = emp_page.page(int(ye))
    username = request.COOKIES['user']
    content = {"all":pages,'user':username}
    return render(request,'suse_admin.html',content)
def add_emp(request):
    emp_num = request.POST.get('sno')
    emp_name = request.POST.get('name')
    emp_sex = request.POST.get('sex')
    emp_age = request.POST.get('age')
    emp = Admin()
    emp.emp_num = emp_num
    emp.emp_name = emp_name
    emp.emp_sex = emp_sex
    emp.emp_age = emp_age
    try:
        emp.save()
    except:
        pass
    return redirect('/emp/1')
def del_emp(request,id):
    eid = int(id)
    admin = Admin.objects.filter(id=eid)
    print(admin)
    try:
        admin.delete()
    except:
        pass
    return redirect('/emp/1')
def edit_emp(request,id):
    eid = int(id)
    admin = Admin.objects.filter(id=eid)
    admin = admin[0]
    sno = request.POST.get('sno')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    admin.emp_num = sno
    admin.emp_name = name
    admin.emp_sex = sex
    admin.emp_age = age
    admin.save()
    try:
        admin.save()
    except:
        pass
    return redirect('/emp/1')

#-------------------------------------
def add_dor(request):
    num = request.POST.get('sno')
    louhao = request.POST.get('name')
    quhao = request.POST.get('sex')
    cenghao = request.POST.get('age')
    sushehao = request.POST.get('dept')
    max_occ = request.POST.get('major')
    occ = request.POST.get('grade')
    phone = request.POST.get('type')

    dor = Dormitory()
    dor.sushe_num = num
    dor.louhao = louhao
    dor.quhao = quhao
    dor.cenghao= cenghao
    dor.sushehao= sushehao
    dor.max_occupancy  = max_occ
    dor.occupancy = occ
    dor.telephone = phone
    try:
        dor.save()
    except Exception as a:
        print(a)
    return redirect('/dor/1')

def list_dor(request,ye):
    all_dor = Dormitory.objects.all()
    dor_page = Paginator(all_dor,2)
    pages = dor_page.page(int(ye))
    username = request.COOKIES['user']
    content = {"all":pages,'user':username}
    return render(request,'dormitory.html',content)

def edit_dor(request,id):
    sid = int(id)
    dor = Dormitory.objects.filter(id=sid)
    dor = dor[0]
    num = request.POST.get('sno')
    louhao = request.POST.get('name')
    quhao = request.POST.get('sex')
    cenghao = request.POST.get('age')
    sushehao = request.POST.get('dept')
    max_occ = request.POST.get('major')
    occ = request.POST.get('grade')
    phone = request.POST.get('type')


    dor.sushe_num = num
    dor.louhao = louhao
    dor.quhao = quhao
    dor.cenghao = cenghao
    dor.sushehao = sushehao
    dor.max_occupancy = max_occ
    dor.occupancy = occ
    dor.telephone = phone
    try:
        dor.save()
    except Exception as a:
        print(a)
    return redirect("/dor/1")

def del_dor(request,id):
    sid = int(id)
    dor = Dormitory.objects.filter(id=sid)
    try:
        dor.delete()
    except:
        pass
    return redirect('/dor/1')
#------------------------------

def list_pay(request,ye):
    all_pay = Pay.objects.all()
    pay_page = Paginator(all_pay,2)
    pages = pay_page.page(int(ye))
    username = request.COOKIES['user']
    content = {"all":pages,'user':username}
    return render(request,'pay.html',content)
def add_pay(request):
    pay_am = request.POST.get('sno')
    shui = request.POST.get('name')
    dian = request.POST.get('sex')
    pay = Pay()
    pay.pay_amount = pay_am
    pay.yongdianliang = dian
    pay.yongshuiliang = shui
    try:
        pay.save()
    except:
        pass
    return redirect('/pay/1')
def del_pay(request,id):
    pid = int(id)
    pay = Pay.objects.filter(id=pid)
    try:
        pay.delete()
    except:
        pass
    return redirect('/pay/1')
def edit_pay(request,id):
    pid = int(id)
    pay = Pay.objects.filter(id=pid)
    pay = pay[0]
    sno = request.POST.get('sno')
    name = request.POST.get('name')
    sex = request.POST.get('sex')

    pay.pay_amount = sno
    pay.yongshuiliang = name
    pay.yongdianliang = sex
    try:
        pay.save()
    except:
        pass
    return redirect('/pay/1')

#------------------------------

def list_repair(request,ye):
    all_repair = Repair.objects.all()
    repair_page = Paginator(all_repair,2)
    pages = repair_page.page(int(ye))
    username = request.COOKIES['user']
    content = {"all":pages,'user':username}
    return render(request,'repair.html',content)
def add_repair(request):
    sushe = request.POST.get('sno')
    people = request.POST.get('name')
    data = request.POST.get('sex')
    reason  = request.POST.get('age')
    repair = Repair()
    repair.sushe = sushe
    repair.people = people
    repair.data = data
    repair.reason = reason
    try:
        repair.save()
    except:
        pass
    return redirect('/repair/1')
def del_repair(request,id):
    rid = int(id)
    repair = Repair.objects.filter(id=rid)
    try:
        repair.delete()
    except:
        pass
    return redirect('/repair/1')
def edit_repair(request,id):
    rid = int(id)
    repair = Repair.objects.filter(id=rid)
    repair = repair[0]
    sno = request.POST.get('sno')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    age = request.POST.get('age')

    repair.sushe = sno
    repair.people = name
    repair.data = sex
    repair.reason = age
    try:
        repair.save()
    except:
        pass
    return redirect('/repair/1')

#--------------------------------------
def search_data(request):
    param = request.POST.get("content")
    if len(param) == 14:
        results = Student.objects.filter(sno=param).values("sno", "sname", "ssex", "sage",
                                                           "waijian__dormitory__sushe_num",
                                                           "waijian__dormitory__louhao", "waijian__dormitory__quhao",
                                                           "waijian__dormitory__telephone", "waijian__repair__reason")
    elif param[-2:]=="缴费":
        param = param[:-2]
        app = 1
        results = Student.objects.filter(sno=param).values("sno", "sname", "ssex", "sage",
                                                           "waijian__dormitory__sushe_num",
                                                           "waijian__dormitory__louhao", "waijian__dormitory__quhao",
                                                           "waijian__pay__pay_amount","waijian__pay__yongshuiliang",
                                                           "waijian__pay__yongdianliang",
                                                           "waijian__dormitory__telephone")
    elif re.match('[\4e00-\u9fa5]+',param):
        results = Student.objects.filter(sname__contains=param).values("sno","sname","ssex","sage","waijian__dormitory__sushe_num",
        "waijian__dormitory__louhao", "waijian__dormitory__quhao",
                  "waijian__dormitory__telephone", "waijian__repair__reason")


    elif len(param)==6:
        results_A = Admin.objects.filter(emp_num=param).values("emp_num","emp_name","emp_sex","emp_age",'waijian__dormitory__louhao',
                                                             'waijian__dormitory__quhao')
    else:
        pass
    username = request.COOKIES['user']
    content = {"results":results,"user":username,"param":app}
    return render(request,"search.html",content)
