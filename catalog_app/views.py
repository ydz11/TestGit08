from django.shortcuts import render
from .models import MyUser
from django.http import HttpResponseRedirect, HttpResponse
import json
import bcrypt

# Create your views here.
def homepage(request):
    context = {
        'vaar1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def my_salt():
    return ('$2b$12$tUimG74HOCBiAA7sm3QX9e').encode('utf-8')

def back_login(request):
    mainuser = request.GET.get('user')
    mainpassword = request.GET.get('passwd')

    bytePwd = mainpassword.encode('utf-8')
    hash = bcrypt.hashpw(bytePwd, my_salt())

    hash_password = hash.decode('utf-8')

    result1 = [{ 'result': 'Success' }]
    result2 = [{ 'result': 'Failure' }]

    if (mainuser == 'user001') and (hash_password == MyUser.objects.values_list('password', flat=True).get(username=mainuser)):
        qs_json = json.dumps(result1[0])
    else:
        qs_json = json.dumps(result2[0])

    return HttpResponse(qs_json, content_type='application/json')