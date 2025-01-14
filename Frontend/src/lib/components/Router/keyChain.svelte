<script>
    import InputField from "../inputField.svelte";
    import Dropdown from "../dropdown.svelte";
    export let id;
    export let check = false; 
    export let params = {
        "number": "",
        "name": "",
        "password": "",
        "ALGO": ""
      }

      export let cssClasses = {
        "number": "correct",
        "name": "correct",
        "password": "correct"
      }



</script>

<InputField
placeholder="1"
type="text"
fieldName="Number"
id="Key-Chain-Number{id}"
bind:value={params.number}
cssClass={check ? cssClasses['number'] : 'correct'}
/>

<InputField
placeholder="KeyChain1"
type="text"
fieldName="Name"
id="Key-Chain-Name{id}"
bind:value={params.name}
cssClass={check ? cssClasses['name'] : 'correct'}
/>


<InputField
placeholder=""
type="password"
fieldName="Password"
id="Key-Chain-Password{id}"
bind:value={params.password}
cssClass={check ? cssClasses['password'] : 'correct'}
/>

<Dropdown
options={["md5", "sha-1", "sha-256", "sha-384" ,"sha-512"]}
fieldName="SSH"
Heading="Choose Algorithm:"
bind:value={params.ALGO}
></Dropdown>

