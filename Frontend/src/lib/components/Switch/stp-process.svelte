<script>
	import Dropdown from '../dropdown.svelte';
	import InputField from '../inputField.svelte';
	export let id;
	export let parameters = {
		mode: '',
		priority: '',
		hello_timer: '',
		forward_timer: '',
		max_age: '',
		vlan: ''
	};

	export let check = false;

	export let cssClasses = {
		priority: 'correct',
		hello_timer: 'correct',
		forward_timer: 'correct',
		max_age: 'correct',
		vlan: 'correct'
	}


	console.log(cssClasses)
</script>

<h2 class="subSubHeading">STP-Process {id}</h2>
<Dropdown
	options={['Rapid-PVST', 'PVST']}
	bind:value={parameters.mode}
	fieldName="DropdownSTP"
	Heading="Mode:"
></Dropdown>
<InputField
	placeholder="4096"
	type="text"
	bind:value={parameters.priority}
	fieldName="Priority"
	id="STP-Priority{id}"
	cssClass={check ? cssClasses.priority : 'correct'}
/>
<InputField
	placeholder="10"
	type="text"
	bind:value={parameters.hello_timer}
	fieldName="Hello-Timer"
	id="STP-Hello-Timer{id}"
	cssClass={check ? cssClasses.hello_timer : 'correct'}
/>
<InputField
	placeholder="10"
	type="text"
	bind:value={parameters.forward_timer}
	fieldName="Forward-Timer"
	id="STP-Forward-Timer{id}"
	cssClass={check ? cssClasses.forward_timer : 'correct'}
/>
<InputField
	placeholder="10"
	type="text"
	bind:value={parameters.max_age}
	fieldName="Max-Age-Timer"
	id="STP-Max-Age-Timer{id}"
	cssClass={check ? cssClasses.max_age : 'correct'}
/>
<InputField
	placeholder="10,20,30"
	type="text"
	bind:value={parameters.vlan}
	fieldName="VLANs"
	id="STP-VLANs{id}"
	cssClass={check ?  cssClasses.vlan : 'correct'}
/>
