from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from vacay.views import views
#from vacay.views.login_view import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', views.landing),
	(r'^landing/$', views.landing),
	#(r'^login/$', login),
	(r'^home/$', views.home),
	(r'^mytrips/$', views.mytrips),
	(r'^pasttrips/$', views.pasttrips),
	(r'^futuretrips/$', views.futuretrips),
	(r'^tripplanning/(?P<id>\d+)/', views.tripplanning),
	(r'^blogging/(?P<id>\d+)/$', views.blogging),
	(r'^viewtrip/(?P<id>\d+)/$', views.viewtrip),
	(r'^viewpost/(?P<id>\d+)/$', views.viewpost),
	(r'^search/', include('haystack.urls')),
	(r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout, {'next_page' : '/accounts/login'}),
    (r'^registration/register/$', views.register),
    (r'^admin/', include(admin.site.urls)),
    (r'^newtrip/$', views.newtrip),
    (r'^contact/$', views.contact),
    (r'^about/$', views.about),
    (r'^contact/thanks/$', views.contact_thanks),
    #(r'/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),

    # Examples:
    # url(r'^$', 'vacay.views.home', name='home'),
    # url(r'^vacay/', include('vacay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
