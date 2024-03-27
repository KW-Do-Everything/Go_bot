// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from baduk_msgs:msg/Vision.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__VISION__FUNCTIONS_H_
#define BADUK_MSGS__MSG__DETAIL__VISION__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "baduk_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "baduk_msgs/msg/detail/vision__struct.h"

/// Initialize msg/Vision message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * baduk_msgs__msg__Vision
 * )) before or use
 * baduk_msgs__msg__Vision__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Vision__init(baduk_msgs__msg__Vision * msg);

/// Finalize msg/Vision message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
void
baduk_msgs__msg__Vision__fini(baduk_msgs__msg__Vision * msg);

/// Create msg/Vision message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * baduk_msgs__msg__Vision__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
baduk_msgs__msg__Vision *
baduk_msgs__msg__Vision__create();

/// Destroy msg/Vision message.
/**
 * It calls
 * baduk_msgs__msg__Vision__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
void
baduk_msgs__msg__Vision__destroy(baduk_msgs__msg__Vision * msg);

/// Check for msg/Vision message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Vision__are_equal(const baduk_msgs__msg__Vision * lhs, const baduk_msgs__msg__Vision * rhs);

/// Copy a msg/Vision message.
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
baduk_msgs__msg__Vision__copy(
  const baduk_msgs__msg__Vision * input,
  baduk_msgs__msg__Vision * output);

/// Initialize array of msg/Vision messages.
/**
 * It allocates the memory for the number of elements and calls
 * baduk_msgs__msg__Vision__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Vision__Sequence__init(baduk_msgs__msg__Vision__Sequence * array, size_t size);

/// Finalize array of msg/Vision messages.
/**
 * It calls
 * baduk_msgs__msg__Vision__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
void
baduk_msgs__msg__Vision__Sequence__fini(baduk_msgs__msg__Vision__Sequence * array);

/// Create array of msg/Vision messages.
/**
 * It allocates the memory for the array and calls
 * baduk_msgs__msg__Vision__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
baduk_msgs__msg__Vision__Sequence *
baduk_msgs__msg__Vision__Sequence__create(size_t size);

/// Destroy array of msg/Vision messages.
/**
 * It calls
 * baduk_msgs__msg__Vision__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
void
baduk_msgs__msg__Vision__Sequence__destroy(baduk_msgs__msg__Vision__Sequence * array);

/// Check for msg/Vision message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_baduk_msgs
bool
baduk_msgs__msg__Vision__Sequence__are_equal(const baduk_msgs__msg__Vision__Sequence * lhs, const baduk_msgs__msg__Vision__Sequence * rhs);

/// Copy an array of msg/Vision messages.
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
baduk_msgs__msg__Vision__Sequence__copy(
  const baduk_msgs__msg__Vision__Sequence * input,
  baduk_msgs__msg__Vision__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // BADUK_MSGS__MSG__DETAIL__VISION__FUNCTIONS_H_
