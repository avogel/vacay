from django.conf.urls import patterns, include, url
from vacay.views.landing_view import landing
from vacay.views.login_view import login
from vacay.views.home_view import home
from vacay.views.mytrips_view import mytrips
from vacay.views.pasttrips_view import pasttrips
from vacay.views.futuretrips_view import futuretrips
from vacay.views.tripplanning_view import tripplanning
from vacay.views.blogging_view import blogging
from vacay.views.viewtrip_view import viewtrip
from vacay.views.viewpost_view import viewpost
from vacay.views.search_view import search

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	('^$',landing),
	('^landing/$', landing),
	('^login/$', login),
	('^home/$', home),
	('^mytrips/$', mytrips),
	('^pasttrips/$', pasttrips),
	('^futuretrips/$', futuretrips),
	('^tripplanning/$', tripplanning),
	('^blogging/$', blogging),
	('^viewtrip/$', viewtrip),
	('^viewpost/$', viewpost),
	('^search/$', search),

    # Examples:
    # url(r'^$', 'vacay.views.home', name='home'),
    # url(r'^vacay/', include('vacay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
