// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from baduk_msgs:msg/Go.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__GO__TRAITS_HPP_
#define BADUK_MSGS__MSG__DETAIL__GO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "baduk_msgs/msg/detail/go__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace baduk_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Go & msg,
  std::ostream & out)
{
  out << "{";
  // member: territory
  {
    out << "territory: ";
    rosidl_generator_traits::value_to_yaml(msg.territory, out);
    out << ", ";
  }

  // member: winrate
  {
    if (msg.winrate.size() == 0) {
      out << "winrate: []";
    } else {
      out << "winrate: [";
      size_t pending_items = msg.winrate.size();
      for (auto item : msg.winrate) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: re_point
  {
    if (msg.re_point.size() == 0) {
      out << "re_point: []";
    } else {
      out << "re_point: [";
      size_t pending_items = msg.re_point.size();
      for (auto item : msg.re_point) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: re_rate
  {
    if (msg.re_rate.size() == 0) {
      out << "re_rate: []";
    } else {
      out << "re_rate: [";
      size_t pending_items = msg.re_rate.size();
      for (auto item : msg.re_rate) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Go & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: territory
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "territory: ";
    rosidl_generator_traits::value_to_yaml(msg.territory, out);
    out << "\n";
  }

  // member: winrate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.winrate.size() == 0) {
      out << "winrate: []\n";
    } else {
      out << "winrate:\n";
      for (auto item : msg.winrate) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: re_point
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.re_point.size() == 0) {
      out << "re_point: []\n";
    } else {
      out << "re_point:\n";
      for (auto item : msg.re_point) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: re_rate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.re_rate.size() == 0) {
      out << "re_rate: []\n";
    } else {
      out << "re_rate:\n";
      for (auto item : msg.re_rate) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Go & msg, bool use_flow_style = false)
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
  const baduk_msgs::msg::Go & msg,
  std::ostream & out, size_t indentation = 0)
{
  baduk_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use baduk_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const baduk_msgs::msg::Go & msg)
{
  return baduk_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<baduk_msgs::msg::Go>()
{
  return "baduk_msgs::msg::Go";
}

template<>
inline const char * name<baduk_msgs::msg::Go>()
{
  return "baduk_msgs/msg/Go";
}

template<>
struct has_fixed_size<baduk_msgs::msg::Go>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<baduk_msgs::msg::Go>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<baduk_msgs::msg::Go>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // BADUK_MSGS__MSG__DETAIL__GO__TRAITS_HPP_
