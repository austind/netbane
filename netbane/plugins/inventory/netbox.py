from nornir.core.inventory import Host


def netbox_transform(host: Host) -> None:
    # store raw netbox data in separate key in case we want it later
    host.data["netbox"] = host.data
    netbox = host.data["netbox"]
    host.data["site"] = netbox["site"]["slug"].lower()
