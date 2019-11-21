""" The file provides the network ip address, works with py 2 and 3. and need external package """
from netifaces import interfaces, ifaddresses, AF_INET

def get_ip_address(ifname):
    """ Method will provide the ip address for an interface.  """
    try:
        for ifaceName in interfaces():
            if ifaceName == ifname :
                addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
                return addresses[0]

        return 'Unable to find NIC.'

    except:
        return 'Unable to find IP(Execption).'


# Test code.
#ip = get_ip_address('eno1')
#ip = get_ip_address('wlan0')
#print (ip)
