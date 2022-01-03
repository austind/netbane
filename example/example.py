from nornir import InitNornir
from nornir.core.plugins.connections import ConnectionPluginRegister
from nornir.core.plugins.inventory import TransformFunctionRegister
from nornir_utils.plugins.functions import print_result

from netbane.plugins.connections import Netbane
from netbane.plugins.inventory.netbox import netbox_transform
from netbane.plugins.tasks.netbane_get import netbane_get

TransformFunctionRegister.register("netbox_transform", netbox_transform)
ConnectionPluginRegister.register("netbane", Netbane)

nr = InitNornir(config_file="config.yaml")
host = nr.filter(name="SWTC21AC02")

result = host.run(task=netbane_get, getters=["cdp_neighbors"])
print_result(result)
