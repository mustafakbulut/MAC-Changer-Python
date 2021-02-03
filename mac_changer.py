import subprocess
import optparse
import re
def get_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    (user_interface,arguments)=parse_object.parse_args()
    return (user_interface,arguments)
def get_interface(user_interface):
    interface = user_interface.interface
    return interface
def get_macAddress(user_interface):
    mac_address=user_interface.mac_address
    return mac_address
def mac_change(interface,mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
def new_mac_control(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None
(user_interface, arguments) = get_inputs()
interface=get_interface(user_interface)
mac_address=get_macAddress(user_interface)
mac_change(interface,mac_address)

new_mac=new_mac_control(str(user_interface.interface))
if new_mac==get_macAddress(user_interface):
    print("MAC address is successfully changed!")
else:
    print("MAC address could not change!")
