from django.conf.urls.defaults import *

from django.contrib import admin

from auditionapp.admin import admin_site

#admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^actorsignup/', 'auditions.views.actorsignup'),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin_site.urls)),
)
