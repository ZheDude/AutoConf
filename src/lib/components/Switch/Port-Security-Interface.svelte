
<script>
    import InputField from "../inputField.svelte";
    export let id;

</script>


<InputField placeholder="Gig0/1" type="text" fieldName="Interface" id="Portsecurity-Interface{id}" />
<InputField placeholder="10" type="text" fieldName="Maximum MAC-Addresses" id="Portsecurity-Maximum{id}" />
<InputField placeholder="Shutdown" type="text" fieldName="Violation" id="Portsecurity-ViolationMode{id}" />
<InputField placeholder="1D:F5:A6:05:3D:33/sticky" type="text" fieldName="MAC-Address" id="Portsecurity-MAC-Address{id}" />