from django.shortcuts import render
from .models import Handbook, Element


# Вьюшка на главную страницу с списком всех справочников
def index(request):
    list_handbooks = Handbook.objects.all()
    return render(request, 'handbook/index.html', {'list_handbooks': list_handbooks})


# Вьюшка на страницу с списком всех элементов
def elements(request):
    list_elements = Element.objects.all()
    return render(request, 'handbook/elements.html', {'list_elements': list_elements})


# Вьюшка на динамические страницы соответствующие справочникам
def by_elements(request, element_id):
    elements = Element.objects.filter(handbook=element_id)
    handbooks = Handbook.objects.all()
    current_handbooks = Handbook.objects.get(pk=element_id)
    context = {
        'elements': elements,
        'handbooks': handbooks,
        'current_handbooks': current_handbooks,
    }
    return render(request, 'handbook/by_elements.html', context)


# Вьюшка на шаблонную страницу с выбором справочников, для отображения элементов
def by_elements_basic(request):
    handbooks = Handbook.objects.all()
    context = {
        'elements': elements,
        'handbooks': handbooks,
    }
    return render(request, 'handbook/by_elements_basic.html', context)


# Вьюшка на шаблонную страницу с датами
def handbooks_bydate_basic(request):
    hanbooks = Handbook.objects.all()
    context = {
        'handbooks': hanbooks
    }
    return render(request, 'handbook/handbooks_bydate_basic.html', context)