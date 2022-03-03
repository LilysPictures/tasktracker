from django.shortcuts import render


def index(request):
    template = 'tasks/index.html'
    context = {
        'title': 'Главная страница Тасктрекера',
        'text': 'Текст главной страницы',
    }
    return render(request, template, context)
