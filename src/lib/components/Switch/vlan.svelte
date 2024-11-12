<script>
    	import InputField from '../inputField.svelte';

        export let id;

</script>

<InputField placeholder="10" type="text" fieldName="VLAN" id="VLAN-Number{id}" />
<InputField placeholder="Management" type="text" fieldName="Name" id="VLAN-Name{id}" />
