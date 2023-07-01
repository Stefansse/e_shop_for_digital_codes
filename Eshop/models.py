from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=200)
    website = models.URLField(max_length=200, blank=True)
    logo = models.ImageField(upload_to="company_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    objects = models.Manager()


class CustomUser(AbstractUser):
    # Add custom fields to the user model
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    # Add any other fields you need

    def __str__(self):
        return self.username


class VideoGame(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    Real_time_strategy = "RE"
    Shooters = "SH"
    Multiplayer_online_battle_arena = "MU"
    Role_playing = "RO"
    Simulation_sports = "SI"
    Puzzlers_party_games = "PU"
    Action_adventure = "AC"
    Genre_Choices = [
        (Real_time_strategy, "RTS"),
        (Role_playing, "RPG"),
        (Shooters, "FPS"),
        (Multiplayer_online_battle_arena, "MOBA"),
        (Simulation_sports, "Sport"),
        (Puzzlers_party_games, "Puzzles"),
        (Action_adventure, "Action-Adventure"),
    ]
    genre = models.CharField(
        max_length=2,
        choices=Genre_Choices,
        default=Real_time_strategy,
    )
    release_date = models.DateField()
    videogame_image = models.ImageField(upload_to="videogame_images/", null=True, blank=True)
    price = models.IntegerField()
    platform = models.CharField(max_length=30, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    def get_genre_display_name(self):
        genre_dict = dict(self.Genre_Choices)
        return genre_dict.get(self.genre, "")

    def get_price(self):
        return f"{self.price}€"

    objects = models.Manager()


class DigitalCode(models.Model):
    videogame = models.ForeignKey(VideoGame, on_delete=models.CASCADE, null=True, blank=True)
    code_value = models.CharField(max_length=30, blank=True, null=True)
    date_of_creation = models.DateField()
    Available = "AV"
    Sold = "SO"
    Expired = "EX"
    Status_Choices = [
        (Available, "Available"),
        (Sold, "Sold"),
        (Expired, "Expired"),

    ]
    status = models.CharField(
        max_length=2,
        choices=Status_Choices,
        default=Available,
    )

    def __str__(self):
        return f"{self.videogame}->{self.code_value}"

    objects = models.Manager()


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    digital_codes = models.ManyToManyField(DigitalCode, related_name="digital_codes")
    order_date = models.DateField()
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    Pending = "PE"
    Completed = "CO"
    Cancelled = "CA"
    order_status_Choices = [
        (Pending, "Pending"),
        (Completed, "Completed"),
        (Cancelled, "Cancelled"),

    ]
    order_status = models.CharField(
        max_length=2,
        choices=order_status_Choices,
        default=Pending,
    )

    def __str__(self):
        codes = ", ".join(str(code) for code in self.digital_codes.all())
        return f"Order ID: {self.pk} | Codes: {codes} | Date: {self.order_date}"

    def get_order_price(self):
        return f"{self.total_price}€"

    objects = models.Manager()


class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.payment_date}->{self.payment_method}"

    objects = models.Manager()
