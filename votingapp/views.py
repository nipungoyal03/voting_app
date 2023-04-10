from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

arr = ['Java' , 'Python' , 'Cplusplus' , 'C' , 'DotNET' , 'JavaScript' , 'PHP' , 'Swift' , 'SQL' , 'Ruby' , 'Delphi' , 'Objective-C' , 'Go' , 'Assemblylanguage' , 'VisualBasic' , 'D' , 'R' , 'Perl' , 'MATLAB'];
globalcnt = dict()
# Create your views here.
def index(request):
   
    mydictionery = {
        "arr" : arr
    };
    return render(request,'index.html',context=mydictionery);

def getquery(request):
    q = request.GET['languages']
    if q in globalcnt:
        globalcnt[q] = globalcnt[q] + 1;
    else:
        globalcnt[q] = 1;   
    mydictionery = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }     
    return render(request,'index.html',context=mydictionery) 

def sortdata(request):
    global globalcnt;
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydictionery = {
        "arr" : arr,
        "globalcnt" : globalcnt
    };
    return render(request,'index.html',context=mydictionery);
