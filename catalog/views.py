from django.shortcuts import render,redirect
from .forms import bookform,musicform
from .models import Books,Music
# Create your views here.
def index(request):
	template='index.html'
	return render(request,template)

def addbook(request):
	
	if request.method=='POST':
		form=bookform(request.POST)
		if form.is_valid():
			p=form.save()
			return redirect('urls:showbook')
			
	else:
		form=bookform()
		context={'form':form}
		template='addbook.html'
	return render(request,template,context)

def addmusic(request):
	
	if request.method=='POST':
		form=musicform(request.POST)
		if form.is_valid():
			p=form.save()
			return redirect('urls:showmusic')
			
	
	else:
		form=musicform()		
		template='addmusic.html'
		context={'form':form}
	return render(request,template,context)

def showbook(request):
	start=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	display=Books.objects.all()
	title='book'
	return render(request,'show.html',{'display':display,'title':title,'start':start})

def showmusic(request):
	start=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	display=Music.objects.all()
	title='music'
	return render(request,'show.html',{'display':display,'title':title,'start':start})


def showbookorder(request,a):
	
	display=Books.objects.all().filter(title__startswith=a)
	title='book'
	return render(request,'showorder.html',{'display':display,'title':title})

def showmusicorder(request,a):

	#display=Music.objects.all()
	#start=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#if display[0].title__startswith='a':
	display=Music.objects.all().filter(title__startswith=a)
	title='music'
	return render(request,'showorder.html',{'display':display,'title':title})



	