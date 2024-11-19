<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import AccessInterface from './access-interface.svelte';
	export let id;
	export let parameters = {
		Interfaces: [],
		InterfaceRanges: [],
		mode: '',
		number: ''
	};

	function addInterface() {
		parameters = {
			...parameters,
			Interfaces: [...parameters.Interfaces, { name: '' }]
		};
	}

	function removeInterface() {
		if (parameters.Interfaces.length != 0) {
			parameters = {
				...parameters,
				Interfaces: parameters.Interfaces.slice(0, -1)
			};
		}
	}

	function addInterfaceRange() {
		parameters = {
			...parameters,
			InterfaceRanges: [...parameters.InterfaceRanges, { startInterface: '', endInterface: '' }]
		};
	}

	function removeInterfaceRange() {
		if (parameters.InterfaceRanges.length != 0) {
			parameters = {
				...parameters,
				InterfaceRanges: parameters.InterfaceRanges.slice(0, -1)
			};
		}
	}
	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}
</script>

<h2 class="subHeading">Etherchannel {id + 1}</h2>

{#each range(0, parameters.Interfaces.length - 1) as count}
	<InputField
		bind:value={parameters.Interfaces[count].name}
		placeholder="Gig0/0"
		type="text"
		fieldName="Interface:"
		id="Etherchannel-Interface {id}"
	/>
{/each}

<button class="leftButton" on:click={addInterface}>Add Interface</button>
<button class="rightButton" on:click={removeInterface}>Remove Interface</button>

{#each range(0, parameters.InterfaceRanges.length - 1) as count}
	<div class="TrunkRangeDiv">
		<InputField
			bind:value={parameters.InterfaceRanges[count].startInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="Start-Interface:"
			id="EtherChannelInterfaceRange{count}.1"
		/>
		<InputField
			bind:value={parameters.InterfaceRanges[count].endInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="End-Interface:"
			id="EtherChannelInterfaceRange{count}.2"
		/>
	</div>
{/each}

<button class="leftButton" on:click={addInterfaceRange} id="uniqueRight">Add Interface Range</button
>
<button class="rightButton" on:click={removeInterfaceRange} id="uniqueRight"
	>Remove Interface Range</button
>

<InputField
	bind:value={parameters.number}
	placeholder="1"
	type="text"
	fieldName="ChannelGroup"
	id="ChannelGroup{id}"
/>

<Dropdown
	bind:value={parameters.mode}
	options={['Active', 'Passive', 'Dynamic Auto', 'Dynamic Desirable', 'on']}
	fieldName="EtherChannelMode{id}"
	Heading="Mode:"
></Dropdown>
