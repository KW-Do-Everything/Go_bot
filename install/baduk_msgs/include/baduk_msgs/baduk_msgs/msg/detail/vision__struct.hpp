// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from baduk_msgs:msg/Vision.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__VISION__STRUCT_HPP_
#define BADUK_MSGS__MSG__DETAIL__VISION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__baduk_msgs__msg__Vision __attribute__((deprecated))
#else
# define DEPRECATED__baduk_msgs__msg__Vision __declspec(deprecated)
#endif

namespace baduk_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Vision_
{
  using Type = Vision_<ContainerAllocator>;

  explicit Vision_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->check_vision = false;
    }
  }

  explicit Vision_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->check_vision = false;
    }
  }

  // field types and members
  using _check_vision_type =
    bool;
  _check_vision_type check_vision;

  // setters for named parameter idiom
  Type & set__check_vision(
    const bool & _arg)
  {
    this->check_vision = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    baduk_msgs::msg::Vision_<ContainerAllocator> *;
  using ConstRawPtr =
    const baduk_msgs::msg::Vision_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<baduk_msgs::msg::Vision_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<baduk_msgs::msg::Vision_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      baduk_msgs::msg::Vision_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<baduk_msgs::msg::Vision_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      baduk_msgs::msg::Vision_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<baduk_msgs::msg::Vision_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<baduk_msgs::msg::Vision_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<baduk_msgs::msg::Vision_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__baduk_msgs__msg__Vision
    std::shared_ptr<baduk_msgs::msg::Vision_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__baduk_msgs__msg__Vision
    std::shared_ptr<baduk_msgs::msg::Vision_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Vision_ & other) const
  {
    if (this->check_vision != other.check_vision) {
      return false;
    }
    return true;
  }
  bool operator!=(const Vision_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Vision_

// alias to use template instance with default allocator
using Vision =
  baduk_msgs::msg::Vision_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace baduk_msgs

#endif  // BADUK_MSGS__MSG__DETAIL__VISION__STRUCT_HPP_
