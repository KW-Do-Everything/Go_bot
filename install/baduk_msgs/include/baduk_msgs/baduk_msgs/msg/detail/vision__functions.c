// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from baduk_msgs:msg/Vision.idl
// generated code does not contain a copyright notice
#include "baduk_msgs/msg/detail/vision__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
baduk_msgs__msg__Vision__init(baduk_msgs__msg__Vision * msg)
{
  if (!msg) {
    return false;
  }
  // check_vision
  return true;
}

void
baduk_msgs__msg__Vision__fini(baduk_msgs__msg__Vision * msg)
{
  if (!msg) {
    return;
  }
  // check_vision
}

bool
baduk_msgs__msg__Vision__are_equal(const baduk_msgs__msg__Vision * lhs, const baduk_msgs__msg__Vision * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // check_vision
  if (lhs->check_vision != rhs->check_vision) {
    return false;
  }
  return true;
}

bool
baduk_msgs__msg__Vision__copy(
  const baduk_msgs__msg__Vision * input,
  baduk_msgs__msg__Vision * output)
{
  if (!input || !output) {
    return false;
  }
  // check_vision
  output->check_vision = input->check_vision;
  return true;
}

baduk_msgs__msg__Vision *
baduk_msgs__msg__Vision__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__msg__Vision * msg = (baduk_msgs__msg__Vision *)allocator.allocate(sizeof(baduk_msgs__msg__Vision), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(baduk_msgs__msg__Vision));
  bool success = baduk_msgs__msg__Vision__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
baduk_msgs__msg__Vision__destroy(baduk_msgs__msg__Vision * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    baduk_msgs__msg__Vision__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
baduk_msgs__msg__Vision__Sequence__init(baduk_msgs__msg__Vision__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__msg__Vision * data = NULL;

  if (size) {
    data = (baduk_msgs__msg__Vision *)allocator.zero_allocate(size, sizeof(baduk_msgs__msg__Vision), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = baduk_msgs__msg__Vision__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        baduk_msgs__msg__Vision__fini(&data[i - 1]);
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
baduk_msgs__msg__Vision__Sequence__fini(baduk_msgs__msg__Vision__Sequence * array)
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
      baduk_msgs__msg__Vision__fini(&array->data[i]);
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

baduk_msgs__msg__Vision__Sequence *
baduk_msgs__msg__Vision__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__msg__Vision__Sequence * array = (baduk_msgs__msg__Vision__Sequence *)allocator.allocate(sizeof(baduk_msgs__msg__Vision__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = baduk_msgs__msg__Vision__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
baduk_msgs__msg__Vision__Sequence__destroy(baduk_msgs__msg__Vision__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    baduk_msgs__msg__Vision__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
baduk_msgs__msg__Vision__Sequence__are_equal(const baduk_msgs__msg__Vision__Sequence * lhs, const baduk_msgs__msg__Vision__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!baduk_msgs__msg__Vision__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
baduk_msgs__msg__Vision__Sequence__copy(
  const baduk_msgs__msg__Vision__Sequence * input,
  baduk_msgs__msg__Vision__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(baduk_msgs__msg__Vision);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    baduk_msgs__msg__Vision * data =
      (baduk_msgs__msg__Vision *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!baduk_msgs__msg__Vision__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          baduk_msgs__msg__Vision__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!baduk_msgs__msg__Vision__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
