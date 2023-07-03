from django.shortcuts import render
from myfiles.models import Student

# Create your views here.

def asosiy_sahifa(malumot):

    return render(malumot, 'index.html')



def studentlar_sahifa(malumot):
    talabalar = Student.objects.all()
    return render(malumot, 'studentlar.html',{"studentlar":talabalar})

def delete_student(malumot,id):
    Student.objects.get(id=id).delete()
    talabalar = Student.objects.all()
    return render(malumot, 'studentlar.html', {"studentlar": talabalar})
"""
CRUD
C --- CREATE --- YARATMOQ
R --- READ   --- O'QIMOQ
U --- UPDATE --- YANGILAMOQ
D --- DELETE --- O'CHIRMOQ


"""