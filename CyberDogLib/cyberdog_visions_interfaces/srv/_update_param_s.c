// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from cyberdog_visions_interfaces:srv/UpdateParam.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "cyberdog_visions_interfaces/srv/detail/update_param__struct.h"
#include "cyberdog_visions_interfaces/srv/detail/update_param__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool cyberdog_visions_interfaces__srv__update_param__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[66];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("cyberdog_visions_interfaces.srv._update_param.UpdateParam_Request", full_classname_dest, 65) == 0);
  }
  cyberdog_visions_interfaces__srv__UpdateParam_Request * ros_message = _ros_message;
  {  // map_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "map_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->map_id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * cyberdog_visions_interfaces__srv__update_param__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of UpdateParam_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("cyberdog_visions_interfaces.srv._update_param");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "UpdateParam_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  cyberdog_visions_interfaces__srv__UpdateParam_Request * ros_message = (cyberdog_visions_interfaces__srv__UpdateParam_Request *)raw_ros_message;
  {  // map_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->map_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "map_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "cyberdog_visions_interfaces/srv/detail/update_param__struct.h"
// already included above
// #include "cyberdog_visions_interfaces/srv/detail/update_param__functions.h"

bool cyberdog_visions_interfaces__msg__reply__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * cyberdog_visions_interfaces__msg__reply__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool cyberdog_visions_interfaces__srv__update_param__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[67];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("cyberdog_visions_interfaces.srv._update_param.UpdateParam_Response", full_classname_dest, 66) == 0);
  }
  cyberdog_visions_interfaces__srv__UpdateParam_Response * ros_message = _ros_message;
  {  // reply
    PyObject * field = PyObject_GetAttrString(_pymsg, "reply");
    if (!field) {
      return false;
    }
    if (!cyberdog_visions_interfaces__msg__reply__convert_from_py(field, &ros_message->reply)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * cyberdog_visions_interfaces__srv__update_param__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of UpdateParam_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("cyberdog_visions_interfaces.srv._update_param");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "UpdateParam_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  cyberdog_visions_interfaces__srv__UpdateParam_Response * ros_message = (cyberdog_visions_interfaces__srv__UpdateParam_Response *)raw_ros_message;
  {  // reply
    PyObject * field = NULL;
    field = cyberdog_visions_interfaces__msg__reply__convert_to_py(&ros_message->reply);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "reply", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
