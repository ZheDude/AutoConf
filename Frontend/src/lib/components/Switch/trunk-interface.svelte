<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
	import Checkbox from '../checkbox.svelte';
	export let trunks = {
		Interfaces: [
			{ name: '', allowed_vlan: '', native_vlan: '', encapsulation: '', mode: '', shutdown: false }
		],
		InterfaceRanges: [
			{
				startInterface: '',
				endInterface: '',
				allowed_vlan: '',
				native_vlan: '',
				encapsulation: '',
				mode: '',
				shutdown: false
			}
		]
	};

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

	function addInterface() {
		trunks.Interfaces = [
			...trunks.Interfaces,
			{ name: '', allowed_vlan: '', native_vlan: '', encapsulation: '', mode: '', shutdown: false }
		];
	}

	function removeInterface() {
		if (trunks.Interfaces.length != 0) {
			trunks.Interfaces = trunks.Interfaces.slice(0, -1);
		}
	}
	function addInterfaceRange() {
		trunks.InterfaceRanges = [
			...trunks.InterfaceRanges,
			{
				startInterface: '',
				endInterface: '',
				allowed_vlan: '',
				native_vlan: '',
				encapsulation: '',
				mode: '',
				shutdown: false
			}
		];
	}

	function removeInterfaceRange() {
		if (trunks.InterfaceRanges.length != 0) {
			trunks.InterfaceRanges = trunks.InterfaceRanges.slice(0, -1);
		}
	}
</script>

<h2 class="subHeading">Single Interfaces</h2>

{#each range(0, trunks.Interfaces.length - 1) as count}
	<InputField
		bind:value={trunks.Interfaces[count].name}
		placeholder="Gig0/1"
		type="text"
		fieldName="Interface:"
		id="Trunk{count}"
	/>

	<InputField
		bind:value={trunks.Interfaces[count].encapsulation}
		placeholder="Dot1q"
		type="text"
		fieldName="Encapsulation:"
		id="Encapsulation{count}"
	/>

	<InputField
		bind:value={trunks.Interfaces[count].allowed_vlan}
		placeholder="10,20,30"
		type="text"
		fieldName="Allowed VLANs:"
		id="AllowedVlans{count}"
	/>

	<InputField
		bind:value={trunks.Interfaces[count].native_vlan}
		placeholder="10"
		type="text"
		fieldName="Native VLAN:"
		id="NativeVlan{count}"
	/>
	<br />

	<Dropdown
		bind:value={trunks.Interfaces[count].mode}
		options={['Dynamic Auto', 'Dynamic Desirable', 'Static']}
		fieldName="Mode{count}"
		Heading="Trunk-Mode:"
	></Dropdown>

	<Checkbox
		bind:isChecked={trunks.Interfaces[count].shutdown}
		name="ShutdownTrunk{count}}"
		Heading="Shutdown"
	></Checkbox>
{/each}

<button class="leftButton" on:click={addInterface}>Add Interface</button>
<button class="rightButton" on:click={removeInterface}>Remove Interface</button>

<h2 class="subHeading">Interface Ranges</h2>
{#each range(0, trunks.InterfaceRanges.length - 1) as count}
	<div class="TrunkRangeDiv">
		<InputField
			bind:value={trunks.InterfaceRanges[count].startInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="Start-Interface:"
			id="Trunk{count}"
		/>
		<InputField
			bind:value={trunks.InterfaceRanges[count].endInterface}
			placeholder="Gig0/1"
			type="text"
			fieldName="End-Interface:"
			id="Trunk{count}"
		/>
	</div>
	<InputField
		placeholder="Dot1q"
		type="text"
		fieldName="Encapsulation:"
		id="Encapsulation{count}"
		bind:value={trunks.InterfaceRanges[count].encapsulation}
	/>

	<InputField
		placeholder="10,20,30"
		type="text"
		fieldName="Allowed VLANs:"
		id="AllowedVlans{count}"
		bind:value={trunks.InterfaceRanges[count].allowed_vlan}
	/>

	<InputField
		placeholder="10"
		type="text"
		fieldName="Native VLAN:"
		id="NativeVlan{count}"
		bind:value={trunks.InterfaceRanges[count].native_vlan}
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

<button class="leftButton" on:click={addInterfaceRange}>Add Interface Range</button>
<button class="rightButton" on:click={removeInterfaceRange}>Remove Interface Range</button>
