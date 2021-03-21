# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/third_party/grpc/health/v1/HealthService.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/third_party/grpc/health/v1/HealthService.proto',
  package='grpc.health.v1',
  syntax='proto3',
  serialized_options=b'\n\021io.grpc.health.v1B\013HealthProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4feast/third_party/grpc/health/v1/HealthService.proto\x12\x0egrpc.health.v1\"%\n\x12HealthCheckRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\"D\n\x13HealthCheckResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.grpc.health.v1.ServingStatus*:\n\rServingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0f\n\x0bNOT_SERVING\x10\x02\x32Z\n\x06Health\x12P\n\x05\x43heck\x12\".grpc.health.v1.HealthCheckRequest\x1a#.grpc.health.v1.HealthCheckResponseB \n\x11io.grpc.health.v1B\x0bHealthProtob\x06proto3'
)

_SERVINGSTATUS = _descriptor.EnumDescriptor(
  name='ServingStatus',
  full_name='grpc.health.v1.ServingStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_SERVING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=181,
  serialized_end=239,
)
_sym_db.RegisterEnumDescriptor(_SERVINGSTATUS)

ServingStatus = enum_type_wrapper.EnumTypeWrapper(_SERVINGSTATUS)
UNKNOWN = 0
SERVING = 1
NOT_SERVING = 2



_HEALTHCHECKREQUEST = _descriptor.Descriptor(
  name='HealthCheckRequest',
  full_name='grpc.health.v1.HealthCheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='grpc.health.v1.HealthCheckRequest.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=72,
  serialized_end=109,
)


_HEALTHCHECKRESPONSE = _descriptor.Descriptor(
  name='HealthCheckResponse',
  full_name='grpc.health.v1.HealthCheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='grpc.health.v1.HealthCheckResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=179,
)

_HEALTHCHECKRESPONSE.fields_by_name['status'].enum_type = _SERVINGSTATUS
DESCRIPTOR.message_types_by_name['HealthCheckRequest'] = _HEALTHCHECKREQUEST
DESCRIPTOR.message_types_by_name['HealthCheckResponse'] = _HEALTHCHECKRESPONSE
DESCRIPTOR.enum_types_by_name['ServingStatus'] = _SERVINGSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HealthCheckRequest = _reflection.GeneratedProtocolMessageType('HealthCheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHCHECKREQUEST,
  '__module__' : 'feast.third_party.grpc.health.v1.HealthService_pb2'
  # @@protoc_insertion_point(class_scope:grpc.health.v1.HealthCheckRequest)
  })
_sym_db.RegisterMessage(HealthCheckRequest)

HealthCheckResponse = _reflection.GeneratedProtocolMessageType('HealthCheckResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHCHECKRESPONSE,
  '__module__' : 'feast.third_party.grpc.health.v1.HealthService_pb2'
  # @@protoc_insertion_point(class_scope:grpc.health.v1.HealthCheckResponse)
  })
_sym_db.RegisterMessage(HealthCheckResponse)


DESCRIPTOR._options = None

_HEALTH = _descriptor.ServiceDescriptor(
  name='Health',
  full_name='grpc.health.v1.Health',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=241,
  serialized_end=331,
  methods=[
  _descriptor.MethodDescriptor(
    name='Check',
    full_name='grpc.health.v1.Health.Check',
    index=0,
    containing_service=None,
    input_type=_HEALTHCHECKREQUEST,
    output_type=_HEALTHCHECKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HEALTH)

DESCRIPTOR.services_by_name['Health'] = _HEALTH

# @@protoc_insertion_point(module_scope)
