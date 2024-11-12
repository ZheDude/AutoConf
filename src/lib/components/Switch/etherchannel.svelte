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



