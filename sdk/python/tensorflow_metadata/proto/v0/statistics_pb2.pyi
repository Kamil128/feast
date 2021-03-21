"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import tensorflow_metadata.proto.v0.path_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class DatasetFeatureStatisticsList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATASETS_FIELD_NUMBER: builtins.int

    @property
    def datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DatasetFeatureStatistics]: ...

    def __init__(self,
        *,
        datasets : typing.Optional[typing.Iterable[global___DatasetFeatureStatistics]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"datasets",b"datasets"]) -> None: ...
global___DatasetFeatureStatisticsList = DatasetFeatureStatisticsList

class DatasetFeatureStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    NUM_EXAMPLES_FIELD_NUMBER: builtins.int
    WEIGHTED_NUM_EXAMPLES_FIELD_NUMBER: builtins.int
    FEATURES_FIELD_NUMBER: builtins.int
    CROSS_FEATURES_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    num_examples: builtins.int = ...
    weighted_num_examples: builtins.float = ...

    @property
    def features(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeatureNameStatistics]: ...

    @property
    def cross_features(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CrossFeatureStatistics]: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        num_examples : builtins.int = ...,
        weighted_num_examples : builtins.float = ...,
        features : typing.Optional[typing.Iterable[global___FeatureNameStatistics]] = ...,
        cross_features : typing.Optional[typing.Iterable[global___CrossFeatureStatistics]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cross_features",b"cross_features",u"features",b"features",u"name",b"name",u"num_examples",b"num_examples",u"weighted_num_examples",b"weighted_num_examples"]) -> None: ...
global___DatasetFeatureStatistics = DatasetFeatureStatistics

class CrossFeatureStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PATH_X_FIELD_NUMBER: builtins.int
    PATH_Y_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    NUM_CROSS_STATS_FIELD_NUMBER: builtins.int
    CATEGORICAL_CROSS_STATS_FIELD_NUMBER: builtins.int
    count: builtins.int = ...

    @property
    def path_x(self) -> tensorflow_metadata.proto.v0.path_pb2.Path: ...

    @property
    def path_y(self) -> tensorflow_metadata.proto.v0.path_pb2.Path: ...

    @property
    def num_cross_stats(self) -> global___NumericCrossStatistics: ...

    @property
    def categorical_cross_stats(self) -> global___CategoricalCrossStatistics: ...

    def __init__(self,
        *,
        path_x : typing.Optional[tensorflow_metadata.proto.v0.path_pb2.Path] = ...,
        path_y : typing.Optional[tensorflow_metadata.proto.v0.path_pb2.Path] = ...,
        count : builtins.int = ...,
        num_cross_stats : typing.Optional[global___NumericCrossStatistics] = ...,
        categorical_cross_stats : typing.Optional[global___CategoricalCrossStatistics] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"categorical_cross_stats",b"categorical_cross_stats",u"cross_stats",b"cross_stats",u"num_cross_stats",b"num_cross_stats",u"path_x",b"path_x",u"path_y",b"path_y"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"categorical_cross_stats",b"categorical_cross_stats",u"count",b"count",u"cross_stats",b"cross_stats",u"num_cross_stats",b"num_cross_stats",u"path_x",b"path_x",u"path_y",b"path_y"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"cross_stats",b"cross_stats"]) -> typing_extensions.Literal["num_cross_stats","categorical_cross_stats"]: ...
global___CrossFeatureStatistics = CrossFeatureStatistics

class NumericCrossStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CORRELATION_FIELD_NUMBER: builtins.int
    COVARIANCE_FIELD_NUMBER: builtins.int
    correlation: builtins.float = ...
    covariance: builtins.float = ...

    def __init__(self,
        *,
        correlation : builtins.float = ...,
        covariance : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"correlation",b"correlation",u"covariance",b"covariance"]) -> None: ...
global___NumericCrossStatistics = NumericCrossStatistics

class CategoricalCrossStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LIFT_FIELD_NUMBER: builtins.int

    @property
    def lift(self) -> global___LiftStatistics: ...

    def __init__(self,
        *,
        lift : typing.Optional[global___LiftStatistics] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"lift",b"lift"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"lift",b"lift"]) -> None: ...
global___CategoricalCrossStatistics = CategoricalCrossStatistics

class LiftStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LIFT_SERIES_FIELD_NUMBER: builtins.int
    WEIGHTED_LIFT_SERIES_FIELD_NUMBER: builtins.int

    @property
    def lift_series(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LiftSeries]: ...

    @property
    def weighted_lift_series(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LiftSeries]: ...

    def __init__(self,
        *,
        lift_series : typing.Optional[typing.Iterable[global___LiftSeries]] = ...,
        weighted_lift_series : typing.Optional[typing.Iterable[global___LiftSeries]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"lift_series",b"lift_series",u"weighted_lift_series",b"weighted_lift_series"]) -> None: ...
global___LiftStatistics = LiftStatistics

class LiftSeries(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Bucket(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        LOW_VALUE_FIELD_NUMBER: builtins.int
        HIGH_VALUE_FIELD_NUMBER: builtins.int
        low_value: builtins.float = ...
        high_value: builtins.float = ...

        def __init__(self,
            *,
            low_value : builtins.float = ...,
            high_value : builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"high_value",b"high_value",u"low_value",b"low_value"]) -> None: ...

    class LiftValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        X_INT_FIELD_NUMBER: builtins.int
        X_STRING_FIELD_NUMBER: builtins.int
        LIFT_FIELD_NUMBER: builtins.int
        X_COUNT_FIELD_NUMBER: builtins.int
        WEIGHTED_X_COUNT_FIELD_NUMBER: builtins.int
        X_AND_Y_COUNT_FIELD_NUMBER: builtins.int
        WEIGHTED_X_AND_Y_COUNT_FIELD_NUMBER: builtins.int
        x_int: builtins.int = ...
        x_string: typing.Text = ...
        lift: builtins.float = ...
        x_count: builtins.int = ...
        weighted_x_count: builtins.float = ...
        x_and_y_count: builtins.int = ...
        weighted_x_and_y_count: builtins.float = ...

        def __init__(self,
            *,
            x_int : builtins.int = ...,
            x_string : typing.Text = ...,
            lift : builtins.float = ...,
            x_count : builtins.int = ...,
            weighted_x_count : builtins.float = ...,
            x_and_y_count : builtins.int = ...,
            weighted_x_and_y_count : builtins.float = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"weighted_x_and_y_count",b"weighted_x_and_y_count",u"weighted_x_count",b"weighted_x_count",u"x_and_y_count",b"x_and_y_count",u"x_and_y_count_value",b"x_and_y_count_value",u"x_count",b"x_count",u"x_count_value",b"x_count_value",u"x_int",b"x_int",u"x_string",b"x_string",u"x_value",b"x_value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"lift",b"lift",u"weighted_x_and_y_count",b"weighted_x_and_y_count",u"weighted_x_count",b"weighted_x_count",u"x_and_y_count",b"x_and_y_count",u"x_and_y_count_value",b"x_and_y_count_value",u"x_count",b"x_count",u"x_count_value",b"x_count_value",u"x_int",b"x_int",u"x_string",b"x_string",u"x_value",b"x_value"]) -> None: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal[u"x_and_y_count_value",b"x_and_y_count_value"]) -> typing_extensions.Literal["x_and_y_count","weighted_x_and_y_count"]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal[u"x_count_value",b"x_count_value"]) -> typing_extensions.Literal["x_count","weighted_x_count"]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal[u"x_value",b"x_value"]) -> typing_extensions.Literal["x_int","x_string"]: ...

    Y_INT_FIELD_NUMBER: builtins.int
    Y_STRING_FIELD_NUMBER: builtins.int
    Y_BUCKET_FIELD_NUMBER: builtins.int
    Y_COUNT_FIELD_NUMBER: builtins.int
    WEIGHTED_Y_COUNT_FIELD_NUMBER: builtins.int
    LIFT_VALUES_FIELD_NUMBER: builtins.int
    y_int: builtins.int = ...
    y_string: typing.Text = ...
    y_count: builtins.int = ...
    weighted_y_count: builtins.float = ...

    @property
    def y_bucket(self) -> global___LiftSeries.Bucket: ...

    @property
    def lift_values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LiftSeries.LiftValue]: ...

    def __init__(self,
        *,
        y_int : builtins.int = ...,
        y_string : typing.Text = ...,
        y_bucket : typing.Optional[global___LiftSeries.Bucket] = ...,
        y_count : builtins.int = ...,
        weighted_y_count : builtins.float = ...,
        lift_values : typing.Optional[typing.Iterable[global___LiftSeries.LiftValue]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"weighted_y_count",b"weighted_y_count",u"y_bucket",b"y_bucket",u"y_count",b"y_count",u"y_count_value",b"y_count_value",u"y_int",b"y_int",u"y_string",b"y_string",u"y_value",b"y_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"lift_values",b"lift_values",u"weighted_y_count",b"weighted_y_count",u"y_bucket",b"y_bucket",u"y_count",b"y_count",u"y_count_value",b"y_count_value",u"y_int",b"y_int",u"y_string",b"y_string",u"y_value",b"y_value"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"y_count_value",b"y_count_value"]) -> typing_extensions.Literal["y_count","weighted_y_count"]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"y_value",b"y_value"]) -> typing_extensions.Literal["y_int","y_string","y_bucket"]: ...
global___LiftSeries = LiftSeries

class FeatureNameStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Type(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Type.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        INT = FeatureNameStatistics.Type.V(0)
        FLOAT = FeatureNameStatistics.Type.V(1)
        STRING = FeatureNameStatistics.Type.V(2)
        BYTES = FeatureNameStatistics.Type.V(3)
        STRUCT = FeatureNameStatistics.Type.V(4)
    class Type(metaclass=_Type):
        V = typing.NewType('V', builtins.int)
    INT = FeatureNameStatistics.Type.V(0)
    FLOAT = FeatureNameStatistics.Type.V(1)
    STRING = FeatureNameStatistics.Type.V(2)
    BYTES = FeatureNameStatistics.Type.V(3)
    STRUCT = FeatureNameStatistics.Type.V(4)

    NAME_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NUM_STATS_FIELD_NUMBER: builtins.int
    STRING_STATS_FIELD_NUMBER: builtins.int
    BYTES_STATS_FIELD_NUMBER: builtins.int
    STRUCT_STATS_FIELD_NUMBER: builtins.int
    CUSTOM_STATS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    type: global___FeatureNameStatistics.Type.V = ...

    @property
    def path(self) -> tensorflow_metadata.proto.v0.path_pb2.Path: ...

    @property
    def num_stats(self) -> global___NumericStatistics: ...

    @property
    def string_stats(self) -> global___StringStatistics: ...

    @property
    def bytes_stats(self) -> global___BytesStatistics: ...

    @property
    def struct_stats(self) -> global___StructStatistics: ...

    @property
    def custom_stats(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CustomStatistic]: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        path : typing.Optional[tensorflow_metadata.proto.v0.path_pb2.Path] = ...,
        type : global___FeatureNameStatistics.Type.V = ...,
        num_stats : typing.Optional[global___NumericStatistics] = ...,
        string_stats : typing.Optional[global___StringStatistics] = ...,
        bytes_stats : typing.Optional[global___BytesStatistics] = ...,
        struct_stats : typing.Optional[global___StructStatistics] = ...,
        custom_stats : typing.Optional[typing.Iterable[global___CustomStatistic]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"bytes_stats",b"bytes_stats",u"field_id",b"field_id",u"name",b"name",u"num_stats",b"num_stats",u"path",b"path",u"stats",b"stats",u"string_stats",b"string_stats",u"struct_stats",b"struct_stats"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bytes_stats",b"bytes_stats",u"custom_stats",b"custom_stats",u"field_id",b"field_id",u"name",b"name",u"num_stats",b"num_stats",u"path",b"path",u"stats",b"stats",u"string_stats",b"string_stats",u"struct_stats",b"struct_stats",u"type",b"type"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"field_id",b"field_id"]) -> typing_extensions.Literal["name","path"]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"stats",b"stats"]) -> typing_extensions.Literal["num_stats","string_stats","bytes_stats","struct_stats"]: ...
global___FeatureNameStatistics = FeatureNameStatistics

class WeightedCommonStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NUM_NON_MISSING_FIELD_NUMBER: builtins.int
    NUM_MISSING_FIELD_NUMBER: builtins.int
    AVG_NUM_VALUES_FIELD_NUMBER: builtins.int
    TOT_NUM_VALUES_FIELD_NUMBER: builtins.int
    num_non_missing: builtins.float = ...
    num_missing: builtins.float = ...
    avg_num_values: builtins.float = ...
    tot_num_values: builtins.float = ...

    def __init__(self,
        *,
        num_non_missing : builtins.float = ...,
        num_missing : builtins.float = ...,
        avg_num_values : builtins.float = ...,
        tot_num_values : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"avg_num_values",b"avg_num_values",u"num_missing",b"num_missing",u"num_non_missing",b"num_non_missing",u"tot_num_values",b"tot_num_values"]) -> None: ...
global___WeightedCommonStatistics = WeightedCommonStatistics

class CustomStatistic(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    NUM_FIELD_NUMBER: builtins.int
    STR_FIELD_NUMBER: builtins.int
    HISTOGRAM_FIELD_NUMBER: builtins.int
    RANK_HISTOGRAM_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    num: builtins.float = ...
    str: typing.Text = ...

    @property
    def histogram(self) -> global___Histogram: ...

    @property
    def rank_histogram(self) -> global___RankHistogram: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        num : builtins.float = ...,
        str : typing.Text = ...,
        histogram : typing.Optional[global___Histogram] = ...,
        rank_histogram : typing.Optional[global___RankHistogram] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"histogram",b"histogram",u"num",b"num",u"rank_histogram",b"rank_histogram",u"str",b"str",u"val",b"val"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"histogram",b"histogram",u"name",b"name",u"num",b"num",u"rank_histogram",b"rank_histogram",u"str",b"str",u"val",b"val"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"val",b"val"]) -> typing_extensions.Literal["num","str","histogram","rank_histogram"]: ...
global___CustomStatistic = CustomStatistic

class NumericStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMMON_STATS_FIELD_NUMBER: builtins.int
    MEAN_FIELD_NUMBER: builtins.int
    STD_DEV_FIELD_NUMBER: builtins.int
    NUM_ZEROS_FIELD_NUMBER: builtins.int
    MIN_FIELD_NUMBER: builtins.int
    MEDIAN_FIELD_NUMBER: builtins.int
    MAX_FIELD_NUMBER: builtins.int
    HISTOGRAMS_FIELD_NUMBER: builtins.int
    WEIGHTED_NUMERIC_STATS_FIELD_NUMBER: builtins.int
    mean: builtins.float = ...
    std_dev: builtins.float = ...
    num_zeros: builtins.int = ...
    min: builtins.float = ...
    median: builtins.float = ...
    max: builtins.float = ...

    @property
    def common_stats(self) -> global___CommonStatistics: ...

    @property
    def histograms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Histogram]: ...

    @property
    def weighted_numeric_stats(self) -> global___WeightedNumericStatistics: ...

    def __init__(self,
        *,
        common_stats : typing.Optional[global___CommonStatistics] = ...,
        mean : builtins.float = ...,
        std_dev : builtins.float = ...,
        num_zeros : builtins.int = ...,
        min : builtins.float = ...,
        median : builtins.float = ...,
        max : builtins.float = ...,
        histograms : typing.Optional[typing.Iterable[global___Histogram]] = ...,
        weighted_numeric_stats : typing.Optional[global___WeightedNumericStatistics] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"common_stats",b"common_stats",u"weighted_numeric_stats",b"weighted_numeric_stats"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"common_stats",b"common_stats",u"histograms",b"histograms",u"max",b"max",u"mean",b"mean",u"median",b"median",u"min",b"min",u"num_zeros",b"num_zeros",u"std_dev",b"std_dev",u"weighted_numeric_stats",b"weighted_numeric_stats"]) -> None: ...
global___NumericStatistics = NumericStatistics

class StringStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class FreqAndValue(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        VALUE_FIELD_NUMBER: builtins.int
        FREQUENCY_FIELD_NUMBER: builtins.int
        value: typing.Text = ...
        frequency: builtins.float = ...

        def __init__(self,
            *,
            value : typing.Text = ...,
            frequency : builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"frequency",b"frequency",u"value",b"value"]) -> None: ...

    COMMON_STATS_FIELD_NUMBER: builtins.int
    UNIQUE_FIELD_NUMBER: builtins.int
    TOP_VALUES_FIELD_NUMBER: builtins.int
    AVG_LENGTH_FIELD_NUMBER: builtins.int
    RANK_HISTOGRAM_FIELD_NUMBER: builtins.int
    WEIGHTED_STRING_STATS_FIELD_NUMBER: builtins.int
    VOCABULARY_FILE_FIELD_NUMBER: builtins.int
    unique: builtins.int = ...
    avg_length: builtins.float = ...
    vocabulary_file: typing.Text = ...

    @property
    def common_stats(self) -> global___CommonStatistics: ...

    @property
    def top_values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StringStatistics.FreqAndValue]: ...

    @property
    def rank_histogram(self) -> global___RankHistogram: ...

    @property
    def weighted_string_stats(self) -> global___WeightedStringStatistics: ...

    def __init__(self,
        *,
        common_stats : typing.Optional[global___CommonStatistics] = ...,
        unique : builtins.int = ...,
        top_values : typing.Optional[typing.Iterable[global___StringStatistics.FreqAndValue]] = ...,
        avg_length : builtins.float = ...,
        rank_histogram : typing.Optional[global___RankHistogram] = ...,
        weighted_string_stats : typing.Optional[global___WeightedStringStatistics] = ...,
        vocabulary_file : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"common_stats",b"common_stats",u"rank_histogram",b"rank_histogram",u"weighted_string_stats",b"weighted_string_stats"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"avg_length",b"avg_length",u"common_stats",b"common_stats",u"rank_histogram",b"rank_histogram",u"top_values",b"top_values",u"unique",b"unique",u"vocabulary_file",b"vocabulary_file",u"weighted_string_stats",b"weighted_string_stats"]) -> None: ...
