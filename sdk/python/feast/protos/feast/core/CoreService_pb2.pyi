"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import feast.core.Entity_pb2
import feast.core.FeatureTable_pb2
import feast.core.Feature_pb2
import feast.core.Store_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetEntityRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    project: typing.Text = ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        project : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"project",b"project"]) -> None: ...
global___GetEntityRequest = GetEntityRequest

class GetEntityResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITY_FIELD_NUMBER: builtins.int

    @property
    def entity(self) -> feast.core.Entity_pb2.Entity: ...

    def __init__(self,
        *,
        entity : typing.Optional[feast.core.Entity_pb2.Entity] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"entity",b"entity"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"entity",b"entity"]) -> None: ...
global___GetEntityResponse = GetEntityResponse

class ListEntitiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Filter(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class LabelsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: typing.Text = ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        PROJECT_FIELD_NUMBER: builtins.int
        LABELS_FIELD_NUMBER: builtins.int
        project: typing.Text = ...

        @property
        def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...

        def __init__(self,
            *,
            project : typing.Text = ...,
            labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"labels",b"labels",u"project",b"project"]) -> None: ...

    FILTER_FIELD_NUMBER: builtins.int

    @property
    def filter(self) -> global___ListEntitiesRequest.Filter: ...

    def __init__(self,
        *,
        filter : typing.Optional[global___ListEntitiesRequest.Filter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"filter",b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"filter",b"filter"]) -> None: ...
global___ListEntitiesRequest = ListEntitiesRequest

class ListEntitiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITIES_FIELD_NUMBER: builtins.int

    @property
    def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[feast.core.Entity_pb2.Entity]: ...

    def __init__(self,
        *,
        entities : typing.Optional[typing.Iterable[feast.core.Entity_pb2.Entity]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"entities",b"entities"]) -> None: ...
global___ListEntitiesResponse = ListEntitiesResponse

class ListFeaturesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Filter(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class LabelsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: typing.Text = ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        LABELS_FIELD_NUMBER: builtins.int
        ENTITIES_FIELD_NUMBER: builtins.int
        PROJECT_FIELD_NUMBER: builtins.int
        entities: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...
        project: typing.Text = ...

        @property
        def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...

        def __init__(self,
            *,
            labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
            entities : typing.Optional[typing.Iterable[typing.Text]] = ...,
            project : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"entities",b"entities",u"labels",b"labels",u"project",b"project"]) -> None: ...

    FILTER_FIELD_NUMBER: builtins.int

    @property
    def filter(self) -> global___ListFeaturesRequest.Filter: ...

    def __init__(self,
        *,
        filter : typing.Optional[global___ListFeaturesRequest.Filter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"filter",b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"filter",b"filter"]) -> None: ...
global___ListFeaturesRequest = ListFeaturesRequest

class ListFeaturesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class FeaturesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...

        @property
        def value(self) -> feast.core.Feature_pb2.FeatureSpecV2: ...

        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[feast.core.Feature_pb2.FeatureSpecV2] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    FEATURES_FIELD_NUMBER: builtins.int

    @property
    def features(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, feast.core.Feature_pb2.FeatureSpecV2]: ...

    def __init__(self,
        *,
        features : typing.Optional[typing.Mapping[typing.Text, feast.core.Feature_pb2.FeatureSpecV2]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"features",b"features"]) -> None: ...
global___ListFeaturesResponse = ListFeaturesResponse

class ListStoresRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Filter(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        NAME_FIELD_NUMBER: builtins.int
        name: typing.Text = ...

        def __init__(self,
            *,
            name : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name"]) -> None: ...

    FILTER_FIELD_NUMBER: builtins.int

    @property
    def filter(self) -> global___ListStoresRequest.Filter: ...

    def __init__(self,
        *,
        filter : typing.Optional[global___ListStoresRequest.Filter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"filter",b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"filter",b"filter"]) -> None: ...
global___ListStoresRequest = ListStoresRequest

class ListStoresResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STORE_FIELD_NUMBER: builtins.int

    @property
    def store(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[feast.core.Store_pb2.Store]: ...

    def __init__(self,
        *,
        store : typing.Optional[typing.Iterable[feast.core.Store_pb2.Store]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"store",b"store"]) -> None: ...
global___ListStoresResponse = ListStoresResponse

class ApplyEntityRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SPEC_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    project: typing.Text = ...

    @property
    def spec(self) -> feast.core.Entity_pb2.EntitySpecV2: ...

    def __init__(self,
        *,
        spec : typing.Optional[feast.core.Entity_pb2.EntitySpecV2] = ...,
        project : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"spec",b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"project",b"project",u"spec",b"spec"]) -> None: ...
global___ApplyEntityRequest = ApplyEntityRequest

class ApplyEntityResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITY_FIELD_NUMBER: builtins.int

    @property
    def entity(self) -> feast.core.Entity_pb2.Entity: ...

    def __init__(self,
        *,
        entity : typing.Optional[feast.core.Entity_pb2.Entity] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"entity",b"entity"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"entity",b"entity"]) -> None: ...
global___ApplyEntityResponse = ApplyEntityResponse

class GetFeastCoreVersionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___GetFeastCoreVersionRequest = GetFeastCoreVersionRequest

class GetFeastCoreVersionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSION_FIELD_NUMBER: builtins.int
    version: typing.Text = ...

    def __init__(self,
        *,
        version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"version",b"version"]) -> None: ...
