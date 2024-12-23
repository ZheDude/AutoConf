<script>
    import InputField from "../inputField.svelte";
    import Dropdown from "../dropdown.svelte";
    export let id;
    export let params = {
        "number": "",
        "name": "",
        "password": "",
        "ALGO": ""
      }


</script>

<InputField
placeholder="1"
type="text"
fieldName="Number"
id="Key-Chain-Number{id}"
bind:value={params.number}
/>

<InputField
placeholder="KeyChain1"
type="text"
fieldName="Name"
id="Key-Chain-Name{id}"
bind:value={params.name}
/>


<InputField
placeholder=""
type="password"
fieldName="Password"
id="Key-Chain-Password{id}"
bind:value={params.password}
/>

<Dropdown
options={["md5", "sha-1", "sha-256", "sha-384" ,"sha-512"]}
fieldName="SSH"
Heading="Choose Algorithm:"
bind:value={params.ALGO}
></Dropdown>

