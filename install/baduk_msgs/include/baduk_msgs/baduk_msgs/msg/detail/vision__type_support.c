// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from baduk_msgs:msg/Vision.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "baduk_msgs/msg/detail/vision__rosidl_typesupport_introspection_c.h"
#include "baduk_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "baduk_msgs/msg/detail/vision__functions.h"
#include "baduk_msgs/msg/detail/vision__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  baduk_msgs__msg__Vision__init(message_memory);
}

void baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_fini_function(void * message_memory)
{
  baduk_msgs__msg__Vision__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_message_member_array[1] = {
  {
    "check_vision",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs__msg__Vision, check_vision),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_message_members = {
  "baduk_msgs__msg",  // message namespace
  "Vision",  // message name
  1,  // number of fields
  sizeof(baduk_msgs__msg__Vision),
  baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_message_member_array,  // message members
  baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_init_function,  // function to initialize message memory (memory has to be allocated)
  baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_message_type_support_handle = {
  0,
  &baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_baduk_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, baduk_msgs, msg, Vision)() {
  if (!baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_message_type_support_handle.typesupport_identifier) {
    baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &baduk_msgs__msg__Vision__rosidl_typesupport_introspection_c__Vision_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
