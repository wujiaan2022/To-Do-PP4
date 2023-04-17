from django.shortcuts import render
from django.http import HttpRequest

def taskList(request):
    return HttpResponse("To Do List ")