global___GetFeastCoreVersionResponse = GetFeastCoreVersionResponse

class UpdateStoreRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STORE_FIELD_NUMBER: builtins.int

    @property
    def store(self) -> feast.core.Store_pb2.Store: ...

    def __init__(self,
        *,
        store : typing.Optional[feast.core.Store_pb2.Store] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"store",b"store"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"store",b"store"]) -> None: ...
global___UpdateStoreRequest = UpdateStoreRequest

class UpdateStoreResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Status(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Status.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        NO_CHANGE = UpdateStoreResponse.Status.V(0)
        UPDATED = UpdateStoreResponse.Status.V(1)
    class Status(metaclass=_Status):
        V = typing.NewType('V', builtins.int)
    NO_CHANGE = UpdateStoreResponse.Status.V(0)
    UPDATED = UpdateStoreResponse.Status.V(1)

    STORE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    status: global___UpdateStoreResponse.Status.V = ...

    @property
    def store(self) -> feast.core.Store_pb2.Store: ...

    def __init__(self,
        *,
        store : typing.Optional[feast.core.Store_pb2.Store] = ...,
        status : global___UpdateStoreResponse.Status.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"store",b"store"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"status",b"status",u"store",b"store"]) -> None: ...
global___UpdateStoreResponse = UpdateStoreResponse

class CreateProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name"]) -> None: ...
global___CreateProjectRequest = CreateProjectRequest

class CreateProjectResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___CreateProjectResponse = CreateProjectResponse

class ArchiveProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name"]) -> None: ...
global___ArchiveProjectRequest = ArchiveProjectRequest

class ArchiveProjectResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___ArchiveProjectResponse = ArchiveProjectResponse

class ListProjectsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___ListProjectsRequest = ListProjectsRequest

class ListProjectsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECTS_FIELD_NUMBER: builtins.int
    projects: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    def __init__(self,
        *,
        projects : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"projects",b"projects"]) -> None: ...
global___ListProjectsResponse = ListProjectsResponse

class UpdateFeatureSetStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___UpdateFeatureSetStatusResponse = UpdateFeatureSetStatusResponse

class ApplyFeatureTableRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_FIELD_NUMBER: builtins.int
    TABLE_SPEC_FIELD_NUMBER: builtins.int
    project: typing.Text = ...

    @property
    def table_spec(self) -> feast.core.FeatureTable_pb2.FeatureTableSpec: ...

    def __init__(self,
        *,
        project : typing.Text = ...,
        table_spec : typing.Optional[feast.core.FeatureTable_pb2.FeatureTableSpec] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"table_spec",b"table_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"project",b"project",u"table_spec",b"table_spec"]) -> None: ...
global___ApplyFeatureTableRequest = ApplyFeatureTableRequest

class ApplyFeatureTableResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TABLE_FIELD_NUMBER: builtins.int

    @property
    def table(self) -> feast.core.FeatureTable_pb2.FeatureTable: ...

    def __init__(self,
        *,
        table : typing.Optional[feast.core.FeatureTable_pb2.FeatureTable] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"table",b"table"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"table",b"table"]) -> None: ...
global___ApplyFeatureTableResponse = ApplyFeatureTableResponse

class GetFeatureTableRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    project: typing.Text = ...
    name: typing.Text = ...

    def __init__(self,
        *,
        project : typing.Text = ...,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"project",b"project"]) -> None: ...
global___GetFeatureTableRequest = GetFeatureTableRequest

class GetFeatureTableResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TABLE_FIELD_NUMBER: builtins.int

    @property
    def table(self) -> feast.core.FeatureTable_pb2.FeatureTable: ...

    def __init__(self,
        *,
        table : typing.Optional[feast.core.FeatureTable_pb2.FeatureTable] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"table",b"table"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"table",b"table"]) -> None: ...
global___GetFeatureTableResponse = GetFeatureTableResponse

class ListFeatureTablesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Filter(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class LabelsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: typing.Text = ...

            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        PROJECT_FIELD_NUMBER: builtins.int
        LABELS_FIELD_NUMBER: builtins.int
        project: typing.Text = ...

        @property
        def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...

        def __init__(self,
            *,
            project : typing.Text = ...,
            labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"labels",b"labels",u"project",b"project"]) -> None: ...

    FILTER_FIELD_NUMBER: builtins.int

    @property
    def filter(self) -> global___ListFeatureTablesRequest.Filter: ...

    def __init__(self,
        *,
        filter : typing.Optional[global___ListFeatureTablesRequest.Filter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"filter",b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"filter",b"filter"]) -> None: ...
global___ListFeatureTablesRequest = ListFeatureTablesRequest

class ListFeatureTablesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TABLES_FIELD_NUMBER: builtins.int

    @property
    def tables(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[feast.core.FeatureTable_pb2.FeatureTable]: ...

    def __init__(self,
        *,
        tables : typing.Optional[typing.Iterable[feast.core.FeatureTable_pb2.FeatureTable]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"tables",b"tables"]) -> None: ...
global___ListFeatureTablesResponse = ListFeatureTablesResponse

class DeleteFeatureTableRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    project: typing.Text = ...
    name: typing.Text = ...

    def __init__(self,
        *,
        project : typing.Text = ...,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"project",b"project"]) -> None: ...
global___DeleteFeatureTableRequest = DeleteFeatureTableRequest

class DeleteFeatureTableResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___DeleteFeatureTableResponse = DeleteFeatureTableResponse
