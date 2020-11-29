from django.shortcuts import render
from .models import Handbook, Element
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Вьюшка на главную страницу с списком всех справочников
def index(request):
    list_handbooks = Handbook.objects.all()
    paginator = Paginator(list_handbooks, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'handbook/index.html', {'posts': posts})


# Вьюшка на страницу с списком всех элементов
def elements(request):
    list_elements = Element.objects.all()
    paginator = Paginator(list_elements, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'handbook/elements.html', {'posts': posts})


# Вьюшка на динамические страницы соответствующие справочникам
def by_elements(request, element_id):
    elements = Element.objects.filter(handbook=element_id)
    handbooks = Handbook.objects.all()
    current_handbooks = Handbook.objects.get(pk=element_id)
    paginator = Paginator(elements, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'elements': elements,
        'handbooks': handbooks,
        'current_handbooks': current_handbooks,
        'posts': posts,
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
