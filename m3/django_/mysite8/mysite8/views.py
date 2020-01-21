import os

from django.http import HttpResponse
from django.shortcuts import render

from django.conf import settings  #未在配置项内的也可以配置到


def test_upload(request):

    if request.method == 'GET':
        return render(request,'test_upload.html')
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        filename = os.path.join(settings.MEDIA_ROOT,myfile.name)

        with open(filename,'wb') as f:
            data = myfile.file.read()
            f.write(data)
        return HttpResponse('%s 文件上传完毕'%(myfile.name))


def test_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename = "test.csv"'
    import csv
    writer = csv.writer(response)
    writer.writerow(['id','name'])
    res = [{'id':1,'name':'a'},{'id':2,'name':'b'},{'id':3,'name':'c'}]
    for data in res:
        writer.writerow([data['id'],data['name']])
    return response

def test_email(request):
    if request.method=='GET':
        return render(request,'test_email.html')
    elif request.method == 'POST':
        users = request.POST.get('users')
        check_users = users.strip()#去空格
        s_users = [i.split() for i in check_users.split(',')]
        from django.core.validators import validate_email
        try:
            _ = [validate_email(k) for k in s_users]
        except Exception as e:
            return HttpResponse('sorry,you had given wrong email addrs')

