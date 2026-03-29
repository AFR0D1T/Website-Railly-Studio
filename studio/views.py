from django.shortcuts import get_object_or_404, render
from .models import Game, TeamMember


def home(request):
    """Главная — контроллер (логика + выбор шаблона)."""
    featured = Game.objects.all()[:3]
    team = TeamMember.objects.all()[:6]
    return render(
        request,
        "studio/home.html",
        {"featured_games": featured, "team": team},
    )


def game_list(request):
    """Каталог игр."""
    games = Game.objects.all()
    return render(request, "studio/game_list.html", {"games": games})


def game_detail(request, slug: str):
    """Страница одной игры."""
    game = get_object_or_404(Game, slug=slug)
    return render(request, "studio/game_detail.html", {"game": game})
