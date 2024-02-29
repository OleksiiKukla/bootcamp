from __future__ import annotations

import typing

from bootcamp.profskills.models import Skill, Topic

if typing.TYPE_CHECKING:
    from django.db.models import QuerySet


class SkillCrud:

    def get_by_name(self, skill_name: str) -> Skill | None:
        return Skill.objects.filter(name=skill_name).first()

    def all(self) -> "QuerySet[Skill]":
        return Skill.objects.all()

    def get_by_id(self, skill_id: str) -> Skill | None:
        return Skill.objects.filter(id=skill_id).first()

    def create(
        self,
        name: str,
        description: str | None,
        topics: list[Topic] | None,
    ) -> Skill:
        skill = Skill.objects.create(
            name=name,
            description=description,
        )
        if topics:
            skill.topics.add(*topics)
        return skill


skill_crud = SkillCrud()
