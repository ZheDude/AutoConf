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
	import EdgeInterfaces from '../../lib/components/Switch/edgeInterfaces.svelte';

	let enableVTP = false;


	onMount(() => {});
	let userParameter = {
		SSH: {
			ip: ''
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

	function formatAPIData(data) {
		return [
			{
				SSH: {
					ip: data.SSH.ip || ''
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
					vlan: stp.vlan || [],
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
	}

	function removeVLAN() {
		if (userParameter.VLAN.length != 0) {
			userParameter.VLAN = userParameter.VLAN.slice(0, -1);
		}
	}

	function addSTPProcess() {
		userParameter.STP = [
			...userParameter.STP,
			{ mode: '', priority: '', hello_timer: '', forward_timer: '', max_age: '', vlan: '' }
		];
	}

	function removeSTPProcess() {
		if (userParameter.STP.length != 0) {
			userParameter.STP = userParameter.STP.slice(0, -1);
		}
	}

	function addPortSecurityInterface() {
		userParameter.Portsecurity = [
			...userParameter.Portsecurity,
			{
				interface: '',
				maximum: '',
				violation: '',
				mac_address: ''
			}
		];
	}

	function removePortSecurityInterface() {
		if (userParameter.Portsecurity.length != 0) {
			userParameter.Portsecurity = userParameter.Portsecurity.slice(0, -1);
		}
	}

	function addEtherChannel() {
		userParameter.EtherChannels = [
			...userParameter.EtherChannels,
			{
				Interfaces: [{ name: '' }],
				InterfaceRanges: [{ startInterface: '', endInterface: '' }],
				mode: '',
				number: ''
			}
		];

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
			]
		}else{
			userParameter.VTP = [];
		}


	}

	$: console.log(userParameter)

	async function sendData() {
		let postData = JSON.stringify(formatAPIData(userParameter))
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
	<h2 class="subHeading">VTP</h2>
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
		/>
		<InputField
			placeholder=""
			type="password"
			bind:value={userParameter.VTP[0]['password']}
			fieldName="VTP-Password"
			id="VTP-Password"
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

	{#if !enableVTP ||  userParameter.VTP[0].mode === 'Server' }
		<h2 class="subHeading">VLANs</h2>
		{#each range(0, userParameter.VLAN.length - 1) as count}
			<VLAN
				id={count}
				bind:number={userParameter.VLAN[count]['number']}
				bind:name={userParameter.VLAN[count]['name']}
			></VLAN>
		{/each}

		<button class="leftButton" on:click={addVLAN}>Add VLAN</button>
		<button class="rightButton" on:click={removeVLAN}>Remove VLAN</button>
	{/if}

	<h2 class="subHeading">STP</h2>
	{#each range(0, userParameter.STP.length - 1) as count}
		<StpProcess id={count + 1} parameters={userParameter.STP[count]}></StpProcess>
	{/each}
	<button class="leftButton" on:click={addSTPProcess}>Add STP Process</button>
	<button class="rightButton" on:click={removeSTPProcess}>Remove STP Process </button>
	<EdgeInterfaces edgeInterfaces={userParameter.EdgePorts}></EdgeInterfaces>

	<h2 class="subHeading">Interfaces</h2>
	<h2 class="subHeading">Trunks</h2>
	<TrunkInterface bind:trunks={userParameter.Trunks}></TrunkInterface>

	<h2 class="subHeading">Access Interfaces</h2>
	<AccessInterface bind:accessInterfaces={userParameter.AccessInterfaces}></AccessInterface>
	<br />

	<h2 class="subHeading">Port-Security</h2>
	{#each range(0, userParameter.Portsecurity.length - 1) as count}
		<PortSecurityInterface bind:parameters={userParameter.Portsecurity[count]} id={count}
		></PortSecurityInterface>
	{/each}
	<button on:click={addPortSecurityInterface} class="leftButton">Add Interface</button>
	<button on:click={removePortSecurityInterface} class="rightButton">Remove Interface</button>

	<h2 class="subHeading">Etherchannels</h2>
	{#each range(0, userParameter.EtherChannels.length - 1) as count}
		<Etherchannel bind:parameters={userParameter.EtherChannels[count]} id={count}></Etherchannel>
	{/each}
	<button class="leftButton" on:click={addEtherChannel}>Add Etherchannel</button>
	<button class="rightButton" on:click={removeEtherChannel}>Remove Etherchannel</button>

	<br />
	<InputField
		placeholder="192.168.10.10"
		type="text"
		bind:value={userParameter.SSH.ip}
		fieldName="SSH-IP"
		id="SSH-IP"
	/>
	<br />
	<button class="generateSkriptButton" on:click={sendData}> Submit</button>
</div>
