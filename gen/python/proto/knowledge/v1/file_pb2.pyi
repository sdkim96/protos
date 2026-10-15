import datetime

from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_STATE_UNSPECIFIED: _ClassVar[FileState]
    FILE_STATE_UPLOADING: _ClassVar[FileState]
    FILE_STATE_SUCCESS: _ClassVar[FileState]
    FILE_STATE_ERROR: _ClassVar[FileState]
FILE_STATE_UNSPECIFIED: FileState
FILE_STATE_UPLOADING: FileState
FILE_STATE_SUCCESS: FileState
FILE_STATE_ERROR: FileState

class File(_message.Message):
    __slots__ = ("name", "display_name", "description", "mime_type", "size_bytes", "create_time", "created_by", "update_time", "updated_by", "delete_time", "deleted_by", "state")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    mime_type: str
    size_bytes: int
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    update_time: _timestamp_pb2.Timestamp
    updated_by: str
    delete_time: _timestamp_pb2.Timestamp
    deleted_by: str
    state: FileState
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., mime_type: _Optional[str] = ..., size_bytes: _Optional[int] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ..., delete_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_by: _Optional[str] = ..., state: _Optional[_Union[FileState, str]] = ...) -> None: ...

class FileMeta(_message.Message):
    __slots__ = ("filename", "content_type", "size_bytes")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    filename: str
    content_type: str
    size_bytes: int
    def __init__(self, filename: _Optional[str] = ..., content_type: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class FileServiceCreateRequest(_message.Message):
    __slots__ = ("file_meta", "chunk", "display_name", "description")
    FILE_META_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    file_meta: FileMeta
    chunk: bytes
    display_name: str
    description: str
    def __init__(self, file_meta: _Optional[_Union[FileMeta, _Mapping]] = ..., chunk: _Optional[bytes] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class FileServiceCreateResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: File
    def __init__(self, file: _Optional[_Union[File, _Mapping]] = ...) -> None: ...