global___StringStatistics = StringStatistics

class WeightedNumericStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MEAN_FIELD_NUMBER: builtins.int
    STD_DEV_FIELD_NUMBER: builtins.int
    MEDIAN_FIELD_NUMBER: builtins.int
    HISTOGRAMS_FIELD_NUMBER: builtins.int
    mean: builtins.float = ...
    std_dev: builtins.float = ...
    median: builtins.float = ...

    @property
    def histograms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Histogram]: ...

    def __init__(self,
        *,
        mean : builtins.float = ...,
        std_dev : builtins.float = ...,
        median : builtins.float = ...,
        histograms : typing.Optional[typing.Iterable[global___Histogram]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"histograms",b"histograms",u"mean",b"mean",u"median",b"median",u"std_dev",b"std_dev"]) -> None: ...
global___WeightedNumericStatistics = WeightedNumericStatistics

class WeightedStringStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOP_VALUES_FIELD_NUMBER: builtins.int
    RANK_HISTOGRAM_FIELD_NUMBER: builtins.int

    @property
    def top_values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StringStatistics.FreqAndValue]: ...

    @property
    def rank_histogram(self) -> global___RankHistogram: ...

    def __init__(self,
        *,
        top_values : typing.Optional[typing.Iterable[global___StringStatistics.FreqAndValue]] = ...,
        rank_histogram : typing.Optional[global___RankHistogram] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"rank_histogram",b"rank_histogram"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"rank_histogram",b"rank_histogram",u"top_values",b"top_values"]) -> None: ...
