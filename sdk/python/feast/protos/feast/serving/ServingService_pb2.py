# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/serving/ServingService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from feast.protos.feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2
from tensorflow_metadata.proto.v0 import (
    statistics_pb2 as tensorflow__metadata_dot_proto_dot_v0_dot_statistics__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/serving/ServingService.proto',
  package='feast.serving',
  syntax='proto3',
  serialized_options=b'\n\023feast.proto.servingB\017ServingAPIProtoZ6github.com/feast-dev/feast/sdk/go/protos/feast/serving',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"feast/serving/ServingService.proto\x12\rfeast.serving\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17\x66\x65\x61st/types/Value.proto\x1a-tensorflow_metadata/proto/v0/statistics.proto\"\x1c\n\x1aGetFeastServingInfoRequest\"{\n\x1bGetFeastServingInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12-\n\x04type\x18\x02 \x01(\x0e\x32\x1f.feast.serving.FeastServingType\x12\x1c\n\x14job_staging_location\x18\n \x01(\t\"9\n\x12\x46\x65\x61tureReferenceV2\x12\x15\n\rfeature_table\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xfd\x02\n\x1aGetOnlineFeaturesRequestV2\x12\x33\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32!.feast.serving.FeatureReferenceV2\x12H\n\x0b\x65ntity_rows\x18\x02 \x03(\x0b\x32\x33.feast.serving.GetOnlineFeaturesRequestV2.EntityRow\x12\x0f\n\x07project\x18\x05 \x01(\t\x1a\xce\x01\n\tEntityRow\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12O\n\x06\x66ields\x18\x02 \x03(\x0b\x32?.feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry\x1a\x41\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.feast.types.Value:\x02\x38\x01\"\xa6\x04\n\x19GetOnlineFeaturesResponse\x12J\n\x0c\x66ield_values\x18\x01 \x03(\x0b\x32\x34.feast.serving.GetOnlineFeaturesResponse.FieldValues\x1a\xdf\x02\n\x0b\x46ieldValues\x12P\n\x06\x66ields\x18\x01 \x03(\x0b\x32@.feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry\x12T\n\x08statuses\x18\x02 \x03(\x0b\x32\x42.feast.serving.GetOnlineFeaturesResponse.FieldValues.StatusesEntry\x1a\x41\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.feast.types.Value:\x02\x38\x01\x1a\x65\n\rStatusesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0e\x32\x34.feast.serving.GetOnlineFeaturesResponse.FieldStatus:\x02\x38\x01\"[\n\x0b\x46ieldStatus\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07PRESENT\x10\x01\x12\x0e\n\nNULL_VALUE\x10\x02\x12\r\n\tNOT_FOUND\x10\x03\x12\x13\n\x0fOUTSIDE_MAX_AGE\x10\x04*o\n\x10\x46\x65\x61stServingType\x12\x1e\n\x1a\x46\x45\x41ST_SERVING_TYPE_INVALID\x10\x00\x12\x1d\n\x19\x46\x45\x41ST_SERVING_TYPE_ONLINE\x10\x01\x12\x1c\n\x18\x46\x45\x41ST_SERVING_TYPE_BATCH\x10\x02\x32\xea\x01\n\x0eServingService\x12l\n\x13GetFeastServingInfo\x12).feast.serving.GetFeastServingInfoRequest\x1a*.feast.serving.GetFeastServingInfoResponse\x12j\n\x13GetOnlineFeaturesV2\x12).feast.serving.GetOnlineFeaturesRequestV2\x1a(.feast.serving.GetOnlineFeaturesResponseB^\n\x13\x66\x65\x61st.proto.servingB\x0fServingAPIProtoZ6github.com/feast-dev/feast/sdk/go/protos/feast/servingb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,feast_dot_types_dot_Value__pb2.DESCRIPTOR,tensorflow__metadata_dot_proto_dot_v0_dot_statistics__pb2.DESCRIPTOR,])

_FEASTSERVINGTYPE = _descriptor.EnumDescriptor(
  name='FeastServingType',
  full_name='feast.serving.FeastServingType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FEAST_SERVING_TYPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FEAST_SERVING_TYPE_ONLINE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FEAST_SERVING_TYPE_BATCH', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1309,
  serialized_end=1420,
)
_sym_db.RegisterEnumDescriptor(_FEASTSERVINGTYPE)

FeastServingType = enum_type_wrapper.EnumTypeWrapper(_FEASTSERVINGTYPE)
FEAST_SERVING_TYPE_INVALID = 0
FEAST_SERVING_TYPE_ONLINE = 1
FEAST_SERVING_TYPE_BATCH = 2


_GETONLINEFEATURESRESPONSE_FIELDSTATUS = _descriptor.EnumDescriptor(
  name='FieldStatus',
  full_name='feast.serving.GetOnlineFeaturesResponse.FieldStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRESENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NULL_VALUE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUTSIDE_MAX_AGE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1216,
  serialized_end=1307,
)
_sym_db.RegisterEnumDescriptor(_GETONLINEFEATURESRESPONSE_FIELDSTATUS)


_GETFEASTSERVINGINFOREQUEST = _descriptor.Descriptor(
  name='GetFeastServingInfoRequest',
  full_name='feast.serving.GetFeastServingInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=186,
)


_GETFEASTSERVINGINFORESPONSE = _descriptor.Descriptor(
  name='GetFeastServingInfoResponse',
  full_name='feast.serving.GetFeastServingInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='feast.serving.GetFeastServingInfoResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='feast.serving.GetFeastServingInfoResponse.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_staging_location', full_name='feast.serving.GetFeastServingInfoResponse.job_staging_location', index=2,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=311,
)


_FEATUREREFERENCEV2 = _descriptor.Descriptor(
  name='FeatureReferenceV2',
  full_name='feast.serving.FeatureReferenceV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_table', full_name='feast.serving.FeatureReferenceV2.feature_table', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.serving.FeatureReferenceV2.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=370,
)


_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=689,
  serialized_end=754,
)

