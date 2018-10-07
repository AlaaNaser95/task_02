from django.shortcuts import render

def home(reference):
	context={
	"msg":"Hello World!"
	}
	return render(reference,"hello.html",context)
# Create your views here.
