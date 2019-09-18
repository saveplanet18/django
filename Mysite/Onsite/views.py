from django.shortcuts import render,HttpResponse
from django.http import HttpResponseNotFound
from django.template import loader
from .form import EmpForm
from .form import eneform
from .funtions.funtions import handle_uploaded_file
from .models import Student
import datetime
from reportlab.pdfgen import canvas
import csv




def home(request):
    return HttpResponse("<h1> hello word</h1>")


def index(request):
    now=datetime.datetime.now()
    html="<html><body><h1> now time is %s</h1></body></html>"%now
    return HttpResponse(html)


def show(request):
    a=1
    if a:
        return HttpResponseNotFound("<h1>page is not found</h1>")
    else:
        return HttpResponse("<h1>page is found</h1>")

def Manju(request):
    return render(request,'index.html')

def edit(request):
    return render(request,'edit.html')



def form1(request):
    stu=EmpForm()

    return render(request,'me.html',{'form':stu})

def Bhumi(request):
    if request.method=='POST':
        bhu=eneform(request.POST,request.FILES)
        if Student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("file upload succfull")
        else:
            bhu = EmpForm()
            return render(request,'bhumi.html',{'form':bhu})
def req(request):
    return HttpResponse("http request is:"+request.method)

def setsession(request):
    request.session['sname']='manjunath'
    request.session['semail']='yarazari10@gmail.com'
    return HttpResponse("set session is set")
def getsession(request):
    studentname=request.session['sname']
    studentemail=request.session['semail']
    return HttpResponse(studentname+""+studentemail)

def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001', 'John', 'Domil', 'CA'])
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
    return response

def getfile(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="file.csv"'
    stu=Student.objects.all()
    writer=csv.writer(response)
    for st in stu:
        writer.writerow([st.first_name,st.last_name,st.contact,st.emial,st.age])
        return response


def pdffile(request):
    response=HttpResponse(content_type='Manju/pdf')
    response['Content-Disposition']='attachment; filename=manju.pdf'
    p=canvas.Canvas(response)
    p.setFont("Times-Roman",55)
    p.drawString(200,700,"hello manjunath kannur")
    p.showPage()
    p.save()
    return response
def boot(request):
    return render(request,"boot.html")




