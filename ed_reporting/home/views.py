from django.shortcuts import render
 
# Create your views here.
def get_view_home_page(request):
    return render(request, "index.html")