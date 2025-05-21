// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from cyberdog_visions_interfaces:msg/RangeData.idl
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
#include "cyberdog_visions_interfaces/msg/detail/range_data__struct.h"
#include "cyberdog_visions_interfaces/msg/detail/range_data__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "cyberdog_visions_interfaces/msg/detail/vector2f__functions.h"
// end nested array functions include
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);
bool cyberdog_visions_interfaces__msg__vector2f__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * cyberdog_visions_interfaces__msg__vector2f__convert_to_py(void * raw_ros_message);
bool cyberdog_visions_interfaces__msg__vector2f__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * cyberdog_visions_interfaces__msg__vector2f__convert_to_py(void * raw_ros_message);
bool cyberdog_visions_interfaces__msg__vector2f__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * cyberdog_visions_interfaces__msg__vector2f__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool cyberdog_visions_interfaces__msg__range_data__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("cyberdog_visions_interfaces.msg._range_data.RangeData", full_classname_dest, 53) == 0);
  }
  cyberdog_visions_interfaces__msg__RangeData * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // origin
    PyObject * field = PyObject_GetAttrString(_pymsg, "origin");
    if (!field) {
      return false;
    }
    if (!cyberdog_visions_interfaces__msg__vector2f__convert_from_py(field, &ros_message->origin)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // returns
    PyObject * field = PyObject_GetAttrString(_pymsg, "returns");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'returns'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    if (!cyberdog_visions_interfaces__msg__Vector2f__Sequence__init(&(ros_message->returns), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create cyberdog_visions_interfaces__msg__Vector2f__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    cyberdog_visions_interfaces__msg__Vector2f * dest = ros_message->returns.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!cyberdog_visions_interfaces__msg__vector2f__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // misses
    PyObject * field = PyObject_GetAttrString(_pymsg, "misses");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'misses'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    if (!cyberdog_visions_interfaces__msg__Vector2f__Sequence__init(&(ros_message->misses), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create cyberdog_visions_interfaces__msg__Vector2f__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    cyberdog_visions_interfaces__msg__Vector2f * dest = ros_message->misses.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!cyberdog_visions_interfaces__msg__vector2f__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * cyberdog_visions_interfaces__msg__range_data__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of RangeData */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("cyberdog_visions_interfaces.msg._range_data");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "RangeData");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  cyberdog_visions_interfaces__msg__RangeData * ros_message = (cyberdog_visions_interfaces__msg__RangeData *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // origin
    PyObject * field = NULL;
    field = cyberdog_visions_interfaces__msg__vector2f__convert_to_py(&ros_message->origin);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "origin", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // returns
    PyObject * field = NULL;
    size_t size = ros_message->returns.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    cyberdog_visions_interfaces__msg__Vector2f * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->returns.data[i]);
      PyObject * pyitem = cyberdog_visions_interfaces__msg__vector2f__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "returns", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // misses
    PyObject * field = NULL;
    size_t size = ros_message->misses.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    cyberdog_visions_interfaces__msg__Vector2f * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->misses.data[i]);
      PyObject * pyitem = cyberdog_visions_interfaces__msg__vector2f__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "misses", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
