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


class LecturerParticipationInlineAdmin(admin.TabularInline):
    """ Administration for lecturer participation in session.
    """

    model = models.Lecturer.sessions.through
    filter_horizontal = ('lectures',)
    extra = 0


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

    filter_horizontal = ('lectures',)


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

    inlines = (
            LecturerParticipationInlineAdmin,
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


class GroupAdmin(admin.ModelAdmin):
    """ Administration for group.
    """

    list_display = (
            'id',
            'session',
            )

    search_fields = (
            'id',
            'session__year',
            )

    filter_horizontal = ('academics', 'lectures',)


class SessionGroupAdmin(admin.ModelAdmin):
    """ Administration for session group.
    """

    list_display = (
            'id',
            'session',
            'section',
            'group_number',
            )

    list_filter = (
            'section',
            'group_number',
            )

    search_fields = (
            'id',
            'session__year',
            'section__title',
            )

    filter_horizontal = ('academics', 'lectures',)

admin.site.register(models.Session, SessionAdmin)
admin.site.register(models.Lecturer, LecturerAdmin)
admin.site.register(
        models.LecturerParticipation, LecturerParticipationAdmin)
admin.site.register(models.Lecture, LectureAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.SessionGroup, SessionGroupAdmin)
