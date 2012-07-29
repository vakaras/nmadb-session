from django.contrib import admin
from django.utils.translation import ugettext as _

from nmadb_session import models


class SessionAdmin(admin.ModelAdmin):
    """ Administration for session.
    """

    list_display = (
            'id',
            'year',
            'session_type',
            'begin',
            'end',
            )

    list_filter = (
            'session_type',
            )

    search_fields = (
            'id',
            'year',
            )


class LecturerAdmin(admin.ModelAdmin):
    """ Administration for lecturer.
    """

    list_display = (
            'id',
            'human',
            )

    search_fields = (
            'id',
            )

admin.site.register(models.Session, SessionAdmin)
admin.site.register(models.Lecturer, LecturerAdmin)
