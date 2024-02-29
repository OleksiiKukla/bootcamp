import pytest

from bootcamp.profskills.models import Profession, Skill, Topic


# Topic fixtures
@pytest.fixture
def topic_data():
    data = {
        "name": "string",
        "description": "description",
        "pet_project_ideas": "pet_project_ideas",
        "useful_links": "useful_links",
    }
    return data


@pytest.fixture
def topic(topic_data):
    return Topic.objects.create(**topic_data)


# Skill fixtures


@pytest.fixture
def skill_data_without_topics():
    data = {
        "name": "actor",
        "description": "can doing cool stuff",
    }
    return data


@pytest.fixture
def skill_with_topic(skill_data_without_topics, topic):
    skill = Skill.objects.create(**skill_data_without_topics)
    skill.topics.add(topic)
    return skill


# Profession fixtures


@pytest.fixture
def profession_data_without_skills():
    data = {
        "name": "architect",
        "description": "make magic",
    }
    return data


@pytest.fixture
def profession_with_skill(profession_data_without_skills, skill_with_topic):
    profession = Profession.objects.create(**profession_data_without_skills)
    profession.skills.add(skill_with_topic)
    return profession
