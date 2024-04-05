// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from baduk_msgs:srv/Initialize.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__SRV__DETAIL__INITIALIZE__TRAITS_HPP_
#define BADUK_MSGS__SRV__DETAIL__INITIALIZE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "baduk_msgs/srv/detail/initialize__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace baduk_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const Initialize_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: do_initialize
  {
    out << "do_initialize: ";
    rosidl_generator_traits::value_to_yaml(msg.do_initialize, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Initialize_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: do_initialize
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "do_initialize: ";
    rosidl_generator_traits::value_to_yaml(msg.do_initialize, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Initialize_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace baduk_msgs

namespace rosidl_generator_traits
{

[[deprecated("use baduk_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const baduk_msgs::srv::Initialize_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  baduk_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use baduk_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const baduk_msgs::srv::Initialize_Request & msg)
{
  return baduk_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<baduk_msgs::srv::Initialize_Request>()
{
  return "baduk_msgs::srv::Initialize_Request";
}

template<>
inline const char * name<baduk_msgs::srv::Initialize_Request>()
{
  return "baduk_msgs/srv/Initialize_Request";
}

template<>
struct has_fixed_size<baduk_msgs::srv::Initialize_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<baduk_msgs::srv::Initialize_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<baduk_msgs::srv::Initialize_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace baduk_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const Initialize_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: done_initialize
  {
    out << "done_initialize: ";
    rosidl_generator_traits::value_to_yaml(msg.done_initialize, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Initialize_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: done_initialize
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "done_initialize: ";
    rosidl_generator_traits::value_to_yaml(msg.done_initialize, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Initialize_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace baduk_msgs

namespace rosidl_generator_traits
{

[[deprecated("use baduk_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const baduk_msgs::srv::Initialize_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  baduk_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use baduk_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const baduk_msgs::srv::Initialize_Response & msg)
{
  return baduk_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<baduk_msgs::srv::Initialize_Response>()
{
  return "baduk_msgs::srv::Initialize_Response";
}

template<>
inline const char * name<baduk_msgs::srv::Initialize_Response>()
{
  return "baduk_msgs/srv/Initialize_Response";
}

template<>
struct has_fixed_size<baduk_msgs::srv::Initialize_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<baduk_msgs::srv::Initialize_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<baduk_msgs::srv::Initialize_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<baduk_msgs::srv::Initialize>()
{
  return "baduk_msgs::srv::Initialize";
}

template<>
inline const char * name<baduk_msgs::srv::Initialize>()
{
  return "baduk_msgs/srv/Initialize";
}

template<>
struct has_fixed_size<baduk_msgs::srv::Initialize>
  : std::integral_constant<
    bool,
    has_fixed_size<baduk_msgs::srv::Initialize_Request>::value &&
    has_fixed_size<baduk_msgs::srv::Initialize_Response>::value
  >
{
};

template<>
struct has_bounded_size<baduk_msgs::srv::Initialize>
  : std::integral_constant<
    bool,
    has_bounded_size<baduk_msgs::srv::Initialize_Request>::value &&
    has_bounded_size<baduk_msgs::srv::Initialize_Response>::value
  >
{
};

template<>
struct is_service<baduk_msgs::srv::Initialize>
  : std::true_type
{
};

template<>
struct is_service_request<baduk_msgs::srv::Initialize_Request>
  : std::true_type
{
};

template<>
struct is_service_response<baduk_msgs::srv::Initialize_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // BADUK_MSGS__SRV__DETAIL__INITIALIZE__TRAITS_HPP_
