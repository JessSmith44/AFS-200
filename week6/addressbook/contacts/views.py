from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.template import loader
# Create your views here.

def show_all_contacts(request):
    contacts = Contact.objects.all()
    template = loader.get_template('index.html')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))


def show_contact(request, contactid):
    try:
        # contactid = Contact.objects.get(id=contactid)
        # return HttpResponse(f'<h1>Showing details for "{contactid}"</h1>')
        template = loader.get_template('index.html')
        contacts = Contact.objects.all()
        def func(contact):
            print(contact.id)
            if(contact.id == contactid):
                return True
            else:
                return False

        oneContact = filter(func, contacts)
        context = {
            'contacts' = oneContact
        }
        return HttpResponse(template.render(context, request))
    except Contact.DoesNotExist:
        return HttpResponse(f'<h1>Unable to locate contact {contactid}</h1>')