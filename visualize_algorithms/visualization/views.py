from __future__ import absolute_import
from django.shortcuts import render_to_response
import os

def index(request):
    return render_to_response('index.html')

def single_array_in_place_algorithm(request):
    algo_name = os.path.split(request.path)[-1]
    return render_to_response('single_array_in_place_algorithm.html',{
        'algo_name': algo_name
    })
