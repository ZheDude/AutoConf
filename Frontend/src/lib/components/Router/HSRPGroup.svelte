<script>
	import InputField from '../inputField.svelte';
	import Dropdown from '../dropdown.svelte';
    import Checkbox from '../checkbox.svelte';
	export let id;

	export let params = {
		group: 10,
		version: 2,
		interface: 'GigabitEthernet0/0.1',
		ip: '1.1.1.1',
		priority: 10,
		preempt: true,
		timers: {
			hello: 10,
			hold: 30
		}
	};
</script>

<InputField id="HSRPGroupID{id}" placeholder="10" fieldName="Group-ID" bind:value={params.group}
></InputField>

<Dropdown bind:value={params.version} options={[1, 2]} fieldName="Version{id}" Heading="Version"
></Dropdown>

<InputField
	id="HSRPGroupInterface{id}"
	placeholder="GigabitEthernet0/0.1"
	fieldName="Interface"
	bind:value={params.interface}
></InputField>



<InputField
	id="HSRPGroupIP{id}"
	placeholder="192.168.10.254"
	fieldName="IP-Address"
	bind:value={params.ip}
></InputField>

<InputField
	id="HSRPGroupPriority{id}"
	placeholder="10"
	fieldName="Priority"
	bind:value={params.priority}
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
></InputField>



<InputField
	id="HSRPHoldTimer{id}"
	placeholder="30"
	fieldName="Holdown-Timer"
	bind:value={params.timers.hold}
></InputField>
