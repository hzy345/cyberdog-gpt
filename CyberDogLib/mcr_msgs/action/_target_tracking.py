# generated from rosidl_generator_py/resource/_idl.py.em
# with input from mcr_msgs:action/TargetTracking.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TargetTracking_Goal(type):
    """Metaclass of message 'TargetTracking_Goal'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'NAVIGATION_TYPE_START_UWB_TRACKING': 11,
        'NAVIGATION_TYPE_STOP_UWB_TRACKING': 12,
        'NAVIGATION_TYPE_START_HUMAN_TRACKING': 13,
        'NAVIGATION_TYPE_STOP_HUMAN_TRACKING': 14,
        'AUTO': 0,
        'BEHIND': 1,
        'LEFT': 2,
        'RIGHT': 3,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__target_tracking__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__target_tracking__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__target_tracking__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__target_tracking__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__target_tracking__goal

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'NAVIGATION_TYPE_START_UWB_TRACKING': cls.__constants['NAVIGATION_TYPE_START_UWB_TRACKING'],
            'NAVIGATION_TYPE_STOP_UWB_TRACKING': cls.__constants['NAVIGATION_TYPE_STOP_UWB_TRACKING'],
            'NAVIGATION_TYPE_START_HUMAN_TRACKING': cls.__constants['NAVIGATION_TYPE_START_HUMAN_TRACKING'],
            'NAVIGATION_TYPE_STOP_HUMAN_TRACKING': cls.__constants['NAVIGATION_TYPE_STOP_HUMAN_TRACKING'],
            'AUTO': cls.__constants['AUTO'],
            'BEHIND': cls.__constants['BEHIND'],
            'LEFT': cls.__constants['LEFT'],
            'RIGHT': cls.__constants['RIGHT'],
        }

    @property
    def NAVIGATION_TYPE_START_UWB_TRACKING(self):
        """Message constant 'NAVIGATION_TYPE_START_UWB_TRACKING'."""
        return Metaclass_TargetTracking_Goal.__constants['NAVIGATION_TYPE_START_UWB_TRACKING']

    @property
    def NAVIGATION_TYPE_STOP_UWB_TRACKING(self):
        """Message constant 'NAVIGATION_TYPE_STOP_UWB_TRACKING'."""
        return Metaclass_TargetTracking_Goal.__constants['NAVIGATION_TYPE_STOP_UWB_TRACKING']

    @property
    def NAVIGATION_TYPE_START_HUMAN_TRACKING(self):
        """Message constant 'NAVIGATION_TYPE_START_HUMAN_TRACKING'."""
        return Metaclass_TargetTracking_Goal.__constants['NAVIGATION_TYPE_START_HUMAN_TRACKING']

    @property
    def NAVIGATION_TYPE_STOP_HUMAN_TRACKING(self):
        """Message constant 'NAVIGATION_TYPE_STOP_HUMAN_TRACKING'."""
        return Metaclass_TargetTracking_Goal.__constants['NAVIGATION_TYPE_STOP_HUMAN_TRACKING']

    @property
    def AUTO(self):
        """Message constant 'AUTO'."""
        return Metaclass_TargetTracking_Goal.__constants['AUTO']

    @property
    def BEHIND(self):
        """Message constant 'BEHIND'."""
        return Metaclass_TargetTracking_Goal.__constants['BEHIND']

    @property
    def LEFT(self):
        """Message constant 'LEFT'."""
        return Metaclass_TargetTracking_Goal.__constants['LEFT']

    @property
    def RIGHT(self):
        """Message constant 'RIGHT'."""
        return Metaclass_TargetTracking_Goal.__constants['RIGHT']


class TargetTracking_Goal(metaclass=Metaclass_TargetTracking_Goal):
    """
    Message class 'TargetTracking_Goal'.

    Constants:
      NAVIGATION_TYPE_START_UWB_TRACKING
      NAVIGATION_TYPE_STOP_UWB_TRACKING
      NAVIGATION_TYPE_START_HUMAN_TRACKING
      NAVIGATION_TYPE_STOP_HUMAN_TRACKING
      AUTO
      BEHIND
      LEFT
      RIGHT
    """

    __slots__ = [
        '_nav_type',
        '_relative_pos',
        '_keep_distance',
        '_behavior_tree',
    ]

    _fields_and_field_types = {
        'nav_type': 'uint8',
        'relative_pos': 'uint8',
        'keep_distance': 'float',
        'behavior_tree': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.nav_type = kwargs.get('nav_type', int())
        self.relative_pos = kwargs.get('relative_pos', int())
        self.keep_distance = kwargs.get('keep_distance', float())
        self.behavior_tree = kwargs.get('behavior_tree', str())

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
        if self.nav_type != other.nav_type:
            return False
        if self.relative_pos != other.relative_pos:
            return False
        if self.keep_distance != other.keep_distance:
            return False
        if self.behavior_tree != other.behavior_tree:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def nav_type(self):
        """Message field 'nav_type'."""
        return self._nav_type

    @nav_type.setter
    def nav_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'nav_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'nav_type' field must be an unsigned integer in [0, 255]"
        self._nav_type = value

    @property
    def relative_pos(self):
        """Message field 'relative_pos'."""
        return self._relative_pos

    @relative_pos.setter
    def relative_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'relative_pos' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'relative_pos' field must be an unsigned integer in [0, 255]"
        self._relative_pos = value

    @property
    def keep_distance(self):
        """Message field 'keep_distance'."""
        return self._keep_distance

    @keep_distance.setter
    def keep_distance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'keep_distance' field must be of type 'float'"
        self._keep_distance = value

    @property
    def behavior_tree(self):
        """Message field 'behavior_tree'."""
        return self._behavior_tree

    @behavior_tree.setter
    def behavior_tree(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'behavior_tree' field must be of type 'str'"
        self._behavior_tree = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_TargetTracking_Result(type):
    """Metaclass of message 'TargetTracking_Result'."""

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
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__target_tracking__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__target_tracking__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__target_tracking__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__target_tracking__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__target_tracking__result

            from std_msgs.msg import Empty
            if Empty.__class__._TYPE_SUPPORT is None:
                Empty.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TargetTracking_Result(metaclass=Metaclass_TargetTracking_Result):
    """Message class 'TargetTracking_Result'."""

    __slots__ = [
        '_result',
    ]

    _fields_and_field_types = {
        'result': 'std_msgs/Empty',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Empty'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Empty
        self.result = kwargs.get('result', Empty())

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
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            from std_msgs.msg import Empty
            assert \
                isinstance(value, Empty), \
                "The 'result' field must be a sub message of type 'Empty'"
        self._result = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_TargetTracking_Feedback(type):
    """Metaclass of message 'TargetTracking_Feedback'."""

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
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__target_tracking__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__target_tracking__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__target_tracking__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__target_tracking__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__target_tracking__feedback

            from builtin_interfaces.msg import Duration
            if Duration.__class__._TYPE_SUPPORT is None:
                Duration.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TargetTracking_Feedback(metaclass=Metaclass_TargetTracking_Feedback):
    """Message class 'TargetTracking_Feedback'."""

    __slots__ = [
        '_current_distance',
        '_tracking_time',
        '_number_of_recoveries',
        '_exception_code',
        '_keep_distance',
        '_max_x',
        '_motion_state',
    ]

    _fields_and_field_types = {
        'current_distance': 'float',
        'tracking_time': 'builtin_interfaces/Duration',
        'number_of_recoveries': 'int16',
        'exception_code': 'int16',
        'keep_distance': 'float',
        'max_x': 'float',
        'motion_state': 'int16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Duration'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.current_distance = kwargs.get('current_distance', float())
        from builtin_interfaces.msg import Duration
        self.tracking_time = kwargs.get('tracking_time', Duration())
        self.number_of_recoveries = kwargs.get('number_of_recoveries', int())
        self.exception_code = kwargs.get('exception_code', int())
        self.keep_distance = kwargs.get('keep_distance', float())
        self.max_x = kwargs.get('max_x', float())
        self.motion_state = kwargs.get('motion_state', int())

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
        if self.current_distance != other.current_distance:
            return False
        if self.tracking_time != other.tracking_time:
            return False
        if self.number_of_recoveries != other.number_of_recoveries:
            return False
        if self.exception_code != other.exception_code:
            return False
        if self.keep_distance != other.keep_distance:
            return False
        if self.max_x != other.max_x:
            return False
        if self.motion_state != other.motion_state:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def current_distance(self):
        """Message field 'current_distance'."""
        return self._current_distance

    @current_distance.setter
    def current_distance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'current_distance' field must be of type 'float'"
        self._current_distance = value

    @property
    def tracking_time(self):
        """Message field 'tracking_time'."""
        return self._tracking_time

    @tracking_time.setter
    def tracking_time(self, value):
        if __debug__:
            from builtin_interfaces.msg import Duration
            assert \
                isinstance(value, Duration), \
                "The 'tracking_time' field must be a sub message of type 'Duration'"
        self._tracking_time = value

    @property
    def number_of_recoveries(self):
        """Message field 'number_of_recoveries'."""
        return self._number_of_recoveries

    @number_of_recoveries.setter
    def number_of_recoveries(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'number_of_recoveries' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'number_of_recoveries' field must be an integer in [-32768, 32767]"
        self._number_of_recoveries = value

    @property
    def exception_code(self):
        """Message field 'exception_code'."""
        return self._exception_code

    @exception_code.setter
    def exception_code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'exception_code' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'exception_code' field must be an integer in [-32768, 32767]"
        self._exception_code = value

    @property
    def keep_distance(self):
        """Message field 'keep_distance'."""
        return self._keep_distance

    @keep_distance.setter
    def keep_distance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'keep_distance' field must be of type 'float'"
        self._keep_distance = value

    @property
    def max_x(self):
        """Message field 'max_x'."""
        return self._max_x

    @max_x.setter
    def max_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'max_x' field must be of type 'float'"
        self._max_x = value

    @property
    def motion_state(self):
        """Message field 'motion_state'."""
        return self._motion_state

    @motion_state.setter
    def motion_state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'motion_state' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'motion_state' field must be an integer in [-32768, 32767]"
        self._motion_state = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_TargetTracking_SendGoal_Request(type):
    """Metaclass of message 'TargetTracking_SendGoal_Request'."""

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
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__target_tracking__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__target_tracking__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__target_tracking__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__target_tracking__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__target_tracking__send_goal__request

            from mcr_msgs.action import TargetTracking
            if TargetTracking.Goal.__class__._TYPE_SUPPORT is None:
                TargetTracking.Goal.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TargetTracking_SendGoal_Request(metaclass=Metaclass_TargetTracking_SendGoal_Request):
    """Message class 'TargetTracking_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'mcr_msgs/TargetTracking_Goal',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['mcr_msgs', 'action'], 'TargetTracking_Goal'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from mcr_msgs.action._target_tracking import TargetTracking_Goal
        self.goal = kwargs.get('goal', TargetTracking_Goal())

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
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @property
    def goal(self):
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value):
        if __debug__:
            from mcr_msgs.action._target_tracking import TargetTracking_Goal
            assert \
                isinstance(value, TargetTracking_Goal), \
                "The 'goal' field must be a sub message of type 'TargetTracking_Goal'"
        self._goal = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_TargetTracking_SendGoal_Response(type):
    """Metaclass of message 'TargetTracking_SendGoal_Response'."""

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
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__target_tracking__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__target_tracking__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__target_tracking__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__target_tracking__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__target_tracking__send_goal__response

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TargetTracking_SendGoal_Response(metaclass=Metaclass_TargetTracking_SendGoal_Response):
    """Message class 'TargetTracking_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
    ]

    _fields_and_field_types = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.accepted = kwargs.get('accepted', bool())
        from builtin_interfaces.msg import Time
        self.stamp = kwargs.get('stamp', Time())

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
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def accepted(self):
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'accepted' field must be of type 'bool'"
        self._accepted = value

    @property
    def stamp(self):
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value


class Metaclass_TargetTracking_SendGoal(type):
    """Metaclass of service 'TargetTracking_SendGoal'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__target_tracking__send_goal

            from mcr_msgs.action import _target_tracking
            if _target_tracking.Metaclass_TargetTracking_SendGoal_Request._TYPE_SUPPORT is None:
                _target_tracking.Metaclass_TargetTracking_SendGoal_Request.__import_type_support__()
            if _target_tracking.Metaclass_TargetTracking_SendGoal_Response._TYPE_SUPPORT is None:
                _target_tracking.Metaclass_TargetTracking_SendGoal_Response.__import_type_support__()


