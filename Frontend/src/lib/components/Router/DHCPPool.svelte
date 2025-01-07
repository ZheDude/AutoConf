<script>
	import InputField from '../inputField.svelte';
	export let id;
	export let params = {
		pool: '',
		network: '',
		subnetmask: '',
		default_router: '',
		dns: '',
		exclude: [],
		'exclude-range': [{ start: '', end: '' }],
		lease: 10
	};

		
	

	function addExclusionRange() {
		params['exclude-range'] = [...params['exclude-range'], { start: '', end: '' }];
	}

	function removeExclusionRange() {
		params['exclude-range'] = params['exclude-range'].slice(0, -1);
	}

	function AddExcludedAddress() {}

	function RemoveExcludedAddress() {}

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}
</script>

<InputField
	bind:value={params.pool}
	placeholder="LAN1"
	type="text"
	fieldName="Pool Name"
	id="DHCPPoolName{id}"
/>
<InputField
	bind:value={params.network}
	placeholder="192.168.10.0"
	type="text"
	fieldName="Network"
	id="DHCPPoolNetwork{id}"
/>

<InputField
	bind:value={params.subnetmask}
	placeholder="255.255.255.0"
	type="text"
	fieldName="Subnetmask"
	id="DHCPPoolSubnetMask{id}"
/>

<InputField
	bind:value={params.default_router}
	placeholder="192.168.10.254"
	type="text"
	fieldName="Default-Router"
	id="DHCPPoolDefaultRouter{id}"
/>
<InputField
	bind:value={params.dns}
	placeholder="192.168.10.100"
	type="text"
	fieldName="DNS-Server"
	id="DHCPPoolDNSServer{id}"
/>

<InputField
	bind:value={params.lease}
	placeholder="10"
	type="text"
	fieldName="Lease Time in Seconds"
	id="DHCPLease{id}"
/>
<h2 class="subHeading">Exlcuded Address-Spaces</h2>

{#each range(0, params['exclude'].length - 1) as number}
	<InputField
		bind:value={params['exclude'][number]}
		placeholder="192.168.10.100"
		type="text"
		fieldName="IP"
		id="ExcludedDHCPAddress{id}.{number}"
	/>
{/each}

{#each range(0, params['exclude-range'].length -1) as number}
	<h2 class="subSubHeading">Exlcusion Range {number}</h2>
	<InputField
		bind:value={params['exclude-range'][number].start}
		placeholder="192.168.10.100"
		type="text"
		fieldName="Start IP"
		id="DHCPExcludedStart{id}.{number}"
	/>

	<InputField
		bind:value={params['exclude-range'][number].end}
		placeholder="192.168.10.100"
		type="text"
		fieldName="Start IP"
		id="DHCPExcludedÊnd{id}.{number}"
	/>
{/each}

<button class="leftButton" on:click={addExclusionRange}>Add Exlcusion Range</button>
<button class="rightButton" on:click={removeExclusionRange}>Remove Exlcusion Range</button>


