from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('',
	(r'^%s' % settings.BASE_URL, include('vacay.vacay_urls')),
)
