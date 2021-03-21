# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/types/Value.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/types/Value.proto',
  package='feast.types',
  syntax='proto3',
  serialized_options=b'\n\021feast.proto.typesB\nValueProtoZ4github.com/feast-dev/feast/sdk/go/protos/feast/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x66\x65\x61st/types/Value.proto\x12\x0b\x66\x65\x61st.types\"\xe0\x01\n\tValueType\"\xd2\x01\n\x04\x45num\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05\x42YTES\x10\x01\x12\n\n\x06STRING\x10\x02\x12\t\n\x05INT32\x10\x03\x12\t\n\x05INT64\x10\x04\x12\n\n\x06\x44OUBLE\x10\x05\x12\t\n\x05\x46LOAT\x10\x06\x12\x08\n\x04\x42OOL\x10\x07\x12\x0e\n\nBYTES_LIST\x10\x0b\x12\x0f\n\x0bSTRING_LIST\x10\x0c\x12\x0e\n\nINT32_LIST\x10\r\x12\x0e\n\nINT64_LIST\x10\x0e\x12\x0f\n\x0b\x44OUBLE_LIST\x10\x0f\x12\x0e\n\nFLOAT_LIST\x10\x10\x12\r\n\tBOOL_LIST\x10\x11\"\x82\x04\n\x05Value\x12\x13\n\tbytes_val\x18\x01 \x01(\x0cH\x00\x12\x14\n\nstring_val\x18\x02 \x01(\tH\x00\x12\x13\n\tint32_val\x18\x03 \x01(\x05H\x00\x12\x13\n\tint64_val\x18\x04 \x01(\x03H\x00\x12\x14\n\ndouble_val\x18\x05 \x01(\x01H\x00\x12\x13\n\tfloat_val\x18\x06 \x01(\x02H\x00\x12\x12\n\x08\x62ool_val\x18\x07 \x01(\x08H\x00\x12\x30\n\x0e\x62ytes_list_val\x18\x0b \x01(\x0b\x32\x16.feast.types.BytesListH\x00\x12\x32\n\x0fstring_list_val\x18\x0c \x01(\x0b\x32\x17.feast.types.StringListH\x00\x12\x30\n\x0eint32_list_val\x18\r \x01(\x0b\x32\x16.feast.types.Int32ListH\x00\x12\x30\n\x0eint64_list_val\x18\x0e \x01(\x0b\x32\x16.feast.types.Int64ListH\x00\x12\x32\n\x0f\x64ouble_list_val\x18\x0f \x01(\x0b\x32\x17.feast.types.DoubleListH\x00\x12\x30\n\x0e\x66loat_list_val\x18\x10 \x01(\x0b\x32\x16.feast.types.FloatListH\x00\x12.\n\rbool_list_val\x18\x11 \x01(\x0b\x32\x15.feast.types.BoolListH\x00\x42\x05\n\x03val\"\x18\n\tBytesList\x12\x0b\n\x03val\x18\x01 \x03(\x0c\"\x19\n\nStringList\x12\x0b\n\x03val\x18\x01 \x03(\t\"\x18\n\tInt32List\x12\x0b\n\x03val\x18\x01 \x03(\x05\"\x18\n\tInt64List\x12\x0b\n\x03val\x18\x01 \x03(\x03\"\x19\n\nDoubleList\x12\x0b\n\x03val\x18\x01 \x03(\x01\"\x18\n\tFloatList\x12\x0b\n\x03val\x18\x01 \x03(\x02\"\x17\n\x08\x42oolList\x12\x0b\n\x03val\x18\x01 \x03(\x08\x42U\n\x11\x66\x65\x61st.proto.typesB\nValueProtoZ4github.com/feast-dev/feast/sdk/go/protos/feast/typesb\x06proto3'
)



_VALUETYPE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='feast.types.ValueType.Enum',
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
      name='BYTES', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BYTES_LIST', index=8, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING_LIST', index=9, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT32_LIST', index=10, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT64_LIST', index=11, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_LIST', index=12, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOAT_LIST', index=13, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOOL_LIST', index=14, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=55,
  serialized_end=265,
)
_sym_db.RegisterEnumDescriptor(_VALUETYPE_ENUM)


_VALUETYPE = _descriptor.Descriptor(
  name='ValueType',
  full_name='feast.types.ValueType',
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
    _VALUETYPE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=265,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='feast.types.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes_val', full_name='feast.types.Value.bytes_val', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='feast.types.Value.string_val', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int32_val', full_name='feast.types.Value.int32_val', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_val', full_name='feast.types.Value.int64_val', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_val', full_name='feast.types.Value.double_val', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='float_val', full_name='feast.types.Value.float_val', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_val', full_name='feast.types.Value.bool_val', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes_list_val', full_name='feast.types.Value.bytes_list_val', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_list_val', full_name='feast.types.Value.string_list_val', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int32_list_val', full_name='feast.types.Value.int32_list_val', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_list_val', full_name='feast.types.Value.int64_list_val', index=10,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_list_val', full_name='feast.types.Value.double_list_val', index=11,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='float_list_val', full_name='feast.types.Value.float_list_val', index=12,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_list_val', full_name='feast.types.Value.bool_list_val', index=13,
      number=17, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='val', full_name='feast.types.Value.val',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=268,
  serialized_end=782,
)


_BYTESLIST = _descriptor.Descriptor(
  name='BytesList',
  full_name='feast.types.BytesList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='feast.types.BytesList.val', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=784,
  serialized_end=808,
)


