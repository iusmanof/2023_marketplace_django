from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {}
    return render(request, 'core/index.html', context)

def contact_view(request):
    context = {}
    return render(request, 'core/contact.html', context)

# 25:00 Items