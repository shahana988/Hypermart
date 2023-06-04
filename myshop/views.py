from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User



from django.shortcuts import render, redirect
from myshop.models import admindb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from myshop.models import catdb
from myshop.models import prodb


# Create your views here.
def index(request):
    return render(request,"index.html")

def shoppage(request):
    return render(request,"add admin.html")


def savedata(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        em = request.POST.get('email')
        use = request.POST.get('username')
        pa = request.POST.get('password')

        obj = admindb(name=na, mobile=mob, email=em, username=use, password=pa)
        obj.save()
        return redirect(shoppage)

def displaydata(request):
     data = admindb.objects.all()
     return render(request, "display.html", {'data': data})

def editpage(request, dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(request,"Editdata.html",{'data':data})



def updatedata(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        em = request.POST.get('email')
        use = request.POST.get('username')
        pa = request.POST.get('password')
        obj = admindb(name=na, mobile=mob, email=em, username=use, password=pa)
        obj.save()
        return redirect(displaydata)

def deletedata(request , dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydata)

def catpage(request):
    return render(request,"add category.html")

def savecat(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        de = request.POST.get('description')
        image = request.FILES['image']
        obj = catdb(name=na, description=de, image=image)
        obj.save()
        return redirect(catpage)

def displaycatdata(request):
    data = catdb.objects.all()
    return render(request, "displaycat.html", {'data': data})


def editcatpage(request,dataid):
    data = catdb.objects.get(id=dataid)
    print(data)
    return render(request, "editcat.html",{'data':data})



def updatecatdata(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('description')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).image
        catdb.objects.filter(id=dataid).update(name=na, description=de,  image=file)
        return redirect(displaycatdata)


def deletecatdata(request, dataid):
    data = catdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycatdata)



def propage(request):
    data = catdb.objects.all()
    return render(request,"add product.html",{'data':data})

def savepro(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pr = request.POST.get('price')
        qt = request.POST.get('quantity')
        de = request.POST.get('description')
        ct = request.POST.get('ct')
        image = request.FILES['image']
        obj = prodb(name=na, price=pr, quantity=qt, description=de,category=ct,image=image)
        obj.save()
        return redirect(propage)

def displayproduct(request):
    data = prodb.objects.all()
    return render(request, "displaypro.html",{'data':data})

def editpropage(request,dataid):
    data = prodb.objects.get(id=dataid)
    da = catdb.objects.all()
    return render(request, "editproduct.html", {'data': data,'da': da})


def updateprodata(request, dataid):
    if request.method == "POST":
         na = request.POST.get('name')
         pr = request.POST.get('price')
         qt = request.POST.get('quantity')
         de = request.POST.get('description')
         ct = request.POST.get('ct')
         try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
         except MultiValueDictKeyError:
            file = prodb.objects.get(id=dataid).image
         prodb.objects.filter(id=dataid).update(name=na, price=pr, quantity=qt, description=de, category=ct, image=file)
         return redirect(displayproduct)

def deleteprodata(request, dataid):
    data = prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)


def logdata(request):
    return render(request,"login.html")

def logindetails(request):
    if request.method == "POST":
       use = request.POST.get('username')
       pas = request.POST.get('password')

       if User.objects.filter(username__contains=use).exists():
           user = authenticate(username=use, password=pas)
           if user is not None:
               login(request, user)
               request.session['username'] = use
               request.session['password'] = pas
               return redirect(shoppage)
           else:
               return redirect(logdata)

       else:
            return redirect(logdata)










