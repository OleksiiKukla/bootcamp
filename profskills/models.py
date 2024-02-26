from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    pet_project_ideas = models.TextField(blank=True, null=True)
    useful_links = models.TextField(blank=True, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    topics = models.ManyToManyField(
        Topic, blank=True,
    )


class Professions(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(
        Skill, blank=True,
    )

