from __future__ import annotations
import typing
from profskills.models import Topic


if typing.TYPE_CHECKING:
    from django.db.models import QuerySet


class TopicCrud:
    def get_by_name(self, topic_name: str) -> Topic | None:
        return Topic.objects.filter(name=topic_name).first()

    def all(self) -> "QuerySet[Topic]":
        return Topic.objects.all()

    def create(self, name: str, description: str | None, pet_project_ideas: str | None, useful_links: str | None) -> Topic:
        topic = Topic.objects.create(
            name = name,
            description = description,
            pet_project_ideas = pet_project_ideas,
            useful_links = useful_links
        )
        return topic

topic_crud = TopicCrud()