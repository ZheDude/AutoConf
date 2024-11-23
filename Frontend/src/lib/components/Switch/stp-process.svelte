
<script>
    import Dropdown from "../dropdown.svelte";
    import InputField from "../inputField.svelte";
    export let id;
    export let parameters = {"mode": '', "priority": '', "hello_timer": '', "forward_timer": '', "max_age": '', "vlan": "" }


    $: {
        if (parameters.vlan != ""){    
        parameters.vlan = getVlanArray(parameters.vlan)
    }
    }

    function getVlanArray(inputString){
        
        return inputString.split(',');
    }

</script>


<h2 class = "subHeading">STP-Process {id}</h2>
<Dropdown options={['Rapid-PVST', 'PVST']} bind:value={parameters.mode} fieldName="DropdownSTP" Heading="Mode:"></Dropdown>
<InputField placeholder="4096" type="text" bind:value={parameters.priority} fieldName="Priority" id="STP-Priority{id}" />
<InputField placeholder="10" type="text" bind:value={parameters.hello_timer} fieldName="Hello-Timer" id="STP-Hello-Timer{id}" />
<InputField placeholder="10" type="text" bind:value={parameters.forward_timer} fieldName="Forward-Timer" id="STP-Forward-Timer{id}" />
<InputField placeholder="10" type="text" bind:value={parameters.max_age} fieldName="Max-Age-Timer" id="STP-Max-Age-Timer{id}" />
<InputField placeholder="10,20,30" type="text" bind:value={parameters.vlan} fieldName="VLANs" id="STP-VLANs{id}" />




