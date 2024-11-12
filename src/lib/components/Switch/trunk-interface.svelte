<script>
	import InputField from '../inputField.svelte';
    import Dropdown from '../dropdown.svelte';
    import Checkbox from '../checkbox.svelte';
	export let id;
	export let interfaceRange;
</script>

{#if interfaceRange == "true"}
<div class="TrunkRangeDiv">
	<InputField
		placeholder="Gig0/0"
		type="text"
		fieldName="Start-Interface:"
		id="Trunk-Interface {id}{id}"/>

<InputField
    placeholder="Gig0/0"
    type="text"
    fieldName="End-Interface:"
    id="Trunk-Interface {id}{id +1}"
/>
</div>

{:else}
	<InputField
		placeholder="Gig0/0"
		type="text"
		fieldName="Trunk-Interface:"
		id="Trunk-Interface {id}"
	/>
{/if}

<InputField
placeholder="Dot1q"
type="text"
fieldName="Encapsulation:"
id="Encapsulation{id}"
/>

<InputField
placeholder="10,20,30"
type="text"
fieldName="Allowed VLANs:"
id="AllowedVlans{id}"
/>

<InputField
placeholder="10"
type="text"
fieldName="Native VLAN:"
id="NativeVlan{id}"
/>
<br>

<Dropdown
options={["Dynamic-Auto", "Dynamic-Desirable", "Static"]}
fieldName="Mode{id}"
Heading="Trunk-Mode:"
></Dropdown>

<Checkbox name="Shutdown{id}" Heading="Shutdown" 
></Checkbox>





