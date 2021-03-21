"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import feast.types.Value_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

global___FeastServingType = FeastServingType
class _FeastServingType(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FeastServingType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    FEAST_SERVING_TYPE_INVALID = FeastServingType.V(0)
    FEAST_SERVING_TYPE_ONLINE = FeastServingType.V(1)
    FEAST_SERVING_TYPE_BATCH = FeastServingType.V(2)
class FeastServingType(metaclass=_FeastServingType):
    V = typing.NewType('V', builtins.int)
FEAST_SERVING_TYPE_INVALID = FeastServingType.V(0)
FEAST_SERVING_TYPE_ONLINE = FeastServingType.V(1)
FEAST_SERVING_TYPE_BATCH = FeastServingType.V(2)

class GetFeastServingInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___GetFeastServingInfoRequest = GetFeastServingInfoRequest

class GetFeastServingInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    JOB_STAGING_LOCATION_FIELD_NUMBER: builtins.int
    version: typing.Text = ...
    type: global___FeastServingType.V = ...
    job_staging_location: typing.Text = ...

    def __init__(self,
        *,
        version : typing.Text = ...,
        type : global___FeastServingType.V = ...,
        job_staging_location : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"job_staging_location",b"job_staging_location",u"type",b"type",u"version",b"version"]) -> None: ...
global___GetFeastServingInfoResponse = GetFeastServingInfoResponse

class FeatureReferenceV2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FEATURE_TABLE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    feature_table: typing.Text = ...
    name: typing.Text = ...

    def __init__(self,
        *,
        feature_table : typing.Text = ...,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"feature_table",b"feature_table",u"name",b"name"]) -> None: ...
global___FeatureReferenceV2 = FeatureReferenceV2

class GetOnlineFeaturesRequestV2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class EntityRow(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class FieldsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...

            @property
            def value(self) -> feast.types.Value_pb2.Value: ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[feast.types.Value_pb2.Value] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        TIMESTAMP_FIELD_NUMBER: builtins.int
        FIELDS_FIELD_NUMBER: builtins.int

        @property
        def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...

        @property
        def fields(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, feast.types.Value_pb2.Value]: ...

        def __init__(self,
            *,
            timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
            fields : typing.Optional[typing.Mapping[typing.Text, feast.types.Value_pb2.Value]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"timestamp",b"timestamp"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"fields",b"fields",u"timestamp",b"timestamp"]) -> None: ...

    FEATURES_FIELD_NUMBER: builtins.int
    ENTITY_ROWS_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    project: typing.Text = ...

    @property
    def features(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeatureReferenceV2]: ...

    @property
    def entity_rows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetOnlineFeaturesRequestV2.EntityRow]: ...

    def __init__(self,
        *,
        features : typing.Optional[typing.Iterable[global___FeatureReferenceV2]] = ...,
        entity_rows : typing.Optional[typing.Iterable[global___GetOnlineFeaturesRequestV2.EntityRow]] = ...,
        project : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"entity_rows",b"entity_rows",u"features",b"features",u"project",b"project"]) -> None: ...
global___GetOnlineFeaturesRequestV2 = GetOnlineFeaturesRequestV2

class GetOnlineFeaturesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FieldStatus(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FieldStatus.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        INVALID = GetOnlineFeaturesResponse.FieldStatus.V(0)
        PRESENT = GetOnlineFeaturesResponse.FieldStatus.V(1)
        NULL_VALUE = GetOnlineFeaturesResponse.FieldStatus.V(2)
        NOT_FOUND = GetOnlineFeaturesResponse.FieldStatus.V(3)
        OUTSIDE_MAX_AGE = GetOnlineFeaturesResponse.FieldStatus.V(4)
    class FieldStatus(metaclass=_FieldStatus):
        V = typing.NewType('V', builtins.int)
    INVALID = GetOnlineFeaturesResponse.FieldStatus.V(0)
    PRESENT = GetOnlineFeaturesResponse.FieldStatus.V(1)
    NULL_VALUE = GetOnlineFeaturesResponse.FieldStatus.V(2)
    NOT_FOUND = GetOnlineFeaturesResponse.FieldStatus.V(3)
    OUTSIDE_MAX_AGE = GetOnlineFeaturesResponse.FieldStatus.V(4)

    class FieldValues(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class FieldsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...

            @property
            def value(self) -> feast.types.Value_pb2.Value: ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Optional[feast.types.Value_pb2.Value] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        class StatusesEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: global___GetOnlineFeaturesResponse.FieldStatus.V = ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : global___GetOnlineFeaturesResponse.FieldStatus.V = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        FIELDS_FIELD_NUMBER: builtins.int
        STATUSES_FIELD_NUMBER: builtins.int

        @property
        def fields(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, feast.types.Value_pb2.Value]: ...

        @property
        def statuses(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, global___GetOnlineFeaturesResponse.FieldStatus.V]: ...

        def __init__(self,
            *,
            fields : typing.Optional[typing.Mapping[typing.Text, feast.types.Value_pb2.Value]] = ...,
            statuses : typing.Optional[typing.Mapping[typing.Text, global___GetOnlineFeaturesResponse.FieldStatus.V]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"fields",b"fields",u"statuses",b"statuses"]) -> None: ...

    FIELD_VALUES_FIELD_NUMBER: builtins.int

    @property
    def field_values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetOnlineFeaturesResponse.FieldValues]: ...

    def __init__(self,
        *,
        field_values : typing.Optional[typing.Iterable[global___GetOnlineFeaturesResponse.FieldValues]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"field_values",b"field_values"]) -> None: ...
global___GetOnlineFeaturesResponse = GetOnlineFeaturesResponse
