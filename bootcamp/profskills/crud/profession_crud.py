from __future__ import annotations

import typing

from bootcamp.profskills.models import Profession, Skill

if typing.TYPE_CHECKING:
    from django.db.models import QuerySet


class ProfessionCrud:

    def get_by_name(self, profession_name: str) -> Profession | None:
        return Profession.objects.filter(name=profession_name).first()

    def get_by_id(self, profession_id: str) -> Profession | None:
        return Profession.objects.filter(id=profession_id).first()

    def all(self) -> "QuerySet[Profession]":
        return Profession.objects.all()

    def create(
        self,
        name: str,
        description: str | None,
        skills: list[Skill] | None,
    ) -> Profession:
        profession = Profession.objects.create(
            name=name,
            description=description,
        )
        if skills:
            profession.skills.add(*skills)

        return profession


profession_crud = ProfessionCrud()