class TargetTracking_SendGoal(metaclass=Metaclass_TargetTracking_SendGoal):
    from mcr_msgs.action._target_tracking import TargetTracking_SendGoal_Request as Request
    from mcr_msgs.action._target_tracking import TargetTracking_SendGoal_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_TargetTracking_GetResult_Request(type):
    """Metaclass of message 'TargetTracking_GetResult_Request'."""

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
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__target_tracking__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__target_tracking__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__target_tracking__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__target_tracking__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__target_tracking__get_result__request

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TargetTracking_GetResult_Request(metaclass=Metaclass_TargetTracking_GetResult_Request):
    """Message class 'TargetTracking_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())

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
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_TargetTracking_GetResult_Response(type):
    """Metaclass of message 'TargetTracking_GetResult_Response'."""

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
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__target_tracking__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__target_tracking__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__target_tracking__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__target_tracking__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__target_tracking__get_result__response

            from mcr_msgs.action import TargetTracking
            if TargetTracking.Result.__class__._TYPE_SUPPORT is None:
                TargetTracking.Result.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TargetTracking_GetResult_Response(metaclass=Metaclass_TargetTracking_GetResult_Response):
    """Message class 'TargetTracking_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
    ]

    _fields_and_field_types = {
        'status': 'int8',
        'result': 'mcr_msgs/TargetTracking_Result',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['mcr_msgs', 'action'], 'TargetTracking_Result'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.status = kwargs.get('status', int())
        from mcr_msgs.action._target_tracking import TargetTracking_Result
        self.result = kwargs.get('result', TargetTracking_Result())

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
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'status' field must be an integer in [-128, 127]"
        self._status = value

    @property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            from mcr_msgs.action._target_tracking import TargetTracking_Result
            assert \
                isinstance(value, TargetTracking_Result), \
                "The 'result' field must be a sub message of type 'TargetTracking_Result'"
        self._result = value


class Metaclass_TargetTracking_GetResult(type):
    """Metaclass of service 'TargetTracking_GetResult'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__target_tracking__get_result

            from mcr_msgs.action import _target_tracking
            if _target_tracking.Metaclass_TargetTracking_GetResult_Request._TYPE_SUPPORT is None:
                _target_tracking.Metaclass_TargetTracking_GetResult_Request.__import_type_support__()
            if _target_tracking.Metaclass_TargetTracking_GetResult_Response._TYPE_SUPPORT is None:
                _target_tracking.Metaclass_TargetTracking_GetResult_Response.__import_type_support__()


class TargetTracking_GetResult(metaclass=Metaclass_TargetTracking_GetResult):
    from mcr_msgs.action._target_tracking import TargetTracking_GetResult_Request as Request
    from mcr_msgs.action._target_tracking import TargetTracking_GetResult_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_TargetTracking_FeedbackMessage(type):
    """Metaclass of message 'TargetTracking_FeedbackMessage'."""

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
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__target_tracking__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__target_tracking__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__target_tracking__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__target_tracking__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__target_tracking__feedback_message

            from mcr_msgs.action import TargetTracking
            if TargetTracking.Feedback.__class__._TYPE_SUPPORT is None:
                TargetTracking.Feedback.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TargetTracking_FeedbackMessage(metaclass=Metaclass_TargetTracking_FeedbackMessage):
    """Message class 'TargetTracking_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'mcr_msgs/TargetTracking_Feedback',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['mcr_msgs', 'action'], 'TargetTracking_Feedback'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from mcr_msgs.action._target_tracking import TargetTracking_Feedback
        self.feedback = kwargs.get('feedback', TargetTracking_Feedback())

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
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @property
    def feedback(self):
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        if __debug__:
            from mcr_msgs.action._target_tracking import TargetTracking_Feedback
            assert \
                isinstance(value, TargetTracking_Feedback), \
                "The 'feedback' field must be a sub message of type 'TargetTracking_Feedback'"
        self._feedback = value


class Metaclass_TargetTracking(type):
    """Metaclass of action 'TargetTracking'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mcr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mcr_msgs.action.TargetTracking')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__target_tracking

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from mcr_msgs.action import _target_tracking
            if _target_tracking.Metaclass_TargetTracking_SendGoal._TYPE_SUPPORT is None:
                _target_tracking.Metaclass_TargetTracking_SendGoal.__import_type_support__()
            if _target_tracking.Metaclass_TargetTracking_GetResult._TYPE_SUPPORT is None:
                _target_tracking.Metaclass_TargetTracking_GetResult.__import_type_support__()
            if _target_tracking.Metaclass_TargetTracking_FeedbackMessage._TYPE_SUPPORT is None:
                _target_tracking.Metaclass_TargetTracking_FeedbackMessage.__import_type_support__()


class TargetTracking(metaclass=Metaclass_TargetTracking):

    # The goal message defined in the action definition.
    from mcr_msgs.action._target_tracking import TargetTracking_Goal as Goal
    # The result message defined in the action definition.
    from mcr_msgs.action._target_tracking import TargetTracking_Result as Result
    # The feedback message defined in the action definition.
    from mcr_msgs.action._target_tracking import TargetTracking_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from mcr_msgs.action._target_tracking import TargetTracking_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from mcr_msgs.action._target_tracking import TargetTracking_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from mcr_msgs.action._target_tracking import TargetTracking_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')
