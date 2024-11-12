<script>
	import InputField from '../inputField.svelte';
    import Dropdown from '../dropdown.svelte';
    import Checkbox from '../checkbox.svelte';
	export let id;
	export let interfaceRange;
</script>

{#if interfaceRange == "true"}
<div class="AccessRangeDiv">
	<InputField
		placeholder="Gig0/0"
		type="text"
		fieldName="Start-Interface:"
		id="Access-Interface {id}{id}"/>

<InputField
    placeholder="Gig0/0"
    type="text"
    fieldName="End-Interface:"
    id="Access-Interface {id}{id +1}"
/>
</div>

{:else}
	<InputField
		placeholder="Gig0/0"
		type="text"
		fieldName="Access-Interface:"
		id="Access-Interface {id}"
	/>
{/if}

<Checkbox name="ShutdownAccess{id}" Heading="Shutdown" 
></Checkbox>





