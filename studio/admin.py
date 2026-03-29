from django.contrib import admin
from django.utils.html import format_html

from .models import Game, TeamMember


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "status", "release_date")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "genre")
    readonly_fields = ("cover_preview",)

    def cover_preview(self, obj):
        if obj.cover:
            return format_html(
                '<img src="{}" style="max-height:120px;border-radius:8px;" />',
                obj.cover.url,
            )
        return "—"

    cover_preview.short_description = "предпросмотр"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "tagline",
                    "description",
                    "genre",
                    "status",
                    "release_date",
                    "cover",
                    "cover_preview",
                )
            },
        ),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order")
    list_editable = ("order",)
