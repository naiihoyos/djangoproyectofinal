"""tienda_online URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from inventario.views import *
from contacto.views import mensaje_contacto
from inicio.views import inicio
from compra.views import compra, venta
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='home'),
    path('busqueda_productos/', vista_busqueda_productos),
    path('obtener_producto/', obtener_producto),
    path('agregar_producto/', agregar_producto, name='add-prods'),
    path('mostrar_productos/', mostrar_productos, name='show-prods'),
    path('editar_producto/<int:pk>', editar_producto, name='edit-prods'),
    path('eliminar_producto/<int:pk>', eliminar_producto, name="del-prods"),
    path('contacto/', mensaje_contacto),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('compra/<int:pk>', compra, name='compra'),
    path('venta/', venta, name='venta')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

