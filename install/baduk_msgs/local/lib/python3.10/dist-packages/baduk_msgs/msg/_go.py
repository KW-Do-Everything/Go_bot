# generated from rosidl_generator_py/resource/_idl.py.em
# with input from baduk_msgs:msg/Go.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'winrate'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Go(type):
    """Metaclass of message 'Go'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('baduk_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'baduk_msgs.msg.Go')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__go
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__go
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__go
            cls._TYPE_SUPPORT = module.type_support_msg__msg__go
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__go

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Go(metaclass=Metaclass_Go):
    """Message class 'Go'."""

    __slots__ = [
        '_territory',
        '_winrate',
        '_re_point',
        '_re_rate',
    ]

    _fields_and_field_types = {
        'territory': 'string',
        'winrate': 'sequence<int64>',
        're_point': 'sequence<string>',
        're_rate': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int64')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.territory = kwargs.get('territory', str())
        self.winrate = array.array('q', kwargs.get('winrate', []))
        self.re_point = kwargs.get('re_point', [])
        self.re_rate = kwargs.get('re_rate', [])

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.territory != other.territory:
            return False
        if self.winrate != other.winrate:
            return False
        if self.re_point != other.re_point:
            return False
        if self.re_rate != other.re_rate:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def territory(self):
        """Message field 'territory'."""
        return self._territory

    @territory.setter
    def territory(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'territory' field must be of type 'str'"
        self._territory = value

    @builtins.property
    def winrate(self):
        """Message field 'winrate'."""
        return self._winrate

    @winrate.setter
    def winrate(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'q', \
                "The 'winrate' array.array() must have the type code of 'q'"
            self._winrate = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -9223372036854775808 and val < 9223372036854775808 for val in value)), \
                "The 'winrate' field must be a set or sequence and each value of type 'int' and each integer in [-9223372036854775808, 9223372036854775807]"
        self._winrate = array.array('q', value)

    @builtins.property
    def re_point(self):
        """Message field 're_point'."""
        return self._re_point

    @re_point.setter
    def re_point(self, value):
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 're_point' field must be a set or sequence and each value of type 'str'"
        self._re_point = value

    @builtins.property
    def re_rate(self):
        """Message field 're_rate'."""
        return self._re_rate

    @re_rate.setter
    def re_rate(self, value):
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 're_rate' field must be a set or sequence and each value of type 'str'"
        self._re_rate = value
