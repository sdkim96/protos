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

class MemberRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMBER_ROLE_UNSPECIFIED: _ClassVar[MemberRole]
    MEMBER_ROLE_OWNER: _ClassVar[MemberRole]
    MEMBER_ROLE_EDITOR: _ClassVar[MemberRole]
    MEMBER_ROLE_VIEWER: _ClassVar[MemberRole]
MEMBER_ROLE_UNSPECIFIED: MemberRole
MEMBER_ROLE_OWNER: MemberRole
MEMBER_ROLE_EDITOR: MemberRole
MEMBER_ROLE_VIEWER: MemberRole

class Member(_message.Message):
    __slots__ = ("name", "account", "role", "create_time", "created_by", "delete_time", "deleted_by")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    name: str
    account: str
    role: MemberRole
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    delete_time: _timestamp_pb2.Timestamp
    deleted_by: str
    def __init__(self, name: _Optional[str] = ..., account: _Optional[str] = ..., role: _Optional[_Union[MemberRole, str]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., delete_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_by: _Optional[str] = ...) -> None: ...
