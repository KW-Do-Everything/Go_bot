// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from baduk_msgs:msg/Go.idl
// generated code does not contain a copyright notice
#include "baduk_msgs/msg/detail/go__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `territory`
// Member `re_point`
// Member `re_rate`
#include "rosidl_runtime_c/string_functions.h"
// Member `winrate`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
baduk_msgs__msg__Go__init(baduk_msgs__msg__Go * msg)
{
  if (!msg) {
    return false;
  }
  // territory
  if (!rosidl_runtime_c__String__init(&msg->territory)) {
    baduk_msgs__msg__Go__fini(msg);
    return false;
  }
  // winrate
  if (!rosidl_runtime_c__int64__Sequence__init(&msg->winrate, 0)) {
    baduk_msgs__msg__Go__fini(msg);
    return false;
  }
  // re_point
  if (!rosidl_runtime_c__String__Sequence__init(&msg->re_point, 0)) {
    baduk_msgs__msg__Go__fini(msg);
    return false;
  }
  // re_rate
  if (!rosidl_runtime_c__String__Sequence__init(&msg->re_rate, 0)) {
    baduk_msgs__msg__Go__fini(msg);
    return false;
  }
  return true;
}

void
baduk_msgs__msg__Go__fini(baduk_msgs__msg__Go * msg)
{
  if (!msg) {
    return;
  }
  // territory
  rosidl_runtime_c__String__fini(&msg->territory);
  // winrate
  rosidl_runtime_c__int64__Sequence__fini(&msg->winrate);
  // re_point
  rosidl_runtime_c__String__Sequence__fini(&msg->re_point);
  // re_rate
  rosidl_runtime_c__String__Sequence__fini(&msg->re_rate);
}

bool
baduk_msgs__msg__Go__are_equal(const baduk_msgs__msg__Go * lhs, const baduk_msgs__msg__Go * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // territory
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->territory), &(rhs->territory)))
  {
    return false;
  }
  // winrate
  if (!rosidl_runtime_c__int64__Sequence__are_equal(
      &(lhs->winrate), &(rhs->winrate)))
  {
    return false;
  }
  // re_point
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->re_point), &(rhs->re_point)))
  {
    return false;
  }
  // re_rate
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->re_rate), &(rhs->re_rate)))
  {
    return false;
  }
  return true;
}

bool
baduk_msgs__msg__Go__copy(
  const baduk_msgs__msg__Go * input,
  baduk_msgs__msg__Go * output)
{
  if (!input || !output) {
    return false;
  }
  // territory
  if (!rosidl_runtime_c__String__copy(
      &(input->territory), &(output->territory)))
  {
    return false;
  }
  // winrate
  if (!rosidl_runtime_c__int64__Sequence__copy(
      &(input->winrate), &(output->winrate)))
  {
    return false;
  }
  // re_point
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->re_point), &(output->re_point)))
  {
    return false;
  }
  // re_rate
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->re_rate), &(output->re_rate)))
  {
    return false;
  }
  return true;
}

baduk_msgs__msg__Go *
baduk_msgs__msg__Go__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__msg__Go * msg = (baduk_msgs__msg__Go *)allocator.allocate(sizeof(baduk_msgs__msg__Go), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(baduk_msgs__msg__Go));
  bool success = baduk_msgs__msg__Go__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
baduk_msgs__msg__Go__destroy(baduk_msgs__msg__Go * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    baduk_msgs__msg__Go__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
baduk_msgs__msg__Go__Sequence__init(baduk_msgs__msg__Go__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__msg__Go * data = NULL;

  if (size) {
    data = (baduk_msgs__msg__Go *)allocator.zero_allocate(size, sizeof(baduk_msgs__msg__Go), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = baduk_msgs__msg__Go__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        baduk_msgs__msg__Go__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
baduk_msgs__msg__Go__Sequence__fini(baduk_msgs__msg__Go__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      baduk_msgs__msg__Go__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

baduk_msgs__msg__Go__Sequence *
baduk_msgs__msg__Go__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__msg__Go__Sequence * array = (baduk_msgs__msg__Go__Sequence *)allocator.allocate(sizeof(baduk_msgs__msg__Go__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = baduk_msgs__msg__Go__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
baduk_msgs__msg__Go__Sequence__destroy(baduk_msgs__msg__Go__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    baduk_msgs__msg__Go__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
baduk_msgs__msg__Go__Sequence__are_equal(const baduk_msgs__msg__Go__Sequence * lhs, const baduk_msgs__msg__Go__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!baduk_msgs__msg__Go__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
baduk_msgs__msg__Go__Sequence__copy(
  const baduk_msgs__msg__Go__Sequence * input,
  baduk_msgs__msg__Go__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(baduk_msgs__msg__Go);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    baduk_msgs__msg__Go * data =
      (baduk_msgs__msg__Go *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!baduk_msgs__msg__Go__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          baduk_msgs__msg__Go__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!baduk_msgs__msg__Go__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
