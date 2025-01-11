<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import Checkbox from '../checkbox.svelte';
    export let id;
    let enableAuthentication = false;
    let enableOspf = false;
    export let check = false;
    export let params =      {
        "interface": "",
        "ip_address": "",
        "subnetmask": "",
        "description": "",
        "shutdown": false,
      }

    export let cssClasses = {
        "interface": "correct",
        "ip_address": "correct",
        "subnetmask": "correct",
        "description": "correct",
      }


      $:{
        if (enableOspf){
          params.ospf =  {
          "area_id": "",
          "cost": "",
          "priority": "",
          "network_type": "broadcast", 
        }

        cssClasses.ospf =  {
          "area_id": "correct",
          "cost": "correct",
          "priority": "correct", 
        }
        
      }

      if (enableAuthentication){
        params.ospf.authentication = {
            "key_chain": ""
          }

          cssClasses.ospf.authentication = {
            "key_chain": "correct"
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

cssClass={check ? cssClasses.interface : 'correct'}
/>

<InputField
placeholder="192.168.10.10"
type="text"
fieldName="IP-Address"
id="IP-AddressInterface{id}"
bind:value={params['ip_address']}
cssClass={check ? cssClasses.ip_address : 'correct'}

/>

<InputField
placeholder="255.255.255.0"
type="text"
fieldName="Subnetzmaske"
id="Subnetzmaske{id}"
bind:value={params['subnetmask']}
cssClass={check ? cssClasses.subnetmask : 'correct'}
/>


<InputField
placeholder="This an Interface Descriptions"
type="text"
fieldName="Description"
id="InterfaceDescription{id}"
bind:value={params['description']}
cssClass={check ? cssClasses.description : 'correct'}
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
cssClass={check ? cssClasses.ospf.area_id : 'correct'}
/>




<InputField
placeholder="10"
type="text"
fieldName="Kosten"
id="OSPFCost-Interface{id}"
bind:value={params['ospf']['cost']}
cssClass={check ? cssClasses.ospf.cost : 'correct'}
/>

<InputField
placeholder="10"
type="text"
fieldName="Priority"
id="OSPFPriority-Interface{id}"
bind:value={params['ospf']['priority']}
cssClass={check ? cssClasses.ospf.priority : 'correct'}
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
cssClass={check ? cssClasses.ospf.authentication.key_chain : 'correct'}
/>
{/if}

{/if}
