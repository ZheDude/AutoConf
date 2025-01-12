<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import Checkbox from '../checkbox.svelte';
	export let id;
	export let check = false;
	export let params = {
		process_id: '',
		networks: [
			{
				network: '',
				area_id: '',
				wildcard: ''
			}
		],
		router_id: '',
		timer_dead: '40',
		timer_hello: '10',
		passive_interfaces: ['']
	};

	export let cssClasses = {
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
	};


	function addNetwork() {
		params['networks'] = [
			...params['networks'],
			{
				network: '',
				area_id: '',
				wildcard: ''
			}
		];

		cssClasses['networks'] = [
			...params['networks'],
			{
				network: 'correct',
				area_id: 'correct',
				wildcard: 'correct'
			}
		];
	}

	function removeNetwork() {
		params.networks = params.networks.slice(0, -1);
		cssClasses.networks = cssClasses.networks.slice(0, -1);
	}

	function addPassiveInterface() {
		params.passive_interfaces = [...params.passive_interfaces, ''];
		cssClasses.passive_interfaces = [...cssClasses.passive_interfaces, 'correct'];
	}

	function removePassiveInterface() {
		params.passive_interfaces = params.passive_interfaces.slice(0, -1);
		cssClasses.passive_interfaces = cssClasses.passive_interfaces.slice(0, -1);
	}
	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}
</script>

<InputField
	placeholder="10"
	type="text"
	fieldName="Process-ID"
	id="OSPFProcessID{id}"
	bind:value={params['process_id']}
	cssClass = {check ? cssClasses.process_id : 'correct'}
/>

<InputField
	placeholder="10.10.0.1"
	type="text"
	fieldName="Router-ID"
	id="OSPF-RouterID{id}"
	bind:value={params['router_id']}
	cssClass = {check ? cssClasses.router_id : 'correct'}
/>

<InputField
	placeholder="15"
	type="text"
	fieldName="Dead-Interval"
	id="OSPF-DeadInterval{id}"
	bind:value={params['timer_dead']}
	cssClass = {check ? cssClasses.timer_dead : 'correct'}
/>

<InputField
	placeholder="15"
	type="text"
	fieldName="Hello-Timer"
	id="OSPF-HelloTimer{id}"
	bind:value={params['timer_hello']}
	cssClass = {check ? cssClasses.timer_hello : 'correct'}
/>
<h2 class="subSubHeading">Passive Interfaces</h2>
{#each range(0, params.passive_interfaces.length - 1) as number}
	<InputField
		placeholder="Gig0/0"
		type="text"
		fieldName=""
		id="OSPF-passiveInterface{number}"
		bind:value={params['passive_interfaces'][number]}
		cssClass = {check ? cssClasses['passive_interfaces'][number] : 'correct'}
	/>
{/each}

<button class="leftButton" on:click={addPassiveInterface}>Add Interface</button>
<button class="rightButton" on:click={removePassiveInterface}>Remove Interface</button>

<h2 class="subSubHeading">Networks</h2>
{#each range(0, params['networks'].length - 1) as number}
	<h2 class="subSubHeading">Network {number}</h2>
	<InputField
		placeholder="192.168.10.0"
		type="text"
		fieldName="Network"
		id="OSPFNetwork{id}{number}"
		bind:value={params['networks'][number]['network']}
		cssClass = {check ? cssClasses['networks'][number]['network']: 'correct'}
	/>

	<InputField
		placeholder="10"
		type="text"
		fieldName="Area-ID"
		id="OSPFProcArea{id}{number}"
		bind:value={params['networks'][number]['area_id']}
		cssClass = {check ? cssClasses['networks'][number]['area_id']: 'correct'}
	/>

	<InputField
		placeholder="0.0.0.255"
		type="text"
		fieldName="Wildcard-Mask"
		id="WildCardOSPF{id}{number}"
		bind:value={params['networks'][number]['wildcard']}
		cssClass = {check ? cssClasses['networks'][number]['wildcard']: 'correct'}
	/>
{/each}

<br />

<button class="leftButton" on:click={addNetwork}>Add Network</button>
<button class="rightButton" on:click={removeNetwork}>Remove Network</button>
