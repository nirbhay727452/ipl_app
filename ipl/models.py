from django.db import models
import uuid
# Create your models here.

class Matches(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    season=models.IntegerField(blank=False)
    city=models.CharField(max_length=90,null=True)
    date=models.DateField()
    team1=models.CharField(max_length=90)
    team2=models.CharField(max_length=90)
    toss_winner=models.CharField(null=True,max_length=90)
    toss_decision=models.CharField(null=True,max_length=90)
    result=models.CharField(null=True,max_length=90)
    dl_applied=models.CharField(default=0,max_length=90)
    winner=models.CharField(null=True,max_length=90)
    win_by_run=models.IntegerField(default=0)
    win_by_wickets=models.IntegerField(default=0)
    player_of_match=models.CharField(null=True,max_length=90)
    venue=models.CharField(max_length=90)
    umpire1=models.CharField(max_length=90,null=True)
    umpire2=models.CharField(max_length=90,null=True)
    umpire3=models.CharField(null=True,max_length=90)

    def __str__(self):
        return self.id


class Deliveries(models.Model):
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
    inning=models.IntegerField()
    batting_team=models.CharField(max_length=90)
    bowling_team=models.CharField(max_length=90)
    over=models.IntegerField()
    ball=models.IntegerField()
    batsman=models.CharField(max_length=90)
    non_striker=models.CharField(max_length=90)
    bowler=models.CharField(max_length=90)
    is_super_over=models.IntegerField(default=0)
    wide_runs=models.IntegerField(default=0)
    bye_runs=models.IntegerField(default=0)
    legbye_runs=models.IntegerField(default=0)
    noball_runs=models.IntegerField(default=0)
    penality_runs=models.IntegerField(default=0)
    batsman_runs=models.IntegerField(default=0)
    extra_runs=models.IntegerField(default=0)
    total_runs=models.IntegerField(default=0)
    player_dismissed=models.CharField(max_length=90, null=True)
    dismissal=models.CharField(max_length=90, null=True)
    fielder=models.CharField(max_length=90, null=True)
