import django.core.urlresolvers
import django.http
import openidgae

def exampleMain(request):
   return django.http.HttpResponse('<a href="%s">Login</a>' %
         openidgae.create_login_url(
            django.core.urlresolvers.reverse(
               'openidgae.views.LoginPage')))