_GETONLINEFEATURESREQUESTV2_ENTITYROW = _descriptor.Descriptor(
  name='EntityRow',
  full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='feast.serving.GetOnlineFeaturesRequestV2.EntityRow.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=548,
  serialized_end=754,
)

_GETONLINEFEATURESREQUESTV2 = _descriptor.Descriptor(
  name='GetOnlineFeaturesRequestV2',
  full_name='feast.serving.GetOnlineFeaturesRequestV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='feast.serving.GetOnlineFeaturesRequestV2.features', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_rows', full_name='feast.serving.GetOnlineFeaturesRequestV2.entity_rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project', full_name='feast.serving.GetOnlineFeaturesRequestV2.project', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESREQUESTV2_ENTITYROW, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=754,
)


_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY = _descriptor.Descriptor(
  name='FieldsEntry',
  full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=689,
  serialized_end=754,
)

_GETONLINEFEATURESRESPONSE_FIELDVALUES_STATUSESENTRY = _descriptor.Descriptor(
  name='StatusesEntry',
  full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.StatusesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.StatusesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.StatusesEntry.value', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1113,
  serialized_end=1214,
)

_GETONLINEFEATURESRESPONSE_FIELDVALUES = _descriptor.Descriptor(
  name='FieldValues',
  full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statuses', full_name='feast.serving.GetOnlineFeaturesResponse.FieldValues.statuses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY, _GETONLINEFEATURESRESPONSE_FIELDVALUES_STATUSESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=863,
  serialized_end=1214,
)

_GETONLINEFEATURESRESPONSE = _descriptor.Descriptor(
  name='GetOnlineFeaturesResponse',
  full_name='feast.serving.GetOnlineFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_values', full_name='feast.serving.GetOnlineFeaturesResponse.field_values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETONLINEFEATURESRESPONSE_FIELDVALUES, ],
  enum_types=[
    _GETONLINEFEATURESRESPONSE_FIELDSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=1307,
)

_GETFEASTSERVINGINFORESPONSE.fields_by_name['type'].enum_type = _FEASTSERVINGTYPE
_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._VALUE
_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY.containing_type = _GETONLINEFEATURESREQUESTV2_ENTITYROW
_GETONLINEFEATURESREQUESTV2_ENTITYROW.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETONLINEFEATURESREQUESTV2_ENTITYROW.fields_by_name['fields'].message_type = _GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY
_GETONLINEFEATURESREQUESTV2_ENTITYROW.containing_type = _GETONLINEFEATURESREQUESTV2
_GETONLINEFEATURESREQUESTV2.fields_by_name['features'].message_type = _FEATUREREFERENCEV2
_GETONLINEFEATURESREQUESTV2.fields_by_name['entity_rows'].message_type = _GETONLINEFEATURESREQUESTV2_ENTITYROW
_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._VALUE
_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY.containing_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES
_GETONLINEFEATURESRESPONSE_FIELDVALUES_STATUSESENTRY.fields_by_name['value'].enum_type = _GETONLINEFEATURESRESPONSE_FIELDSTATUS
_GETONLINEFEATURESRESPONSE_FIELDVALUES_STATUSESENTRY.containing_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES
_GETONLINEFEATURESRESPONSE_FIELDVALUES.fields_by_name['fields'].message_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY
_GETONLINEFEATURESRESPONSE_FIELDVALUES.fields_by_name['statuses'].message_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES_STATUSESENTRY
_GETONLINEFEATURESRESPONSE_FIELDVALUES.containing_type = _GETONLINEFEATURESRESPONSE
_GETONLINEFEATURESRESPONSE.fields_by_name['field_values'].message_type = _GETONLINEFEATURESRESPONSE_FIELDVALUES
_GETONLINEFEATURESRESPONSE_FIELDSTATUS.containing_type = _GETONLINEFEATURESRESPONSE
DESCRIPTOR.message_types_by_name['GetFeastServingInfoRequest'] = _GETFEASTSERVINGINFOREQUEST
DESCRIPTOR.message_types_by_name['GetFeastServingInfoResponse'] = _GETFEASTSERVINGINFORESPONSE
DESCRIPTOR.message_types_by_name['FeatureReferenceV2'] = _FEATUREREFERENCEV2
DESCRIPTOR.message_types_by_name['GetOnlineFeaturesRequestV2'] = _GETONLINEFEATURESREQUESTV2
DESCRIPTOR.message_types_by_name['GetOnlineFeaturesResponse'] = _GETONLINEFEATURESRESPONSE
DESCRIPTOR.enum_types_by_name['FeastServingType'] = _FEASTSERVINGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeastServingInfoRequest = _reflection.GeneratedProtocolMessageType('GetFeastServingInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGINFOREQUEST,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingInfoRequest)
  })
