from django.shortcuts import render

def index(request):
    context = {
        'title': 'OptiMedia',
        'page': 'Home',
        'nav': [
            ['/','Home'],
            ['/imageProcess/','Image'],
            ['/audioProcess/','Audio'],
            ['/videoProcess/','Video']
        ],
    }
    return render(request, "index.html", context)