// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from baduk_msgs:msg/Go.idl
// generated code does not contain a copyright notice

#ifndef BADUK_MSGS__MSG__DETAIL__GO__STRUCT_HPP_
#define BADUK_MSGS__MSG__DETAIL__GO__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__baduk_msgs__msg__Go __attribute__((deprecated))
#else
# define DEPRECATED__baduk_msgs__msg__Go __declspec(deprecated)
#endif

namespace baduk_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Go_
{
  using Type = Go_<ContainerAllocator>;

  explicit Go_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->territory = "";
    }
  }

  explicit Go_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : territory(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->territory = "";
    }
  }

  // field types and members
  using _territory_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _territory_type territory;
  using _winrate_type =
    std::vector<int64_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int64_t>>;
  _winrate_type winrate;
  using _re_point_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _re_point_type re_point;
  using _re_rate_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _re_rate_type re_rate;

  // setters for named parameter idiom
  Type & set__territory(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->territory = _arg;
    return *this;
  }
  Type & set__winrate(
    const std::vector<int64_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int64_t>> & _arg)
  {
    this->winrate = _arg;
    return *this;
  }
  Type & set__re_point(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->re_point = _arg;
    return *this;
  }
  Type & set__re_rate(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->re_rate = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    baduk_msgs::msg::Go_<ContainerAllocator> *;
  using ConstRawPtr =
    const baduk_msgs::msg::Go_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<baduk_msgs::msg::Go_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<baduk_msgs::msg::Go_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      baduk_msgs::msg::Go_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<baduk_msgs::msg::Go_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      baduk_msgs::msg::Go_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<baduk_msgs::msg::Go_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<baduk_msgs::msg::Go_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<baduk_msgs::msg::Go_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__baduk_msgs__msg__Go
    std::shared_ptr<baduk_msgs::msg::Go_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__baduk_msgs__msg__Go
    std::shared_ptr<baduk_msgs::msg::Go_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Go_ & other) const
  {
    if (this->territory != other.territory) {
      return false;
    }
    if (this->winrate != other.winrate) {
      return false;
    }
    if (this->re_point != other.re_point) {
      return false;
    }
    if (this->re_rate != other.re_rate) {
      return false;
    }
    return true;
  }
  bool operator!=(const Go_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Go_

// alias to use template instance with default allocator
using Go =
  baduk_msgs::msg::Go_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace baduk_msgs

#endif  // BADUK_MSGS__MSG__DETAIL__GO__STRUCT_HPP_
