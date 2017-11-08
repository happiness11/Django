from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm
# Create your views here.

def get_index(request):
    results = TodoItem.objects.all()
    return render(request, "index.html", {'items': results})
    
def add_item(request):
    if request.method == "POST":
        # Get the details from the request
        form = TodoItemForm(request.POST)
        # Handle Saving to DB
        if form.is_valid():
            form.save()
            return redirect(get_index)
    else:
        # GET Request so just give them a blank form
        form = TodoItemForm()    
    
    return render(request, "item_form.html", { 'form': form })   
