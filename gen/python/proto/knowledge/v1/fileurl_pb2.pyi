import datetime

from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileUrlState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_URL_STATE_UNSPECIFIED: _ClassVar[FileUrlState]
    FILE_URL_STATE_SUBMITTED: _ClassVar[FileUrlState]
    FILE_URL_STATE_PROCESSING: _ClassVar[FileUrlState]
    FILE_URL_STATE_SUCCESS: _ClassVar[FileUrlState]
    FILE_URL_STATE_ERROR: _ClassVar[FileUrlState]
FILE_URL_STATE_UNSPECIFIED: FileUrlState
FILE_URL_STATE_SUBMITTED: FileUrlState
FILE_URL_STATE_PROCESSING: FileUrlState
FILE_URL_STATE_SUCCESS: FileUrlState
FILE_URL_STATE_ERROR: FileUrlState

class FileUrl(_message.Message):
    __slots__ = ("name", "display_name", "description", "url", "mime_type", "headers", "size_bytes", "sha256_hash", "state", "created_by", "deleted_by", "create_time", "delete_time")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    url: str
    mime_type: str
    headers: _containers.ScalarMap[str, str]
    size_bytes: int
    sha256_hash: bytes
    state: FileUrlState
    created_by: str
    deleted_by: str
    create_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., url: _Optional[str] = ..., mime_type: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., size_bytes: _Optional[int] = ..., sha256_hash: _Optional[bytes] = ..., state: _Optional[_Union[FileUrlState, str]] = ..., created_by: _Optional[str] = ..., deleted_by: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
