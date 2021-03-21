# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/storage/Redis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.types import Field_pb2 as feast_dot_types_dot_Field__pb2
from feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/storage/Redis.proto',
  package='feast.storage',
  syntax='proto3',
  serialized_options=b'\n\023feast.proto.storageB\nRedisProtoZ6github.com/feast-dev/feast/sdk/go/protos/feast/storage',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x66\x65\x61st/storage/Redis.proto\x12\rfeast.storage\x1a\x17\x66\x65\x61st/types/Field.proto\x1a\x17\x66\x65\x61st/types/Value.proto\"^\n\nRedisKeyV2\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x14\n\x0c\x65ntity_names\x18\x02 \x03(\t\x12)\n\rentity_values\x18\x03 \x03(\x0b\x32\x12.feast.types.ValueBY\n\x13\x66\x65\x61st.proto.storageB\nRedisProtoZ6github.com/feast-dev/feast/sdk/go/protos/feast/storageb\x06proto3'
  ,
  dependencies=[feast_dot_types_dot_Field__pb2.DESCRIPTOR,feast_dot_types_dot_Value__pb2.DESCRIPTOR,])




_REDISKEYV2 = _descriptor.Descriptor(
  name='RedisKeyV2',
  full_name='feast.storage.RedisKeyV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='feast.storage.RedisKeyV2.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_names', full_name='feast.storage.RedisKeyV2.entity_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_values', full_name='feast.storage.RedisKeyV2.entity_values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=94,
  serialized_end=188,
)

_REDISKEYV2.fields_by_name['entity_values'].message_type = feast_dot_types_dot_Value__pb2._VALUE
DESCRIPTOR.message_types_by_name['RedisKeyV2'] = _REDISKEYV2
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedisKeyV2 = _reflection.GeneratedProtocolMessageType('RedisKeyV2', (_message.Message,), {
  'DESCRIPTOR' : _REDISKEYV2,
  '__module__' : 'feast.storage.Redis_pb2'
  # @@protoc_insertion_point(class_scope:feast.storage.RedisKeyV2)
  })
_sym_db.RegisterMessage(RedisKeyV2)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
