from django.shortcuts import render
import requests
import json
from firstapp.models import Travel
from requests.structures import CaseInsensitiveDict

# Create your views here.
def index(request):

    # counter data
    OOD = len(Travel.objects.filter(code='OOD'))
    INT = len(Travel.objects.filter(code='INT'))
    DEX = len(Travel.objects.filter(code='DEX'))
    NFI = len(Travel.objects.filter(code='NFI'))
    DEL = len(Travel.objects.filter(code='DEL'))
    
    t1 = Travel.objects.filter(code='INT')

    # Table data
    data = {
        'counter':{
            'DEX':DEX,
            'DEL':DEL,
            'INT':INT,
            'NFI':NFI,
            'OOD':OOD
        },
        'tool':t1

    }
    if request.method=='POST':
        code = request.POST.get('code')
        c1 = code[:3]
        if c1=='OOD':
            t1 = Travel.objects.filter(code='OOD')
            data['tool'] = t1
            return render(request,'index.html',context = data)
        elif c1=='INT':
            t1 = Travel.objects.filter(code='INT')
            data['tool'] = t1
            return render(request,'index.html',context = data)
        elif c1=='NFI':
            t1 = Travel.objects.filter(code='NFI')
            data['tool'] = t1
            return render(request,'index.html',context = data)
        elif c1=='DEX':
            t1 = Travel.objects.filter(code='DEX')
            data['tool'] = t1
            return render(request,'index.html',context = data)

    return render(request,'index.html',context = data)