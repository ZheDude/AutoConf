<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import Checkbox from '../checkbox.svelte';

	export let check = false;
	export let accessInterfaces = {
		Interfaces: [],
		InterfaceRanges: []
	};

	export let cssClasses = {
		Interfaces: [],
		InterfaceRanges: []
	}

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

	function addInterface() {
		accessInterfaces.Interfaces = [
			...accessInterfaces.Interfaces,
			{ name: '', vlan: '', shutdown: false }
		];

		cssClasses.Interfaces = [ ...cssClasses.Interfaces, {name: 'correct', vlan: 'correct'}]
	}

	function removeInterface() {
			accessInterfaces.Interfaces = accessInterfaces.Interfaces.slice(0, -1);
			cssClasses.Interfaces = cssClasses.Interfaces.slice(0,-1);
	}
	function addInterfaceRange() {
		accessInterfaces.InterfaceRanges = [
			...accessInterfaces.InterfaceRanges,
			{
				startInterface: '',
				endInterface: '',
				vlan: '',
				shutdown: false
			}
		];

		cssClasses.InterfaceRanges = [ ... cssClasses.InterfaceRanges, {
				startInterface: 'correct',
				endInterface: 'correct',
				vlan: 'correct'
			}]
	}

	function removeInterfaceRange() {

			accessInterfaces.InterfaceRanges = accessInterfaces.InterfaceRanges.slice(0, -1);
			cssClasses.InterfaceRanges = accessInterfaces.InterfaceRanges.slice(0,-1);
	}
</script>

<h2 class="subSubSubHeading">Single Interfaces</h2>

{#each range(0, accessInterfaces.Interfaces.length - 1) as count}
	<InputField
		bind:value={accessInterfaces.Interfaces[count].name}
		placeholder="Gig0/1"
		type="text"
		fieldName="Interface:"
		id="AccessInterface{count}"
		cssClass={check ? cssClasses.Interfaces[count].name : 'correct'}
	/>
	<InputField
		bind:value={accessInterfaces.Interfaces[count].vlan}
		placeholder="10"
		type="text"
		fieldName="VLAN:"
		id="AccessPortVLAN{count}"
		cssClass={check ? cssClasses.Interfaces[count].vlan : 'correct'}
	/>
	<Checkbox
		bind:isChecked={accessInterfaces.Interfaces[count].shutdown}
		name="AccessInterfaceShutdown{count}"
		Heading="Shutdown"
	></Checkbox>
{/each}

<button class="leftButton extra-margin" on:click={addInterface}>Add Interface</button>
<button class="rightButton extra-margin" on:click={removeInterface}>Remove Interface</button>

<h2 class="subSubSubHeading">Interface Ranges</h2>
{#each range(0, accessInterfaces.InterfaceRanges.length - 1) as count}
	<div class="TrunkRangeDiv">
		<InputField
			bind:value={accessInterfaces.InterfaceRanges[count].startInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="Start-Interface:"
			id="AccessInterface{count}.1"
			cssClass={check ? cssClasses.InterfaceRanges[count].startInterface : 'correct'}
		/>
		<InputField
			bind:value={accessInterfaces.InterfaceRanges[count].endInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="End-Interface:"
			id="AccessInterface{count}.2"
			cssClass={check ? cssClasses.InterfaceRanges[count].endInterface : 'correct'}
		/>
	</div>

	<InputField
		bind:value={accessInterfaces.InterfaceRanges[count].vlan}
		placeholder="10"
		type="text"
		fieldName="VLAN:"
		id="AccessPortRangeVLAN{count}"
		cssClass={check ? cssClasses.InterfaceRanges[count].vlan : 'correct'}
	/>
	<Checkbox
		bind:isChecked={accessInterfaces.InterfaceRanges[count].shutdown}
		name="AccessInterfaceRangeShutdown{count}"
		Heading="Shutdown"
	></Checkbox>
{/each}

<button class="leftButton extra-margin" on:click={addInterfaceRange}>Add Interface Range</button>
<button class="rightButton extra-margin" on:click={removeInterfaceRange}
	>Remove Interface Range</button
>
