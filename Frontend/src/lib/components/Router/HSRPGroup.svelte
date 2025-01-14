<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
    import Checkbox from '../checkbox.svelte';
	export let id;
	export let check = false;

	export let params = {
		group: '',
		version: '2',
		interface: '',
		ip: '',
		priority: '',
		preempt: true,
		timers: {
			hello: '',
			hold: ''
		}
	};

	export let cssClasses = {
		group: 'correct',
		interface: 'correct',
		ip: 'correct',
		priority: 'correct',
		timers: {
			hello: 'correct',
			hold: 'correct'
		}
	};
</script>

<InputField id="HSRPGroupID{id}" placeholder="10" fieldName="Group-ID" bind:value={params.group} cssClass={ check ? cssClasses.group : 'correct'}
></InputField>

<Dropdown bind:value={params.version} options={[1, 2]} fieldName="Version{id}" Heading="Version"
></Dropdown>

<InputField
	id="HSRPGroupInterface{id}"
	placeholder="GigabitEthernet0/0.1"
	fieldName="Interface"
	bind:value={params.interface}
	cssClass={ check ? cssClasses.interface : 'correct'}
></InputField>



<InputField
	id="HSRPGroupIP{id}"
	placeholder="192.168.10.254"
	fieldName="IP-Address"
	bind:value={params.ip}
	cssClass={ check ? cssClasses.ip : 'correct'}
></InputField>

<InputField
	id="HSRPGroupPriority{id}"
	placeholder="10"
	fieldName="Priority"
	bind:value={params.priority}
	cssClass={ check ? cssClasses.priority : 'correct'}
></InputField>

<Checkbox
bind:isChecked={params.preempt}
name="HSRPPreempt{id}"
Heading="Preempt"
></Checkbox>



<InputField
	id="HSRPHelloTimer{id}"
	placeholder="10"
	fieldName="Hello-Timer"
	bind:value={params.timers.hello}
	cssClass={ check ? cssClasses.timers.hello : 'correct'}
></InputField>



<InputField
	id="HSRPHoldTimer{id}"
	placeholder="30"
	fieldName="Holdown-Timer"
	bind:value={params.timers.hold}
	cssClass={ check ? cssClasses.timers.hold : 'correct'}
></InputField>
