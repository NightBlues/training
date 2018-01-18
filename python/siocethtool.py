import socket
import fcntl
import array
import struct


SIOCETHTOOL = 0x8946
"""
/* for compatibility with glibc net/if.h */
#if __UAPI_DEF_IF_IFREQ
struct ifreq {
#define IFHWADDRLEN     6
        union
        {
                char    ifrn_name[IFNAMSIZ];            /* if name, e.g. "en0" */
        } ifr_ifrn;
        
        union {
                struct  sockaddr ifru_addr;
                struct  sockaddr ifru_dstaddr;
                struct  sockaddr ifru_broadaddr;
                struct  sockaddr ifru_netmask;
                struct  sockaddr ifru_hwaddr;
                short   ifru_flags;
                int     ifru_ivalue;
                int     ifru_mtu;
                struct  ifmap ifru_map;
                char    ifru_slave[IFNAMSIZ];   /* Just fits the size */
                char    ifru_newname[IFNAMSIZ];
                void *  ifru_data;
                struct  if_settings ifru_settings;
        } ifr_ifru;
};
#endif /* __UAPI_DEF_IF_IFREQ */
"""
ETHTOOL_GDRVINFO = 0x00000003
ETHTOOL_GSET = 0x00000001
ETHTOOL_FWVERS_LEN = 32
ETHTOOL_BUSINFO_LEN = 32
"""
struct ethtool_drvinfo {
        __u32   cmd;
        char    driver[32];
        char    version[32];
        char    fw_version[ETHTOOL_FWVERS_LEN];
        char    bus_info[ETHTOOL_BUSINFO_LEN];
        char    erom_version[ETHTOOL_EROMVERS_LEN];
        char    reserved2[12];
        __u32   n_priv_flags;
        __u32   n_stats;
        __u32   testinfo_len;
        __u32   eedump_len;
        __u32   regdump_len;
};
"""
driver_start = 4
driver_end = 4 + 32
bus_info_start = 4 + 32 + 32 + ETHTOOL_FWVERS_LEN
bus_info_end = bus_info_start + ETHTOOL_BUSINFO_LEN

name = 'enp0s31f6'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ecmd = array.array('B', struct.pack('I1020s', ETHTOOL_GDRVINFO, b'\x00'*1020))
ifreq = struct.pack('16sP', name, ecmd.buffer_info()[0])
fcntl.ioctl(sock.fileno(), SIOCETHTOOL, ifreq)
result = ecmd.tostring()
print 'driver: ', result[driver_start:driver_end]
print 'bus_info: ', result[bus_info_start:bus_info_end]
