"""vivalviar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from .core.views import home, history, special_participation, photos, playlist, contact_us, champions, \
    CircuitDetailView, CircuitListView, champions_team, BestYearPageView, get_player_stats

urlpatterns = []
if settings.DEVELOPER:
    urlpatterns += [
        path('admin/doc/', include('django.contrib.admindocs.urls')),
    ]

urlpatterns += [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('historia/', history, name='history'),
    path('campeoes/', champions, name='champions'),
    path('ajax/get_player_stats/', get_player_stats, name='get_player_stats'),
    path('campeoes/times/', champions_team, name='champions_team'),
    path('participacoes_especiais/', special_participation, name='special_participation'),
    path('melhores_do_ano/', BestYearPageView.as_view(), name='best_year'),
    path('fotos/', photos, name='photos'),
    path('videos/', playlist, name='playlist'),
    path('fale_conosco/', contact_us, name='contact_us'),
    path('circuitos/', CircuitListView.as_view(), name='circuit-list'),
    path('circuitos/<int:pk>/', CircuitDetailView.as_view(), name='circuit-detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
