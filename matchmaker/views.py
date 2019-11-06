from django.shortcuts import render
from .models import Seller

def home(request):
    return render(request, 'home.html')

# THIS IS SOLELY FOR MILESTONE 2 PROGRESS REPORT
def test(request):
    sellers_in_egypt = Seller.objects.filter(country_name='Egypt')
    return render(request, 'test.html', {'sellers_in_egypt': sellers_in_egypt})
