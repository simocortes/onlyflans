from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required


def index(request):
    public_flans = Flan.objects.filter(is_private=False)
    
    if request.user.is_authenticated: 
        favoritos_ids = request.user.favoritos.values_list('flan_id', flat=True )
    else:
        favoritos_ids = []    
    return render(
        request,
        'index.html', 
        { 
          'public_flans': public_flans,
          'favoritos_ids': favoritos_ids,
        }
)

def about(request):
    return render(request, 'about.html', {})

@login_required
def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)
    
    return render(
        request,
        'welcome.html', 
        {
            'private_flans': private_flans
        }
    )
def message(request):
    if request.method == 'POST':
        
        form = ContactFormModelForm(request.POST)
        
        if form.is_valid():
            
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            
            return HttpResponseRedirect('/exito')
        
    else:
        form = ContactFormModelForm()
    
    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})
 
def toggle_favorito(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    if request.user.is_authenticated:
        favorito, created = favorito.objects.get_or_create(user=request.user, flan=flan)
        if not created:
            favorito.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def favoritos(request):
    if request.user.is_authenticated:
        flanes_favoritos = request.user.favoritos.all()
        return render(request, 'favoritos.html', {'flanes_favoritos': flanes_favoritos})
    return HttpResponseRedirect('login/')
