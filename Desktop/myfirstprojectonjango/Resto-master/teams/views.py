from django.db.models import fields
from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)
from .models import TeamMember


class TeamMemberCreateView(CreateView):
    model = TeamMember
    fields = (
        'user',
        'position',
        'education',
        'experience',
        'companies',
    )

    template_name = 'teams/team.html'

    def get_context_data(self, **kwargs):
        kwargs['teammember_list'] = TeamMember.objects.all()
        return super().get_context_data(**kwargs)


class TeamMemberDetailView(DetailView):
    model = TeamMember
    template_name = 'teams/teams_details.html'
