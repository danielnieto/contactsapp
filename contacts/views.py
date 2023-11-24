from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return redirect("contacts")

def contacts(request):
    return HttpResponse("Contacts")
