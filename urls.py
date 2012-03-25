from django.conf.urls.defaults import *

urlpatterns = patterns('',
   (r'^$', 'views.exampleMain'),
   (r'', include('openidgae.urls')),
)
