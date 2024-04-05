// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from baduk_msgs:msg/Vision.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__VISION__TRAITS_HPP_
#define BADUK_MSGS__MSG__DETAIL__VISION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "baduk_msgs/msg/detail/vision__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace baduk_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Vision & msg,
  std::ostream & out)
{
  out << "{";
  // member: check_vision
  {
    out << "check_vision: ";
    rosidl_generator_traits::value_to_yaml(msg.check_vision, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Vision & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: check_vision
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "check_vision: ";
    rosidl_generator_traits::value_to_yaml(msg.check_vision, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Vision & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace baduk_msgs

namespace rosidl_generator_traits
{

[[deprecated("use baduk_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const baduk_msgs::msg::Vision & msg,
  std::ostream & out, size_t indentation = 0)
{
  baduk_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use baduk_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const baduk_msgs::msg::Vision & msg)
{
  return baduk_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<baduk_msgs::msg::Vision>()
{
  return "baduk_msgs::msg::Vision";
}

template<>
inline const char * name<baduk_msgs::msg::Vision>()
{
  return "baduk_msgs/msg/Vision";
}

template<>
struct has_fixed_size<baduk_msgs::msg::Vision>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<baduk_msgs::msg::Vision>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<baduk_msgs::msg::Vision>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // BADUK_MSGS__MSG__DETAIL__VISION__TRAITS_HPP_
