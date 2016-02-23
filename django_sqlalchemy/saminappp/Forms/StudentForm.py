#from saminappp.Model.StudentModel import Student
from django import forms
from django.core.exceptions import ValidationError
import bleach
from django.http.response import HttpResponse
from django.shortcuts import render
from Models.UserModel import Student



def clean_Name(name):


        if name == "ramin":

            return name
        else:
            return -1

        
'''
    def clean_Name(self):

        test = self.cleaned_data.get('Name')
        address = self.cleaned_data.get('Lastname')

        if test != address:
            raise ValidationError('error')

        return test

        '''



