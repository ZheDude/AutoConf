<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import Checkbox from '../checkbox.svelte';
	export let id;
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
		timer_dead: 40,
		timer_hello: 10,
		passive_interfaces: ['']
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


	function removeNetwork() {
		params.networks =  params.networks.slice(0, -1)
	}




function addPassiveInterface(){
	
	params.passive_interfaces =  [...params.passive_interfaces, ""]

}


function removePassiveInterface(){
	
	params.passive_interfaces =  params.passive_interfaces.slice(0, -1)

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


<InputField
placeholder="15"
type="text"
fieldName="Hello-Timer"
id="OSPF-HelloTimer{id}"
bind:value={params['timer_hello']}
/>
<h2 class="subSubHeading">Passive Interfaces</h2>
{#each range(0, params.passive_interfaces.length-1) as number}

<InputField
placeholder="Gig0/0"
type="text"
fieldName=""
id="OSPF-passiveInterface{number}"
bind:value={params['passive_interfaces'][number]}
/>

{/each}


<button class="leftButton" on:click={addPassiveInterface}>Add Interface</button>
<button class="rightButton" on:click={removePassiveInterface}>Remove Interface</button>

{#each range(0, params['networks'].length-1) as number}
<h2 class="subSubHeading">Network {number}</h2>
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


<br>

<button class="leftButton" on:click={addNetwork}>Add Network</button>
<button class="rightButton" on:click={removeNetwork}>Remove Network</button>
