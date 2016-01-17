from django.http import Http404
from django.http import HttpResponse
from .models import Question
from django.template import RequestContext,loader
from django.shortcuts import render
'''
def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template("polls/index.html")
	context=RequestContext(request,{"latest_question_list":latest_question_list})
	return HttpResponse(template.render(context)) 
'''
def index(request):
	try:
		latest_question_list=Question.objects.order_by('-pub_date')[:5]
		context={'latest_question_list':latest_question_list}
	except Question.DoesNotExist:
		raise Http404("Question is not exist!")
	return render(request,'polls/index.html',context)

	return HttpResponse("Hello ,world,you are at the polls index. ")
def detail(request,question_id):
	try:
		question=Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404('Question is not exist!')
	return render(request ,"polls/detail.html",{'question':question})

def results(request,question_id):
	response="you are looking at the results of question %s"
	return HttpResponse(response % question_id )
def vote(request,question_id):
	return HttpReponse("you are voting on question %s" % question_id)



