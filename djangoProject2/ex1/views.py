from django.shortcuts import render

# Create your views here.

def router_view(request):
	return render(request,'router.html',{})

def router_list(request):
	return render(request,'router_list.html',{})

def router_edit(request,id):
	return render(request,'routeredit.html',{"routerid":id})