_STRINGLIST = _descriptor.Descriptor(
  name='StringList',
  full_name='feast.types.StringList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='feast.types.StringList.val', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=810,
  serialized_end=835,
)


_INT32LIST = _descriptor.Descriptor(
  name='Int32List',
  full_name='feast.types.Int32List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='feast.types.Int32List.val', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=837,
  serialized_end=861,
)


_INT64LIST = _descriptor.Descriptor(
  name='Int64List',
  full_name='feast.types.Int64List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='feast.types.Int64List.val', index=0,
      number=1, type=3, cpp_type=2, label=3,
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
  serialized_start=863,
  serialized_end=887,
)


_DOUBLELIST = _descriptor.Descriptor(
  name='DoubleList',
  full_name='feast.types.DoubleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='feast.types.DoubleList.val', index=0,
      number=1, type=1, cpp_type=5, label=3,
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
  serialized_start=889,
  serialized_end=914,
)


_FLOATLIST = _descriptor.Descriptor(
  name='FloatList',
  full_name='feast.types.FloatList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='feast.types.FloatList.val', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=916,
  serialized_end=940,
)


_BOOLLIST = _descriptor.Descriptor(
  name='BoolList',
  full_name='feast.types.BoolList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='feast.types.BoolList.val', index=0,
      number=1, type=8, cpp_type=7, label=3,
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
  serialized_start=942,
  serialized_end=965,
)

_VALUETYPE_ENUM.containing_type = _VALUETYPE
_VALUE.fields_by_name['bytes_list_val'].message_type = _BYTESLIST
_VALUE.fields_by_name['string_list_val'].message_type = _STRINGLIST
_VALUE.fields_by_name['int32_list_val'].message_type = _INT32LIST
_VALUE.fields_by_name['int64_list_val'].message_type = _INT64LIST
_VALUE.fields_by_name['double_list_val'].message_type = _DOUBLELIST
_VALUE.fields_by_name['float_list_val'].message_type = _FLOATLIST
_VALUE.fields_by_name['bool_list_val'].message_type = _BOOLLIST
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['bytes_val'])
_VALUE.fields_by_name['bytes_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['string_val'])
_VALUE.fields_by_name['string_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['int32_val'])
_VALUE.fields_by_name['int32_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['int64_val'])
_VALUE.fields_by_name['int64_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['double_val'])
_VALUE.fields_by_name['double_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['float_val'])
_VALUE.fields_by_name['float_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['bool_val'])
_VALUE.fields_by_name['bool_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['bytes_list_val'])
_VALUE.fields_by_name['bytes_list_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['string_list_val'])
_VALUE.fields_by_name['string_list_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['int32_list_val'])
_VALUE.fields_by_name['int32_list_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['int64_list_val'])
_VALUE.fields_by_name['int64_list_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['double_list_val'])
_VALUE.fields_by_name['double_list_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['float_list_val'])
_VALUE.fields_by_name['float_list_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['bool_list_val'])
_VALUE.fields_by_name['bool_list_val'].containing_oneof = _VALUE.oneofs_by_name['val']
DESCRIPTOR.message_types_by_name['ValueType'] = _VALUETYPE
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['BytesList'] = _BYTESLIST
DESCRIPTOR.message_types_by_name['StringList'] = _STRINGLIST
DESCRIPTOR.message_types_by_name['Int32List'] = _INT32LIST
DESCRIPTOR.message_types_by_name['Int64List'] = _INT64LIST
DESCRIPTOR.message_types_by_name['DoubleList'] = _DOUBLELIST
DESCRIPTOR.message_types_by_name['FloatList'] = _FLOATLIST
DESCRIPTOR.message_types_by_name['BoolList'] = _BOOLLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValueType = _reflection.GeneratedProtocolMessageType('ValueType', (_message.Message,), {
  'DESCRIPTOR' : _VALUETYPE,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.ValueType)
  })
_sym_db.RegisterMessage(ValueType)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.Value)
  })
_sym_db.RegisterMessage(Value)

BytesList = _reflection.GeneratedProtocolMessageType('BytesList', (_message.Message,), {
  'DESCRIPTOR' : _BYTESLIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.BytesList)
  })
_sym_db.RegisterMessage(BytesList)

StringList = _reflection.GeneratedProtocolMessageType('StringList', (_message.Message,), {
  'DESCRIPTOR' : _STRINGLIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.StringList)
  })
_sym_db.RegisterMessage(StringList)

Int32List = _reflection.GeneratedProtocolMessageType('Int32List', (_message.Message,), {
  'DESCRIPTOR' : _INT32LIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.Int32List)
  })
_sym_db.RegisterMessage(Int32List)

Int64List = _reflection.GeneratedProtocolMessageType('Int64List', (_message.Message,), {
  'DESCRIPTOR' : _INT64LIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.Int64List)
  })
_sym_db.RegisterMessage(Int64List)

DoubleList = _reflection.GeneratedProtocolMessageType('DoubleList', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLELIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.DoubleList)
  })
_sym_db.RegisterMessage(DoubleList)

FloatList = _reflection.GeneratedProtocolMessageType('FloatList', (_message.Message,), {
  'DESCRIPTOR' : _FLOATLIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.FloatList)
  })
_sym_db.RegisterMessage(FloatList)

BoolList = _reflection.GeneratedProtocolMessageType('BoolList', (_message.Message,), {
  'DESCRIPTOR' : _BOOLLIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.BoolList)
  })
_sym_db.RegisterMessage(BoolList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
