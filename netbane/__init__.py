from napalm import get_network_driver as napalm_get_network_driver
import importlib
import inspect

from napalm.base.base import NetworkDriver

def get_network_driver(name, prepend=True):
    # Look for netbane driver first, then pass on to napalm
    netbane_module = f'netbane.drivers.{name}.{name}'
    try:
        module = importlib.import_module(netbane_module)
    except ImportError as e:
        raise e
    
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, NetworkDriver):
            return obj
    
