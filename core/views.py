from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def home(request):
   return render(request, 'index.html')

def about_us(request):
   return render(request, 'about.html')

def contact(request):
   form = ContactForm()
   if request.method == 'POST':
      form = ContactForm(data=request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request, messages.SUCCESS, "Message has been succesfully sent!")
         return redirect(reverse_lazy('contact_us'))
   context = {
      'form': form
   }
   return render(request, 'contact.html', context=context)