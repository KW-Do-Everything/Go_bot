// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from baduk_msgs:msg/State.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__STATE__BUILDER_HPP_
#define BADUK_MSGS__MSG__DETAIL__STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "baduk_msgs/msg/detail/state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace baduk_msgs
{

namespace msg
{

namespace builder
{

class Init_State_state
{
public:
  Init_State_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::baduk_msgs::msg::State state(::baduk_msgs::msg::State::_state_type arg)
  {
    msg_.state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::baduk_msgs::msg::State msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::baduk_msgs::msg::State>()
{
  return baduk_msgs::msg::builder::Init_State_state();
}

}  // namespace baduk_msgs

#endif  // BADUK_MSGS__MSG__DETAIL__STATE__BUILDER_HPP_
