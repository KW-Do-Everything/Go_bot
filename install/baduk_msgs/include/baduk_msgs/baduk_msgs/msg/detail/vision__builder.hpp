// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from baduk_msgs:msg/Vision.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__VISION__BUILDER_HPP_
#define BADUK_MSGS__MSG__DETAIL__VISION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "baduk_msgs/msg/detail/vision__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace baduk_msgs
{

namespace msg
{

namespace builder
{

class Init_Vision_check_vision
{
public:
  Init_Vision_check_vision()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::baduk_msgs::msg::Vision check_vision(::baduk_msgs::msg::Vision::_check_vision_type arg)
  {
    msg_.check_vision = std::move(arg);
    return std::move(msg_);
  }

private:
  ::baduk_msgs::msg::Vision msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::baduk_msgs::msg::Vision>()
{
  return baduk_msgs::msg::builder::Init_Vision_check_vision();
}

}  // namespace baduk_msgs

#endif  // BADUK_MSGS__MSG__DETAIL__VISION__BUILDER_HPP_
