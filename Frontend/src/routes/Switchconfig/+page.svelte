<script>
	import '$lib/stylesheet.css';
	import InputField from '../../lib/components/inputField.svelte';
	import Dropdown from '../../lib/components/dropdown.svelte';
	import Checkbox from '../../lib/components/checkbox.svelte';
	import VLAN from '../../lib/components/Switch/vlan.svelte';
	import TrunkInterface from '../../lib/components/Switch/trunk-interface.svelte';
	import Etherchannel from '../../lib/components/Switch/etherchannel.svelte';
	import AccessInterface from '../../lib/components/Switch/access-interface.svelte';
	import StpProcess from '../../lib/components/Switch/stp-process.svelte';
	import PortSecurityInterface from '../../lib/components/Switch/Port-Security-Interface.svelte';
	import { onMount } from 'svelte';
	import { beforeNavigate } from '$app/navigation';
	import { afterNavigate } from '$app/navigation';
	import EdgeInterfaces from '../../lib/components/Switch/edgeInterfaces.svelte';
	import SshCredentials from '../../lib/components/sshCredentials.svelte';

	/* Flags*/

	let enableCheck; /* set to True if the submit button is pressed*/
	let enableConnectivityCheck = false; /* set to True when a connectivity check is performed */
	let enableVTP = false; /* set to true when VTP is enabled */
	let generate = false;
	let showError = false;




	function resetInputs() {
		generate = false;
		showError = false;
		enableConnectivityCheck = false;
		cssClasses = {
			SSH: {},
			VTP: [],
			VLAN: [],
			STP: [],
			EdgePorts: {
				Interfaces: [],
				InterfaceRanges: []
			},
			Trunks: {
				Interfaces: [],
				InterfaceRanges: []
			},
			AccessInterfaces: {
				Interfaces: [],
				InterfaceRanges: []
			},
			Portsecurity: [],
			EtherChannels: []
		};

		userParameter = {
			SSH: {
				ip: '',
				username: '',
				password: ''
			},
			VTP: [],
			VLAN: [],
			STP: [],
			EdgePorts: {
				Interfaces: [],
				InterfaceRanges: []
			},
			Trunks: {
				Interfaces: [],
				InterfaceRanges: []
			},
			AccessInterfaces: {
				Interfaces: [],
				InterfaceRanges: []
			},
			Portsecurity: [],
			EtherChannels: []
		};
	}

	function saveToLocalStorage() {
		localStorage.setItem('SwitchParams', JSON.stringify(userParameter));
	}


	beforeNavigate(() => {
		saveToLocalStorage();
	
	});

	afterNavigate(() => {
		const savedParams = localStorage.getItem('SwitchParams');
		if (savedParams) {
			userParameter = JSON.parse(savedParams);
		}
	})
	onMount(() => {
		const savedParams = localStorage.getItem('SwitchParams');
		if (savedParams) {
			userParameter = JSON.parse(savedParams);
		}
	});


	let userParameter = {
		SSH: {
			ip: '',
			username: '',
			password: ''
		},
		VTP: [],
		VLAN: [],
		STP: [],
		EdgePorts: {
			Interfaces: [],
			InterfaceRanges: []
		},
		Trunks: {
			Interfaces: [],
			InterfaceRanges: []
		},
		AccessInterfaces: {
			Interfaces: [],
			InterfaceRanges: []
		},
		Portsecurity: [],
		EtherChannels: []
	};

	let cssClasses = {
		SSH: {},
		VTP: [],
		VLAN: [],
		STP: [],
		EdgePorts: {
			Interfaces: [],
			InterfaceRanges: []
		},
		Trunks: {
			Interfaces: [],
			InterfaceRanges: []
		},
		AccessInterfaces: {
			Interfaces: [],
			InterfaceRanges: []
		},
		Portsecurity: [],
		EtherChannels: []
	};

	function formatAPIData(data) {
		return [
			{
				SSH: {
					ip: data.SSH.ip || '',
					username: data.SSH.username || '',
					password: data.SSH.password || ''
				}
			},
			{
				VTP: data.VTP.map((vtp) => ({
					version: vtp.version || '',
					mode: vtp.mode || '',
					domain: vtp.domain || '',
					password: vtp.password || '',
					pruning: vtp.pruning || '',
					is_primary: vtp.is_primary || '',
					vlan: vtp.vlan || ''
				}))
			},
			{
				VLAN: data.VLAN.map((vlan) => ({
					name: vlan.name || '',
					number: vlan.number || ''
				}))
			},
			{
				STP: data.STP.map((stp) => ({
					mode: stp.mode || '',
					priority: stp.priority || '',
					hello_timer: stp.hello_timer || '',
					max_age: stp.max_age || '',
					vlan: stp.vlan.split(',') || [],
					forward_timer: stp.forward_timer || ''
				}))
			},
			{
				EdgePorts: {
					Interfaces: data.EdgePorts.Interfaces.map((interfaceItem) => ({
						name: interfaceItem.name || '',
						portfast: interfaceItem.portfast || '',
						bpduguard: interfaceItem.bpduguard || ''
					})),
					InterfaceRanges: data.EdgePorts.InterfaceRanges.map((range) => ({
						startInterface: range.startInterface || '',
						endInterface: range.endInterface || '',
						portfaste: range.portfaste || '',
						bpduguard: range.bpduguard || ''
					}))
				}
			},
			{
				Trunks: {
					Interfaces: data.Trunks.Interfaces.map((interfaceItem) => ({
						name: interfaceItem.name || '',
						allowed_vlan: interfaceItem.allowed_vlan || '',
						native_vlan: interfaceItem.native_vlan || '',
						encapsulation: interfaceItem.encapsulation || '',
						mode: interfaceItem.mode || '',
						shutdown: interfaceItem.shutdown || ''
					})),
					InterfaceRanges: data.Trunks.InterfaceRanges.map((range) => ({
						startInterface: range.startInterface || '',
						endInterface: range.endInterface || '',
						allowed_vlan: range.allowed_vlan || '',
						native_vlan: range.native_vlan || '',
						encapsulation: range.encapsulation || '',
						mode: range.mode || '',
						shutdown: range.shutdown || ''
					}))
				}
			},
			{
				AccessInterfaces: {
					Interfaces: data.AccessInterfaces.Interfaces.map((interfaceItem) => ({
						name: interfaceItem.name || '',
						allowed_vlan: interfaceItem.allowed_vlan || '',
						native_vlan: interfaceItem.native_vlan || '',
						encapsulation: interfaceItem.encapsulation || '',
						mode: interfaceItem.mode || '',
						shutdown: interfaceItem.shutdown || '',
						vlan: interfaceItem.vlan || ''
					})),
					InterfaceRanges: data.AccessInterfaces.InterfaceRanges.map((range) => ({
						startInterface: range.startInterface || '',
						endInterface: range.endInterface || '',
						allowed_vlan: range.allowed_vlan || '',
						native_vlan: range.native_vlan || '',
						encapsulation: range.encapsulation || '',
						mode: range.mode || '',
						shutdown: range.shutdown || '',
						vlan: range.vlan || ''
					}))
				}
			},
			{
				Portsecurity: data.Portsecurity.map((item) => ({
					interface: item.interface || '',
					maximum: item.maximum || '',
					violation: item.violation || '',
					mac_address: item.mac_address || ''
				}))
			},
			{
				EtherChannels: data.EtherChannels.map((channel) => ({
					Interfaces: channel.Interfaces.map((interfaceItem) => ({
						name: interfaceItem.name || ''
					})),
					InterfaceRanges: channel.InterfaceRanges.map((range) => ({
						startInterface: range.startInterface || '',
						endInterface: range.endInterface || ''
					})),
					mode: channel.mode || '',
					number: channel.number || ''
				}))
			}
		];
	}

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

	function addVLAN() {
		userParameter.VLAN = [...userParameter.VLAN, { name: '', number: '' }];
		cssClasses.VLAN = [...cssClasses.VLAN, { name: 'correct', number: 'correct' }];
	}

	function removeVLAN() {
		if (userParameter.VLAN.length != 0) {
			userParameter.VLAN = userParameter.VLAN.slice(0, -1);
			cssClasses.VLAN = cssClasses.VLAN.slice(0, -1);
		}
	}

	function addSTPProcess() {
		userParameter.STP = [
			...userParameter.STP,
			{
				mode: 'Rapid-PVST',
				priority: '32768',
				hello_timer: '2',
				forward_timer: '15',
				max_age: '20',
				vlan: ''
			}
		];

		cssClasses.STP = [
			...cssClasses.STP,
			{
				priority: 'correct',
				hello_timer: 'correct',
				forward_timer: 'correct',
				max_age: 'correct',
				vlan: 'correct'
			}
		];
	}

	function removeSTPProcess() {
		if (userParameter.STP.length != 0) {
			userParameter.STP = userParameter.STP.slice(0, -1);
			cssClasses.STP = cssClasses.STP.slice(0, -1);
		}
	}

	function addPortSecurityInterface() {
		userParameter.Portsecurity = [
			...userParameter.Portsecurity,
			{
				interface: '',
				maximum: '',
				violation: 'Shutdown',
				mac_address: ''
			}
		];

		cssClasses.Portsecurity = [
			...cssClasses.Portsecurity,
			{
				interface: 'correct',
				maximum: 'correct',
				mac_address: 'correct'
			}
		];
	}

	function removePortSecurityInterface() {
		userParameter.Portsecurity = userParameter.Portsecurity.slice(0, -1);
		cssClasses.Portsecurity = cssClasses.Portsecurity.slice(0, -1);
	}

	function addEtherChannel() {
		userParameter.EtherChannels = [
			...userParameter.EtherChannels,
			{
				Interfaces: [],
				InterfaceRanges: [],
				mode: 'on',
				number: ''
			}
		];

		cssClasses.EtherChannels = [ ...cssClasses.EtherChannels, {
				Interfaces: [],
				InterfaceRanges: [],
				number: 'correct'
			}]
	}

	function removeEtherChannel() {
		if (userParameter.EtherChannels.length != 0) {
			userParameter.EtherChannels = userParameter.EtherChannels.slice(0, -1);
		}
	}

	$: {
		if (enableVTP) {
			userParameter.VTP = [
				{
					enabled: false,
					mode: 'Server',
					domain: '',
					password: '',
					pruning: true,
					is_primary: false
				}
			];

			cssClasses.VTP = [
				{
					domain: 'correct',
					password: 'correct'
				}
			];
		} else {
			cssClasses.VTP = [];
			userParameter.VTP = [];
		}
	}

	async function checkConectivity() {
		generate = false;
		showError = false;
		enableConnectivityCheck = true;
		let postData = { userParameter: userParameter['SSH'] };
		const response = await fetch('/api/checkConnectivity/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(postData)
		});
		let data = await response.json();
		cssClasses.SSH = data;


		return new Response("", {
        headers: {
            'Content-Type': 'application/json'
        }
    });
	}

	async function checkUserParameter() {
		enableCheck = true;
		await checkConectivity();

		let postData = { userParameter: userParameter, cssClasses: cssClasses };
		const response = await fetch('/api/parameterChecks/Switchconfig', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(postData)
		});
		let data = await response.json();
		cssClasses = data.cssClasses;
		console.log(cssClasses.SSH.isReachable)
		if(data.isCorrect && cssClasses.SSH.isReachable){
			 showError = false;
			 generate = true;
			sendData()
		}else{
			console.log("soos")
			showError = true;
			generate = false;
		}


	}
	async function sendData() {
		console.log('sending data')
		let postData = JSON.stringify(formatAPIData(userParameter));
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
		<h1>Switchconfig</h1>
	</div>

	<SshCredentials
		cssClasses={cssClasses.SSH}
		connectivityCheck={enableConnectivityCheck}
		bind:params={userParameter.SSH}
	></SshCredentials>
	<button class="generateSkriptButton" on:click={checkConectivity}> Check Connectivity</button>
	<h2 class="subHeading" id="VTP">VTP</h2>
	<Checkbox name="enableVTP" bind:isChecked={enableVTP} Heading="Enable VTP"></Checkbox>
	{#if enableVTP}
		<Dropdown
			options={['Server', 'Client', 'Transparent']}
			bind:value={userParameter.VTP[0]['mode']}
			fieldName="DropdownVTP"
			Heading="Mode:"
		></Dropdown>

		<InputField
			placeholder="corp.at"
			type="text"
			bind:value={userParameter.VTP[0]['domain']}
			fieldName="VTP-Domain"
			id="VTP-Domain"
			cssClass={enableCheck ? cssClasses.VTP[0].domain : 'correct'}
		/>
		<InputField
			placeholder=""
			type="password"
			bind:value={userParameter.VTP[0]['password']}
			fieldName="VTP-Password"
			id="VTP-Password"
			cssClass={enableCheck ? cssClasses.VTP[0].password : 'correct'}
		/>
		<Checkbox
			name="VTP-Pruning"
			bind:value={userParameter.VTP[0]['pruning']}
			isChecked="true"
			Heading="Enable VTP-Pruning"
		></Checkbox>
		{#if userParameter.VTP[0]['mode'] == 'Server'}
			<Checkbox
				name="VTP-Primary"
				bind:value={userParameter.VTP[0]['is_primary']}
				isChecked="true"
				Heading="VTP Primary"
			></Checkbox>
		{/if}
	{/if}

	{#if !enableVTP || userParameter.VTP[0].mode === 'Server'}
		<h2 class="subHeading" id="VLANs">VLANs</h2>
		{#each range(0, userParameter.VLAN.length - 1) as count}
			<VLAN
				cssClasses={cssClasses.VLAN[count]}
				check={enableConnectivityCheck}
				id={count}
				bind:number={userParameter.VLAN[count]['number']}
				bind:name={userParameter.VLAN[count]['name']}
			></VLAN>
		{/each}

		<button class="leftButton" on:click={addVLAN}>Add VLAN</button>
		<button class="rightButton" on:click={removeVLAN}>Remove VLAN</button>
	{/if}

	<h2 class="subHeading" id="STP">STP</h2>
	{#each range(0, userParameter.STP.length - 1) as count}
		<StpProcess
			cssClasses={cssClasses.STP[count]}
			check={enableCheck}
			id={count + 1}
			parameters={userParameter.STP[count]}
		></StpProcess>
	{/each}
	<button class="leftButton" on:click={addSTPProcess}>Add STP Process</button>
	<button class="rightButton" on:click={removeSTPProcess}>Remove STP Process </button>
	<EdgeInterfaces
		check={enableCheck}
		bind:edgeInterfaces={userParameter.EdgePorts}
		InterfaceCssClasses={cssClasses.EdgePorts}
	></EdgeInterfaces>

	<h2 class="subHeading" id="Interfaces">Interfaces</h2>
	<h2 class="subSubHeading">Trunks</h2>
	<TrunkInterface
		check={enableCheck}
		cssClasses={cssClasses.Trunks}
		bind:trunks={userParameter.Trunks}
	></TrunkInterface>

	<h2 class="subSubHeading">Access Interfaces</h2>
	<AccessInterface
		check={enableCheck}
		cssClasses={cssClasses.AccessInterfaces}
		bind:accessInterfaces={userParameter.AccessInterfaces}
	></AccessInterface>
	<br />

	<h2 class="subHeading" id="Port-Security">Port-Security</h2>
	{#each range(0, userParameter.Portsecurity.length - 1) as count}
		<PortSecurityInterface check={enableCheck} cssClasses={cssClasses['Portsecurity'][count]} bind:parameters={userParameter.Portsecurity[count]} id={count}
		></PortSecurityInterface>
	{/each}
	<button on:click={addPortSecurityInterface} class="leftButton">Add Interface</button>
	<button on:click={removePortSecurityInterface} class="rightButton">Remove Interface</button>

	<h2 class="subHeading" id="Etherchannels">Etherchannels</h2>
	{#each range(0, userParameter.EtherChannels.length - 1) as count}
		<Etherchannel  check={enableCheck} cssClasses={cssClasses.EtherChannels[count]} bind:parameters={userParameter.EtherChannels[count]} id={count}></Etherchannel>
	{/each}
	<button class="leftButton" on:click={addEtherChannel}>Add Etherchannel</button>
	<button class="rightButton" on:click={removeEtherChannel}>Remove Etherchannel</button>
	<br />
	<button class="generateSkriptButton" id="Submit" on:click={checkUserParameter}> Submit</button>
	<button class="generateSkriptButton" on:click={sendData}> Show Script</button>
	<button class="generateSkriptButton" on:click={resetInputs}>Reset Inputs</button>
</div>

{#if generate}
<div id="textAreaDiv">
	<h1>Generating...</h1>
</div>
{/if}

{#if showError}
<div id="textAreaDiv">
	<h1 style="color: red">Es sind noch nicht alle Felder korrekt ausgefüllt!</h1>
	<p>Bitte überprüfen Sie die rot markierten Felder und füllen Sie diese korrekt aus!</p>
</div>
{/if}