global___WeightedStringStatistics = WeightedStringStatistics

class BytesStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMMON_STATS_FIELD_NUMBER: builtins.int
    UNIQUE_FIELD_NUMBER: builtins.int
    AVG_NUM_BYTES_FIELD_NUMBER: builtins.int
    MIN_NUM_BYTES_FIELD_NUMBER: builtins.int
    MAX_NUM_BYTES_FIELD_NUMBER: builtins.int
    unique: builtins.int = ...
    avg_num_bytes: builtins.float = ...
    min_num_bytes: builtins.float = ...
    max_num_bytes: builtins.float = ...

    @property
    def common_stats(self) -> global___CommonStatistics: ...

    def __init__(self,
        *,
        common_stats : typing.Optional[global___CommonStatistics] = ...,
        unique : builtins.int = ...,
        avg_num_bytes : builtins.float = ...,
        min_num_bytes : builtins.float = ...,
        max_num_bytes : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"common_stats",b"common_stats"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"avg_num_bytes",b"avg_num_bytes",u"common_stats",b"common_stats",u"max_num_bytes",b"max_num_bytes",u"min_num_bytes",b"min_num_bytes",u"unique",b"unique"]) -> None: ...
global___BytesStatistics = BytesStatistics

class StructStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMMON_STATS_FIELD_NUMBER: builtins.int

    @property
    def common_stats(self) -> global___CommonStatistics: ...

    def __init__(self,
        *,
        common_stats : typing.Optional[global___CommonStatistics] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"common_stats",b"common_stats"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"common_stats",b"common_stats"]) -> None: ...
