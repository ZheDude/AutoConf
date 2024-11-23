<script>
    	import InputField from '../inputField.svelte';
        export let number = " ";
        export let name = " ";
        export let id;

</script>

<InputField placeholder="10"  bind:value={number} type="text" fieldName="VLAN" id="VLAN-Number{id}" />
<InputField placeholder="Management" bind:value={name} type="text" fieldName="Name" id="VLAN-Name{id}" />
