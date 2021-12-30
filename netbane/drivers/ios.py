import os
from netbane import config
from napalm.ios.ios import IOSDriver as NapalmIOSDriver

# Netmiko requires this env var when using ntc_templates
os.environ["NET_TEXTFSM"] = config.NTC_TEMPLATES_PATH

def map_cdp_capab(capab_string):
    capab = []
    if 'Host' in capab_string:
        capab.append('station')
    if 'Phone' in capab_string:
        capab.append('telephone')
    if 'Two-port Mac Relay' in capab_string:
        capab.append('bridge')
    if 'Switch' in capab_string:
        capab.append('bridge')
    if 'Router' in capab_string:
        capab.append('router')
    return capab


class IOSDriver(NapalmIOSDriver):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def get_cdp_neighbors(self):
        cdp = {}

        cmd = 'show cdp neighbors detail'
        cdp_entries = self.device.send_command(cmd, use_textfsm=True)
        for cdp_entry in cdp_entries:
            local_intf = cdp_entry['local_port']
            cdp.setdefault(local_intf, [])
            cdp[local_intf].append({
                'remote_system_name': cdp_entry['destination_host'],
                'remote_system_platform': cdp_entry['platform'],
                'remote_management_ip': cdp_entry['management_ip'],
                'remote_software_version': cdp_entry['software_version'],
                'remote_system_capab': map_cdp_capab(cdp_entry['capabilities']),
                'remote_interface': cdp_entry['remote_port'],
            })
        return cdp
