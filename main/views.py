from django.shortcuts import render

# Create your views here.
"""
def holaMundo(request):

    return render(request, 'index.html', {})
#End holaMundo
"""
def main_view(request):

    return render(request, 'main.html', {})
#End main_view