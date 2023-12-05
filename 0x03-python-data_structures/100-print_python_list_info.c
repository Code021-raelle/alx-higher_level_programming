#include <python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about python list
 * @p: python object
*/

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    printf("Number of elements in the list: %ld\n", size);
    printf("Elements of the list:\n");
    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject* item = PyList_GetItem(p, i);
        printf("Element %ld: ", i+1);
        PyObject_Print(item, stdout, 0);
        printf("\n");
    }
}
