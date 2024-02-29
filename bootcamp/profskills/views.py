from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import CharField

from bootcamp.profskills.crud.profession_crud import profession_crud
from bootcamp.profskills.crud.skill_crud import skill_crud
from bootcamp.profskills.crud.topic_crud import topic_crud
from bootcamp.profskills.serializers import (
    ProfessionSerializer,
    SkillSerializer,
    TopicSerializer,
)


@extend_schema(tags=["Topic"])
class TopicViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get_serializer(self, *args, **kwargs):
        return TopicSerializer(*args, **kwargs)

    @action(
        detail=False,
        methods=["get"],
        name="Get all",
        url_path="get_all",
    )
    def get_all(self, request):
        topics = topic_crud.all()
        serializer = self.get_serializer(topics, many=True)

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
            name=request.data["name"],
            description=request.data["description"],
            pet_project_ideas=request.data["pet_project_ideas"],
            useful_links=request.data["useful_links"],
        )
        serializer = self.get_serializer(topic)
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
        responses={
            "200": OpenApiResponse(
                response=TopicSerializer,
            ),
            "404": OpenApiResponse(
                description="Topic object with Name 'id' does not exist.",
                response=inline_serializer(
                    name="Topic object with Name 'id' does not exist.",
                    fields={
                        "error": bool,
                        "message": CharField(),
                    },
                ),
            ),
        },
    )
    @action(
        detail=False,
        methods=["get"],
        name="Get by name",
        url_path="get_by_name",
    )
    def get_by_name(self, request):
        topic_name = request.GET.get("name")
        topic = topic_crud.get_by_name(topic_name)
        if not topic:
            return Response(
                data={
                    "error": True,
                    "message": f"Topic object with Name '{topic_name}' does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(topic)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type={"type": "int"},
                location=OpenApiParameter.QUERY,
                required=False,
                style="form",
                explode=False,
            )
        ],
        responses={
            "200": OpenApiResponse(
                response=TopicSerializer,
            ),
            "404": OpenApiResponse(
                description="Topic object with ID 'id' does not exist.",
                response=inline_serializer(
                    name="Topic object with ID 'id' does not exist.",
                    fields={
                        "error": bool,
                        "message": CharField(),
                    },
                ),
            ),
        },
    )
    @action(
        detail=False,
        methods=["get"],
        name="Get by ID",
        url_path="get_by_id",
    )
    def get_by_id(self, request):
        topic_id = request.GET.get("id")
        topic = topic_crud.get_by_id(topic_id)
        if not topic:
            return Response(
                data={
                    "error": True,
                    "message": f"Topic object with ID '{topic_id}' does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(topic)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


@extend_schema(tags=["Skill"])
class SkillViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get_serializer(self, *args, **kwargs):
        return SkillSerializer(*args, **kwargs)

    @action(
        detail=False,
        methods=["get"],
        name="Get all",
        url_path="get_all",
    )
    def get_all(self, request):
        skills = skill_crud.all()
        serializer = self.get_serializer(skills, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        request=SkillSerializer,
        responses={
            "201": OpenApiResponse(
                response=SkillSerializer,
            ),
            "404": OpenApiResponse(
                description="Skill object with ID 'topic_id' does not exist.",
                response=inline_serializer(
                    name="Skill object with ID 'topic_id' does not exist.",
                    fields={
                        "error": bool,
                        "message": CharField(),
                    },
                ),
            ),
        },
    )
    def create(self, request):
        topics = request.data["topics"]
        for topic_id in topics:
            topic = topic_crud.get_by_id(topic_id)
            if not topic:
                return Response(
                    data={
                        "error": True,
                        "message": f"Topic object with ID '{topic_id}' does not exist.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

        topic = skill_crud.create(
            name=request.data["name"],
            description=request.data["description"],
            topics=topics,
        )
        serializer = self.get_serializer(topic)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type={"type": "int"},
                location=OpenApiParameter.QUERY,
                required=False,
                style="form",
                explode=False,
            )
        ],
        responses={
            "200": OpenApiResponse(
                response=SkillSerializer,
            ),
            "404": OpenApiResponse(
                description="Skill object with ID 'id' does not exist.",
                response=inline_serializer(
                    name="Skill object with ID 'id' does not exist.",
                    fields={
                        "error": bool,
                        "message": CharField(),
                    },
                ),
            ),
        },
    )
    @action(
        detail=False,
        methods=["get"],
        name="Get by ID",
        url_path="get_by_id",
    )
    def get_by_id(self, request):
        skill_id = request.GET.get("id")
        skill = skill_crud.get_by_id(skill_id)
        if not skill:
            return Response(
                data={
                    "error": True,
                    "message": f"Skill object with ID '{skill_id}' does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(skill)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
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
        responses=SkillSerializer(),
    )
    @action(
        detail=False,
        methods=["get"],
        name="Get by name",
        url_path="get_by_name",
    )
    def get_by_name(self, request):
        skill_name = request.GET.get("name")
        skill = skill_crud.get_by_name(skill_name)
        if not skill:
            return Response(
                data={
                    "error": True,
                    "message": f"Skill object with Name '{skill_name}' does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(skill)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


@extend_schema(tags=["Profession"])
class ProfessionViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get_serializer(self, *args, **kwargs):
        return ProfessionSerializer(*args, **kwargs)

    @action(
        detail=False,
        methods=["get"],
        name="Get all",
        url_path="get_all",
    )
    def get_all(self, request):
        professions = profession_crud.all()
        serializer = self.get_serializer(professions, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        request=ProfessionSerializer,
        responses={
            "201": OpenApiResponse(
                response=ProfessionSerializer,
            ),
            "404": OpenApiResponse(
                description="Profession object with ID 'profession_id' does not exist.",
                response=inline_serializer(
                    name="Profession object with ID 'profession_id' does not exist.",
                    fields={
                        "error": bool,
                        "message": CharField(),
                    },
                ),
            ),
        },
    )
    def create(self, request):
        skills = request.data["skills"]
        for skill_id in skills:
            skill = skill_crud.get_by_id(skill_id)
            if not skill:
                return Response(
                    data={
                        "error": True,
                        "message": f"Skill object with ID '{skill_id}' does not exist.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

        topic = profession_crud.create(
            name=request.data["name"],
            description=request.data["description"],
            skills=skills,
        )
        serializer = self.get_serializer(topic)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type={"type": "int"},
                location=OpenApiParameter.QUERY,
                required=False,
                style="form",
                explode=False,
            )
        ],
        responses={
            "200": OpenApiResponse(
                response=ProfessionSerializer,
            ),
            "404": OpenApiResponse(
                description="Profession object with ID 'id' does not exist.",
                response=inline_serializer(
                    name="Profession object with ID 'id' does not exist.",
                    fields={
                        "error": bool,
                        "message": CharField(),
                    },
                ),
            ),
        },
    )
    @action(
        detail=False,
        methods=["get"],
        name="Get by ID",
        url_path="get_by_id",
    )
    def get_by_id(self, request):
        profession_id = request.GET.get("id")
        profession = profession_crud.get_by_id(profession_id)
        if not profession:
            return Response(
                data={
                    "error": True,
                    "message": f"Profession object with ID '{profession_id}' does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(profession)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
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
        responses=ProfessionSerializer(),
    )
    @action(
        detail=False,
        methods=["get"],
        name="Get by name",
        url_path="get_by_name",
    )
    def get_by_name(self, request):
        profession_name = request.GET.get("name")
        profession = profession_crud.get_by_name(profession_name)
        if not profession:
            return Response(
                data={
                    "error": True,
                    "message": f"Profession object with Name '{profession_name}' does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(profession)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
