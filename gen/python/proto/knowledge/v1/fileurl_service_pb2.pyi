from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from proto.knowledge.v1 import fileurl_pb2 as _fileurl_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileUrlRequest(_message.Message):
    __slots__ = ("parent", "file_url")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    file_url: _fileurl_pb2.FileUrl
    def __init__(self, parent: _Optional[str] = ..., file_url: _Optional[_Union[_fileurl_pb2.FileUrl, _Mapping]] = ...) -> None: ...

class GetFileUrlRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
