from django.contrib import admin

from .models import Cluster


class ClusterAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    list_display_links = ["id", "nome"]
    list_filter = ["nome"]
    search_fields = ["nome"]
    list_per_page = 15


admin.site.register(Cluster, ClusterAdmin)
