from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    return render(request,'home.html', )

def gpa(request):

    first=float( request.GET['num1'])
    sec= float(request.GET['num2'])
    thr=float(request.GET['num3'])
    frt=float(request.GET['num4'])
    fif=float(request.GET['num5'])
    six=float(request.GET['num6'])
    sev=float(request.GET['num7'])
    ind=float(request.GET['num8'])
    fs=float(first*5/100)
    second=float(sec*5/100)
    third=float(thr*5/100)
    fourth=float(frt*10/100)
    fifth=float(fif*15/100)
    sixth=float(six*20/100)
    seven=float(sev*25/100)
    indtr=float(ind*15/100)

    #this is your cgpa 
    cgpa=format(fs+second+third+fourth+fifth+sixth+seven+indtr,'.2f')
    txt="Your CGPA is : "



    return render(request,"base.html",{'Cgpa':txt+cgpa})
