// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from baduk_msgs:msg/Go.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "baduk_msgs/msg/detail/go__rosidl_typesupport_introspection_c.h"
#include "baduk_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "baduk_msgs/msg/detail/go__functions.h"
#include "baduk_msgs/msg/detail/go__struct.h"


// Include directives for member types
// Member `territory`
// Member `re_point`
// Member `re_rate`
#include "rosidl_runtime_c/string_functions.h"
// Member `winrate`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  baduk_msgs__msg__Go__init(message_memory);
}

void baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_fini_function(void * message_memory)
{
  baduk_msgs__msg__Go__fini(message_memory);
}

size_t baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__size_function__Go__winrate(
  const void * untyped_member)
{
  const rosidl_runtime_c__int64__Sequence * member =
    (const rosidl_runtime_c__int64__Sequence *)(untyped_member);
  return member->size;
}

const void * baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_const_function__Go__winrate(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int64__Sequence * member =
    (const rosidl_runtime_c__int64__Sequence *)(untyped_member);
  return &member->data[index];
}

void * baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_function__Go__winrate(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int64__Sequence * member =
    (rosidl_runtime_c__int64__Sequence *)(untyped_member);
  return &member->data[index];
}

void baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__fetch_function__Go__winrate(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int64_t * item =
    ((const int64_t *)
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_const_function__Go__winrate(untyped_member, index));
  int64_t * value =
    (int64_t *)(untyped_value);
  *value = *item;
}

void baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__assign_function__Go__winrate(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int64_t * item =
    ((int64_t *)
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_function__Go__winrate(untyped_member, index));
  const int64_t * value =
    (const int64_t *)(untyped_value);
  *item = *value;
}

bool baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__resize_function__Go__winrate(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int64__Sequence * member =
    (rosidl_runtime_c__int64__Sequence *)(untyped_member);
  rosidl_runtime_c__int64__Sequence__fini(member);
  return rosidl_runtime_c__int64__Sequence__init(member, size);
}

size_t baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__size_function__Go__re_point(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_const_function__Go__re_point(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_function__Go__re_point(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__fetch_function__Go__re_point(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_const_function__Go__re_point(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__assign_function__Go__re_point(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_function__Go__re_point(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__resize_function__Go__re_point(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__size_function__Go__re_rate(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_const_function__Go__re_rate(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_function__Go__re_rate(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__fetch_function__Go__re_rate(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_const_function__Go__re_rate(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__assign_function__Go__re_rate(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_function__Go__re_rate(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__resize_function__Go__re_rate(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_message_member_array[4] = {
  {
    "territory",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs__msg__Go, territory),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "winrate",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs__msg__Go, winrate),  // bytes offset in struct
    NULL,  // default value
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__size_function__Go__winrate,  // size() function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_const_function__Go__winrate,  // get_const(index) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_function__Go__winrate,  // get(index) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__fetch_function__Go__winrate,  // fetch(index, &value) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__assign_function__Go__winrate,  // assign(index, value) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__resize_function__Go__winrate  // resize(index) function pointer
  },
  {
    "re_point",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs__msg__Go, re_point),  // bytes offset in struct
    NULL,  // default value
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__size_function__Go__re_point,  // size() function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_const_function__Go__re_point,  // get_const(index) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_function__Go__re_point,  // get(index) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__fetch_function__Go__re_point,  // fetch(index, &value) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__assign_function__Go__re_point,  // assign(index, value) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__resize_function__Go__re_point  // resize(index) function pointer
  },
  {
    "re_rate",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs__msg__Go, re_rate),  // bytes offset in struct
    NULL,  // default value
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__size_function__Go__re_rate,  // size() function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_const_function__Go__re_rate,  // get_const(index) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__get_function__Go__re_rate,  // get(index) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__fetch_function__Go__re_rate,  // fetch(index, &value) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__assign_function__Go__re_rate,  // assign(index, value) function pointer
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__resize_function__Go__re_rate  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_message_members = {
  "baduk_msgs__msg",  // message namespace
  "Go",  // message name
  4,  // number of fields
  sizeof(baduk_msgs__msg__Go),
  baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_message_member_array,  // message members
  baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_init_function,  // function to initialize message memory (memory has to be allocated)
  baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_message_type_support_handle = {
  0,
  &baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_baduk_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, baduk_msgs, msg, Go)() {
  if (!baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_message_type_support_handle.typesupport_identifier) {
    baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &baduk_msgs__msg__Go__rosidl_typesupport_introspection_c__Go_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
