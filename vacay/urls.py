from django.conf.urls import *
from vacay import settings
import os.path
#from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

print os.path.join(os.path.dirname(__file__)).replace('\\','/')


#dajaxice_autodiscover()

urlpatterns = patterns('',
	(r'vacay/', include('vacay.vacay_urls')),
	#url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
#urlpatterns += staticfiles_urlpatterns()