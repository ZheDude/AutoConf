<script>
    	import InputField from '../inputField.svelte';
        export let number = " ";
        export let name = " ";
        export let id;
        export let cssClasses = {
            number: 'correct',
            name: 'correct'
        }
        export let check = false;

</script>

<InputField placeholder="10"  cssClass={check ? cssClasses['number'] : 'correct'} bind:value={number} type="text" fieldName="VLAN" id="VLAN-Number{id}" />
<InputField placeholder="Management" cssClass={check ? cssClasses['name'] : 'correct'} bind:value={name} type="text" fieldName="Name" id="VLAN-Name{id}" />
