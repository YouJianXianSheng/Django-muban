from django.shortcuts import render
from django.http import HttpResponse
from .models import Grades,Students

# Create your views here.
def Index(request):
    return HttpResponse("Hello Python!!!!")

def detail(request,num):
	return HttpResponse("detail-%s"%num)
	
def grades(request):
	#从模型中获取数据
	gradesList = Grades.objects.all()
	#将数据返回至grades.html
	return render(request,"myApp/grades.html",{"grades":gradesList}) 

def students(request):
	#从模型中获取数据
	studentsList = Students.objects.all()
	#将数据返回至grades.html
	return render(request,"myApp/students.html",{"students":studentsList})

def gradesStudents(request,num):
	grade = Grades.objects.get(id=num)
	studentsList = grade.students_set.all()

	return render(request,'myApp/students.html',{'students':studentsList})