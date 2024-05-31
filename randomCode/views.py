from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

def random_number(request):
    number = random.randint(1000, 9999)  # generates a random number between 1 and 100
    return JsonResponse({'rand': number})