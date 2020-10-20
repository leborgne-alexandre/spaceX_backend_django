from django.shortcuts import render
from django.http import JsonResponse
import requests

def apiOverview(request):
    r = requests.get('https://api.spacexdata.com/v3/dragons')
    r = r.json()
    #return (r, safe=False)
    return JsonResponse(r, safe=False)
