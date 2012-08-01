from django.db import models
from django.utils.translation import ugettext as _

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
            )

    session_type = models.CharField(
            choices=SESSION_TYPE,
            max_length=3,
            )

    begin = models.DateField(
            )

    end = models.DateField(
            )

    academics = models.ManyToManyField(
            Academic,
            through='AcademicParticipation',
            )

    class Meta(object):
        ordering = [u'year', u'session_type',]
        unique_together = ((u'year', u'session_type'),)

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
            )


    title = models.CharField(
            max_length=255,
            )

    duration = models.IntegerField(
            help_text=_(u'In academic hours.'),
            )

    lecture_type = models.CharField(
            choices=LECTURE_TYPE,
            max_length=3,
            verbose_name=_(u'type'),
            )

    class Meta(object):
        ordering = [u'session', u'title',]

    def __unicode__(self):
        return u'{0.title}'.format(self)


class Lecturer(models.Model):
    """ Information about human, who was at least one time in
    session and gave lecture.
    """

    human = models.OneToOneField(
            Human,
            )

    comment = models.TextField(
            blank=True,
            null=True,
            )

    sessions = models.ManyToManyField(
            Session,
            through='LecturerParticipation',
            help_text=_(u'Sessions in which he was.')
            )


class LecturerParticipation(models.Model):
    """ Marker that lecturer was in session.
    """

    lecturer = models.ForeignKey(
            Lecturer,
            )

    session = models.ForeignKey(
            Session,
            )

    rating = models.FloatField(
            blank=True,
            null=True,
            )

    lectures = models.ManyToManyField(
            Lecture,
            help_text=_(u'Lectures, he gave.')
            )


class Group(models.Model):
    """ Informal unit of academics participation in lectures.
    """

    session = models.ForeignKey(
            Session,
            )

    academics = models.ManyToManyField(
            'AcademicParticipation',
            )

    lectures = models.ManyToManyField(
            Lecture,
            help_text=_(u'Lectures, this group has listened.')
            )


class SessionGroup(Group):
    """ Formal group of academics in session.
    """

    section = models.ForeignKey(
            Section,
            )

    group = models.OneToOneField(
            Group,
            parent_link=True,
            )

    group_number = models.PositiveSmallIntegerField(
            )

    comment = models.TextField(
            blank=True,
            null=True,
            )

    def __unicode__(self):
        return u'{0.section} {0.group_number}'.format(self)


class AcademicParticipation(models.Model):
    """ Marker that academic was in session.
    """

    academic = models.ForeignKey(
            Academic,
            )

    session = models.ForeignKey(
            Session,
            )

    payment = models.DecimalField(
            max_digits=7,
            decimal_places=2,
            )
