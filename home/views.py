from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    all_contacts = Contact.objects.all()
    print(all_contacts)
    context = {
        'contacts': all_contacts, 
    }
    return render(request, 'index.html', context=context)