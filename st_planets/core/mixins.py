from typing import Any

from rest_framework.request import HttpRequest
from rest_framework.serializers import Serializer

from st_planets.typing.views import CreateReadSerializerMixinProtocol


class CreateReadSerializerMixin:
    read_serializer_class: type[Serializer] | None = None
    create_serializer_class: type[Serializer] | None = None

    def initial(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        super().initial(request, *args, **kwargs)  # type: ignore
        if not self.create_serializer_class or not self.read_serializer_class:
            raise AttributeError(
                "read_serializer_class and create_serializer class mustn't be None"
            )

    def get_serializer_class(
        self: CreateReadSerializerMixinProtocol,
    ) -> type[Serializer]:
        if self.request.method == "GET":
            return self.read_serializer_class
        return self.create_serializer_class
