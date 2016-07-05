from django.conf.urls import url
from . import views,models

urlpatterns=[

		url(r'^$',views.index,name='index'),
		url(r'^addbook/$',views.addbook,name='addbook'),
		url(r'^addmusic/$',views.addmusic,name='addmusic'),
		url(r'^showbook/$',views.showbook,name='showbook'),
		url(r'^showmusic/$',views.showmusic,name='showmusic'),
		url(r'^showbookorder/(?P<a>[a-z]+)/$',views.showbookorder,name='showbooksorder'),
		url(r'^showmusicorder/(?P<a>[a-z]+)/$',views.showmusicorder,name='showmusicorder')


		]