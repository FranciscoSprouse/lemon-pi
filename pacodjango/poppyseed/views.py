from django.http import JsonResponse
from django.shortcuts import render
from poppyseed.MCP3008 import MCP3008

DRY = 760
WET = 380
MAX = 1023
MIN = 0
OFF = 11

def hydration(request):
    adc = MCP3008()
    value = adc.read( channel = 0 ) # You can of course adapt the channel to be read out
    return JsonResponse({'sensor 1': value})



