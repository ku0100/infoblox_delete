#! /usr/bin/env python3.6

import requests
from infoblox_client import connector
from infoblox_client import objects

def deleteNetwork():
    delete_url = "wapi_url"
    wapi_url = "wapi_url/network?network~=XX.XX"
    networks = requests.get(wapi_url,
                            auth=("username", "password"),
                            verify=False)
    all_networks = networks.json()
    print(all_networks)
    all_networks = networks.json()
    for network in all_networks:
        url = delete_url + str(network["_ref"])
        print(url)
        deletion = requests.delete(url,
                                    auth=("username", "password"),
                                    verify=False)

deleteNetwork()