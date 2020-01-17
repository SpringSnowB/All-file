from django.contrib import admin
from .models import Author
# Register your models here.

#将Author类注册后台 注册后 admin后台可以显示该类的对应的表

class AuthorManger(admin.ModelAdmin):
    #规定列表中显示字段
    list_display = ['name','age','desc']
    #规定列表页显示字段中，哪个字段上添加链接
    list_display_links = ['name']
    #列表页 右侧过滤器按照哪个字段进行分类过滤
    list_filter = ['age']
    #列表页中 左上方 搜索栏 按哪些字段进行查找
    search_fields = ['name','age']
    #列表中哪些字段可直接修改 无需进入详情页面;该列表中的属性不可与link中的冲突
    list_editable = ['age','desc']


admin.site.register(Author,AuthorManger)
