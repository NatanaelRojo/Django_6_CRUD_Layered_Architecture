from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI

from apps.persons.api import handlers
from apps.persons.api.api import router as person_router

# Instanciamos la API
api = NinjaAPI(title="Mi Proyecto CRUD API")

# Registramos el handler de errores de validación
handlers.set_handlers(api)
# Añadimos los routers de cada app (puedes añadir el de products luego)
api.add_router("/persons/", person_router)

urlpatterns = [
    # Admin route
    path("admin/", admin.site.urls),
    # Include the URLs from persons app.
    path("", include("apps.persons.urls")),
    # API routes Django Ninja
    path("api/", api.urls),
]
