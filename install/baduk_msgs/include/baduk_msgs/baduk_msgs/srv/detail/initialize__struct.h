// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from baduk_msgs:srv/Initialize.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__SRV__DETAIL__INITIALIZE__STRUCT_H_
#define BADUK_MSGS__SRV__DETAIL__INITIALIZE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Initialize in the package baduk_msgs.
typedef struct baduk_msgs__srv__Initialize_Request
{
  bool do_initialize;
} baduk_msgs__srv__Initialize_Request;

// Struct for a sequence of baduk_msgs__srv__Initialize_Request.
typedef struct baduk_msgs__srv__Initialize_Request__Sequence
{
  baduk_msgs__srv__Initialize_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} baduk_msgs__srv__Initialize_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Initialize in the package baduk_msgs.
typedef struct baduk_msgs__srv__Initialize_Response
{
  bool done_initialize;
} baduk_msgs__srv__Initialize_Response;

// Struct for a sequence of baduk_msgs__srv__Initialize_Response.
typedef struct baduk_msgs__srv__Initialize_Response__Sequence
{
  baduk_msgs__srv__Initialize_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} baduk_msgs__srv__Initialize_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // BADUK_MSGS__SRV__DETAIL__INITIALIZE__STRUCT_H_
