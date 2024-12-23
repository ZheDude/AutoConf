<script>
	import InputField from '../inputField.svelte';
	import Checkbox from '../checkbox.svelte';
	import Dropdown from '../dropdown.svelte';
	export let id;
	let isEnabled = false;
	export let params = {
		version: 2,
		'auto-summary': true,
		networks: [
			{
				network: ''
			}
		],
		timer_update: 30,
		passive_interface: ['GigabitEthernet0/1']
	};

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}




    function addPassiveInterface(){
	
	params.passive_interface =  [...params.passive_interface, ""]

}


function removePassiveInterface(){
	
	params.passive_interface =  params.passive_interface.slice(0, -1)

}


function addNetwork() {
		params['networks'] = [
			...params['networks'],
			{
				network: ''
			}
		];
	}


	function removeNetwork() {
		params.networks =  params.networks.slice(0, -1)
	}

</script>

<Checkbox
name="enableRIP{id}"
Heading="Enable RIP"
bind:isChecked={isEnabled}
/>

{#if isEnabled}

<Dropdown options={[1, 2]} fieldName="RIP-Version" Heading="RIP-Version" bind:value={params.version}
></Dropdown>

<Checkbox
	name="autoSummaryRIP{id}"
	bind:isChecked={params['auto-summary']}
	Heading="Enable Auto-Summary"
></Checkbox>


<InputField
    placeholder="30"
    type="text"
    fieldName="Update-Timer"
    id="RIPUpdateTimer{id}"
    bind:value={params.timer_update}
/>  

<h2 class="subHeading">Networks</h2>
{#each range(0, params['networks'].length - 1) as number}
	<h2 class="subSubHeading">Network {number}</h2>
	<InputField
		placeholder="192.168.10.0"
		type="text"
		fieldName="Network"
		id="RIPNetwork{id}{number}"
		bind:value={params['networks'][number].network}
	/>
{/each}

<button class="leftButton" on:click={addNetwork}>Add Network</button>
<button class="rightButton" on:click={removeNetwork}>Remove Network</button>


<h2 class="subSubHeading">Passive Interfaces</h2>

{#each range(0, params.passive_interface.length-1) as number}

<InputField
placeholder="Gig0/0"
type="text"
fieldName=""
id="RIP-passiveInterface{number}"
bind:value={params['passive_interface'][number]}
/>

{/each}

<button class="leftButton" on:click={addPassiveInterface}>Add Interface</button>
<button class="rightButton" on:click={removePassiveInterface}>Remove Interface</button>
{/if}