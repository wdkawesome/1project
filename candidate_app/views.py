from django.shortcuts import render

"""
This file contains the definition for three view functions on the app.
The render function is used to render the below templates which are located in the 'templates' directory.
"""

# Create your views here.
def home(request):
    """
    home: returns the 'home.html' template, which is the home page for the political candidate's website.
    """
    return render(request, 'home.html')

def about(request):
    """
    about: returns the 'about.html' template which contains the details about the political candidate.
    """
    return render(request, 'about.html')

def contact(request):
    """
    contact: returns the 'contact.html' template which displays the contact details for the political candidate.
    """
    return render(request, 'contact.html')