<script>
	import InputField from '../inputField.svelte';
	export let id;
	export let params = {
		pool: '',
		network: '',
		subnetmask: '',
		default_router: '',
		dns: '',
		exclude: [{ start: '', end: '' }],
		lease: 10
	};

	function addExclusionRange() {
		params.exclude = [...params.exclude, { start: '', end: '' }];
		console.log(params.exclude);
	}

	function removeExclusionRange() {
		params.exclude = params.exclude.slice(0, -1);
	}

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
<h2 class="subHeading">Exlcuded Address-Spaces</h2>
{#each range(0, params.exclude.length - 1) as number}
    <h2 class="subSubHeading">Exlcusion Range {number}</h2>
	<InputField
		bind:value={params.exclude[number].start}
		placeholder="192.168.10.100"
		type="text"
		fieldName="Start IP"
		id="DHCPExcludedStart{id}.{number}"
	/>

	<InputField
		bind:value={params.exclude[number].end}
		placeholder="192.168.10.100"
		type="text"
		fieldName="Start IP"
		id="DHCPExcludedÊnd{id}.{number}"
	/>
{/each}

<button class="leftButton" on:click={addExclusionRange}>Add Exlcusion Range</button>
<button class="rightButton" on:click={removeExclusionRange}>Remove Exlcusion Range</button>

<InputField
	bind:value={params.lease}
	placeholder="10"
	type="text"
	fieldName="Lease Time in Seconds"
	id="DHCPLease{id}"
/>
