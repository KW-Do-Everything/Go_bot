// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from baduk_msgs:msg/Vision.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "baduk_msgs/msg/detail/vision__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace baduk_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Vision_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) baduk_msgs::msg::Vision(_init);
}

void Vision_fini_function(void * message_memory)
{
  auto typed_message = static_cast<baduk_msgs::msg::Vision *>(message_memory);
  typed_message->~Vision();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Vision_message_member_array[1] = {
  {
    "check_vision",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs::msg::Vision, check_vision),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Vision_message_members = {
  "baduk_msgs::msg",  // message namespace
  "Vision",  // message name
  1,  // number of fields
  sizeof(baduk_msgs::msg::Vision),
  Vision_message_member_array,  // message members
  Vision_init_function,  // function to initialize message memory (memory has to be allocated)
  Vision_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Vision_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Vision_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace baduk_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<baduk_msgs::msg::Vision>()
{
  return &::baduk_msgs::msg::rosidl_typesupport_introspection_cpp::Vision_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, baduk_msgs, msg, Vision)() {
  return &::baduk_msgs::msg::rosidl_typesupport_introspection_cpp::Vision_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
