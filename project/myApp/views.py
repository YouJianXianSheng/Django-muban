from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Grades,Students
#引入绘图模块
from PIL import Image,ImageDraw,ImageFont
#引入随机变量
import random
import io

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
	return render(request,"myApp/index.html",{'code':'<h1>Hello Python </h1>'})
#反向解析测试
def good(request):
	return render(request,"myApp/good.html")
#测试模板继承
def main(request):
	return render(request,"myApp/main.html")
def mains(request):
	return render(request,"myApp/mains.html")

#测试CSRF
def postfile(request):
	f =request.session.get('verify',True)
	if f == False:
		str = "请再一次输入验证码"
		return render(request,"myApp/postfile.html",{'str':str})
		
	else:
		return render(request,"myApp/postfile.html")

def info(request):
	username = request.POST.get('username')	
	verifycode = request.POST.get('verifycode').upper()
	verify = request.session['verify'].upper()

	if verifycode == verify:
		request.session.clear()
		return render(request,"myApp/info.html",{"username":username})
	else:
		request.session['verify'] = False
		return redirect('/postfile/')
#创建验证码
def verifycode(request):
	#定义变量，用于画面的背景色、宽、高
	bgcolor = (random.randrange(20,100),random.randrange(20,100),
		random.randrange(20,100),random.randrange(20,100))
	width = 100
	hight = 50
	#创建画面对象
	im = Image.new('RGB',(width,hight),bgcolor)
	#创建画笔对象
	draw = ImageDraw.Draw(im)
	#调用画笔的point()函数绘制噪点
	for i in range(0,100):
		xy = (random.randrange(0,width),random.randrange(0,hight))
		fill = (random.randrange(0,255),255,random.randrange(0,255))
		draw.point(xy,fill=fill)
	#定义验证码的被选值
	str = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
	#随机从str中选择4个数
	rand_str = ''
	for i in range(0,4):
		rand_str += str[random.randrange(0,len(str))] 
	#构造字体对象
	font = ImageFont.truetype(r'C:\Windows\Fonts\Arvo-Regular.ttf',38)
	#构造字体颜色
	fontcolor = (255,random.randrange(0,255),random.randrange(0,255))
	#绘制4个字
	draw.text((5,2),rand_str[0],font=font,fill=fontcolor)
	draw.text((25,2),rand_str[1],font=font,fill=fontcolor)
	draw.text((50,2),rand_str[2],font=font,fill=fontcolor)
	draw.text((75,2),rand_str[3],font=font,fill=fontcolor)
	#释放画笔
	del draw
	#存入session，用于进一步验证
	request.session['verify'] = rand_str
	buf = io.BytesIO()
	#将图片保存在内存里，文件类型为png
	im.save(buf,'png')
	#将内存中的图片数据返回到客户端，MIME类型为图片png
	return HttpResponse(buf.getvalue(),'image/png')