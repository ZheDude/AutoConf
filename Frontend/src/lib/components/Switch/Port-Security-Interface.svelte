
<script>
    import InputField from "../inputField.svelte";
    export let id;
    export let parameters = 			{
				interface: "",
				maximum: "",
				violation: "",
				mac_address: ""
			}

</script>


<InputField bind:value={parameters.interface} placeholder="Gig0/1" type="text" fieldName="Interface" id="Portsecurity-Interface{id}" />
<InputField bind:value={parameters.maximum} placeholder="10" type="text" fieldName="Maximum MAC-Addresses" id="Portsecurity-Maximum{id}" />
<InputField bind:value={parameters.violation}  placeholder="Shutdown" type="text" fieldName="Violation" id="Portsecurity-ViolationMode{id}" />
<InputField bind:value={parameters.mac_address} placeholder="1D:F5:A6:05:3D:33/sticky" type="text" fieldName="MAC-Address" id="Portsecurity-MAC-Address{id}" />