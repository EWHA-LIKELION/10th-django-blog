"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
import blog.views
from django.conf import settings
from django.conf.urls.static import static
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home,name='home'),
    path('blog/<int:blog_id>',blog.views.detail,name="detail"),
    path('new/',blog.views.new,name="new"),
    path('create/',blog.views.create,name="create"),
    path('delete/<int:blog_id>',blog.views.delete,name="delete"),
    path('update/<int:blog_id>',blog.views.update,name="update"),
    path('update2/<int:blog_id>',blog.views.update2,name="update2"),

    path('<int:blog_id>/comment',blog.views.add_comment, name="add_comment"),
    path('<int:blog_id>/comment/<int:comment_id>/delete/',blog.views.delete_comment, name="delete_comment"),

    path('account/login', account.views.login_view, name="login"),
    path('account/logout', account.views.logout_view, name="logout"),
    path('account/signup', account.views.signup_view, name="signup"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
