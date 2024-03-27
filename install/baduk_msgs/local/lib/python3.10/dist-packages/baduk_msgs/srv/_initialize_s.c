// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from baduk_msgs:srv/Initialize.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "baduk_msgs/srv/detail/initialize__struct.h"
#include "baduk_msgs/srv/detail/initialize__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool baduk_msgs__srv__initialize__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[46];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("baduk_msgs.srv._initialize.Initialize_Request", full_classname_dest, 45) == 0);
  }
  baduk_msgs__srv__Initialize_Request * ros_message = _ros_message;
  {  // do_initialize
    PyObject * field = PyObject_GetAttrString(_pymsg, "do_initialize");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->do_initialize = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * baduk_msgs__srv__initialize__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Initialize_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("baduk_msgs.srv._initialize");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Initialize_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  baduk_msgs__srv__Initialize_Request * ros_message = (baduk_msgs__srv__Initialize_Request *)raw_ros_message;
  {  // do_initialize
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->do_initialize ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "do_initialize", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "baduk_msgs/srv/detail/initialize__struct.h"
// already included above
// #include "baduk_msgs/srv/detail/initialize__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool baduk_msgs__srv__initialize__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[47];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("baduk_msgs.srv._initialize.Initialize_Response", full_classname_dest, 46) == 0);
  }
  baduk_msgs__srv__Initialize_Response * ros_message = _ros_message;
  {  // done_initialize
    PyObject * field = PyObject_GetAttrString(_pymsg, "done_initialize");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->done_initialize = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * baduk_msgs__srv__initialize__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Initialize_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("baduk_msgs.srv._initialize");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Initialize_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  baduk_msgs__srv__Initialize_Response * ros_message = (baduk_msgs__srv__Initialize_Response *)raw_ros_message;
  {  // done_initialize
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->done_initialize ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "done_initialize", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
