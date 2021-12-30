from netbane import config
from netbane.drivers.ios import IOSDriver
import ipdb
from copy import copy
from pprint import pprint

args = copy(config.NAPALM_ARGS)
args.update({'hostname': '172.18.13.129'})
device = IOSDriver(**args)
device.open()
pprint(device.get_cdp_neighbors())
device.close()
#ipdb.set_trace()
