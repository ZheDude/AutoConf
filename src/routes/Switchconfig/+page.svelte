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
		VTP: [
			{
				mode: 'Server',
				domain: '',
				password: '',
				pruning: true,
				is_primary: false
			}
		],
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
		console.log(userParameter);
	}

	function removeEtherChannel() {
		if (userParameter.EtherChannels.length != 0) {
			userParameter.EtherChannels = userParameter.EtherChannels.slice(0, -1);
		}
	}
	$: console.log(JSON.stringify(userParameter));

	function submit() {
		console.log(JSON.stringify(userParameter));
	}

	$: {
    if (enableVTP ) {
		userParameter.VTP= [
			...userParameter.VTP,
			{
				enabled: false,
				mode: 'Server',
				domain: '',
				password: '',
				pruning: true,
				is_primary: false
			}
		];
    } 
  }
</script>

<div id="parameterDivGrundkonfig">
	<div class="mainHeading">
		<h1>Switchconfig</h1>
	</div>
	<h2 class="subHeading">VTP</h2>
	<Checkbox name="enableVTP" bind:isChecked={enableVTP} Heading="Enable VTP"
	></Checkbox>
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

	{#if userParameter.VTP[0].mode  === "Server" || !enableVTP}
		<h2 class="subHeading">VLANs</h2>
		{#each range(0, userParameter.VLAN.length - 1) as count}
			<VLAN
				id={count}
				bind:number={userParameter.VLAN[count]['number']}
				bind:name={userParameter.VLAN[count]['name']}
			></VLAN>
		{/each}

		<button class="VtyButton" on:click={addVLAN}>Add VLAN</button>
		<button class="VtyButton" on:click={removeVLAN}>Remove VLAN</button>
	{/if}

	<h2 class="subHeading">STP</h2>
	{#each range(0, userParameter.STP.length - 1) as count}
		<StpProcess id={count + 1} parameters={userParameter.STP[count]}></StpProcess>
	{/each}
	<button class="VtyButton" on:click={addSTPProcess}>Add STP Process</button>
	<button class="VtyButton" on:click={removeSTPProcess}>Remove STP Process </button>
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
	<button on:click={addPortSecurityInterface} class="VtyButton">Add Interface</button>
	<button on:click={removePortSecurityInterface} class="VtyButton">Remove Interface</button>

	<h2 class="subHeading">Etherchannels</h2>
	{#each range(0, userParameter.EtherChannels.length - 1) as count}
		<Etherchannel bind:parameters={userParameter.EtherChannels[count]} id={count}></Etherchannel>
	{/each}
	<button class="VtyButton" on:click={addEtherChannel}>Add Etherchannel</button>
	<button class="VtyButton" on:click={removeEtherChannel}>Remove Etherchannel</button>

	<br />

	<button class="VtyButton" on:click={submit}> Submit</button>
</div>
