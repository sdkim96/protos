from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from proto.knowledge.v1 import file_pb2 as _file_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("parent", "file_name", "display_name", "description", "expected_size_bytes")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    file_name: str
    display_name: str
    description: str
    expected_size_bytes: int
    def __init__(self, parent: _Optional[str] = ..., file_name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., expected_size_bytes: _Optional[int] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _file_pb2.File
    def __init__(self, file: _Optional[_Union[_file_pb2.File, _Mapping]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _file_pb2.File
    def __init__(self, file: _Optional[_Union[_file_pb2.File, _Mapping]] = ...) -> None: ...

class UploadMetadata(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UploadRequest(_message.Message):
    __slots__ = ("name", "content")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: _httpbody_pb2.HttpBody
    def __init__(self, name: _Optional[str] = ..., content: _Optional[_Union[_httpbody_pb2.HttpBody, _Mapping]] = ...) -> None: ...

class UploadResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _file_pb2.File
    def __init__(self, file: _Optional[_Union[_file_pb2.File, _Mapping]] = ...) -> None: ...
