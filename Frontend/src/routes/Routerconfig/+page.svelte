<script>
	import Interface from '../../lib/components/Router/Interface.svelte';
	import Ospf from '../../lib/components/Router/ospf.svelte';
	import KeyChain from '../../lib/components/Router/keyChain.svelte';
	import RIP from '../../lib/components/Router/RIP.svelte';
	import BGP from '../../lib/components/Router/BGP.svelte';
	import Checkbox from '../../lib/components/checkbox.svelte';
	import StaticRoute from '../../lib/components/Router/staticRoute.svelte';
	import GRE from '../../lib/components/Router/GRE.svelte';
	import HsrpGroup from '../../lib/components/Router/HSRPGroup.svelte';
	import DHCPPool from '../../lib/components/Router/DHCPPool.svelte';
	let enableOSPF = false;
	let enableHSRP = false;
	let enableDHCP = false;
	let userParameters = [
		{
			Interface: [
				{
					interface: '',
					ip_address: '',
					subnetmask: '',
					description: '',
					shutdown: false,
					ospf: {
						area_id: '',
						cost: '',
						priority: '',
						network_type: '',
						authentication: {
							key_chain: ''
						}
					}
				}
			]
		},
		{
			OSPF: []
		},
		{
			'Key-Chain': [
				{
					number: '',
					name: '',
					password: '',
					ALGO: ''
				}
			]
		},
		{
			RIP: {
				/*
				version: '',
				'auto-summary': true,
				*/
				networks: [
					{
						network: ''
					}
				],
				/*
				neighbor: '10.0.0.3', 
				timer_update: 30,
				passive_interface: ['']
				redistribute: ['bgp', 'ospf'] 
				*/
				passive_interface: ['']
			}
		},
		{
			BGP: {
				neighbor: [],
				networks: []
			}
		},
		{
			'Static-Routes': [
				{
					source: '',
					mask: '',
					destination: '',
					interface: '',
					distance: ''
				}
			]
		},
		{
			GRE: [
				{
					tunnel: '',
					source: '',
					source_ip: '',
					destination: '',
					ip: '',
					subnetmask: ''
				}
			]
		},
		{
			HSRP: [
				{
					group: '',
					version: '',
					interface: '',
					ip: '',
					priority: '',
					preempt: true,
					timers: {
						hello: '',
						hold: ''
					}
				}
			]
		},
		{
			DHCP: [
				{
					pool: '',
					network: '',
					subnetmask: '',
					default_router: '',
					dns: '',
					exclude: [{ start: '', end: '' }],
					lease: 10
				}
			]
		}
	];

	$: console.log(userParameters)

	function addInterface() {
		userParameters[0]['Interface'] = [
			...userParameters[0]['Interface'],
			{
				interface: '',
				ip_address: '',
				subnetmask: '',
				description: '',
				shutdown: false,
				ospf: {
					area_id: '',
					cost: '',
					priority: '',
					network_type: '',
					authentication: {
						key_chain: ''
					}
				}
			}
		];
	}

	function removeInterface() {
		if (userParameters[0]['Interface'].length > 0) {
			userParameters[0]['Interface'] = userParameters[0]['Interface'].slice(0, -1);
		}
	}

	function addOspfProcess() {
		userParameters[mappings.OSPF]['OSPF'] = [
			...userParameters[mappings.OSPF]['OSPF'],
			{
				process_id: '',
				networks: [
					{
						network: '',
						area_id: '',
						wildcard: ''
					}
				],
				router_id: '',
				timer_dead: 30,
				timer_hello: 10,
				passive_interfaces: ['']
			}
		];
		console.log(userParameters[mappings.OSPF].OSPF);
		console.log(userParameters[mappings.OSPF].OSPF.length);
	}

	function removeOspfProcess() {
		userParameters[mappings.OSPF].OSPF = userParameters[mappings.OSPF].OSPF.slice(0, -1);
	}

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

	function addKeyChain() {
		userParameters[mappings['Key-Chain']]['Key-Chain'] = [
			...userParameters[mappings['Key-Chain']]['Key-Chain'],
			{
				number: '',
				name: '',
				password: '',
				ALGO: ''
			}
		];
	}

	function removeKeyChain() {
		userParameters[mappings['Key-Chain']]['Key-Chain'] = userParameters[mappings['Key-Chain']][
			'Key-Chain'
		].slice(0, -1);
	}

	function addStaticRoute() {
		userParameters[mappings['Static-Routes']]['Static-Routes'] = [
			...userParameters[mappings['Static-Routes']]['Static-Routes'],
			{
				source: '',
				mask: '',
				destination: '',
				interface: '',
				distance: ''
			}
		];
	}

	function removeStaticRoute() {
		userParameters[mappings['Static-Routes']]['Static-Routes'] = userParameters[
			mappings['Static-Routes']
		]['Static-Routes'].slice(0, -1);
	}

	function addGRETunnel() {
		userParameters[mappings['GRE']]['GRE'] = [
			...userParameters[mappings['GRE']]['GRE'],
			{
				tunnel: '',
				source: '',
				source_ip: '',
				destination: '',
				ip: '',
				subnetmask: ''
			}
		];
	}

	function removeGRETunnel() {
		userParameters[mappings['GRE']]['GRE'] = userParameters[mappings['GRE']]['GRE'].slice(0, -1);
	}

	function addHSRPGroup() {
		userParameters[mappings['HSRP']]['HSRP'] = [
			...userParameters[mappings['HSRP']]['HSRP'],
			{
				group: '',
				version: '',
				interface: '',
				ip: '',
				priority: '',
				preempt: true,
				timers: {
					hello: '',
					hold: ''
				}
			}
		];
	}

	function removeHSRPGroup() {
		userParameters[mappings['HSRP']]['HSRP'] = userParameters[mappings['HSRP']]['HSRP'].slice(
			0,
			-1
		);
	}

	function addDHCPPool() {
		userParameters[mappings['DHCP']]['DHCP'] = [
			...userParameters[mappings['DHCP']]['DHCP'],
			{
				pool: '',
				network: '',
				subnetmask: '',
				default_router: '',
				dns: '',
				exclude: [{ start: '', end: '' }],
				lease: 10
			}
		];
	}

	function removeDHCPPool() {
		userParameters[mappings['DHCP']]['DHCP'] = userParameters[mappings['DHCP']]['DHCP'].slice(
			0,
			-1
		);
	}

	const mappings = {
		OSPF: 1,
		'Key-Chain': 2,
		RIP: 3,
		BGP: 4,
		Interface: 0,
		'Static-Routes': 5,
		GRE: 6,
		HSRP: 7,
		DHCP: 8
	};
