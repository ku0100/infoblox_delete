#! /usr/bin/env python3.6

import urllib3
import requests
from infoblox_client import connector
from infoblox_client import objects
from infoblox_client import object_manager

def deleteNetworks():
    opts = {"host": "infoblox url",
            "username": "username",
            "password": "password"}
    conn = connector.Connector(opts)
    all_networks = conn.get_object("network",
                                {"network~": "XX.XX",
                                "network_view": "default"})
    keep_networks = ["list of networks"]
    remove_networks = []
    remove_shared = []
    add_back_networks = []
    for network in all_networks:
        if network["network"] in keep_networks:
            remove_networks = remove_networks
        else:
            shared_name = network["comment"]
            shared_name = shared_name[:-11]
            remove_shared.append(shared_name)
            remove_networks.append(network["_ref"])
            add_back_networks.append(network)

    for network in remove_shared:
        r = conn.get_object("sharednetwork",
                                {"name": network})

        print(r)

    for network in remove_networks:
        delete = conn.delete_object(network)

    print(remove_shared)

requests.packages.urllib3.disable_warnings() # suprress irrelevant messages to enduser
deleteNetworks()
