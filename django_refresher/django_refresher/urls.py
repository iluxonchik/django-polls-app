"""django_refresher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
Notes
-----------------------------------------------------------------------------

* include() - reference other URLconfs
    Whenever Django encounters an include(), it strips out whatever part
    of the url was matched up to that point, and sends the remainder to the
    included URLconf. Note, how we're not dispatching a vew function here,
    but rather passing the remainder of the URLs string for further matching.

"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # NOTE: if the polls app was under /content/polls/, fun_polls/, it would still work
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
