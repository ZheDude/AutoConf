<script>
	import InputField from '../inputField.svelte';
	export let check = false;
	export let id;
	export let params = {
		source: '',
		mask: '',
		destination: '',
		interface: '',
		distance: '1'
	};

	export let cssClasses = {
		source: 'correct',
		mask: 'correct',
		destination: 'correct',
		interface: 'correct',
		distance: 'correct'
	};
</script>

<InputField
	id="staticRouterSource{id}"
	placeholder="192.168.10.10"
	fieldName="Source"
	bind:value={params.source}
	cssClass = {check ? cssClasses['source'] : 'correct'}
/>

<InputField
	id="staticRouterMask{id}"
	placeholder="255.255.255.0"
	fieldName="Subnetmask"
	bind:value={params.mask}
	cssClass = {check ? cssClasses['mask'] : 'correct'}
/>

<InputField
	id="staticRouterDestination{id}"
	placeholder="10.0.0.10"
	fieldName="Destination"
	bind:value={params.destination}
	cssClass = {check ? cssClasses['destination'] : 'correct'}
/>

<InputField
	id="staticRouterInterface{id}"
	placeholder="GigabitEthernet0/0 (optional)"
	fieldName="Outgoing Interface"
	bind:value={params.interface}
	cssClass = {check ? cssClasses['interface'] : 'correct'}
/>

{#if check && params.interface == '' && params.destination == ''}
	<p style='color: red'>Error you must either specify an outgoing interface or IP-Address or both!</p>
{/if}

<InputField
	id="staticRouterDistance{id}"
	placeholder="10 (Default = 1)"
	fieldName="Administrative Distance"
	bind:value={params.distance}
	cssClass = {check ? cssClasses['distance'] : 'correct'}
/>
