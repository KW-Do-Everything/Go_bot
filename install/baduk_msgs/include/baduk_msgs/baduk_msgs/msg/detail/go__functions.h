// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from baduk_msgs:msg/Go.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__GO__FUNCTIONS_H_
#define BADUK_MSGS__MSG__DETAIL__GO__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "baduk_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "baduk_msgs/msg/detail/go__struct.h"

/// Initialize msg/Go message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * baduk_msgs__msg__Go
 * )) before or use
 * baduk_msgs__msg__Go__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Go__init(baduk_msgs__msg__Go * msg);

/// Finalize msg/Go message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
void
baduk_msgs__msg__Go__fini(baduk_msgs__msg__Go * msg);

/// Create msg/Go message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * baduk_msgs__msg__Go__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
baduk_msgs__msg__Go *
baduk_msgs__msg__Go__create();

/// Destroy msg/Go message.
/**
 * It calls
 * baduk_msgs__msg__Go__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
void
baduk_msgs__msg__Go__destroy(baduk_msgs__msg__Go * msg);

/// Check for msg/Go message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Go__are_equal(const baduk_msgs__msg__Go * lhs, const baduk_msgs__msg__Go * rhs);

/// Copy a msg/Go message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Go__copy(
  const baduk_msgs__msg__Go * input,
  baduk_msgs__msg__Go * output);

/// Initialize array of msg/Go messages.
/**
 * It allocates the memory for the number of elements and calls
 * baduk_msgs__msg__Go__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Go__Sequence__init(baduk_msgs__msg__Go__Sequence * array, size_t size);

/// Finalize array of msg/Go messages.
/**
 * It calls
 * baduk_msgs__msg__Go__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
void
baduk_msgs__msg__Go__Sequence__fini(baduk_msgs__msg__Go__Sequence * array);

/// Create array of msg/Go messages.
/**
 * It allocates the memory for the array and calls
 * baduk_msgs__msg__Go__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
baduk_msgs__msg__Go__Sequence *
baduk_msgs__msg__Go__Sequence__create(size_t size);

/// Destroy array of msg/Go messages.
/**
 * It calls
 * baduk_msgs__msg__Go__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
void
baduk_msgs__msg__Go__Sequence__destroy(baduk_msgs__msg__Go__Sequence * array);

/// Check for msg/Go message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Go__Sequence__are_equal(const baduk_msgs__msg__Go__Sequence * lhs, const baduk_msgs__msg__Go__Sequence * rhs);

/// Copy an array of msg/Go messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Go__Sequence__copy(
  const baduk_msgs__msg__Go__Sequence * input,
  baduk_msgs__msg__Go__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // BADUK_MSGS__MSG__DETAIL__GO__FUNCTIONS_H_
