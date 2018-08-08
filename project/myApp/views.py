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
#测试模板变量
def index(request):

	# stu = Students.objects.get(id=1)
	stu = Students.objects.all()
	return render(request,"myApp/index.html",{"stu":stu,'str':'abcdefg','list':['python','good']})

#反向解析测试
def good(request):

	return render(request,"myApp/good.html")
#测试模板继承
def main(request):

	return render(request,"myApp/main.html")
def mains(request):

	return render(request,"myApp/mains.html")