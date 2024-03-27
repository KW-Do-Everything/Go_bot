// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from baduk_msgs:srv/Initialize.idl
// generated code does not contain a copyright notice
#include "baduk_msgs/srv/detail/initialize__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
baduk_msgs__srv__Initialize_Request__init(baduk_msgs__srv__Initialize_Request * msg)
{
  if (!msg) {
    return false;
  }
  // do_initialize
  return true;
}

void
baduk_msgs__srv__Initialize_Request__fini(baduk_msgs__srv__Initialize_Request * msg)
{
  if (!msg) {
    return;
  }
  // do_initialize
}

bool
baduk_msgs__srv__Initialize_Request__are_equal(const baduk_msgs__srv__Initialize_Request * lhs, const baduk_msgs__srv__Initialize_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // do_initialize
  if (lhs->do_initialize != rhs->do_initialize) {
    return false;
  }
  return true;
}

bool
baduk_msgs__srv__Initialize_Request__copy(
  const baduk_msgs__srv__Initialize_Request * input,
  baduk_msgs__srv__Initialize_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // do_initialize
  output->do_initialize = input->do_initialize;
  return true;
}

baduk_msgs__srv__Initialize_Request *
baduk_msgs__srv__Initialize_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__srv__Initialize_Request * msg = (baduk_msgs__srv__Initialize_Request *)allocator.allocate(sizeof(baduk_msgs__srv__Initialize_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(baduk_msgs__srv__Initialize_Request));
  bool success = baduk_msgs__srv__Initialize_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
baduk_msgs__srv__Initialize_Request__destroy(baduk_msgs__srv__Initialize_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    baduk_msgs__srv__Initialize_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
baduk_msgs__srv__Initialize_Request__Sequence__init(baduk_msgs__srv__Initialize_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__srv__Initialize_Request * data = NULL;

  if (size) {
    data = (baduk_msgs__srv__Initialize_Request *)allocator.zero_allocate(size, sizeof(baduk_msgs__srv__Initialize_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = baduk_msgs__srv__Initialize_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        baduk_msgs__srv__Initialize_Request__fini(&data[i - 1]);
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
baduk_msgs__srv__Initialize_Request__Sequence__fini(baduk_msgs__srv__Initialize_Request__Sequence * array)
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
      baduk_msgs__srv__Initialize_Request__fini(&array->data[i]);
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

baduk_msgs__srv__Initialize_Request__Sequence *
baduk_msgs__srv__Initialize_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__srv__Initialize_Request__Sequence * array = (baduk_msgs__srv__Initialize_Request__Sequence *)allocator.allocate(sizeof(baduk_msgs__srv__Initialize_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = baduk_msgs__srv__Initialize_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
baduk_msgs__srv__Initialize_Request__Sequence__destroy(baduk_msgs__srv__Initialize_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    baduk_msgs__srv__Initialize_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
baduk_msgs__srv__Initialize_Request__Sequence__are_equal(const baduk_msgs__srv__Initialize_Request__Sequence * lhs, const baduk_msgs__srv__Initialize_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!baduk_msgs__srv__Initialize_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
baduk_msgs__srv__Initialize_Request__Sequence__copy(
  const baduk_msgs__srv__Initialize_Request__Sequence * input,
  baduk_msgs__srv__Initialize_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(baduk_msgs__srv__Initialize_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    baduk_msgs__srv__Initialize_Request * data =
      (baduk_msgs__srv__Initialize_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!baduk_msgs__srv__Initialize_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          baduk_msgs__srv__Initialize_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!baduk_msgs__srv__Initialize_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
baduk_msgs__srv__Initialize_Response__init(baduk_msgs__srv__Initialize_Response * msg)
{
  if (!msg) {
    return false;
  }
  // done_initialize
  return true;
}

void
baduk_msgs__srv__Initialize_Response__fini(baduk_msgs__srv__Initialize_Response * msg)
{
  if (!msg) {
    return;
  }
  // done_initialize
}

bool
baduk_msgs__srv__Initialize_Response__are_equal(const baduk_msgs__srv__Initialize_Response * lhs, const baduk_msgs__srv__Initialize_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // done_initialize
  if (lhs->done_initialize != rhs->done_initialize) {
    return false;
  }
  return true;
}

bool
baduk_msgs__srv__Initialize_Response__copy(
  const baduk_msgs__srv__Initialize_Response * input,
  baduk_msgs__srv__Initialize_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // done_initialize
  output->done_initialize = input->done_initialize;
  return true;
}

baduk_msgs__srv__Initialize_Response *
baduk_msgs__srv__Initialize_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__srv__Initialize_Response * msg = (baduk_msgs__srv__Initialize_Response *)allocator.allocate(sizeof(baduk_msgs__srv__Initialize_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(baduk_msgs__srv__Initialize_Response));
  bool success = baduk_msgs__srv__Initialize_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
baduk_msgs__srv__Initialize_Response__destroy(baduk_msgs__srv__Initialize_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    baduk_msgs__srv__Initialize_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
baduk_msgs__srv__Initialize_Response__Sequence__init(baduk_msgs__srv__Initialize_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__srv__Initialize_Response * data = NULL;

  if (size) {
    data = (baduk_msgs__srv__Initialize_Response *)allocator.zero_allocate(size, sizeof(baduk_msgs__srv__Initialize_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = baduk_msgs__srv__Initialize_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        baduk_msgs__srv__Initialize_Response__fini(&data[i - 1]);
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
baduk_msgs__srv__Initialize_Response__Sequence__fini(baduk_msgs__srv__Initialize_Response__Sequence * array)
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
      baduk_msgs__srv__Initialize_Response__fini(&array->data[i]);
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

baduk_msgs__srv__Initialize_Response__Sequence *
baduk_msgs__srv__Initialize_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  baduk_msgs__srv__Initialize_Response__Sequence * array = (baduk_msgs__srv__Initialize_Response__Sequence *)allocator.allocate(sizeof(baduk_msgs__srv__Initialize_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = baduk_msgs__srv__Initialize_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
baduk_msgs__srv__Initialize_Response__Sequence__destroy(baduk_msgs__srv__Initialize_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    baduk_msgs__srv__Initialize_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
baduk_msgs__srv__Initialize_Response__Sequence__are_equal(const baduk_msgs__srv__Initialize_Response__Sequence * lhs, const baduk_msgs__srv__Initialize_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!baduk_msgs__srv__Initialize_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
baduk_msgs__srv__Initialize_Response__Sequence__copy(
  const baduk_msgs__srv__Initialize_Response__Sequence * input,
  baduk_msgs__srv__Initialize_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(baduk_msgs__srv__Initialize_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    baduk_msgs__srv__Initialize_Response * data =
      (baduk_msgs__srv__Initialize_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!baduk_msgs__srv__Initialize_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          baduk_msgs__srv__Initialize_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!baduk_msgs__srv__Initialize_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
