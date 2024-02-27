from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema, OpenApiResponse
)
from rest_framework import viewsets

from profskills.crud.topic_crud import topic_crud
from profskills.serializers import TopicSerializer

@extend_schema(tags=["Topic"])
class TopicViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(
        detail=False,
        methods=["get"],
        name="Get all",
        url_path="get_all",
            )
    def get_all(self, request):
        topics = topic_crud.all()
        serializer = TopicSerializer(topics, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
    @extend_schema(
        request=TopicSerializer,
        responses={
            "201": OpenApiResponse(
                response=TopicSerializer,
            ),
        },
    )
    def create(self, request):
        topic = topic_crud.create(
            name=request.data['name'],
            description=request.data['description'],
            pet_project_ideas=request.data['pet_project_ideas'],
            useful_links=request.data['useful_links']
        )
        serializer = TopicSerializer(topic)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                type={"type": "str"},
                location=OpenApiParameter.QUERY,
                required=False,
                style="form",
                explode=False,
            )
        ],
        responses=TopicSerializer(),
    )
    @action(
        detail=False,
        methods=["get"],
        name="Get by name",
        url_path="get_by_name",
    )
    def get_by_name(self, request):
        topic = topic_crud.get_by_name(request.GET.get("name"))
        serializer = TopicSerializer(topic)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )