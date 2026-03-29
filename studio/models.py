from django.db import models
from django.urls import reverse


class Game(models.Model):
    """Игра студии — модель (M в MVC)."""

    class Status(models.TextChoices):
        DEVELOPMENT = "dev", "В разработке"
        EARLY_ACCESS = "ea", "Ранний доступ"
        RELEASED = "released", "Выпущена"

    title = models.CharField("название", max_length=200)
    slug = models.SlugField("slug", max_length=200, unique=True)
    tagline = models.CharField("слоган", max_length=300, blank=True)
    description = models.TextField("описание")
    genre = models.CharField("жанр", max_length=120)
    status = models.CharField(
        "статус",
        max_length=20,
        choices=Status.choices,
        default=Status.DEVELOPMENT,
    )
    release_date = models.DateField("дата релиза", null=True, blank=True)
    cover = models.ImageField(
        "обложка",
        upload_to="games/covers/",
        blank=True,
        help_text="JPEG или PNG, желательно 16:9",
    )
    created_at = models.DateTimeField("создано", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "игра"
        verbose_name_plural = "игры"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("studio:game_detail", kwargs={"slug": self.slug})


class TeamMember(models.Model):
    """Участник команды."""

    name = models.CharField("имя", max_length=120)
    role = models.CharField("роль", max_length=120)
    bio = models.TextField("био", blank=True)
    order = models.PositiveSmallIntegerField("порядок", default=0)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "участник команды"
        verbose_name_plural = "команда"

    def __str__(self) -> str:
        return f"{self.name} — {self.role}"
