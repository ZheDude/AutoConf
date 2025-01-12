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
	import InputField from '../../lib/components/inputField.svelte';
	import SshCredentials from '../../lib/components/sshCredentials.svelte';
	import { beforeNavigate } from '$app/navigation';
	import { onMount } from 'svelte';
	let enableOSPF = false;
	let enableHSRP = false;
	let enableDHCP = false;
	let enableRIP = false;
	let enableBGP = false;
	let enableConnectivityCheck = false;
	let enableCheck = false;

	/*
	function saveToLocalStorage() {
		localStorage.setItem('RouterParams', JSON.stringify(userParameters));
	}

	beforeNavigate(() => {
		saveToLocalStorage();
	});

	onMount(() => {
		const savedParams = localStorage.getItem('RouterParams');
		if (savedParams) {
			userParameters = JSON.parse(savedParams);
		}
	});
	*/
	let userParameters = [
		{
			Interface: [
				{
					interface: '',
					ip_address: '',
					subnetmask: '',
					description: '',
					shutdown: false
				}
			]
		},
		{
			OSPF: []
		},
		{
			'Key-Chain': []
		},
		{
			RIP: {}
		},
		{
			BGP: {}
		},
		{
			'Static-Routes': []
		},
		{
			GRE: []
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
					exclude: [],
					'exclude-range': [{ start: '', end: '' }],
					lease: 10
				}
			]
		},
		{
			SSH: {
				ip: '',
				username: '',
				password: ''
			}
		}
	];

	let cssClasses = [
		{
			Interface: [
				{
					interface: 'correct',
					ip_address: 'correct',
					subnetmask: 'correct',
					description: 'correct'
				}
			]
		},
		{
			OSPF: []
		},
		{
			'Key-Chain': []
		},
		{
			RIP: {}
		},
		{
			BGP: {}
		},
		{
			'Static-Routes': []
		},
		{
			GRE: []
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
					exclude: [],
					'exclude-range': [{ start: '', end: '' }],
					lease: 10
				}
			]
		},
		{
			SSH: {}
		}
	];
	$: console.log(userParameters);
	$: console.log(userParameters);

	function addInterface() {
		userParameters[mappings['Interface']]['Interface'] = [
			...userParameters[mappings['Interface']]['Interface'],
			{
				interface: '',
				ip_address: '',
				subnetmask: '',
				description: '',
				shutdown: false
			}
		];

		cssClasses[mappings['Interface']]['Interface'] = [
			...userParameters[mappings['Interface']]['Interface'],
			{
				interface: 'correct',
				ip_address: 'correct',
				subnetmask: 'correct',
				description: 'correct'
			}
		];
	}

	function removeInterface() {
		userParameters[mappings['Interface']]['Interface'] = userParameters[0]['Interface'].slice(
			0,
			-1
		);
		cssClasses[mappings['Interface']['Interface']] = cssClasses[
			mappings['Interface']['Interface']
		].slice(0, -1);
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
				timer_dead: '30',
				timer_hello: '10',
				passive_interfaces: ['']
			}
		];

		cssClasses[mappings.OSPF]['OSPF'] = [
			...userParameters[mappings.OSPF]['OSPF'],
			{
				process_id: 'correct',
				networks: [
					{
						network: 'correct',
						area_id: 'correct',
						wildcard: 'correct'
					}
				],
				router_id: 'correct',
				timer_dead: 'correct',
				timer_hello: 'correct',
				passive_interfaces: ['correct']
			}
		];
	}

	function removeOspfProcess() {
		if (!enableOSPF) {
			userParameters[mappings.OSPF].OSPF = [];
		} else {
			userParameters[mappings.OSPF].OSPF = userParameters[mappings.OSPF].OSPF.slice(0, -1);
			cssClasses[mappings.OSPF].OSPF = cssClasses[mappings.OSPF].OSPF.slice(0, -1);

			if (userParameters[mappings.OSPF].OSPF.length == 0) {
				enableOSPF = false;
			}
		}
	}

	$: {
		if (enableOSPF) {
			addOspfProcess();
		}

		if (!enableOSPF) {
			removeOspfProcess();
		}

		if (enableRIP) {
			userParameters[mappings.RIP].RIP = {
				version: 2,
				'auto-summary': true,
				networks: [
					{
						network: ''
					}
				],
				timer_update: '30'
			};

			cssClasses[mappings.RIP].RIP = {
				version: 2,
				'auto-summary': true,
				networks: [
					{
						network: ''
					}
				],
				timer_update: '30'
			};
		}

		if (!enableRIP) {
			userParameters[mappings.RIP].RIP = {};

			cssClasses[mappings.RIP].RIP = {};
		}

		if (enableBGP) {
			userParameters[mappings.BGP].BGP = {
				neighbor: [
					{
						ip_of_neighbor: '',
						as: '',
						update_source: '',
						next_hop_self: false,
						route_reflector: false,
						default_originate: false
					}
				],
				networks: [
					{
						network: '',
						subnetmask: ''
					}
				],
				timer_bgp: '30',
				hold_time: '180',
				local_as: '100'
			};

			cssClasses[mappings.BGP].BGP = {
				neighbor: [
					{
						ip_of_neighbor: 'correct',
						as: 'correct',
						update_source: 'correct'
					}
				],
				networks: [
					{
						network: 'correct',
						subnetmask: 'correct'
					}
				],
				timer_bgp: 'correct',
				hold_time: 'correct',
				local_as: 'correct'
			};
		}

		if (!enableBGP) {
			userParameters[mappings.BGP].BGP = {};
			cssClasses[mappings.BGP].BGP = {};
		}
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
				ALGO: 'sha-512'
			}
		];

		cssClasses[mappings['Key-Chain']]['Key-Chain'] = [
			...cssClasses[mappings['Key-Chain']]['Key-Chain'],
			{
				number: 'correct',
				name: 'correct',
				password: 'correct'
			}
		];
	}

	function removeKeyChain() {
		userParameters[mappings['Key-Chain']]['Key-Chain'] = userParameters[mappings['Key-Chain']][
			'Key-Chain'
		].slice(0, -1);
		cssClasses[mappings['Key-Chain']]['Key-Chain'] = userParameters[mappings['Key-Chain']][
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
				distance: '1'
			}
		];

		cssClasses[mappings['Static-Routes']]['Static-Routes'] = [
			...cssClasses[mappings['Static-Routes']]['Static-Routes'],
			{
				source: 'correct',
				mask: 'correct',
				destination: 'correct',
				interface: 'correct',
				distance: 'correct'
			}
		];
	}

	function removeStaticRoute() {
		userParameters[mappings['Static-Routes']]['Static-Routes'] = userParameters[
			mappings['Static-Routes']
		]['Static-Routes'].slice(0, -1);

		cssClasses[mappings['Static-Routes']]['Static-Routes'] = cssClasses[
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
				exclude: [],
				'exclude-range': [],
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
		DHCP: 8,
		SSH: 9
	};

	async function checkConnectivity() {
		enableConnectivityCheck = true;
		let postData = { userParameter: userParameters[mappings['SSH']].SSH };
		const response = await fetch('/api/checkConnectivity/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(postData)
		});
		let data = await response.json();
		cssClasses[mappings['SSH']].SSH = data;
	}

	async function checkUserParameter() {
		enableCheck = true;
		checkConnectivity();

		let postData = { userParameter: userParameters, cssClasses: cssClasses };
		const response = await fetch('/api/parameterChecks/Routerconfig', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(postData)
		});
		let data = await response.json();
		cssClasses = data.cssClasses;
		/*
		if(data.isCorrect && userParameters[mappings['SSH']].SSH){
			sendData()
		}
		*/
	}
	async function sendData() {
		console.log('sending data');
		let postData = JSON.stringify(userParameters);
		const response = await fetch('/api/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: postData
		});
		let ApiData = await response.json();

		return true;
	}
