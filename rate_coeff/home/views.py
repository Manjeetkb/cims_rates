from http.client import HTTPResponse
from telnetlib import DM
from django.http import HttpResponse
from django.shortcuts import render
import math
from math import *
from django import forms
import pandas as pd
import sys
sys.path


# Create your views here.


def home(request):
    return render(request, 'home.html')

