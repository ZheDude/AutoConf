<script>
	import InputField from '../inputField.svelte';
	import Checkbox from '../checkbox.svelte';
	import Dropdown from '../dropdown.svelte';
	export let id;
	export let check = false;

	export let params = {
		version: 2,
		'auto-summary': true,
		networks: [
			{
				network: ''
			}
		],
		timer_update: '30',
	};

	export let cssClasses = {
		networks: [
			{
				network: 'correct'
			}
		],
		timer_update: 'correct',

		}

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}






function addNetwork() {
		params['networks'] = [
			...params['networks'],
			{
				network: ''
			}
		];

		cssClasses['networks'] = [... cssClasses['networks'], { network: 'correct'}]
	}


	function removeNetwork() {
		params.networks =  params.networks.slice(0, -1)
		cssClasses.networks = cssClasses.networks.slice(0,-1)
	}

</script>





<Dropdown options={[2, 1]} fieldName="RIP-Version" Heading="RIP-Version" bind:value={params.version}
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
	cssClass={check ? cssClasses['timer_update'] : 'correct'}
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
		cssClass={check ? cssClasses['networks'][number].network : 'correct'}
	/>
{/each}

<button class="leftButton" on:click={addNetwork}>Add Network</button>
<button class="rightButton" on:click={removeNetwork}>Remove Network</button>

