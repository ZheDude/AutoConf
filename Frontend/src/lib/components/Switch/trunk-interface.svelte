<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import Checkbox from '../checkbox.svelte';

	export let check = false;
	export let trunks = {
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
		trunks.Interfaces = [
			...trunks.Interfaces,
			{ name: '', allowed_vlan: '', native_vlan: '', encapsulation: 'dot1q', mode: 'Trunk', shutdown: false }
		];

		cssClasses.Interfaces = [... cssClasses.Interfaces, { name: 'correct', allowed_vlan: 'correct', native_vlan: 'correct' } ]
	}

	function removeInterface() {

			trunks.Interfaces = trunks.Interfaces.slice(0, -1);
			cssClasses.Interfaces = trunks.Interfaces.slice(0,-1);
		
	}
	function addInterfaceRange() {
		trunks.InterfaceRanges = [
			...trunks.InterfaceRanges,
			{
				startInterface: '',
				endInterface: '',
				allowed_vlan: '',
				native_vlan: '',
				encapsulation: 'dot1q',
				mode: 'Trunk',
				shutdown: false
			}
		];

		cssClasses.InterfaceRanges = [... trunks.InterfaceRanges,{
				startInterface: 'correct',
				endInterface: 'correct',
				allowed_vlan: 'correct',
				native_vlan: 'correct'
			} ]
	}

	function removeInterfaceRange() {
			trunks.InterfaceRanges = trunks.InterfaceRanges.slice(0, -1);
			cssClasses.InterfaceRanges = cssClasses.InterfaceRanges.slice(0, -1);
	}
</script>

<h2 class="subSubSubHeading">Single Interfaces</h2>

{#each range(0, trunks.Interfaces.length - 1) as count}
	<InputField
		bind:value={trunks.Interfaces[count].name}
		placeholder="Gig0/1"
		type="text"
		fieldName="Interface:"
		id="Trunk{count}"
		cssClass={check ? cssClasses.Interfaces[count].name : 'correct'}
	/>


	<InputField
		bind:value={trunks.Interfaces[count].allowed_vlan}
		placeholder="10,20,30"
		type="text"
		fieldName="Allowed VLANs:"
		id="AllowedVlans{count}"
		cssClass={check ? cssClasses.Interfaces[count].allowed_vlan : 'correct'}
	/>

	<InputField
		bind:value={trunks.Interfaces[count].native_vlan}
		placeholder="10"
		type="text"
		fieldName="Native VLAN:"
		id="NativeVlan{count}"
		cssClass={check ? cssClasses.Interfaces[count].native_vlan : 'correct'}
	/>
	<br />

	<Dropdown
		bind:value={trunks.Interfaces[count].mode}
		options={['Dynamic Auto', 'Dynamic Desirable', 'Trunk']}
		fieldName="Mode{count}"
		Heading="Trunk-Mode:"
	></Dropdown>

	<Checkbox
		bind:isChecked={trunks.Interfaces[count].shutdown}
		name="ShutdownTrunk{count}}"
		Heading="Shutdown"
	></Checkbox>
{/each}

<button class="leftButton extra-margin" on:click={addInterface}>Add Interface</button>
<button class="rightButton extra-margin" on:click={removeInterface}>Remove Interface</button>

<h2 class="subSubSubHeading">Interface Ranges</h2>
{#each range(0, trunks.InterfaceRanges.length - 1) as count}
	<div class="TrunkRangeDiv">
		<InputField
			bind:value={trunks.InterfaceRanges[count].startInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="Start-Interface:"
			id="Trunk{count}"
			cssClass={check ? cssClasses.InterfaceRanges[count].startInterface : 'correct'}
		/>
		<InputField
			bind:value={trunks.InterfaceRanges[count].endInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="End-Interface:"
			id="Trunk{count}"
			cssClass={check ? cssClasses.InterfaceRanges[count].endInterface : 'correct'}
		/>
	</div>
	<InputField
		placeholder="10,20,30"
		type="text"
		fieldName="Allowed VLANs:"
		id="AllowedVlans{count}"
		bind:value={trunks.InterfaceRanges[count].allowed_vlan}
		cssClass={check ? cssClasses.InterfaceRanges[count].allowed_vlan : 'correct'}
	/>

	<InputField
		placeholder="10"
		type="text"
		fieldName="Native VLAN:"
		id="NativeVlan{count}"
		bind:value={trunks.InterfaceRanges[count].native_vlan}
		cssClass={check ? cssClasses.InterfaceRanges[count].native_vlan : 'correct'}
	/>
	<br />

	<Dropdown
		options={['Dynamic-Auto', 'Dynamic-Desirable', 'Static']}
		fieldName="Mode{count}"
		Heading="Trunk-Mode:"
		bind:value={trunks.InterfaceRanges[count].mode}
	></Dropdown>

	<Checkbox
		name="ShutdownTrunk{count}}"
		Heading="Shutdown"
		bind:isChecked={trunks.InterfaceRanges[count].shutdown}
	></Checkbox>
{/each}

<button class="leftButton extra-margin" on:click={addInterfaceRange}>Add Interface Range</button>
<button class="rightButton extra-margin" on:click={removeInterfaceRange}
	>Remove Interface Range</button
>