_sym_db.RegisterMessage(GetFeastServingInfoRequest)

GetFeastServingInfoResponse = _reflection.GeneratedProtocolMessageType('GetFeastServingInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFEASTSERVINGINFORESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetFeastServingInfoResponse)
  })
_sym_db.RegisterMessage(GetFeastServingInfoResponse)

FeatureReferenceV2 = _reflection.GeneratedProtocolMessageType('FeatureReferenceV2', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREREFERENCEV2,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.FeatureReferenceV2)
  })
_sym_db.RegisterMessage(FeatureReferenceV2)

GetOnlineFeaturesRequestV2 = _reflection.GeneratedProtocolMessageType('GetOnlineFeaturesRequestV2', (_message.Message,), {

  'EntityRow' : _reflection.GeneratedProtocolMessageType('EntityRow', (_message.Message,), {

    'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY,
      '__module__' : 'feast.serving.ServingService_pb2'
      # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry)
      })
    ,
    'DESCRIPTOR' : _GETONLINEFEATURESREQUESTV2_ENTITYROW,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequestV2.EntityRow)
    })
  ,
  'DESCRIPTOR' : _GETONLINEFEATURESREQUESTV2,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesRequestV2)
  })
_sym_db.RegisterMessage(GetOnlineFeaturesRequestV2)
_sym_db.RegisterMessage(GetOnlineFeaturesRequestV2.EntityRow)
_sym_db.RegisterMessage(GetOnlineFeaturesRequestV2.EntityRow.FieldsEntry)

GetOnlineFeaturesResponse = _reflection.GeneratedProtocolMessageType('GetOnlineFeaturesResponse', (_message.Message,), {

  'FieldValues' : _reflection.GeneratedProtocolMessageType('FieldValues', (_message.Message,), {

    'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY,
      '__module__' : 'feast.serving.ServingService_pb2'
      # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse.FieldValues.FieldsEntry)
      })
    ,

    'StatusesEntry' : _reflection.GeneratedProtocolMessageType('StatusesEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE_FIELDVALUES_STATUSESENTRY,
      '__module__' : 'feast.serving.ServingService_pb2'
      # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse.FieldValues.StatusesEntry)
      })
    ,
    'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE_FIELDVALUES,
    '__module__' : 'feast.serving.ServingService_pb2'
    # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse.FieldValues)
    })
  ,
  'DESCRIPTOR' : _GETONLINEFEATURESRESPONSE,
  '__module__' : 'feast.serving.ServingService_pb2'
  # @@protoc_insertion_point(class_scope:feast.serving.GetOnlineFeaturesResponse)
  })
_sym_db.RegisterMessage(GetOnlineFeaturesResponse)
_sym_db.RegisterMessage(GetOnlineFeaturesResponse.FieldValues)
_sym_db.RegisterMessage(GetOnlineFeaturesResponse.FieldValues.FieldsEntry)
_sym_db.RegisterMessage(GetOnlineFeaturesResponse.FieldValues.StatusesEntry)


DESCRIPTOR._options = None
_GETONLINEFEATURESREQUESTV2_ENTITYROW_FIELDSENTRY._options = None
_GETONLINEFEATURESRESPONSE_FIELDVALUES_FIELDSENTRY._options = None
_GETONLINEFEATURESRESPONSE_FIELDVALUES_STATUSESENTRY._options = None

_SERVINGSERVICE = _descriptor.ServiceDescriptor(
  name='ServingService',
  full_name='feast.serving.ServingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1423,
  serialized_end=1657,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeastServingInfo',
    full_name='feast.serving.ServingService.GetFeastServingInfo',
    index=0,
    containing_service=None,
    input_type=_GETFEASTSERVINGINFOREQUEST,
    output_type=_GETFEASTSERVINGINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOnlineFeaturesV2',
    full_name='feast.serving.ServingService.GetOnlineFeaturesV2',
    index=1,
    containing_service=None,
    input_type=_GETONLINEFEATURESREQUESTV2,
    output_type=_GETONLINEFEATURESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVINGSERVICE)

DESCRIPTOR.services_by_name['ServingService'] = _SERVINGSERVICE

# @@protoc_insertion_point(module_scope)
