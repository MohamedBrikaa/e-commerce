"""e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from products import views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import home_view, signup_view, activation_sent_view, activate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
    path("products/", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", signup_view, name="signup"),
    path("sent/", activation_sent_view, name="activation_sent"),
    path("activate/<slug:uidb64>/<slug:token>/", activate, name="activate"),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
