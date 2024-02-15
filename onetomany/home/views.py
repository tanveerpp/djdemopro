from django.shortcuts import render
from .models import Student,Trainer
def home(request):
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
def addstudent(request):
    s=Student()
    s.sname=request.POST['sname']
    s.branch=request.POST['branch']
    tid=request.POST['trainer']
    t=Trainer.objects.get(id=tid)
    s.trainer=t
    s.save()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
def updatestudent(request):
    s=Student()
    s.id=request.POST['id']
    s.sname=request.POST['sname']
    s.branch=request.POST['branch']
    tid=request.POST['trainer']
    t=Trainer.objects.get(id=tid)
    s.trainer=t
    s.save()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
def deletestudent(request):
    id=request.GET['id']
    Student.objects.get(id=id).delete()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
def addtrainer(request):
    t=Trainer()
    t.tname=request.POST['name']
    t.spcl=request.POST['spcl']
    t.save()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
def updatetrainer(request):
    t=Trainer()
    t.id=request.POST['id']
    t.tname=request.POST['name']
    t.spcl=request.POST['spcl']
    t.save()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
def home(request):
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
def deletetrainer(request):
    id=request.GET['id']
    Trainer.objects.get(id=id).delete()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})