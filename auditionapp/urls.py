from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin

from auditionapp.admin import admin_site

#admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^actorsignup/', 'auditions.views.actorsignup'),
    (r'^actorphoto/(?P<actor_id>\d+)$', 'auditions.views.actorphoto'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin_site.urls)),
    
)

# Let django serve static files (for now)
urlpatterns += patterns('', 
  (r'^static/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root': settings.STATIC_ROOT}),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root': settings.MEDIA_ROOT})
)
