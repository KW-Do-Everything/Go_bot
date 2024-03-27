// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from baduk_msgs:srv/Initialize.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__SRV__DETAIL__INITIALIZE__BUILDER_HPP_
#define BADUK_MSGS__SRV__DETAIL__INITIALIZE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "baduk_msgs/srv/detail/initialize__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace baduk_msgs
{

namespace srv
{

namespace builder
{

class Init_Initialize_Request_do_initialize
{
public:
  Init_Initialize_Request_do_initialize()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::baduk_msgs::srv::Initialize_Request do_initialize(::baduk_msgs::srv::Initialize_Request::_do_initialize_type arg)
  {
    msg_.do_initialize = std::move(arg);
    return std::move(msg_);
  }

private:
  ::baduk_msgs::srv::Initialize_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::baduk_msgs::srv::Initialize_Request>()
{
  return baduk_msgs::srv::builder::Init_Initialize_Request_do_initialize();
}

}  // namespace baduk_msgs


namespace baduk_msgs
{

namespace srv
{

namespace builder
{

class Init_Initialize_Response_done_initialize
{
public:
  Init_Initialize_Response_done_initialize()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::baduk_msgs::srv::Initialize_Response done_initialize(::baduk_msgs::srv::Initialize_Response::_done_initialize_type arg)
  {
    msg_.done_initialize = std::move(arg);
    return std::move(msg_);
  }

private:
  ::baduk_msgs::srv::Initialize_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::baduk_msgs::srv::Initialize_Response>()
{
  return baduk_msgs::srv::builder::Init_Initialize_Response_done_initialize();
}

}  // namespace baduk_msgs

#endif  // BADUK_MSGS__SRV__DETAIL__INITIALIZE__BUILDER_HPP_
