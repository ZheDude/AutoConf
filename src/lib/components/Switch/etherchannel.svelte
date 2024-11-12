<script>
    import InputField from "../inputField.svelte"
    import Dropdown from "../dropdown.svelte";
    export let id;
</script>


<InputField
placeholder="1"
type="text"
fieldName="ChannelGroup"
id="ChannelGroup{id}"
/>

<Dropdown
options={["Active", "Passive", "Dynamic Auto", "Dynamic Desirable", "on"]}
fieldName="EtherChannelMode{id}"
Heading="Mode:"
></Dropdown>

<InputField
placeholder="Gig0/0"
type="text"
fieldName="Interface:"
id="Etherchannel-Interface {id}"
/>



<button class="VtyButton">Add Interface</button>
<button class="VtyButton" id="uniqueRight">Add Interface Range</button>




