from django.shortcuts import render

from django.views.generic import CreateView

from .models import Contacts
from .forms import ContactForm


class ContactView(CreateView):
    model = Contacts
    form_class = ContactForm
    success_url = "/"
