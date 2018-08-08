from django.contrib import admin
from .models import Grades,Students

# Register your models here.

#页面增添一条Students添加表
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 1

#设置admin站点页面
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    #在添加或者修改班级页添加Students表
    inlines = [StudentsInfo]
    #设置列表属性
    #显示数据库字段
    list_display = ['id','gname','gdate','ggirlnum','gboynum','isDelete']
    #显示过滤器，按班级名过滤
    list_filter = ['gname']
    #设置搜索动作,按班级名搜索
    search_fields = ['gname']
    #设置分页
    list_per_page = 10
    #设置添加、修改页面的属性
    #设置字段的添加或者修改排序
    #fields = []
    #对字段进行分组
    fieldsets = [
        ('str',{'fields':['gname','gdate']}),
        ('num', {'fields': ['ggirlnum', 'gboynum','isDelete']})
                 ]

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    #设置sgender为男或者女
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return '女'
    #修改字段的名字
    gender.short_description = '性别'
    def age(self):
        return self.sage
    age.short_description = '年龄'
    #设置列表属性
    #显示数据库字段
    list_display = ['id','sname',gender,age,'scontend','isDelete','sgrade']
    #显示过滤器，按班级名过滤
    list_filter = ['sname']
    #设置搜索动作,按班级名搜索
    search_fields = ['sname']
    #设置分页
    list_per_page = 10
    #设置执行动作的位置
    actions_on_top = False
    actions_on_bottom = True