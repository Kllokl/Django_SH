from django.shortcuts import render, HttpResponse, redirect

from index.models import user_info


# Create your views here.


def info_list(request):
    # u_info = user_info.objects.filter(id=1).first()
    all_user = user_info.objects.all()

    return render(request,'info_list.html',{"info_list":all_user})

def user_add(request):

    if request.method == 'GET':
        return render(request,'user_add.html',{"msg":''})
    elif request.method == 'POST':
        post_get = request.POST
        user_name = post_get.get('name')
        user_password = post_get.get('password')
        user_info.objects.create(user=user_name,password=user_password)
        if user_info.objects.filter(user=user_name).first():
            return redirect('/user/info_list/')
        else:
            msg = '填写错误'
            return render(request,'user_add.html',{'msg': msg })

def user_del(request):
    nid = request.GET.get('nid')
    user_info.objects.filter(id=nid).delete()
    return redirect('/user/info_list/')

def reset_password(request):
    nid = request.GET.get('nid')
    user_info.objects.filter(id=nid).update(password='123456')
    return redirect('/user/info_list/')

def edit_account(request,nid):

    if request.method == 'GET':
        row_object = user_info.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'nid': row_object})

    new_name = request.POST.get('name')
    print(new_name)
    user_info.objects.filter(id=nid).update(user=new_name)

    return redirect('/user/info_list/')

