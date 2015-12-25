from BL.StudentBL import Datainsert
from saminappp.Forms.StudentForm import clean_Name
from django.shortcuts import HttpResponse,render, render_to_response
from BL.UserBL import InsertDB,SelectAll
from Models.UserModel import Student



def Insert(request):

     id = 1
     if request.POST:

          name = request.POST.get('Name')
          lastname = request.POST.get('Lastname')

          if clean_Name(name) != -1:

               o = Student(id=id,name=name,fullname=lastname,password=1234345)
               #oo = Helper()
               InsertDB(o)

          else:
               return HttpResponse('error')

     return render(request,'test.html')


def SelectAll(request):


    # from BL.UserBL import Helper
    # Access2Def = Helper()
     lst =  SelectAll(Student)
     return render(request,'select.html',{'lstform':lst})

    # return render(request,'select.html',{'lstform':lstt})























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
