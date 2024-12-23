<script>
	import InputField from '../inputField.svelte';
	import Checkbox from '../checkbox.svelte';
	export let id;
    let isEnabled = false;
	export let params = {
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
				network: '10.0.0.0',
				subnetmask: '0.0.0.255'
			},

		],
		timer_bgp: 30,
		hold_time: 180,
		local_as: 696969
	};

	function addNeighbor() {
		params.neighbor = [
			...params['neighbor'],
			{
                ip_of_neighbor: '',
				as: '',
				update_source: '',
				next_hop_self: false,
				route_reflector: false,
				default_originate: false
			}
		];
	}

	function removeNeighbor() {
		params.neighbor = params.neighbor.slice(0, -1);
	}


	function addNetwork() {
		params.networks = [
			...params['networks'],
			{
				network: '',
				subnetmask: ''
			}
		];
	}

	function removeNetwork() {
		params.networks = params.networks.slice(0, -1);
	}

    function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

</script>

<Checkbox
name="enableBGP{id}"
Heading="Enable BGP"
bind:isChecked={isEnabled}
/>

{#if isEnabled}

<h2 class="subSubHeading">Neighbors</h2>

{#each range(0, params['neighbor'].length-1) as number}
	<InputField
		id="BGPNeighborIP{id}.{number}"
		placeholder="192.168.10.10"
		fieldName="IP of Neighbor"
		bind:value={params.neighbor[number].ip_of_neighbor}
	/>
	<InputField
		id="BGPNeighborAS{id}.{number}"
		placeholder="100"
		fieldName="Autonomes System"
		bind:value={params.neighbor[number].as}
	/>
	<InputField
		id="BGPNeighborUpdateSource{id}.{number}"
		placeholder="Loopback1"
		fieldName="Update Source"
		bind:value={params.neighbor[number].update_source}
	/>
	<Checkbox
		name="BGPNextHopSelf{id}.{number}"
		Heading="Next Hop Self"
		bind:isChecked={params.neighbor[number].next_hop_self}
	/>
	<Checkbox
		name="BGPRouteRefelctor{id}.{number}"
		Heading="Route Reflector"
		bind:isChecked={params.neighbor[number].route_reflector}
	/>
	<Checkbox
		name="BGPDefaultOriginate{id}.{number}"
		Heading="Default Originate"
		bind:isChecked={params.neighbor[number].default_originate}
	/>
{/each}

<button class="leftButton" on:click={addNeighbor}>Add Neighbor</button>
<button class="rightButton" on:click={removeNeighbor}>Remove Neighbor</button>



{#each range(0, params['networks'].length-1) as number}
	<h2 class="subSubHeading">Network {number}</h2>
	<InputField
		id="BGPNetwork{id}.{number}"
		placeholder="1.1.1.0"
		fieldName="Network"
		bind:value={params.networks[number].network}
	/>

	<InputField
	id="BGPSubnetmask{id}.{number}"
	placeholder="1.1.1.0"
	fieldName="Subentmask"
	bind:value={params.networks[number].subnetmask}
/>
{/each}


<button class="leftButton" on:click={addNetwork}>Add Network</button>
<button class="rightButton" on:click={removeNetwork}>Remove Network</button>
{/if}