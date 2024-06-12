from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def test(request):
    t = loader.get_template("test.html") 
    return HttpResponse(t.render())
