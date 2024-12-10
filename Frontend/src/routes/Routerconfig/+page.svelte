
<script>
  import Interface from '../../lib/components/Router/Interface.svelte';
	import Ospf from '../../lib/components/Router/ospf.svelte';
  import OSPF from '../../lib/components/Router/ospf.svelte';

    let userParameters = 
    [
    {
    "Interface": [
      {
        "interface": "",
        "ip_address": "",
        "subnetmask": "",
        "description": "",
        "shutdown": false,
        "ospf": {
          "area_id": "",
          "cost": "",
          "priority": "",
          "network_type": "",
          "authentication": {
            "key_chain": "",
          }
        }
      }
    ]
  },
  {
    "OSPF": [
      {
        "process_id": "",
        "networks": [
          {
            "network": "",
            "area_id": "",
            "wildcard": ""
          }
        ],
        "router_id": "10.0.0.1",
        "timer_dead": 30,
        "timer_hello": 10,
        "passive_interfaces": [
          "GigabitEthernet0/1",
          "GigabitEthernet0/2"
        ]
      }
    ]
  },
  {
    "Key-Chain": [
      {
        "number": 12,
        "name": "NAME",
        "password": "PASSWORD",
        "ALGO": "hmac-sha-512"
      },
      {
        "number": 112341232,
        "name": "NA1234123ME",
        "password": "PASSWO123412RD",
        "ALGO": "hmac-sha-256"
      }
    ]
  },
  {
    "RIP": {
      "version": 2,
      "auto-summary": true,
      "networks": [
        {
          "network": "10.0.0.0"
        },
        {
          "network": "172.0.0.0"
        }
      ],
      "neighbor": "10.0.0.3",
      "timer_update": 30,
      "passive_interface": [
        "GigabitEthernet0/1",
        "GigabitEthernet0/2"
      ],
      "redistribute": [
        "bgp",
        "ospf"
      ]
    }
  },
  {
    "BGP": {
      "neighbor": [
        {
          "ip_of_neighbor": "192.168.0.1",
          "as": 100,
          "update_source": "Loopback1",
          "next_hop_self": true,
          "route_reflector": true,
          "default_originate": true
        },
        {
          "ip_of_neighbor": "6.6.6.6",
          "as": 1234,
          "update_source": "Loopback1",
          "next_hop_self": true,
          "route_reflector": true,
          "default_originate": true
        }
      ],
      "networks": [
        {
          "network": "10.0.0.0",
          "subnetmask": "0.0.0.255"
        },
        {
          "network": "172.0.0.0",
          "submask": "0.0.0.3"
        }
      ],
      "timer_bgp": 30,
      "hold_time": 180,
      "local_as": 696969
    }
  },
  {
    "Static-Routes": [
      {
        "source": "0.0.0.0",
        "mask": "0.0.0.0",
        "destination": "1.1.1.1",
        "interface": "GigabitEthernet0/0",
        "distance": 1
      }
    ]
  },
  {
    "GRE": [
      {
        "tunnel": "Tunnel0",
        "source": "GigabitEthernet0/0",
        "source_ip": "",
        "destination": "1.2.2.1",
        "ip": "1.1.1.1",
        "subnetmask": "255.255.255.0"
      }
    ]
  },
  {
    "HSRP": [
      {
        "group": 10,
        "version": 2,
        "interface": "GigabitEthernet0/0.1",
        "ip": "1.1.1.1",
        "priority": 10,
        "preempt": true,
        "timers": {
          "hello": 10,
          "hold": 30
        }
      }
    ]
  },
  {
    "DHCP": [
      {
        "pool": "POOL",
        "network": "1.1.1.0",
        "subnetmask": "255.255.255.0",
        "default_router": "1.1.1.1",
        "dns": "as.dasd",
        "exclude": [
          "1.1.1.1"
        ],
        "lease": 10
      },
      {
        "pool": "POOL123123",
        "network": "1.1.1.0",
        "subnetmask": "255.255.255.0",
        "default_router": "1.1.1.1",
        "dns": "as.dasd",
        "exclude": [
          "1.1.1.1"
        ],
        "lease": 10
      }
    ]
  }
]



function addInterface() {
    
    userParameters[0]["Interface"] = [
      ...userParameters[0]["Interface"],
      {
        "interface": "",
        "ip_address": "",
        "subnetmask": "",
        "description": "",
        "shutdown": false,
        "ospf": {
          "area_id": "",
          "cost": "",
          "priority": "",
          "network_type": "",
          "authentication": {
            "key_chain": "",
          }
        }
      }
    ];
  }


  function removeInterface() {
  if (userParameters[0]["Interface"].length > 0) {
    userParameters[0]["Interface"] = userParameters[0]["Interface"].slice(0, -1);
  }
}


function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}


const mappings = {'OSPF': 1, 'Key-Chain': 2, 'RIP': 3, 'BGP': 4, 
'Interface': 0, 'Static-Routes:': 5, 'GRE': 6, 'HSRP': 7, 'DHCP': 8}


</script>

<div class="mainHeading">
<h1>Routerconfig</h1>

<h2 class="subHeading">Interfaces</h2>

{#each range(0, userParameters[mappings['Interface']]['Interface'].length-1) as number}
<Interface id={number} bind:params={userParameters[mappings['Interface']]['Interface'][number]}></Interface>

{/each}
<button class="leftButton" on:click={addInterface}>Add Interface</button>
<button class="rightButton" on:click={removeInterface}>Remove Interface</button>

<h1>OSPF</h1>
<Ospf id=1></Ospf>
</div>