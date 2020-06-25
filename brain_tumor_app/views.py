from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from .models import office_details
from .models import client_details
from .models import agent_details
from .models import add_insurance_details
from .models import add_claim_details
from .models import forward_claim_details
from .models import response
from django.contrib.sessions.models import Session
# Create your views here.
def index(request):
    return render(request,'index.html')
def back_office_home(request):
    return render(request,'back_office_home.html')
def agent_home(request):
    return render(request,'agent_home.html',{'aname':request.session['aname']})
def client_home(request):
    return render(request,'client_home.html',{'cname':request.session['cname']})
def client_reg(request):
    return render(request,'client_reg.html')
def agent_reg(request):
    return render(request,'agent_reg.html')
def client_login(request):
    return render(request,'client_login.html')
def agent_login(request):
    return render(request,'agent_login.html')
def back_office_login(request):
    return render(request,'back_office_login.html')
def office_login(request):
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    ad = office_details.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['offname'] = x.username
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return render(request, 'back_office_home.html', {'uname': x.username})
    return render(request, 'back_office_login.html', {'msg': "Incorrect username or password.Try again"})

def office_logout(request):
    # logout(request)
    # return render(request, 'home.html')

    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['offname'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'back_office_login.html')

def client_signup(request):
    db = client_details(fname=request.POST.get('fname'),
                      lname=request.POST.get('lname'), dob=request.POST.get('dob'),
                      gender=request.POST.get('gender'),street=request.POST.get('street'),hname=request.POST.get('hname'),district=request.POST.get('dis'),state=request.POST.get('state'),pincode=request.POST.get('pin'),
                      country=request.POST.get('country'), email=request.POST.get('email'),
                      phone=request.POST.get('phone'),
                      username=request.POST.get('uname'), password=request.POST.get('pass'),status='Inactive')

    db.save()
    return render(request, 'client_reg.html', {'msg': "Successfully Inserted"})

def agent_signup(request):
    db = agent_details(fname=request.POST.get('fname'),
                      lname=request.POST.get('lname'), dob=request.POST.get('dob'),
                      gender=request.POST.get('gender'),street=request.POST.get('street'),hname=request.POST.get('hname'),district=request.POST.get('dis'),state=request.POST.get('state'),pincode=request.POST.get('pin'),
                      country=request.POST.get('country'), email=request.POST.get('email'),
                      phone=request.POST.get('phone'),
                      username=request.POST.get('uname'), password=request.POST.get('pass'),license_num=request.POST.get('lnum'),status='Inactive')

    db.save()
    return render(request, 'agent_reg.html', {'msg': "Successfully Inserted"})

def view_client(request):
    client = client_details.objects.all()
    return render(request, 'view_client.html', {'client': client})

def user_active(request):
    obj = client_details.objects.get(id=request.POST.get('uid'))
    obj.status = 'active'
    obj.save()
    client = client_details.objects.all()
    #cmp = vacancy.objects.all().order_by('-jid')
    return render(request, 'view_client.html', {'msg': 'Successfully Updated','client': client})

def user_inactive(request):
    obj = client_details.objects.get(id=request.POST.get('uid'))
    obj.status = 'Inactive'
    obj.save()
    client = client_details.objects.all()
    #cmp = vacancy.objects.all().order_by('-jid')
    return render(request, 'view_client.html', {'msg': 'Successfully Updated','client': client})

def view_agent(request):
    agent = agent_details.objects.all()
    return render(request, 'view_agent.html', {'agent': agent})


def agent_active(request):
    obj = agent_details.objects.get(id=request.POST.get('uid'))
    obj.status = 'active'
    obj.save()
    agent = agent_details.objects.all()
    #cmp = vacancy.objects.all().order_by('-jid')
    return render(request, 'view_agent.html', {'msg': 'Successfully Updated','agent': agent})

def agent_inactive(request):
    obj = agent_details.objects.get(id=request.POST.get('uid'))
    obj.status = 'Inactive'
    obj.save()
    agent = agent_details.objects.all()
    #cmp = vacancy.objects.all().order_by('-jid')
    return render(request, 'view_agent.html', {'msg': 'Successfully Updated','agent': agent})

def manage_request(request):
    #agent = agent_details.objects.all()
    return render(request, 'manage_request.html', {})

def view_insurance_details(request):
    office = add_insurance_details.objects.all()
    return render(request, 'view_insurance_details.html', {'office':office})

def send_response(request):
    #agent = agent_details.objects.all()
    return render(request, 'send_response.html', {})

def client_signin(request):
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    ad = client_details.objects.all()
    for x in ad:
        if x.username == username and x.password == password and x.status == 'active':
            request.session['cname'] = x.username
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return render(request, 'client_home.html', {'cname': x.username})
    return render(request, 'client_login.html', {'msg': "Incorrect username or password.Try again"})


def client_logout(request):
    # logout(request)
    # return render(request, 'home.html')

    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['cname'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'client_login.html')


def agent_signin(request):
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    ad = agent_details.objects.all()
    for x in ad:
        if x.username == username and x.password == password and x.status == 'active':
            request.session['aname'] = x.username
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return render(request, 'agent_home.html', {'aname': x.username})
    return render(request, 'agent_login.html', {'msg': "Incorrect username or password.Try again"})


def agent_logout(request):
    # logout(request)
    # return render(request, 'home.html')

    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['aname'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'agent_login.html')

def add_insurance(request):
    return render(request,'add_insurance.html')

def agent_add_insurance(request):
    db = add_insurance_details(uid=request.POST.get('uid'),
                      aid=request.POST.get('aid'), aname=request.POST.get('aname'),
                      date=request.POST.get('date'),license_num=request.POST.get('lnum'))

    db.save()
    return render(request, 'add_insurance.html', {'msg': "Successfully Inserted"})

