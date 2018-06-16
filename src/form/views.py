from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Doctor
from .models import Perasitamol
from .models import Ketorolac
from .models import Fexofenadine
from .models import Ceftriaxone
from .form import Contactform




def home_page(request):

	try:

		if request.method == 'POST':
			contratForm = Contactform(request.POST)
			if contratForm.is_valid():
				m=request.POST['content']
				m = m.replace('(','|')
				m = m.replace('\n','|')
				m = m.replace(')','')
				m = m.replace('\r','')
				m = m.replace('\t','')



				m = m.split('|')


				med = []
				dose = []

				for i in range(0, len(m),2):
				    med.append(m[i])
				    dose.append(m[i+1])


				

				new_comment = Doctor(
									name=request.POST['fullname'],
	    							Email=request.POST['email'],
	    							content=med,content1=dose)
				new_comment.save()


				# database read by email where email == Email
				# get all id
				# Max id
				# id
				# www.fdf/.fdd/gg/id"""Peracitamol (2-0-1)
	                                   #Seclo (1-1-1)
	                                   #Histacine (0-1-0)"""

				return redirect('P_page')

		else:
			contratForm = Contactform()


		context= {
		    "title":"Form",
		    "content":"Doctor page",
		    "form":contratForm,
		    'Error': 'Check All Feilds'
	    }
	except:
		contratForm = Contactform()


		context= {
		    "title":"Form",
		    "content":"Doctor page",
		    "form":contratForm,
		    'Error': 'Check All Feilds'
	    }


	return render(request,"home_page.html",context)


def P_page(request):
	contents= Doctor.objects.order_by('-date')[0:1].get()
	context ={'contents': contents}
	return render(request,"P_page.html",context)



def viewname(request):
	user = request.GET['user_id']
	contents= Doctor.objects.get(pk=user)
	med = [1,2,3]
	med = contents.content
	med = med.replace('[','')
	med = med.replace(']','')
	med = med.replace(' ','')
	med = med.split(',')

	
	contents ={'contents': contents, 'med':med}
    #do something with this user
	return render(request,"P2_page.html",contents)

def med_page(request):
	contents= Perasitamol.objects.order_by('-date')
	contents1= Ketorolac.objects.order_by('-date')
	contents2= Fexofenadine.objects.order_by('-date')
	contents3= Ceftriaxone.objects.order_by('-date')
	context ={'contents': contents,'contents1':contents1,'contents2':contents2,'contents3':contents3}
	return render(request,"med.html",context)


def med_page2(request):
	user = request.GET['med_id']
	# user = user.replace("'","")

	if user=="'Perasitamols'":
		contents= Perasitamol.objects.order_by('-date')

	elif user=="'Ketorolacs'":
		contents= Ketorolac.objects.order_by('-date')

	elif user=="'Fexofenadines'":
		contents= Fexofenadine.objects.order_by('-date')
	elif user=="'Ceftriaxones'":
		contents= Ceftriaxone.objects.order_by('-date')
	else:
		contents = [user]


	context ={'contents': contents, 'user':user}
	return render(request,"med2.html",context)