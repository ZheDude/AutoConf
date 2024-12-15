<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import Checkbox from '../checkbox.svelte';
	export let id;

	let params = {
		process_id: '',
		networks: [
			{
				network: '',
				area_id: '',
				wildcard: ''
			}
		],
		router_id: '',
		timer_dead: 40,
		timer_hello: 10,
		passive_interfaces: ['GigabitEthernet0/1', 'GigabitEthernet0/2']
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
	}


    function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}
</script>

<InputField
	placeholder="10"
	type="text"
	fieldName="Process-ID"
	id="OSPFRocessID{id}"
	bind:value={params['process_id']}
/>

<InputField
placeholder="10.10.0.1"
type="text"
fieldName="Router-ID"
id="OSPF-RouterID{id}"
bind:value={params['router_id']}
/>

<InputField
placeholder="15"
type="text"
fieldName="Dead-Interval"
id="OSPF-DeadInterval{id}"
bind:value={params['timer_dead']}
/>


{#each range(0, params['networks'].length-1) as number}
<h2>Network {number}</h2>
<InputField
placeholder="192.168.10.0"
type="text"
fieldName="Network"
id="OSPFNetwork{id}{number}"
bind:value={params['networks'][number]['network']}
/>

<InputField
placeholder="10"
type="text"
fieldName="Area-ID"
id="OSPFProcArea{id}{number}"
bind:value={params['networks'][number]['area_id']}
/>

<InputField
placeholder="0.0.0.255"
type="text"
fieldName="Wildcard-Mask"
id="WildCardOSPF{id}{number}"
bind:value={params['networks'][number]['wildcard']}
/>
{/each}




<button class="leftButton" on:click={addNetwork}>Add Interface</button>
<button class="rightButton" on:click={addNetwork}>Remove Interface</button>
