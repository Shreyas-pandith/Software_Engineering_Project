from django.shortcuts import render, redirect
from .forms import PlayerProfileForm
from .models import Player
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from performance.models import PerformanceMatchWise


def player_home(request):
    if request.user.username:
        user = Player.objects.get(pk=request.user)
        context = {'P': user}
        return render(request, 'player/home.html', context)
    else:
        return redirect('player:player_login')


def player_performance(request):
    try:
        player = Player.objects.get(pk=request.user.id)
        data = PerformanceMatchWise.objects.filter(player=player).order_by('name')
        labels = []
        values = []
        for key in data:
            labels.append(key.name)
            values.append(key.batting_runs)
        context = {'labels': labels, 'values': values}
        return render(request, 'player/performance.html', context)
    except Exception:
        return redirect('login')


def player_view_profile(request):
    if request.user.username :
        user = Player.objects.get(pk=request.user)
        # player = vars(user) to list all attributes
        player = user.profile()
        context = {'player': player, 'P': user}
        return render(request, 'player/view_profile.html', context)
    else:
        return redirect('login')


def player_edit_profile(request):
    if request.user.username:
        player = Player.objects.get(pk=request.user.id)
        if request.method == 'POST':
            form = PlayerProfileForm(request.POST, instance=player)
            if form.is_valid():
                form.save()
                return redirect('player:player_view_profile')
        else:
            form = PlayerProfileForm(instance=player)
            context = {'form': form, 'P': player}
            return render(request, 'player/edit_profile.html', context)
    else:
        return redirect('login')


def player_change_password(request):
    if request.user.username:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('player:player_change_password_done')
            else:
                messages.error(request, 'Please correct the error below.')
                return redirect('player:player_change_password')
        else:
            form = PasswordChangeForm(user=request.user)
            context = {'form': form, 'P': Player.objects.get(pk=request.user.id)}
            return render(request, 'player/change_password.html', context)
    else:
        return redirect('login')


def player_change_password_done(request):
    if request.user.username:
        context = {'P': Player.objects.get(pk=request.user.id)}
        return render(request, 'player/change_password_done.html', context)
    return redirect('login')


