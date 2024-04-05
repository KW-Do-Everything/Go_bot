// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from baduk_msgs:msg/Vision.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__VISION__STRUCT_H_
#define BADUK_MSGS__MSG__DETAIL__VISION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Vision in the package baduk_msgs.
typedef struct baduk_msgs__msg__Vision
{
  bool check_vision;
} baduk_msgs__msg__Vision;

// Struct for a sequence of baduk_msgs__msg__Vision.
typedef struct baduk_msgs__msg__Vision__Sequence
{
  baduk_msgs__msg__Vision * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} baduk_msgs__msg__Vision__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // BADUK_MSGS__MSG__DETAIL__VISION__STRUCT_H_
