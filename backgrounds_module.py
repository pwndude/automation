# use WMI library
import wmi

# prints all properties
wmi.WMI().Win32_Process.properties.keys()

# prints all methods
wmi.WMI().Win32_Process.methods.keys()

