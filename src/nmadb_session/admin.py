from django.contrib import admin
from django.utils.translation import ugettext as _

from nmadb_session import models
from nmadb_utils import admin as utils


class SessionAdmin(utils.ModelAdmin):
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


class LecturerParticipationAdmin(utils.ModelAdmin):
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

    search_fields = (
            'lecturer__first_name',
            'lecturer__last_name',
            'lecturer__old_last_name',
            'session__year',
            )

    filter_horizontal = ('lectures',)


class AcademicParticipationAdmin(utils.ModelAdmin):
    """ Administration for academic participation in session.
    """

    list_display = (
            'id',
            'academic',
            'session',
            'payment',
            )

    list_filter = (
            'session',
            )

    search_fields = (
            'academic__first_name',
            'academic__last_name',
            'academic__old_last_name',
            'session__year',
            )


class LecturerAdmin(utils.ModelAdmin):
    """ Administration for lecturer.
    """

    list_display = (
            'id',
            'human',
            )

    search_fields = (
            'id',
            'human__first_name',
            'human__last_name',
            'human__old_last_name',
            )

    inlines = (
            LecturerParticipationInlineAdmin,
            )


class LectureAdmin(utils.ModelAdmin):
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
            'session__year',
            )


class GroupAdmin(utils.ModelAdmin):
    """ Administration for group.
    """

    list_display = (
            'id',
            'session',
            )

    list_filter = (
            'session',
            )

    search_fields = (
            'id',
            'session__year',
            )

    filter_horizontal = ('academics', 'lectures',)


class SessionGroupAdmin(utils.ModelAdmin):
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
admin.site.register(
        models.AcademicParticipation, AcademicParticipationAdmin)
