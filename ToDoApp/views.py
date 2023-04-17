from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

def taskList(request):
    return HttpResponse("To Do List ")

