from django.shortcuts import render

def addition(request):
    if request.method=="POST":
        print(request.POST)
        n1=request.POST['num1']
        n2=request.POST['num2']
        result=int(n1)+int(n2)
        context={'result':result}
        return render(request,'addition.html',context)
    return render(request, 'addition.html')


def fact(request):
    if request.method=="POST":

        n=int(request.POST['num1'])
        f=1
        for i in range(1,n+1):
            f=f*i
        context={'result':f}
        return render(request, 'factorial.html', context)
    return render(request,'factorial.html')