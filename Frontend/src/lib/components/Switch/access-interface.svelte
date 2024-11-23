<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import Checkbox from '../checkbox.svelte';
	export let accessInterfaces = {
		Interfaces: [{ name: '', vlan: '', shutdown: false }],
		InterfaceRanges: [
			{
				startInterface: '',
				endInterface: '',
				vlan: '',
				shutdown: false
			}
		]
	};

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

	function addInterface() {
		accessInterfaces.Interfaces = [
			...accessInterfaces.Interfaces,
			{ name: '', vlan: '', shutdown: false }
		];
	}

	function removeInterface() {
		if (accessInterfaces.Interfaces.length != 0) {
			accessInterfaces.Interfaces = accessInterfaces.Interfaces.slice(0, -1);
		}
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
	}

	function removeInterfaceRange() {
		if (accessInterfaces.InterfaceRanges.length != 0) {
			accessInterfaces.InterfaceRanges = accessInterfaces.InterfaceRanges.slice(0, -1);
		}
	}
</script>

<h2 class="subHeading">Single Interfaces</h2>

{#each range(0, accessInterfaces.Interfaces.length - 1) as count}
	<InputField
		bind:value={accessInterfaces.Interfaces[count].name}
		placeholder="Gig0/1"
		type="text"
		fieldName="Interface:"
		id="AccessInterface{count}"
	/>
	<InputField
		bind:value={accessInterfaces.Interfaces[count].vlan}
		placeholder="10"
		type="text"
		fieldName="VLAN:"
		id="AccessPortVLAN{count}"
	/>
	<Checkbox
		bind:isChecked={accessInterfaces.Interfaces[count].shutdown}
		name="AccessInterfaceShutdown{count}"
		Heading="Shutdown"
	></Checkbox>
{/each}

<button class="leftButton" on:click={addInterface}>Add Interface</button>
<button class="rightButton" on:click={removeInterface}>Remove Interface</button>

<h2 class="subHeading">Interface Ranges</h2>
{#each range(0, accessInterfaces.InterfaceRanges.length - 1) as count}
	<div class="TrunkRangeDiv">
		<InputField
			bind:value={accessInterfaces.InterfaceRanges[count].startInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="Start-Interface:"
			id="AccessInterface{count}.1"
		/>
		<InputField
			bind:value={accessInterfaces.InterfaceRanges[count].endInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="End-Interface:"
			id="AccessInterface{count}.2"
		/>
	</div>

	<InputField
		bind:value={accessInterfaces.InterfaceRanges[count].vlan}
		placeholder="10"
		type="text"
		fieldName="VLAN:"
		id="AccessPortRangeVLAN{count}"
	/>
	<Checkbox
		bind:isChecked={accessInterfaces.InterfaceRanges[count].shutdown}
		name="AccessInterfaceRangeShutdown{count}"
		Heading="Shutdown"
	></Checkbox>
{/each}

<button class="leftButton" on:click={addInterfaceRange}>Add Interface Range</button>
<button class="rightButton" on:click={removeInterfaceRange}>Remove Interface Range</button>
