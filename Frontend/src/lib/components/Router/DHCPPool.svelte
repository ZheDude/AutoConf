<script>
	import InputField from '../inputField.svelte';
	export let id;
	export let check = false;
	export let params = {
		pool: '',
		network: '',
		subnetmask: '',
		default_router: '',
		dns: '',
		exclude: [''],
		'exclude-range': [{ start: '', end: '' }],
		lease: '10'
	};


	export let cssClasses = {
		pool: 'correct',
		network: 'correct',
		subnetmask: 'correct',
		default_router: 'correct',
		dns: 'correct',
		exclude: [''],
		'exclude-range': [{ start: '', end: '' }],
		lease: 'correct'
	};

		
	
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
	cssClass ={check ? cssClasses.pool : 'correct'}
/>
<InputField
	bind:value={params.network}
	placeholder="192.168.10.0"
	type="text"
	fieldName="Network"
	id="DHCPPoolNetwork{id}"
	cssClass ={check ? cssClasses.network : 'correct'}
/>

<InputField
	bind:value={params.subnetmask}
	placeholder="255.255.255.0"
	type="text"
	fieldName="Subnetmask"
	id="DHCPPoolSubnetMask{id}"
	cssClass ={check ? cssClasses.subnetmask : 'correct'}
/>

<InputField
	bind:value={params.default_router}
	placeholder="192.168.10.254"
	type="text"
	fieldName="Default-Router"
	id="DHCPPoolDefaultRouter{id}"
	cssClass ={check ? cssClasses.default_router : 'correct'}
/>
<InputField
	bind:value={params.dns}
	placeholder="192.168.10.100"
	type="text"
	fieldName="DNS-Server"
	id="DHCPPoolDNSServer{id}"
	cssClass ={check ? cssClasses.dns : 'correct'}
/>

<InputField
	bind:value={params.lease}
	placeholder="10"
	type="text"
	fieldName="Lease Time (Days| Hours | Minutes)"
	id="DHCPLease{id}"
	cssClass ={check ? cssClasses.lease : 'correct'}
/>

<br>


