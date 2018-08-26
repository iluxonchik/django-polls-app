from .models import Question
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

def index_not_optimized(request):
    """
    Index view, where verbose template loading and rendering is done.
    Notice how the index() view, simply uses the render() method.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])

    # This is why the polls index is at /polls/templates/polls/index.html (notice the second "polls").
    # If the index was put straight under "templates", it would still work, but if another app
    # was trying to load "index", Django's template loader, wouldn't know which "index.html" to load.
    # Thus, the second "polls" is used for namespacing.
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    rendered_template = template.render(context, request)
    return HttpResponse(rendered_template)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])

    # This is why the polls index is at /polls/templates/polls/index.html (notice the second "polls").
    # If the index was put straight under "templates", it would still work, but if another app
    # was trying to load "index", Django's template loader, wouldn't know which "index.html" to load.
    # Thus, the second "polls" is used for namespacing.
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail_not_optimized(request, question_id):
    """
    Detail view, where verbose "return 404 if object does not exist" is used.
    Notice how the detail() view simply uses get_object_or_404()
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f'Question with id {question_id} does not exist')
    return render(request, 'polls/detail.html', {'question' : question})

def detail(request, question_id):
    # all of the kwargs get passed to Question.objects.get
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})


def results(request, question_id):
    response  = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    response = f"You're voting on question {question_id}"
    return HttpResponse(response)
