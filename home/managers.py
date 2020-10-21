from django.db import models
from django.db.models import Count
from django.shortcuts import render, redirect


class dashboarsDados(models.Manager):
    def count_realState(self,request):
        #return self.filter(userid=request.user.id).aggregate(Count('id'))['id__count']
        return



    def count_residents(self):
        return self.all().aggregate(Count('id'))['id__count']