</script>

<div id="parameterDivGrundkonfig">
	<div class="mainHeading">
		<h1>Routerconfig</h1>
	</div>

	<SshCredentials
		cssClasses={cssClasses[mappings['SSH']].SSH}
		connectivityCheck={enableConnectivityCheck}
		bind:params={userParameters[mappings['SSH']].SSH}
	></SshCredentials>

	<button class="generateSkriptButton" on:click={checkConnectivity}> Check Connectivity</button>

	<h2 class="subHeading" id="Interfaces">Interfaces</h2>

	{#each range(0, userParameters[mappings['Interface']]['Interface'].length - 1) as number}
		<Interface
			check={enableCheck}
			cssClasses={cssClasses[mappings['Interface']]['Interface'][number]}
			id={number}
			bind:params={userParameters[mappings['Interface']]['Interface'][number]}
		></Interface>
	{/each}
	<button class="leftButton" on:click={addInterface}>Add Interface</button>
	<button class="rightButton" on:click={removeInterface}>Remove Interface</button>

	<h1 class="subHeading" id="Key-Chains">Key-Chains</h1>

	{#each range(0, userParameters[mappings['Key-Chain']]['Key-Chain'].length - 1) as number}
		<h1 class="subSubHeading">Key Chain {number}</h1>
		<KeyChain
			id={number}
			check={enableCheck}
			cssClasses={cssClasses[mappings['Key-Chain']]['Key-Chain'][number]}
			bind:params={userParameters[mappings['Key-Chain']]['Key-Chain'][number]}
		></KeyChain>
	{/each}

	<button class="leftButton" on:click={addKeyChain}>Add Key-Chain</button>
	<button class="rightButton" on:click={removeKeyChain}>Remove Key-Chain</button>

	<h1 class="subHeading" id="OSPF">OSPF</h1>

	<Checkbox name="enableOSPF{1}" Heading="Enable OSPF" bind:isChecked={enableOSPF} />
	{#if enableOSPF}
		{#each range(0, userParameters[mappings.OSPF].OSPF.length - 1) as number}
			<Ospf
				check={enableCheck}
				cssClasses={cssClasses[mappings.OSPF]['OSPF'][number]}
				id={number}
				bind:params={userParameters[mappings.OSPF]['OSPF'][number]}
			></Ospf>
		{/each}
		<br />
		<button class="leftButton" on:click={addOspfProcess}>Add OSPF Process</button>
		<button class="rightButton" on:click={removeOspfProcess}>Remove OSPF Process</button>
	{/if}

	<h2 class="subHeading" id="RIP">RIP</h2>
	<Checkbox name="enableRIP" Heading="Enable RIP" bind:isChecked={enableRIP} />

	{#if enableRIP}
		<RIP
			id="1"
			check={enableCheck}
			cssClasses={cssClasses[mappings.RIP].RIP}
			bind:params={userParameters[mappings.RIP].RIP}
		></RIP>
	{/if}
	<h2 class="subHeading" id="BGP">BGP</h2>
	<Checkbox name="enableBGP" Heading="Enable BGP" bind:isChecked={enableBGP} />
	{#if enableBGP}
		<BGP id="1" check={enableCheck} cssClasses={cssClasses[mappings.BGP].BGP} bind:params={userParameters[mappings.BGP].BGP}></BGP>
	{/if}

	<h2 class="subHeading" id="StaticRoutes">Static Routes</h2>
	{#each range(0, userParameters[mappings['Static-Routes']]['Static-Routes'].length - 1) as route, i}
		<h2 class="subSubHeading">Route {i + 1}</h2>
		<StaticRoute id={i} check={enableCheck} cssClasses={cssClasses[mappings['Static-Routes']]['Static-Routes'][i]} bind:params={userParameters[mappings['Static-Routes']]['Static-Routes'][i]}
		></StaticRoute>
	{/each}

	<button class="leftButton" on:click={addStaticRoute}>Add Static-Route</button>
	<button class="rightButton" on:click={removeStaticRoute}>Remove Static-Route</button>

	<h2 class="subHeading" id="GRE-Tunnels">GRE-Tunnels</h2>
	{#each range(0, userParameters[mappings.GRE].GRE.length - 1) as number}
		<h2 class="subSubHeading">Tunnel {number + 1}</h2>
		<GRE id={number} bind:params={userParameters[mappings.GRE].GRE[number]}></GRE>
	{/each}

	<button class="leftButton" on:click={addGRETunnel}>Add GRE-Tunnel</button>
	<button class="rightButton" on:click={removeGRETunnel}>Remove GRE-Tunnel</button>

	<h2 class="subHeading" id="HSRP">HSRP</h2>
	<Checkbox name="enableHSRP{1}" Heading="Enable HSRP" bind:isChecked={enableHSRP} />
	{#if enableHSRP}
		{#each range(0, userParameters[mappings.HSRP].HSRP.length - 1) as number}
			<h2 class="subSubHeading">HSRP-Group {number + 1}</h2>
			<HsrpGroup id={number} bind:params={userParameters[mappings.HSRP].HSRP[number]}></HsrpGroup>
		{/each}
		<button class="leftButton" on:click={addHSRPGroup}>Add HSRP-Group</button>
		<button class="rightButton" on:click={removeHSRPGroup}>Remove HSRP-Group</button>
	{/if}

	<h2 class="subHeading" id="DHCP">DHCP</h2>
	<Checkbox name="enableDHCP{1}" Heading="Enable DHCP" bind:isChecked={enableDHCP} />
	{#if enableDHCP}
		{#each range(0, userParameters[mappings.DHCP].DHCP.length - 1) as number}
			<DHCPPool id={number} bind:params={userParameters[mappings.DHCP].DHCP[number]}></DHCPPool>
		{/each}
		<button class="leftButton" on:click={addDHCPPool}>Add DHCP-Pool</button>
		<button class="rightButton" on:click={removeDHCPPool}>Remove DHCP-Pool</button>
	{/if}

	<button class="generateSkriptButton" id="Submit" on:click={checkUserParameter}> Submit</button>
	<button class="generateSkriptButton" on:click={checkUserParameter}> Show Script</button>
</div>
