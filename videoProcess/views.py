from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'OptiMedia',
        'page': 'Video Processing',
        'nav': [
            ['/','Home'],
            ['/imageProcess/','Image'],
            ['/audioProcess/','Audio'],
            ['/videoProcess/','Video']
        ],
    }
    return render(request, "videoProcess/index.html", context)

def dct(request):
    context = {
        'title': 'OptiMedia',
        'page': 'Discrete Cosine Algorithm',
        'nav': [
            ['/','Home'],
            ['/imageProcess/','Image'],
            ['/audioProcess/','Audio'],
            ['/videoProcess/','Video']
        ],
    }
    return render(request, "videoProcess/dct.html", context)

def dft(request):
    context = {
        'title': 'OptiMedia',
        'page': 'Discrete Fourier Algorithm',
        'nav': [
            ['/','Home'],
            ['/imageProcess/','Image'],
            ['/audioProcess/','Audio'],
            ['/videoProcess/','Video']
        ],
    }
    return render(request, "videoProcess/dft.html", context)
