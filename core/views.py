from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
from .models import ContactUs
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

# Create your views here.
def home(request):
   return render(request, 'index.html')

def about_us(request):
   return render(request, 'about.html')

# def contact(request):
#    form = ContactForm()
#    if request.method == 'POST':
#       form = ContactForm(data=request.POST)
#       if form.is_valid():
#          form.save()
#          messages.add_message(request, messages.SUCCESS, "Message has been succesfully sent!")
#          return redirect(reverse_lazy('contact_us'))
#    context = {
#       'form': form
#    }
#    return render(request, 'contact.html', context=context)


class ContactCreateView(CreateView):
   template_name = 'contact.html'
   form_class = ContactForm
   success_url=reverse_lazy('contact_us')

   def form_valid(self, form):
      messages.add_message(self.request, messages.SUCCESS, _("Message has been succesfully sent!"))
      return super().form_valid(form)
   