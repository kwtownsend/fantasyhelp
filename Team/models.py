from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Players.models import Player


class Team(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User)
    players = models.ManyToManyField(Player)
    
    def __unicode__(self):
        return self.name
        
    # def get_owner(self):
    #     owner = self.policies.owner.username
    #     # return leader
    #     return "leader guy"

    def add_player(self, new_player):
        self.players.add(Player.objects.get(pk=new_player.pk))

    def delete_player(self, old_player):
        self.players.remove(Player.objects.get(pk=old_player.pk))
        

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('Team:detail', args=[str(self.id)])

    def is_owner(self, user):
        if user == self.owner:
            return True
        return False


    # def is_owner(self, member):
    #     owned = User.objects.filter(team=self)
    #     if  owned in owner:
    #         return True
    #     return False

    def player_requests_list(self):
        return PlayerRequest.objects.filter(clubToJoin=self)

    # @staticmethod
    # def member_requests_count(self):
    #     return len(self.member_requests_list()) > 0





        
        
    


class PlayerRequest(models.Model):
    player = models.ForeignKey(Player, default=1)
    requester = models.ForeignKey(User)
    teamToJoin = models.ForeignKey(Team, verbose_name='Team Name')
    # request_date = models.DateField(default=timezone.now)
    reasonMessage = models.CharField(max_length=200, help_text="Why do you want to join this club?")



    
