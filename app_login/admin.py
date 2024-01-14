from django.contrib import admin
from .models import Ticket, Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha"]
    search_fields = ["nombre"]
    #puede servir para activar o no solicitudes de evento
    #list_editable = []
    #list_filter = ["fecha"]
    #list_per_page = []
admin.site.register(Ticket)
admin.site.register(Evento, EventoAdmin)