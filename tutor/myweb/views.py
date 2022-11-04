from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context = {
        'judul' : 'myweb1',
        'h1'    : 'Dean Teguh Imansyah',
        'menu'  : [['myweb/', 'Home'], ['myweb/recent',], ['/post', 'Post']]

    }
    return render(request, 'myweb/index.html', context)

def recent(request):
    return HttpResponse("Recent Blog")