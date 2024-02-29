import pytest
from rest_framework import status as http_statuses
from rest_framework.test import APIClient

profession_endpoint = "/api/professions/"


class TestProfessionsViewSet:
    def setup_method(self):
        self.client = APIClient()

    @pytest.mark.django_db
    def test_create_profession(self, profession_data_without_skills, skill_with_topic):
        profession_data_without_skills["skills"] = [skill_with_topic.id]
        response = self.client.post(profession_endpoint, profession_data_without_skills)
        assert response.status_code == http_statuses.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_get_all_professions_empty_response(self):
        response = self.client.get(profession_endpoint + "get_all/")

        assert response.status_code == http_statuses.HTTP_200_OK
        assert len(response.data) == 0

    @pytest.mark.django_db
    def test_get_all_professions(self, profession_with_skill):
        response = self.client.get(profession_endpoint + "get_all/")
        assert response.status_code == http_statuses.HTTP_200_OK
        assert response.data != []
        assert len(response.data) == 1

    @pytest.mark.django_db
    def test_get_topics_by_id(self, profession_with_skill):
        profession_id = profession_with_skill.id
        response = self.client.get(
            profession_endpoint + f"get_by_id/?id={profession_id}"
        )
        assert response.status_code == http_statuses.HTTP_200_OK

        response = response.data
        assert response["id"] == profession_with_skill.id
        assert response["name"] == profession_with_skill.name
        assert response["description"] == profession_with_skill.description
        assert len(response["skills"]) == profession_with_skill.skills.count()

    @pytest.mark.django_db
    def test_get_topics_by_name(self, profession_with_skill):
        profession_name = profession_with_skill.name
        response = self.client.get(
            profession_endpoint + f"get_by_name/?name={profession_name}"
        )
        assert response.status_code == http_statuses.HTTP_200_OK

        response = response.data
        assert response["id"] == profession_with_skill.id
        assert response["name"] == profession_with_skill.name
        assert response["description"] == profession_with_skill.description
        assert len(response["skills"]) == profession_with_skill.skills.count()
