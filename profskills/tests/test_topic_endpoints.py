import pytest
from rest_framework import status as http_statuses
from rest_framework.test import APIClient

topics_endpoint = "/api/topics/"


class TestTopicViewSet:
    def setup_method(self):
        self.client = APIClient()

    @pytest.mark.django_db
    def test_create_topic(self, topic_data):
        response = self.client.post(topics_endpoint, topic_data)
        assert response.status_code == http_statuses.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_get_all_topics_empty_response(self):
        response = self.client.get(topics_endpoint + "get_all/")

        assert response.status_code == http_statuses.HTTP_200_OK
        assert len(response.data) == 0

    @pytest.mark.django_db
    def test_get_all_topics(self, topic):
        response = self.client.get(topics_endpoint + "get_all/")
        assert response.status_code == http_statuses.HTTP_200_OK
        assert response.data != []
        assert len(response.data) == 1

    @pytest.mark.django_db
    def test_get_topics_by_id(self, topic):
        topic_id = topic.id
        response = self.client.get(topics_endpoint + f"get_by_id/?id={topic_id}")
        assert response.status_code == http_statuses.HTTP_200_OK

        response = response.data
        assert response["id"] == topic.id
        assert response["name"] == topic.name
        assert response["description"] == topic.description
        assert response["useful_links"] == topic.useful_links
        assert response["pet_project_ideas"] == topic.pet_project_ideas

    @pytest.mark.django_db
    def test_get_topics_by_name(self, topic):
        topic_name = topic.name
        response = self.client.get(topics_endpoint + f"get_by_name/?name={topic_name}")
        assert response.status_code == http_statuses.HTTP_200_OK

        response = response.data
        assert response["id"] == topic.id
        assert response["name"] == topic.name
        assert response["description"] == topic.description
        assert response["useful_links"] == topic.useful_links
        assert response["pet_project_ideas"] == topic.pet_project_ideas
