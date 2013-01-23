from django.conf.urls import *
from vacay import settings

print "settings.BASE_URL is: " + settings.BASE_URL 

urlpatterns = patterns('',
	(r'vacay/', include('vacay.vacay_urls')),
)
