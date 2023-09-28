from django.shortcuts import render

def simple(request):
    return render(request, "simple.html", {"name": "Mundo"})

def dinamico(request, name):
    categories = ["Programación", "Tecnología", "Ciencia", "lp2"]
    context = {"name": name, "categories": categories}
    return render(request,"dinamico.html", context) 

def estaticos(request):
    return render(request, "estaticos.html") 