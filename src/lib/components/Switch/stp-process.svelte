
<script>
    import Dropdown from "../dropdown.svelte";
    import InputField from "../inputField.svelte";
    export let id;

</script>


<h2 class = "subHeading">STP-Process {id}</h2>
<Dropdown options={['Rapid-PVST', 'PVST']} fieldName="DropdownSTP" Heading="Mode:"></Dropdown>
<InputField placeholder="4096" type="text" fieldName="Priority" id="STP-Priority{id}" />
<InputField placeholder="10" type="text" fieldName="Hello-Timer" id="STP-Hello-Timer{id}" />
<InputField placeholder="10" type="text" fieldName="Forward-Timer" id="STP-Forward-Timer{id}" />
<InputField placeholder="10" type="text" fieldName="Max-Age-Timer" id="STP-Max-Age-Timer{id}" />


<h2 class = "subHeading">Edge-Ports</h2>
<InputField placeholder="Gig0/1" type="text" fieldName="Interface" id="STP-Edge-Interface{id}" />
<InputField placeholder="10" type="text" fieldName="Priority" id="STP-Edge-Interface-Priority{id}" />
<button class="VtyButton">Add Interface</button>
<button class="VtyButton">Add Interface Range</button>