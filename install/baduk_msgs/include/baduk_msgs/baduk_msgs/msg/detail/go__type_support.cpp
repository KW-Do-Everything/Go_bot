// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from baduk_msgs:msg/Go.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "baduk_msgs/msg/detail/go__struct.hpp"
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

void Go_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) baduk_msgs::msg::Go(_init);
}

void Go_fini_function(void * message_memory)
{
  auto typed_message = static_cast<baduk_msgs::msg::Go *>(message_memory);
  typed_message->~Go();
}

size_t size_function__Go__winrate(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int64_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Go__winrate(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int64_t> *>(untyped_member);
  return &member[index];
}

void * get_function__Go__winrate(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int64_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__Go__winrate(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int64_t *>(
    get_const_function__Go__winrate(untyped_member, index));
  auto & value = *reinterpret_cast<int64_t *>(untyped_value);
  value = item;
}

void assign_function__Go__winrate(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int64_t *>(
    get_function__Go__winrate(untyped_member, index));
  const auto & value = *reinterpret_cast<const int64_t *>(untyped_value);
  item = value;
}

void resize_function__Go__winrate(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int64_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__Go__re_point(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Go__re_point(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__Go__re_point(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__Go__re_point(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__Go__re_point(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__Go__re_point(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__Go__re_point(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__Go__re_point(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__Go__re_rate(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Go__re_rate(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__Go__re_rate(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__Go__re_rate(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__Go__re_rate(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__Go__re_rate(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__Go__re_rate(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__Go__re_rate(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Go_message_member_array[4] = {
  {
    "territory",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs::msg::Go, territory),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "winrate",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs::msg::Go, winrate),  // bytes offset in struct
    nullptr,  // default value
    size_function__Go__winrate,  // size() function pointer
    get_const_function__Go__winrate,  // get_const(index) function pointer
    get_function__Go__winrate,  // get(index) function pointer
    fetch_function__Go__winrate,  // fetch(index, &value) function pointer
    assign_function__Go__winrate,  // assign(index, value) function pointer
    resize_function__Go__winrate  // resize(index) function pointer
  },
  {
    "re_point",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs::msg::Go, re_point),  // bytes offset in struct
    nullptr,  // default value
    size_function__Go__re_point,  // size() function pointer
    get_const_function__Go__re_point,  // get_const(index) function pointer
    get_function__Go__re_point,  // get(index) function pointer
    fetch_function__Go__re_point,  // fetch(index, &value) function pointer
    assign_function__Go__re_point,  // assign(index, value) function pointer
    resize_function__Go__re_point  // resize(index) function pointer
  },
  {
    "re_rate",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(baduk_msgs::msg::Go, re_rate),  // bytes offset in struct
    nullptr,  // default value
    size_function__Go__re_rate,  // size() function pointer
    get_const_function__Go__re_rate,  // get_const(index) function pointer
    get_function__Go__re_rate,  // get(index) function pointer
    fetch_function__Go__re_rate,  // fetch(index, &value) function pointer
    assign_function__Go__re_rate,  // assign(index, value) function pointer
    resize_function__Go__re_rate  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Go_message_members = {
  "baduk_msgs::msg",  // message namespace
  "Go",  // message name
  4,  // number of fields
  sizeof(baduk_msgs::msg::Go),
  Go_message_member_array,  // message members
  Go_init_function,  // function to initialize message memory (memory has to be allocated)
  Go_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Go_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Go_message_members,
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
get_message_type_support_handle<baduk_msgs::msg::Go>()
{
  return &::baduk_msgs::msg::rosidl_typesupport_introspection_cpp::Go_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, baduk_msgs, msg, Go)() {
  return &::baduk_msgs::msg::rosidl_typesupport_introspection_cpp::Go_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
