// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from baduk_msgs:msg/Go.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__GO__STRUCT_H_
#define BADUK_MSGS__MSG__DETAIL__GO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'territory'
// Member 're_point'
// Member 're_rate'
#include "rosidl_runtime_c/string.h"
// Member 'winrate'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/Go in the package baduk_msgs.
typedef struct baduk_msgs__msg__Go
{
  rosidl_runtime_c__String territory;
  rosidl_runtime_c__int64__Sequence winrate;
  rosidl_runtime_c__String__Sequence re_point;
  rosidl_runtime_c__String__Sequence re_rate;
} baduk_msgs__msg__Go;

// Struct for a sequence of baduk_msgs__msg__Go.
typedef struct baduk_msgs__msg__Go__Sequence
{
  baduk_msgs__msg__Go * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} baduk_msgs__msg__Go__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // BADUK_MSGS__MSG__DETAIL__GO__STRUCT_H_