</script>

<div class="mainHeading">
	<h1>Routerconfig</h1>

	<h2 class="subHeading">Interfaces</h2>

	{#each range(0, userParameters[mappings['Interface']]['Interface'].length - 1) as number}
		<Interface id={number} bind:params={userParameters[mappings['Interface']]['Interface'][number]}
		></Interface>
	{/each}
	<button class="leftButton" on:click={addInterface}>Add Interface</button>
	<button class="rightButton" on:click={removeInterface}>Remove Interface</button>

	<h1 class="subHeading">Key-Chains</h1>

	{#each range(0, userParameters[mappings['Key-Chain']]['Key-Chain'].length - 1) as number}
		<KeyChain id={number} bind:params={userParameters[mappings['Key-Chain']]['Key-Chain'][number]}
		></KeyChain>
	{/each}

	<button class="leftButton" on:click={addKeyChain}>Add Key-Chain</button>
	<button class="rightButton" on:click={removeKeyChain}>Remove Key-Chain</button>

	<h1 class="subHeading">OSPF</h1>

	<Checkbox name="enableOSPF{1}" Heading="Enable OSPF" bind:isChecked={enableOSPF} />
	{#if enableOSPF}
		{#each range(0, userParameters[mappings.OSPF].OSPF.length - 1) as number}
			<Ospf id={number} bind:params={userParameters[mappings.OSPF]['OSPF'][number]}></Ospf>
		{/each}
		<button class="leftButton" on:click={addOspfProcess}>Add OSPF Process</button>
		<button class="rightButton" on:click={removeOspfProcess}>Remove OSPF Process</button>
	{/if}

	<h2 class="subHeading">RIP</h2>
	<RIP id="1" bind:params={userParameters[mappings.RIP].RIP}></RIP>
	<h2 class="subHeading">BGP</h2>
	<BGP id="1" bind:params={userParameters[mappings.BGP].BGP}></BGP>

	<h2 class="subHeading">Static Routes</h2>
	{#each range(0, userParameters[mappings['Static-Routes']]['Static-Routes'].length - 1) as route, i}
		<h2 class="subSubHeading">Route {i + 1}</h2>
		<StaticRoute id={i} bind:params={userParameters[mappings['Static-Routes']]['Static-Routes'][i]}
		></StaticRoute>
	{/each}

	<button class="leftButton" on:click={addStaticRoute}>Add Static-Route</button>
	<button class="rightButton" on:click={removeStaticRoute}>Remove Static-Route</button>

	<h2 class="subHeading">GRE-Tunnels</h2>
	{#each range(0, userParameters[mappings.GRE].GRE.length - 1) as number}
		<h2 class="subSubHeading">Tunnel {number + 1}</h2>
		<GRE id={number} bind:params={userParameters[mappings.GRE].GRE[number]}></GRE>
	{/each}

	<button class="leftButton" on:click={addGRETunnel}>Add GRE-Tunnel</button>
	<button class="rightButton" on:click={removeGRETunnel}>Remove GRE-Tunnel</button>

	<h2 class="subHeading">HSRP</h2>
	<Checkbox name="enableHSRP{1}" Heading="Enable HSRP" bind:isChecked={enableHSRP} />
	{#if enableHSRP}
		{#each range(0, userParameters[mappings.HSRP].HSRP.length - 1) as number}
			<h2 class="subSubHeading">HSRP-Group {number + 1}</h2>
			<HsrpGroup id={number} bind:params={userParameters[mappings.HSRP].HSRP[number]}></HsrpGroup>
		{/each}
		<button class="leftButton" on:click={addHSRPGroup}>Add HSRP-Group</button>
		<button class="rightButton" on:click={removeHSRPGroup}>Remove HSRP-Group</button>
	{/if}

	<h2 class="subHeading">DHCP</h2>
	<Checkbox name="enableDHCP{1}" Heading="Enable DHCP" bind:isChecked={enableDHCP} />
	{#if enableDHCP}
		{#each range(0, userParameters[mappings.DHCP].DHCP.length - 1) as number}
			<DHCPPool id={number} bind:params={userParameters[mappings.DHCP].DHCP[number]}></DHCPPool>
		{/each}
		<button class="leftButton" on:click={addDHCPPool}>Add DHCP-Pool</button>
		<button class="rightButton" on:click={removeDHCPPool}>Remove DHCP-Pool</button>
	{/if}


</div>
