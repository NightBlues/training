#include <stdio.h>
#include <string.h>

#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <linux/sockios.h>
#include <linux/ethtool.h>

#include <unistd.h>

#include <Python.h>


int get_device_info(const char * devname, struct ethtool_drvinfo * result) {
  struct ifreq ifr;
  struct ethtool_cmd ecmd;
  memset(&ecmd, 0, sizeof(ecmd));
  memset(&ifr, 0, sizeof(ifr));
  strncpy(&ifr.ifr_name[0], devname, IFNAMSIZ);
  ifr.ifr_name[IFNAMSIZ - 1] = 0;
  ifr.ifr_data = (caddr_t) result;
  ecmd.cmd = ETHTOOL_GDRVINFO;
  memcpy(result, &ecmd, sizeof(ecmd));

  int fd = socket(AF_INET, SOCK_DGRAM, 0);
  if(fd < 0) {
    return -1;
  }
  int err = ioctl(fd, SIOCETHTOOL, &ifr);
  if (err < 0) {
    close(fd);
    return -1;
  }

  close(fd);
  return 0;
}


static PyObject * get_info(PyObject * self, PyObject *args) {
  const char * devname;
  if (!PyArg_ParseTuple(args, "s", &devname))
    return NULL;

  struct ethtool_drvinfo result;
  if (get_device_info(devname, &result) < 0) {
    return PyErr_SetFromErrno(PyExc_OSError);
  }

  PyObject * res = PyTuple_New(2);
  PyTuple_SetItem(res, 0, PyString_FromString(result.driver));
  PyTuple_SetItem(res, 1, PyString_FromString(result.bus_info));
  return res;
}


static PyMethodDef EthtoolMethods[] = {
    {"get_info",  get_info, METH_VARARGS,
     "Return driver name and bus-slot number."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC initethtool (void) {
  (void) Py_InitModule("ethtool", EthtoolMethods);
}
