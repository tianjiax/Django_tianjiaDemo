from django.shortcuts import render


def page(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['list'] = ['甲乙', '丙丁']
    views_dict = {"name": "教程", "age": 18}
    context['views_dict'] = views_dict
    return render(request, 'index.html', context)
