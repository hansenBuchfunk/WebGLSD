from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('angebote.urls')),
]

# Anpassung Admin Area
admin.site.site_header = "Sprecher:innen Datenbank Admin Area"
admin.site.site_title = "xoup Buchfunk 2023"
admin.site.index_title = "Dieser Bereich ist nur für Mitarbeiter"