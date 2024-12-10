<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import Checkbox from '../checkbox.svelte';
    export let id;
    let enableAuthentication = false;
    let enableOspf = false;
    export let params =      {
        "interface": "",
        "ip_address": "",
        "subnetmask": "",
        "description": "",
        "shutdown": false,
        "ospf": {
          "area_id": "",
          "cost": "",
          "priority": "",
          "network_type": "",
          "authentication": {
            "key_chain": ""
          }
        }
      }
</script>  

<InputField
placeholder="Gig0/0"
type="text"
fieldName="InterfaceType"
id="InterfaceType{id}"
bind:value={params['interface']}
/>

<InputField
placeholder="192.168.10.10"
type="text"
fieldName="IP-Address"
id="IP-AddressInterface{id}"
bind:value={params['ip_address']}

/>

<InputField
placeholder="255.255.255.0"
type="text"
fieldName="Subnetzmaske"
id="Subnetzmaske{id}"
bind:value={params['subnetmask']}
/>


<InputField
placeholder="This an Interface Descriptions"
type="text"
fieldName="Description"
id="InterfaceDescription{id}"
bind:value={params['description']}
/>

<Checkbox name="InterfaceShutdown{id}" bind:isChecked={params['shutdown']} Heading="Shutdown"></Checkbox>


<Checkbox name="enableInterfaceOSPF{id}" bind:isChecked={enableOspf} Heading="Enable OSPF"></Checkbox>

{#if enableOspf}
<InputField
placeholder="10"
type="text"
fieldName="Area-ID"
id="AreaID-Interface{id}"
bind:value={params['ospf']['area_id']}
/>


<InputField
placeholder="10"
type="text"
fieldName="Kosten"
id="OSPFCost-Interface{id}"
bind:value={params['ospf']['cost']}
/>

<InputField
placeholder="10"
type="text"
fieldName="Kosten"
id="OSPFCost-Interface{id}"
bind:value={params['ospf']['cost']}
/>

<InputField
placeholder="10"
type="text"
fieldName="Priorit"
id="OSPFPriority-Interface{id}"
bind:value={params['ospf']['priority']}
/>


<Dropdown
options={['broadcast', 'point-to-point', 'point-to-multipoint']}
bind:value={params['ospf']['network_type']}
fieldName="DropdownVTP"
Heading="Network Type:"
></Dropdown>


<Checkbox name="enableOSPFAuthentication{id}" bind:isChecked={enableAuthentication} Heading="Enable Authentication"></Checkbox>
{#if enableAuthentication}
<InputField
placeholder="10"
type="text"
fieldName="key-chain1"
id="OSPFPriority-Interface{id}"
bind:value={params['ospf']['authentication']['key_chain']}
/>
{/if}

{/if}
