<script>
	import InputField from '../inputField.svelte';

	export let id;
	export let params = {
		tunnel: '',
		source: '',
		source_ip: '',
		destination: '',
		ip: '',
		subnetmask: ''
	};
</script>

<InputField
	id="GRETunnel{id}"
	placeholder="Tunnel0"
	fieldName="Tunnel-Interface"
	bind:value={params.tunnel}
/>

<InputField
	id="GRESourceInterface{id}"
	placeholder="Gig0/0"
	fieldName="Tunnel-Source Interface"
	bind:value={params.source}
/>

<InputField
	id="GRESourceIP{id}"
	placeholder="192.168.10.10"
	fieldName="Tunnel-Source IP (optional)"
	bind:value={params.source_ip}
/>

<InputField
	id="GREDestinationIP{id}"
	placeholder="192.168.20.10"
	fieldName="Tunnel Destination IP"
	bind:value={params.destination}
/>

<InputField
	id="GREInterfaceIP{id}"
	placeholder="192.168.10.1"
	fieldName="Tunnel IP Address"
	bind:value={params.ip}
/>

<InputField
	id="GREInterfaceSubnetmask{id}"
	placeholder="255.255.0.0"
	fieldName="Subnetmask"
	bind:value={params.subnetmask}
/>
