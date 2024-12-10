<script>
	import InputField from '../inputField.svelte';
	import Checkbox from '../checkbox.svelte';

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}
	export let edgeInterfaces = {
		Interfaces: [{ name: '', portfast: true, bpduguard: true }],
		InterfaceRanges: [{ startInterface: '', endInterface: '', portfast: true, bpduguard: true }]
	};

	function addEdgeInterface() {
		edgeInterfaces.Interfaces = [
			...edgeInterfaces.Interfaces,
			{ name: '', portfast: true, bpduguard: true }
		];
	}

	function removeEdgeInterface() {
		if (edgeInterfaces.Interfaces.length != 1) {
			edgeInterfaces.Interfaces = edgeInterfaces.Interfaces.slice(0, -1);
		}
	}
	function addEdegInterfaceRange() {
		edgeInterfaces.InterfaceRanges = [
			...edgeInterfaces.InterfaceRanges,
			{ startInterface: '', endInterface: '', portfaste: true, bpduguard: true }
		];
	}

	function removeEdegInterfaceRange() {
		if (edgeInterfaces.InterfaceRanges.length != 1) {
			edgeInterfaces.InterfaceRanges = edgeInterfaces.InterfaceRanges.slice(0, -1);
		}
	}
</script>

<h2 class="subSubHeading">Edge-Ports</h2>
<h2 class="subSubSubHeading">Single Interfaces</h2>

{#each range(0, edgeInterfaces.Interfaces.length - 1) as count}
	<InputField
		bind:value={edgeInterfaces.Interfaces[count].name}
		placeholder="Gig0/1"
		type="text"
		fieldName="Interface"
		id="EdgeInterface{edgeInterfaces.Interfaces.length}"
	/>
	<Checkbox
		bind:isChecked={edgeInterfaces.Interfaces[count].portfast}
		name="portFast{edgeInterfaces.Interfaces.length}"
		Heading="Enable Port-Fast"
	></Checkbox>
	<Checkbox
		bind:isChecked={edgeInterfaces.Interfaces[count].bpduguard}
		name="BPDUGuard{edgeInterfaces.Interfaces.length}"
		Heading="Enable BPDU-Guard"
	></Checkbox>
{/each}
<button class="leftButton extra-margin" on:click={addEdgeInterface}>Add Interface</button>
<button class="rightButton extra-margin" on:click={removeEdgeInterface}>Remove Interface</button>
<h2 class="subSubSubHeading">Interface Ranges</h2>

{#each range(0, edgeInterfaces.InterfaceRanges.length - 1) as count}
	<InputField
		bind:value={edgeInterfaces.InterfaceRanges[count].startInterface}
		placeholder="Gig0/1"
		type="text"
		fieldName="Start-Interface"
		id="EdgeInterface{edgeInterfaces.Interfaces.length}"
	/>
	<InputField
		bind:value={edgeInterfaces.InterfaceRanges[count].endInterface}
		placeholder="Gig0/1"
		type="text"
		fieldName="End-Interface"
		id="EdgeInterface{edgeInterfaces.Interfaces.length}"
	/>
	<Checkbox
		bind:isChecked={edgeInterfaces.InterfaceRanges[count].portfast}
		name="portFast{edgeInterfaces.Interfaces.length}"
		Heading="Enable Port-Fast"
	></Checkbox>
	<Checkbox
		bind:isChecked={edgeInterfaces.InterfaceRanges[count].bpduguard}
		name="BPDUGuard{edgeInterfaces.Interfaces.length}"
		Heading="Enable BPDU-Guard"
	></Checkbox>
{/each}

<button class="leftButton extra-margin" on:click={addEdegInterfaceRange}>Add Interface Range</button
>
<button class="rightButton extra-margin" on:click={removeEdegInterfaceRange}
	>Remove Interface Range</button
>
