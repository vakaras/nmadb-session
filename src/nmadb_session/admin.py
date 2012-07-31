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


class LecturerParticipationAdmin(admin.ModelAdmin):
    """ Administration for lecturer participation in session.
    """

    list_display = (
            'id',
            'lecturer',
            'session',
            'rating',
            )

    list_filter = (
            'session',
            )


class LectureAdmin(admin.ModelAdmin):
    """ Administration for lecture.
    """

    list_display = (
            'id',
            'session',
            'title',
            'duration',
            'lecture_type',
            )

    list_filter = (
            'session',
            'lecture_type',
            )

    search_fields = (
            'id',
            'title',
            )


admin.site.register(models.Session, SessionAdmin)
admin.site.register(models.Lecturer, LecturerAdmin)
admin.site.register(
        models.LecturerParticipation, LecturerParticipationAdmin)
admin.site.register(models.Lecture, LectureAdmin)
