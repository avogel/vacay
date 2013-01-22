from django.conf.urls import *
from vacay import settings

print "settings.BASE_URL is: " + settings.BASE_URL 

urlpatterns = patterns('',
	(r'^%s' % settings.BASE_URL, include('vacay.vacay_urls')),
)
