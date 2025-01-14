<script>
	import InputField from '../inputField.svelte';
	export let check = false;
	export let id;
	export let params = {
		tunnel: '',
		source: '',
		source_ip: '',
		destination: '',
		ip: '',
		subnetmask: ''
	};

	export let cssClasses  = {
		tunnel: 'correct',
		source: 'correct',
		source_ip: 'correct',
		destination: 'correct',
		ip: 'correct',
		subnetmask: 'correct'
	};
</script>

<InputField
	id="GRETunnel{id}"
	placeholder="Tunnel0"
	fieldName="Tunnel-Interface"
	bind:value={params.tunnel}
	cssClass={check ? cssClasses.tunnel : 'correct'}
/>

<InputField
	id="GRESourceInterface{id}"
	placeholder="Gig0/0"
	fieldName="Tunnel-Source Interface"
	bind:value={params.source}
	cssClass={check ? cssClasses.source : 'correct'}
/>

<InputField
	id="GRESourceIP{id}"
	placeholder="192.168.10.10"
	fieldName="Tunnel-Source IP (optional)"
	bind:value={params.source_ip}
	cssClass={check ? cssClasses.source_ip : 'correct'}
/>


{#if check && params.source == '' && params.source_ip == ''}
<p style='color: red'>Error you must either specify an source interface or source IP-Address or both!</p>
{/if}

<InputField
	id="GREDestinationIP{id}"
	placeholder="192.168.20.10"
	fieldName="Tunnel Destination IP"
	bind:value={params.destination}
	cssClass={check ? cssClasses.destination : 'correct'}
/>

<InputField
	id="GREInterfaceIP{id}"
	placeholder="192.168.10.1"
	fieldName="Tunnel IP Address"
	bind:value={params.ip}
	cssClass={check ? cssClasses.ip : 'correct'}
/>

<InputField
	id="GREInterfaceSubnetmask{id}"
	placeholder="255.255.0.0"
	fieldName="Subnetmask"
	bind:value={params.subnetmask}
	cssClass={check ? cssClasses.subnetmask : 'correct'}
/>
