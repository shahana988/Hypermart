from django.urls import path
from myshop import views

urlpatterns = [
    path('index/', views.index , name="index"),
    path('shoppage/', views.shoppage, name="shoppage"),
    path('savedata/',views.savedata, name="savedata"),
    path('displaydata/',views.displaydata, name="displaydata"),
    path('editpage/<int:dataid>/', views.editpage, name="editpage"),
    path('updatedata/',views.updatedata, name ="updatedata"),
    path('deletedata/<int:dataid>/',views.deletedata, name ="deletedata"),
    path('catpage/', views.catpage, name="catpage"),
    path('savecat/',views.savecat, name="savecat"),
    path('displaycatdata/',views.displaycatdata,name="displaycatdata"),
    path('editcatpage/<int:dataid>/',views.editcatpage, name="editcatpage"),
    path('updatecatdata/',views.updatecatdata, name="updatecatdata"),
    path('deletecatdata/<int:dataid>/',views.deletecatdata, name="deletecatdata"),
    path('propage/', views.propage, name="propage"),
    path('savepro/', views.savepro, name="savepro"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editpropage/<int:dataid>/', views.editpropage, name="editpropage"),
    path('updateprodata/<int:dataid>/',views.updateprodata,name="updateprodata"),
    path('deleteprodata/<int:dataid>/', views.deleteprodata, name="deleteprodata"),
    path('logdata/', views.logdata, name="logdata"),
    path('logindetails/', views.logindetails, name="logindetails")


]