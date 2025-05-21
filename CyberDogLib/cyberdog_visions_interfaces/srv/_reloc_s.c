// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from cyberdog_visions_interfaces:srv/Reloc.idl
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
#include "cyberdog_visions_interfaces/srv/detail/reloc__struct.h"
#include "cyberdog_visions_interfaces/srv/detail/reloc__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool cyberdog_visions_interfaces__srv__reloc__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[53];
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
    assert(strncmp("cyberdog_visions_interfaces.srv._reloc.Reloc_Request", full_classname_dest, 52) == 0);
  }
  cyberdog_visions_interfaces__srv__Reloc_Request * ros_message = _ros_message;
  {  // reloc_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "reloc_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->reloc_id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * cyberdog_visions_interfaces__srv__reloc__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Reloc_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("cyberdog_visions_interfaces.srv._reloc");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Reloc_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  cyberdog_visions_interfaces__srv__Reloc_Request * ros_message = (cyberdog_visions_interfaces__srv__Reloc_Request *)raw_ros_message;
  {  // reloc_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->reloc_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "reloc_id", field);
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
// #include "cyberdog_visions_interfaces/srv/detail/reloc__struct.h"
// already included above
// #include "cyberdog_visions_interfaces/srv/detail/reloc__functions.h"

bool cyberdog_visions_interfaces__msg__reply__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * cyberdog_visions_interfaces__msg__reply__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool geometry_msgs__msg__pose_stamped__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * geometry_msgs__msg__pose_stamped__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool cyberdog_visions_interfaces__srv__reloc__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[54];
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
    assert(strncmp("cyberdog_visions_interfaces.srv._reloc.Reloc_Response", full_classname_dest, 53) == 0);
  }
  cyberdog_visions_interfaces__srv__Reloc_Response * ros_message = _ros_message;
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
  {  // reloc_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "reloc_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->reloc_id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // is_verified
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_verified");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->is_verified = (Py_True == field);
    Py_DECREF(field);
  }
  {  // confidence
    PyObject * field = PyObject_GetAttrString(_pymsg, "confidence");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->confidence = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pose
    PyObject * field = PyObject_GetAttrString(_pymsg, "pose");
    if (!field) {
      return false;
    }
    if (!geometry_msgs__msg__pose_stamped__convert_from_py(field, &ros_message->pose)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * cyberdog_visions_interfaces__srv__reloc__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Reloc_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("cyberdog_visions_interfaces.srv._reloc");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Reloc_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  cyberdog_visions_interfaces__srv__Reloc_Response * ros_message = (cyberdog_visions_interfaces__srv__Reloc_Response *)raw_ros_message;
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
  {  // reloc_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->reloc_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "reloc_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // is_verified
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->is_verified ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_verified", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // confidence
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->confidence);
    {
      int rc = PyObject_SetAttrString(_pymessage, "confidence", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pose
    PyObject * field = NULL;
    field = geometry_msgs__msg__pose_stamped__convert_to_py(&ros_message->pose);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "pose", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