global___StructStatistics = StructStatistics

class CommonStatistics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NUM_NON_MISSING_FIELD_NUMBER: builtins.int
    NUM_MISSING_FIELD_NUMBER: builtins.int
    MIN_NUM_VALUES_FIELD_NUMBER: builtins.int
    MAX_NUM_VALUES_FIELD_NUMBER: builtins.int
    AVG_NUM_VALUES_FIELD_NUMBER: builtins.int
    TOT_NUM_VALUES_FIELD_NUMBER: builtins.int
    NUM_VALUES_HISTOGRAM_FIELD_NUMBER: builtins.int
    WEIGHTED_COMMON_STATS_FIELD_NUMBER: builtins.int
    FEATURE_LIST_LENGTH_HISTOGRAM_FIELD_NUMBER: builtins.int
    num_non_missing: builtins.int = ...
    num_missing: builtins.int = ...
    min_num_values: builtins.int = ...
    max_num_values: builtins.int = ...
    avg_num_values: builtins.float = ...
    tot_num_values: builtins.int = ...

    @property
    def num_values_histogram(self) -> global___Histogram: ...

    @property
    def weighted_common_stats(self) -> global___WeightedCommonStatistics: ...

    @property
    def feature_list_length_histogram(self) -> global___Histogram: ...

    def __init__(self,
        *,
        num_non_missing : builtins.int = ...,
        num_missing : builtins.int = ...,
        min_num_values : builtins.int = ...,
        max_num_values : builtins.int = ...,
        avg_num_values : builtins.float = ...,
        tot_num_values : builtins.int = ...,
        num_values_histogram : typing.Optional[global___Histogram] = ...,
        weighted_common_stats : typing.Optional[global___WeightedCommonStatistics] = ...,
        feature_list_length_histogram : typing.Optional[global___Histogram] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"feature_list_length_histogram",b"feature_list_length_histogram",u"num_values_histogram",b"num_values_histogram",u"weighted_common_stats",b"weighted_common_stats"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"avg_num_values",b"avg_num_values",u"feature_list_length_histogram",b"feature_list_length_histogram",u"max_num_values",b"max_num_values",u"min_num_values",b"min_num_values",u"num_missing",b"num_missing",u"num_non_missing",b"num_non_missing",u"num_values_histogram",b"num_values_histogram",u"tot_num_values",b"tot_num_values",u"weighted_common_stats",b"weighted_common_stats"]) -> None: ...
