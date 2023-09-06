from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Michael Marcellino Satyanegara',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.
