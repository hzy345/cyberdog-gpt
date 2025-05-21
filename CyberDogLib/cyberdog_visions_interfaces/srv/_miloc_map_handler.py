# generated from rosidl_generator_py/resource/_idl.py.em
# with input from cyberdog_visions_interfaces:srv/MilocMapHandler.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MilocMapHandler_Request(type):
    """Metaclass of message 'MilocMapHandler_Request'."""

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
                'cyberdog_visions_interfaces.srv.MilocMapHandler_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__miloc_map_handler__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__miloc_map_handler__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__miloc_map_handler__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__miloc_map_handler__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__miloc_map_handler__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MilocMapHandler_Request(metaclass=Metaclass_MilocMapHandler_Request):
    """Message class 'MilocMapHandler_Request'."""

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


class Metaclass_MilocMapHandler_Response(type):
    """Metaclass of message 'MilocMapHandler_Response'."""

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
                'cyberdog_visions_interfaces.srv.MilocMapHandler_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__miloc_map_handler__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__miloc_map_handler__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__miloc_map_handler__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__miloc_map_handler__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__miloc_map_handler__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MilocMapHandler_Response(metaclass=Metaclass_MilocMapHandler_Response):
    """Message class 'MilocMapHandler_Response'."""

    __slots__ = [
        '_code',
        '_message',
    ]

    _fields_and_field_types = {
        'code': 'int32',
        'message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.code = kwargs.get('code', int())
        self.message = kwargs.get('message', str())

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
        if self.code != other.code:
            return False
        if self.message != other.message:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def code(self):
        """Message field 'code'."""
        return self._code

    @code.setter
    def code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'code' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'code' field must be an integer in [-2147483648, 2147483647]"
        self._code = value

    @property
    def message(self):
        """Message field 'message'."""
        return self._message

    @message.setter
    def message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'message' field must be of type 'str'"
        self._message = value


class Metaclass_MilocMapHandler(type):
    """Metaclass of service 'MilocMapHandler'."""

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
                'cyberdog_visions_interfaces.srv.MilocMapHandler')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__miloc_map_handler

            from cyberdog_visions_interfaces.srv import _miloc_map_handler
            if _miloc_map_handler.Metaclass_MilocMapHandler_Request._TYPE_SUPPORT is None:
                _miloc_map_handler.Metaclass_MilocMapHandler_Request.__import_type_support__()
            if _miloc_map_handler.Metaclass_MilocMapHandler_Response._TYPE_SUPPORT is None:
                _miloc_map_handler.Metaclass_MilocMapHandler_Response.__import_type_support__()


class MilocMapHandler(metaclass=Metaclass_MilocMapHandler):
    from cyberdog_visions_interfaces.srv._miloc_map_handler import MilocMapHandler_Request as Request
    from cyberdog_visions_interfaces.srv._miloc_map_handler import MilocMapHandler_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
