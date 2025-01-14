
<script>
    import InputField from "../inputField.svelte";
	import Dropdown from "../dropdown.svelte";
    export let id;
	export let check = false;
    export let parameters = 			{
				interface: "",
				maximum: "",
				violation: "Shutdown",
				mac_address: ""
			}


	export let cssClasses = {
			interface: "correct",
				maximum: "correct",
				mac_address: "correct"
	}

	console.log(cssClasses, "soos")

</script>


<InputField cssClass={check ? cssClasses['interface'] : 'correct'} bind:value={parameters.interface} placeholder="Gig0/1" type="text" fieldName="Interface" id="Portsecurity-Interface{id}" />
<InputField cssClass={check ? cssClasses['maximum'] : 'correct'} bind:value={parameters.maximum} placeholder="10" type="text" fieldName="Maximum MAC-Addresses" id="Portsecurity-Maximum{id}" />
<Dropdown
		options={['Shutdown', 'Restrict', 'Protect']}
		fieldName="violationMode{id}"
		Heading="Violation Mode:"
		bind:value={parameters.violation}
	></Dropdown>

<InputField cssClass={ check ? cssClasses['mac_address'] : 'correct'} bind:value={parameters.mac_address} placeholder="1D:F5:A6:05:3D:33/sticky" type="text" fieldName="MAC-Address" id="Portsecurity-MAC-Address{id}" />