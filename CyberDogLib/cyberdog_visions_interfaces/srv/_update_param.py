# generated from rosidl_generator_py/resource/_idl.py.em
# with input from cyberdog_visions_interfaces:srv/UpdateParam.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_UpdateParam_Request(type):
    """Metaclass of message 'UpdateParam_Request'."""

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
            module = import_type_support('cyberdog_visions_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'cyberdog_visions_interfaces.srv.UpdateParam_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__update_param__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__update_param__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__update_param__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__update_param__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__update_param__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class UpdateParam_Request(metaclass=Metaclass_UpdateParam_Request):
    """Message class 'UpdateParam_Request'."""

    __slots__ = [
        '_map_id',
    ]

    _fields_and_field_types = {
        'map_id': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.map_id = kwargs.get('map_id', int())

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
        if self.map_id != other.map_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def map_id(self):
        """Message field 'map_id'."""
        return self._map_id

    @map_id.setter
    def map_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'map_id' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'map_id' field must be an integer in [-2147483648, 2147483647]"
        self._map_id = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_UpdateParam_Response(type):
    """Metaclass of message 'UpdateParam_Response'."""

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
            module = import_type_support('cyberdog_visions_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'cyberdog_visions_interfaces.srv.UpdateParam_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__update_param__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__update_param__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__update_param__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__update_param__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__update_param__response

            from cyberdog_visions_interfaces.msg import Reply
            if Reply.__class__._TYPE_SUPPORT is None:
                Reply.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class UpdateParam_Response(metaclass=Metaclass_UpdateParam_Response):
    """Message class 'UpdateParam_Response'."""

    __slots__ = [
        '_reply',
    ]

    _fields_and_field_types = {
        'reply': 'cyberdog_visions_interfaces/Reply',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['cyberdog_visions_interfaces', 'msg'], 'Reply'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from cyberdog_visions_interfaces.msg import Reply
        self.reply = kwargs.get('reply', Reply())

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
        if self.reply != other.reply:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def reply(self):
        """Message field 'reply'."""
        return self._reply

    @reply.setter
    def reply(self, value):
        if __debug__:
            from cyberdog_visions_interfaces.msg import Reply
            assert \
                isinstance(value, Reply), \
                "The 'reply' field must be a sub message of type 'Reply'"
        self._reply = value


class Metaclass_UpdateParam(type):
    """Metaclass of service 'UpdateParam'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('cyberdog_visions_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'cyberdog_visions_interfaces.srv.UpdateParam')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__update_param

            from cyberdog_visions_interfaces.srv import _update_param
            if _update_param.Metaclass_UpdateParam_Request._TYPE_SUPPORT is None:
                _update_param.Metaclass_UpdateParam_Request.__import_type_support__()
            if _update_param.Metaclass_UpdateParam_Response._TYPE_SUPPORT is None:
                _update_param.Metaclass_UpdateParam_Response.__import_type_support__()


class UpdateParam(metaclass=Metaclass_UpdateParam):
    from cyberdog_visions_interfaces.srv._update_param import UpdateParam_Request as Request
    from cyberdog_visions_interfaces.srv._update_param import UpdateParam_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
