from typing import Protocol

from rest_framework.request import HttpRequest
from rest_framework.serializers import Serializer


class APIViewProtocol(Protocol):
    request: HttpRequest


class GenericAPIViewProtocol(APIViewProtocol, Protocol):
    def get_serializer_class(self) -> type[Serializer]: ...


class CreateReadSerializerMixinProtocol(GenericAPIViewProtocol, Protocol):
    read_serializer_class: type[Serializer]
    create_serializer_class: type[Serializer]
