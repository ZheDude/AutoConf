<script>
    import InputField from "../inputField.svelte";

    export let id;
    export let params = {
					source: '0.0.0.0',
					mask: '0.0.0.0',
					destination: '1.1.1.1',
					interface: 'GigabitEthernet0/0',
					distance: 1
				}


</script>


<InputField
id="staticRouterSource{id}"
placeholder="192.168.10.10"
fieldName="Source"
bind:value={params.source}
/>


<InputField
id="staticRouterMask{id}"
placeholder="255.255.255.0"
fieldName="Subnetmask"
bind:value={params.mask}
/>

<InputField
id="staticRouterDestination{id}"
placeholder="10.0.0.10"
fieldName="Destination"
bind:value={params.destination}
/>

<InputField
id="staticRouterInterface{id}"
placeholder="GigabitEthernet0/0 (optional)"
fieldName="Outgoing Interface"
bind:value={params.interface}
/>



<InputField
id="staticRouterDistance{id}"
placeholder="10 (Default = 1)"
fieldName="Administrative Distance"
bind:value={params.distance}
/>