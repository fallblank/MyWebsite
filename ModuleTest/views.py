from django.shortcuts import render

# Create your views here.

def string_test(request):
	string = u'this is a testing string';
	return render(request,'./module_test/test.html',{'string':string})

import os
def for_test(request):
	environment = os.environ
	return render(request,'./module_test/test.html',{'EnvironmentList':environment,'string':'fallblank'})

def dict_test(request):
	info = {'author':'fallblank','email':'fallblank525@gmail.com'}
	return render(request,'./module_test/test.html',{'info':info})

def if_test(request):
	List = map(str,range(0,100))
	return render(request,'./module_test/test.html',{'List':List})