from django.forms import ModelForm

from Team.models import Team, PlayerRequest
from Players.models import Player
from django.contrib.auth.models import User

from django.http import Http404
import datetime



# class PlayerRequest(models.Model):
#     requester = models.ForeignKey(User)
#     teamToJoin = models.ForeignKey(Team)
#     # request_date = models.DateField(default=timezone.now)
    # reasonMessage = models.CharField(max_length=200, help_text="Why do you want to join this club?")


class newPlayerRequest(ModelForm):
    class Meta:
        model = PlayerRequest
        fields = ["teamToJoin"]


    _requester = None
    _owner = None
    _teamToJoin = None
    _player = None
    _team = None

    def set_requester(self, requester):
        self._requester = requester

    def __init__(self, *args, **kwargs):
        curr = kwargs.pop('current_owner')
        super(newPlayerRequest, self).__init__(*args, **kwargs)
        self.fields['teamToJoin'].queryset = Team.objects.filter(owner=curr)


    def set_owner(self, requester):
        self._owner = owner

    def set_player(self, player):
        self._player = player

    def set_teams(self, current_logged):
        self._team = current_logged

    def save(self, *args, **kwargs):
        # if self._policy:
        #     self.instance.policies = self._policy
        # else:
        #     return Http404("something is wrong")

        # self.instance.request_date = datetime.datetime.now()
        self.instance.requester = self._requester
        self.instance.player = Player.objects.get(pk=self._player)
        self.instance.teamToJoin = Team.objects.filter(owner = self._team)
        # teamWanted = Team.objects.get(pk=self._teamToJoin)
        # self.instance.teamToJoin = teamWanted
        # teamWanted = Team.objects.get(pk=self._teamToJoin)
        # self.instance.teamToJoin = teamWanted
        # self.instance.clubToJoin = self._clubToJoin
        resp = super(newPlayerRequest, self).save(*args, **kwargs)
        return resp
