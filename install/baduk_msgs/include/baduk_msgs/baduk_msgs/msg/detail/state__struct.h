// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from baduk_msgs:msg/State.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__STATE__STRUCT_H_
#define BADUK_MSGS__MSG__DETAIL__STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'state'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/State in the package baduk_msgs.
typedef struct baduk_msgs__msg__State
{
  rosidl_runtime_c__String state;
} baduk_msgs__msg__State;

// Struct for a sequence of baduk_msgs__msg__State.
typedef struct baduk_msgs__msg__State__Sequence
{
  baduk_msgs__msg__State * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} baduk_msgs__msg__State__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // BADUK_MSGS__MSG__DETAIL__STATE__STRUCT_H_
