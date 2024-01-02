from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {
        'question_list': page_obj
    }
    return render(request, 'mysite/index.html', context)


def detail(requst, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(requst, 'mysite/detail.html', context)
