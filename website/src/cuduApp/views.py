from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "index.html", {})


def electronics(request):
    print("View called")
    return render(request, "electronics.html", {})
