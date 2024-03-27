// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from baduk_msgs:msg/Go.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__GO__BUILDER_HPP_
#define BADUK_MSGS__MSG__DETAIL__GO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "baduk_msgs/msg/detail/go__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace baduk_msgs
{

namespace msg
{

namespace builder
{

class Init_Go_re_rate
{
public:
  explicit Init_Go_re_rate(::baduk_msgs::msg::Go & msg)
  : msg_(msg)
  {}
  ::baduk_msgs::msg::Go re_rate(::baduk_msgs::msg::Go::_re_rate_type arg)
  {
    msg_.re_rate = std::move(arg);
    return std::move(msg_);
  }

private:
  ::baduk_msgs::msg::Go msg_;
};

class Init_Go_re_point
{
public:
  explicit Init_Go_re_point(::baduk_msgs::msg::Go & msg)
  : msg_(msg)
  {}
  Init_Go_re_rate re_point(::baduk_msgs::msg::Go::_re_point_type arg)
  {
    msg_.re_point = std::move(arg);
    return Init_Go_re_rate(msg_);
  }

private:
  ::baduk_msgs::msg::Go msg_;
};

class Init_Go_winrate
{
public:
  explicit Init_Go_winrate(::baduk_msgs::msg::Go & msg)
  : msg_(msg)
  {}
  Init_Go_re_point winrate(::baduk_msgs::msg::Go::_winrate_type arg)
  {
    msg_.winrate = std::move(arg);
    return Init_Go_re_point(msg_);
  }

private:
  ::baduk_msgs::msg::Go msg_;
};

class Init_Go_territory
{
public:
  Init_Go_territory()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Go_winrate territory(::baduk_msgs::msg::Go::_territory_type arg)
  {
    msg_.territory = std::move(arg);
    return Init_Go_winrate(msg_);
  }

private:
  ::baduk_msgs::msg::Go msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::baduk_msgs::msg::Go>()
{
  return baduk_msgs::msg::builder::Init_Go_territory();
}

}  // namespace baduk_msgs

#endif  // BADUK_MSGS__MSG__DETAIL__GO__BUILDER_HPP_
