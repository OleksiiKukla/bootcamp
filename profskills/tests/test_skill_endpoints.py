import pytest
from rest_framework import status as http_statuses
from rest_framework.test import APIClient

skill_endpoint = "/api/skills/"


class TestSkillViewSet:
    def setup_method(self):
        self.client = APIClient()

    @pytest.mark.django_db
    def test_create_skill(self, skill_data_without_topics, topic):
        skill_data_without_topics["topics"] = [topic.id]
        response = self.client.post(skill_endpoint, skill_data_without_topics)
        assert response.status_code == http_statuses.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_get_all_skills_empty_response(self):
        response = self.client.get(skill_endpoint + "get_all/")

        assert response.status_code == http_statuses.HTTP_200_OK
        assert len(response.data) == 0

    @pytest.mark.django_db
    def test_get_all_topics(self, skill_with_topic):
        response = self.client.get(skill_endpoint + "get_all/")
        assert response.status_code == http_statuses.HTTP_200_OK
        assert response.data != []
        assert len(response.data) == 1

    @pytest.mark.django_db
    def test_get_topics_by_id(self, skill_with_topic):
        skill_id = skill_with_topic.id
        response = self.client.get(skill_endpoint + f"get_by_id/?id={skill_id}")
        assert response.status_code == http_statuses.HTTP_200_OK

        response = response.data
        assert response["id"] == skill_with_topic.id
        assert response["name"] == skill_with_topic.name
        assert response["description"] == skill_with_topic.description
        assert len(response["topics"]) == skill_with_topic.topics.count()

    @pytest.mark.django_db
    def test_get_topics_by_name(self, skill_with_topic):
        skill_name = skill_with_topic.name
        response = self.client.get(skill_endpoint + f"get_by_name/?name={skill_name}")
        assert response.status_code == http_statuses.HTTP_200_OK

        response = response.data
        assert response["id"] == skill_with_topic.id
        assert response["name"] == skill_with_topic.name
        assert response["description"] == skill_with_topic.description
        assert len(response["topics"]) == skill_with_topic.topics.count()
