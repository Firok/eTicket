from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class Cinema(models.Model):
    name = models.CharField(max_length=100, verbose_name=_(u"Cinema name"))
    description = models.TextField(max_length=500, verbose_name=_(u"Description"))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name=_(u"Genre"))
    description = models.TextField(max_length=500, verbose_name=_(u"Description"))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name=_(u"Title"))
    synopsis = models.TextField(max_length=1000, verbose_name=_(u"Synopsis"))
    origin = models.CharField(max_length=50, verbose_name=_(u"Origin"), default=u"INDIA")
    slug = models.SlugField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, verbose_name=_(u"Genre"))

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug': self.slug})

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Movie, self).save()


class Trailer(models.Model):
    trailer = models.FileField(upload_to=u"movies/trailers/", verbose_name=_(u"Trailer"))
    movie = models.OneToOneField(Movie, verbose_name=_(u"Movie"))


class Media(models.Model):
    name = models.CharField(max_length=50, verbose_name=_(u"Media"))
    image = models.ImageField(upload_to=u"movies/images/", verbose_name=_(u"Image"))
    movie = models.ForeignKey(Movie, verbose_name=_(u"Movie"))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u"Address"))
    street = models.CharField(max_length=50, verbose_name=_(u"Street name"))
    city = models.CharField(max_length=50, verbose_name=_("City"))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=50, verbose_name=_(u"Hall"))
    cinema = models.ForeignKey(Cinema, verbose_name=_(u"Cinema name"))
    address = models.OneToOneField(Address, verbose_name=_(u"Address"))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


SEAT_TYPE = (
    ('G', 'Gold'),
    ('S', 'Silver'),
    ('P', 'Platinum'),
)


class Seat(models.Model):
    row = models.CharField(max_length=10, verbose_name=_(u"Row"))
    no = models.IntegerField(verbose_name=_(u"Number"))
    seat_type = models.CharField(max_length=1, verbose_name=_(u"Seat type"), choices=SEAT_TYPE)
    hall = models.ForeignKey(Hall, verbose_name=_(u"Hall"))

    def __unicode__(self):
        return self.row+" "+str(self.no)

    def __str__(self):
        return self.row+" "+str(self.no)


class Show(models.Model):
    date = models.DateField(verbose_name=_(u"Date"))
    time = models.TimeField(verbose_name=_(u"Time"))
    language = models.CharField(max_length=50, verbose_name=_(u"Language"))
    screen = models.CharField(max_length=10, verbose_name=_(u"Format"))
    movie = models.ForeignKey(Movie, verbose_name=_(u"Movie"))
    hall = models.ForeignKey(Hall, verbose_name=_(u"Hall"))

    def __unicode__(self):
        return self.movie.title+" "+str(self.date)

    def __str__(self):
        return self.movie.title+" "+str(self.date)


class TicketType(models.Model):
    seat_type = models.CharField(max_length=1, verbose_name=_(u"Seat type"), choices=SEAT_TYPE)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_(u"Price"))
    show = models.ForeignKey(Show, verbose_name=_(u"Show"))

    def __unicode__(self):
        return self.get_seat_type_display()

    def __str__(self):
        return self.get_seat_type_display()


class Booking(models.Model):
    booking_id = models.CharField(max_length=50, verbose_name=_(u"Booking Id"))
    total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_(u"Total price"))
    user = models.ForeignKey(User, verbose_name=_(u"MovieGoer"))
    seat = models.ManyToManyField(Seat, verbose_name=_(u"Seats"))

    def __unicode__(self):
        return self.booking_id

    def __str__(self):
        return self.booking_id


class Review(models.Model):
    rating = models.IntegerField(verbose_name=_(u"Rating"))
    description = models.TextField(max_length=1000, verbose_name=_(u"Description"))
    movie = models.ForeignKey(Movie, verbose_name=_(u"Movie"))
    user = models.ForeignKey(User, verbose_name=_(u"MovieGoer"))

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description
