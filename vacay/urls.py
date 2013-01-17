from django.conf.urls import patterns, include, url
from vacay.landing_view import landing
from vacay.login_view import login
from vacay.home_view import home
from vacay.mytrips_view import mytrips
from vacay.pasttrips_view import pasttrips
from vacay.futuretrips_view import futuretrips
from vacay.tripplanning_view import tripplanning
from vacay.blogging_view import blogging
from vacay.viewtrip_view import viewtrip
from vacay.viewpost_view import viewpost
from vacay.search_view import search

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
