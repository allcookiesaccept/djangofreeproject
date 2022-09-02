from django.shortcuts import render

def index(request):

    data = {
        'title': 'Main Page!',
        'values': ['Good day today', 'don\'t you think?'],
        'obj': {
            'age': 33,
            'name': 'Billy D'

        }
    }

    return render(request, 'main/index.html', data)

def about(request):

    return render(request, 'main/about.html')

def blog(request):

    return render(request, 'main/blog.html')