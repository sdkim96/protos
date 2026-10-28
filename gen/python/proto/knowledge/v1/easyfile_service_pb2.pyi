from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from proto.knowledge.v1 import file_pb2 as _file_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EasyUploadRequest(_message.Message):
    __slots__ = ("parent", "file_name", "display_name", "description", "mime_type", "content")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    file_name: str
    display_name: str
    description: str
    mime_type: str
    content: bytes
    def __init__(self, parent: _Optional[str] = ..., file_name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., mime_type: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...