global___CommonStatistics = CommonStatistics

class Histogram(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _HistogramType(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[HistogramType.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STANDARD = Histogram.HistogramType.V(0)
        QUANTILES = Histogram.HistogramType.V(1)
    class HistogramType(metaclass=_HistogramType):
        V = typing.NewType('V', builtins.int)
    STANDARD = Histogram.HistogramType.V(0)
    QUANTILES = Histogram.HistogramType.V(1)

    class Bucket(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        LOW_VALUE_FIELD_NUMBER: builtins.int
        HIGH_VALUE_FIELD_NUMBER: builtins.int
        SAMPLE_COUNT_FIELD_NUMBER: builtins.int
        low_value: builtins.float = ...
        high_value: builtins.float = ...
        sample_count: builtins.float = ...

        def __init__(self,
            *,
            low_value : builtins.float = ...,
            high_value : builtins.float = ...,
            sample_count : builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"high_value",b"high_value",u"low_value",b"low_value",u"sample_count",b"sample_count"]) -> None: ...

    NUM_NAN_FIELD_NUMBER: builtins.int
    NUM_UNDEFINED_FIELD_NUMBER: builtins.int
    BUCKETS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    num_nan: builtins.int = ...
    num_undefined: builtins.int = ...
    type: global___Histogram.HistogramType.V = ...
    name: typing.Text = ...

    @property
    def buckets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Histogram.Bucket]: ...

    def __init__(self,
        *,
        num_nan : builtins.int = ...,
        num_undefined : builtins.int = ...,
        buckets : typing.Optional[typing.Iterable[global___Histogram.Bucket]] = ...,
        type : global___Histogram.HistogramType.V = ...,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"buckets",b"buckets",u"name",b"name",u"num_nan",b"num_nan",u"num_undefined",b"num_undefined",u"type",b"type"]) -> None: ...
global___Histogram = Histogram

class RankHistogram(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Bucket(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        LOW_RANK_FIELD_NUMBER: builtins.int
        HIGH_RANK_FIELD_NUMBER: builtins.int
        LABEL_FIELD_NUMBER: builtins.int
        SAMPLE_COUNT_FIELD_NUMBER: builtins.int
        low_rank: builtins.int = ...
        high_rank: builtins.int = ...
        label: typing.Text = ...
        sample_count: builtins.float = ...

        def __init__(self,
            *,
            low_rank : builtins.int = ...,
            high_rank : builtins.int = ...,
            label : typing.Text = ...,
            sample_count : builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"high_rank",b"high_rank",u"label",b"label",u"low_rank",b"low_rank",u"sample_count",b"sample_count"]) -> None: ...

    BUCKETS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    @property
    def buckets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RankHistogram.Bucket]: ...

    def __init__(self,
        *,
        buckets : typing.Optional[typing.Iterable[global___RankHistogram.Bucket]] = ...,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"buckets",b"buckets",u"name",b"name"]) -> None: ...
global___RankHistogram = RankHistogram
