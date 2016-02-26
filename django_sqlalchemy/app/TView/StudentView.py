from django.shortcuts import HttpResponse,render
from app.controller.UserBL import InsertDB
from app.controller.UserBL import django_sqlA

'''
     Here Connect to controller with parameters users from view and controller connect to database , return object to TampleteView with control validation for display user

'''


def SelectAll(request):

     ## Connect to Connector

     lst =  SelectAll(django_sqlA)

     return render(request,'index.html')























     '''
     infostud = StudentForm(request.POST or None)

     if infostud.is_valid():

          object_bl = Datainsert()
          object_bl.insert(infostud)
          return HttpResponse("Done!")


     contaxt = {'infoform':infostud}
     return render(request,'test.html',contaxt)

     '''





     '''
     object_model = Student()
     object_model.ID        = 1
     object_model.Firstname = " ramin "
     object_model.Lastename = " farajpour "
     object_model.Address   = " bandpi "
     object_bl = Datainsert()

     return HttpResponse(object_bl.insert(object_model))
     '''
