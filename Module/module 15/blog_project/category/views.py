from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST) 
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category') 
    
    else: # user normally website e gele blank form pabe
        category_form = forms.CategoryForm()
    return render(request, 'category.html', {'form' : category_form})