import pytest
from django.urls import reverse
from rest_framework import status as http_statuses
from rest_framework.test import APIClient

topics_endpoint = "api/topics/"


class TestTopicViewSet:
    def setup_method(self):
        self.client = APIClient()

    # todo Make tests

    # @pytest.mark.django_db
    # def test_create_topic(self):
    #     data = {
    #         "name": "string",
    #         "description":"description",
    #         "pet_project_ideas" :"pet_project_ideas",
    #         "useful_links" : "useful_links"
    #     }
    #     response = self.client.post(topics_endpoint, data)
    #     assert response.status_code == http_statuses.HTTP_200_OK

    # @pytest.mark.django_db
    # def test_get_all_topics(self):
    #     response = self.client.get(reverse("profskills:get_all_topics"))
    #
    #     assert response.status_code == http_statuses.HTTP_200_OK
