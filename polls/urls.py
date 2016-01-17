from  django.conf.urls import include ,url
from . import views

urlpatterns=[
	url(r"^$",views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	url (r'^(?P<question_id>[0-9]+)/',include([url(r'^results/$',views.results,name='results'),url(r'^vote/$',views.vote,name='vote'),])),
#	url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
#	url(r'T^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]
