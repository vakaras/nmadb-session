from django.db import models
from django.utils.translation import ugettext_lazy as _

from nmadb_academics.models import Academic, Section
from nmadb_contacts.models import Human


class Session(models.Model):
    """ Information about session.
    """

    SESSION_TYPE = (
            (u'Wi', _(u'winter'),),
            (u'Sp', _(u'spring'),),
            (u'Su', _(u'summer'),),
            (u'Au', _(u'autumn'),),
            )

    year = models.IntegerField(
            verbose_name = _(u'year'),
            )

    session_type = models.CharField(
            choices=SESSION_TYPE,
            max_length=3,
            verbose_name = _(u'type'),
            )

    begin = models.DateField(
            verbose_name = _(u'begin'),
            )

    end = models.DateField(
            verbose_name = _(u'end'),
            )

    academics = models.ManyToManyField(
            Academic,
            through='AcademicParticipation',
            verbose_name = _(u'academics'),
            )

    class Meta(object):
        ordering = [u'year', u'session_type',]
        unique_together = ((u'year', u'session_type'),)
        verbose_name = _(u'session')
        verbose_name_plural = _(u'sessions')

    def __unicode__(self):
        return u'{0.year} {1}'.format(self, self.get_session_type_display())


class Lecture(models.Model):
    """ Information about lecture.
    """


    LECTURE_TYPE = (
            (u'su', _(u'Subject'),),
            (u'pe', _(u'Personality education'),),
            (u'ev', _(u'Evening event'),),
            )

    session = models.ForeignKey(
            Session,
            verbose_name = _(u'session'),
            )

    title = models.CharField(
            max_length=255,
            verbose_name = _(u'title'),
            )

    duration = models.IntegerField(
            verbose_name = _(u'duration'),
            help_text=_(u'In academic hours.'),
            )

    lecture_type = models.CharField(
            choices=LECTURE_TYPE,
            max_length=3,
            verbose_name=_(u'type'),
            )

    class Meta(object):
        ordering = [u'session', u'title',]
        verbose_name = _(u'lecture')
        verbose_name_plural = _(u'lectures')

    def __unicode__(self):
        return u'{0.title}'.format(self)


class Lecturer(models.Model):
    """ Information about human, who was at least one time in
    session and gave lecture.
    """

    human = models.OneToOneField(
            Human,
            verbose_name=_(u'human'),
            )

    comment = models.TextField(
            blank=True,
            null=True,
            verbose_name=_(u'comment'),
            )

    sessions = models.ManyToManyField(
            Session,
            through='LecturerParticipation',
            verbose_name=_(u'sessions'),
            help_text=_(u'Sessions in which he was.')
            )

    class Meta(object):
        verbose_name = _(u'lecturer')
        verbose_name_plural = _(u'lecturers')


class LecturerParticipation(models.Model):
    """ Marker that lecturer was in session.
    """

    lecturer = models.ForeignKey(
            Lecturer,
            verbose_name=_(u'lecturer'),
            )

    session = models.ForeignKey(
            Session,
            verbose_name=_(u'session'),
            )

    rating = models.FloatField(
            blank=True,
            null=True,
            verbose_name=_(u'rating'),
            )

    lectures = models.ManyToManyField(
            Lecture,
            verbose_name=_(u'lectures'),
            help_text=_(u'Lectures, he gave.')
            )

    class Meta(object):
        verbose_name = _(u'lecturer participation')
        verbose_name_plural = _(u'lecturers participations')


class Group(models.Model):
    """ Informal unit of academics participation in lectures.
    """

    session = models.ForeignKey(
            Session,
            verbose_name=_(u'session'),
            )

    academics = models.ManyToManyField(
            'AcademicParticipation',
            verbose_name=_(u'academics'),
            )

    lectures = models.ManyToManyField(
            Lecture,
            verbose_name=_(u'lectures'),
            help_text=_(u'Lectures, this group has listened.')
            )

    class Meta(object):
        verbose_name = _(u'group')
        verbose_name_plural = _(u'groups')


class SessionGroup(Group):
    """ Formal group of academics in session.
    """

    section = models.ForeignKey(
            Section,
            verbose_name=_(u'section'),
            )

    group = models.OneToOneField(
            Group,
            parent_link=True,
            verbose_name=_(u'group'),
            )

    group_number = models.PositiveSmallIntegerField(
            verbose_name=_(u'group number'),
            )

    comment = models.TextField(
            blank=True,
            null=True,
            verbose_name=_(u'comment'),
            )

    def __unicode__(self):
        return u'{0.section} {0.group_number}'.format(self)

    class Meta(object):
        verbose_name = _(u'session group')
        verbose_name_plural = _(u'sessions groups')


class AcademicParticipation(models.Model):
    """ Marker that academic was in session.
    """

    academic = models.ForeignKey(
            Academic,
            verbose_name=_(u'academic'),
            )

    session = models.ForeignKey(
            Session,
            verbose_name=_(u'session'),
            )

    payment = models.DecimalField(
            max_digits=7,
            decimal_places=2,
            verbose_name=_(u'payment'),
            )

    class Meta(object):
        verbose_name = _(u'academic participation')
        verbose_name_plural = _(u'academics participations')