def agent_view_insurance(request):
    aname = request.session['aname']
    cm = agent_details.objects.get(username=aname)

    view = add_insurance_details.objects.filter(aid=cm.id)
    return render(request,'agent_view_insurance.html', {'view1':view})

def view_profile(request):
    aname = request.session['aname']
    agent = agent_details.objects.get(username=aname)
    return render(request, 'view_profile.html', {'agent': agent})

def update_agent_profile(request):
    obj = agent_details.objects.get(username=request.session['aname'])
    obj.fname = request.POST.get('fname')
    obj.password = request.POST.get('pass')
    obj.email = request.POST.get('email')
    obj.phone = request.POST.get('phone')
    obj.save()
    agent = agent_details.objects.get(username=request.session['aname'])
    #cmp = vacancy.objects.all().order_by('-jid')
    return render(request, 'view_profile.html', {'msg': 'Successfully Updated','agent': agent})

def client_view_insurance(request):
    cname = request.session['cname']
    cm = client_details.objects.get(username=cname)

    view = add_insurance_details.objects.filter(uid=cm.id)
    return render(request,'client_view_insurance.html', {'view1':view})

def user_profile(request):
    cname = request.session['cname']
    client = client_details.objects.get(username=cname)
    return render(request, 'user_profile.html', {'client': client})

def update_client_profile(request):
    obj = client_details.objects.get(username=request.session['cname'])
    obj.fname = request.POST.get('fname')
    obj.password = request.POST.get('pass')
    obj.email = request.POST.get('email')
    obj.phone = request.POST.get('phone')
    obj.save()
    client = client_details.objects.get(username=request.session['cname'])
    #cmp = vacancy.objects.all().order_by('-jid')
    return render(request, 'user_profile.html', {'msg': 'Successfully Updated','client': client})


def add_claim(request):
    return render(request, 'add_claim.html')

def claim_values(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fname = uploaded_file.name
        filename = fs.save(fname, uploaded_file)
        uploaded_file_url = fs.url(filename)

    db = add_claim_details(Inid=request.POST.get('Inid'),uid=request.POST.get('uid'), aid=request.POST.get('aid'),image = request.FILES['file'])

    db.save()
    return render(request, 'add_claim.html', {'msg': "Successfully Inserted"})

def user_claim_details(request):
    aname = request.session['aname']
    cm = agent_details.objects.get(username=aname)

    view = add_claim_details.objects.filter(aid=cm.id)
    return render(request,'client_claim_details.html', {'view1':view})

def forward_claim(request):
    db = forward_claim_details(Inid=request.POST.get('Inid'),uid=request.POST.get('uid'), aid=request.POST.get('aid'), image = request.POST.get('image'))
    db.save()
    aname = request.session['aname']
    cm = agent_details.objects.get(username=aname)

    view = add_claim_details.objects.filter(aid=cm.id)
    return render(request, 'client_claim_details.html', {'msg1': "Successfully Forwared",'view1':view})

def forwared_claim_details(request):
    claim = forward_claim_details.objects.all()
    return render(request, 'forwared_claim_details.html', {'claim':claim})

def show_result(request):
    if request.method == 'POST':
       is_private = request.POST.get('file', False)
       uid = request.POST.get('uid')
       #print(is_private)
       import numpy as np
       import cv2
       import matplotlib.pyplot as plt

       img_path = "media/"+is_private
       print(img_path)
       image = cv2.imread(img_path)
       #print("width:{} pixels ".format(image.shape[1]))
       #print("height:{} pixels ".format(image.shape[0]))
       #print("channels:{}".format(image.shape[2]))
       dim = (500, 590)
       image = cv2.resize(image, dim)
       cv2.imshow("new", image)

       gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, 0.7)
       cv2.imshow("gray", gray)

       (T, thresh) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY)
       cv2.imshow("thresh", thresh)

       (T, threshInv) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY_INV)
       cv2.imshow("threshInv", threshInv)

       kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))
       closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
       cv2.imshow("Morphology", closed)

       closed = cv2.erode(closed, None, iterations=14)
       cv2.imshow("MorphologyErrotion", closed)
       closed = cv2.dilate(closed, None, iterations=13)
       cv2.imshow("MorphologyDilation", closed)

       def auto_canny(image):
           lower = 100
           upper = 200
           edged = cv2.Canny(image, lower, upper)
           # return the edged image
           return edged

       canny = auto_canny(closed)
       cv2.imshow("Canny", canny)

       # lap = cv2.Laplacian(img,cv2.CV_64F)
       # cv2.imshow('Edge',lap)

       (cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
       cv2.drawContours(image, cnts, -1, (0, 0, 255), 2)
       cv2.imshow("Tumour or Not", image)
       cv2.waitKey()
       claim = forward_claim_details.objects.all()
       return render(request, 'forwared_claim_details.html', {'claim': claim})
       #return render(request, 'result.html', {'image': image})
       #return HttpResponse(cv2.imshow("Tumour or Not", image))


def save_response(request):
    db = response(uid=request.POST.get('uid'),
                               aid=request.POST.get('aid'),
                               date=request.POST.get('date'), result=request.POST.get('result'))

    db.save()
    return render(request, 'send_response.html', {'msg': "Successfully Inserted"})

def view_claim_result(request):
    cname = request.session['cname']
    cm = client_details.objects.get(username=cname)

    reply = response.objects.filter(uid=cm.id)
    return render(request, 'view_claim_result.html', {'reply': reply})
