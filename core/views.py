from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from core.forms import TaskForm
from item.models import Category, Item
from .forms import SignUpForm, TaskForm


def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'core/index.html',
                  {'categories': categories,
                   'items': items,}
                  )


def contact(request):
    return render(request, 'core/contact.html')


def privacy(request):
    return render(request, 'core/privacy.html')


def term_of_use(request):
    return render(request, 'core/terms.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def check_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            return solution(request, a)
    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, 'core/task.html', context)


# Дано вещественное число A. Вычислить x = 0 при a > 100; x = a при a < 61, в противном случае x = a**4.
def solution(request, a):
    if a > 100:
        ans = 0
    elif a < 61:
        ans = a
    else:
        ans = a ** 4

    context = {'answer': ans, 'question': a}
    return render(request, 'core/answer.html', context)


def about(request):
    context = {
        'my': {
            'name': 'Мурадханова Полина Раджабалиевна',
            'phone': '+79679425833',
            'mail': 'prmuradkhanova@edu.hse.ru',
            'imgurl': 'https://n1s1.hsmedia.ru/be/1b/1b/be1b1bb5f29c51f945d361ea86348a4d/332x332_1_37e481a1cec03d2c0406a1f8e071ea13@415x415_0xac120003_3151271871596024352.jpg'
        },
        'program': {
            'name': 'Экономика',
            'description': 'Образовательная программа «Экономика»  сочетает фундаментальную подготовку студентов в области теоретической и прикладной экономики и финансов с проектно-ориентированным обучением, дающим практические навыки, обеспечивающие выпускникам преимущества в трудоустройстве и гарантирующие профессиональный рост. ',
            'ruk': {
                'name': 'Кирилл Александрович Букин',
                'mail': 'kabukin@hse.ru',
                'imgurl':'https://www.hse.ru/pubs/share/thumb/187225977:c2103x2103+50+0:r380x380!.jpg'
            },
            'man': {
                'name': 'Макарова Галина Викторовна',
                'mail': 'gvmakarova@hse.ru',
                'imgurl':'https://www.hse.ru/pubs/share/thumb/223562260:c527x527+93+0:r380x380!.jpg'
            }
        },
        'pal1': {
            'name': 'Ушатова Арина Юрьевна',
            'phone': '+79000000000',
            'mail': 'ayuushatova@edu.hse.ru',
            'imgurl': 'https://avatars.dzeninfra.ru/get-zen_doc/3724792/pub_603e34c38da63757af6856a7_60a7bc2857455d23caa3d214/scale_720'
        },
        'pal2': {
            'name': 'Зорина Лина Юрьевна',
            'phone': '+79111111111',
            'mail': 'luzorina@edu.hse.ru',
            'imgurl': 'https://n1s2.hsmedia.ru/80/89/18/8089181c9788e14eb451a3eca4d26d72/418x600_1_e1785549b61ac612388792a31281d65b@486x698_0xac120003_15674663381613017379.jpg'
        },
    }
    return render(request, 'core/about.html', context)
