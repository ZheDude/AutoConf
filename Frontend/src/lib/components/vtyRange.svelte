<script>
	import '$lib/stylesheet.css';
	import InputField from '$lib/components/inputField.svelte';
	import Checkbox from '$lib/components/checkbox.svelte';
	import ExecTimeout from '$lib/components/execTimeout.svelte';
	import Dropdown from './dropdown.svelte';
	export let count;
	export let required = false;
	export let attributes = {
		startLine: '',
		endLine: '',
		loggingSyn: '',
		loginLocal: '',
		transportInput: 'SSH',
		execTimeout: {
			minutes: '',
			seconds: ''
		}
	};
	let startLine = attributes.startLine !== undefined ? attributes.startLine : '';
	let endLine = attributes.endLine !== undefined ? attributes.endLine : '';
	let execTimeout = attributes.execTimeout;
	let loggingSyn = attributes.loggingSyn !== undefined ? attributes.loggingSyn : false;
	let loginLocal = attributes.loginLocal !== undefined ? attributes.loginLocal : false;
	$: attributes.startLine = startLine;
	$: attributes.endLine = endLine;
	$: attributes.execTimeout = execTimeout;
	$: attributes.loggingSyn = loggingSyn;
	$: attributes.loginLocal = loginLocal;
</script>

<div class="vtyDiv">
	<h2 class="subSubHeading">
		Line <input type="text" bind:value={startLine} /> to
		<input type="text" bind:value={endLine} />
	</h2>

	<ExecTimeout id="console" bind:execTime={attributes.execTimeout}></ExecTimeout>

	<Checkbox name="syn VTY {count}" Heading="Logging Synchronous" bind:isChecked={loggingSyn}
	></Checkbox>
	{#if !required}
		<Checkbox name="local {count}" Heading="Login Local" bind:isChecked={loginLocal}></Checkbox>

		<Dropdown
			options={["SSH", "Telnet", "Telnet/SSH"]}
			fieldName="TransportInput{count}"
			Heading="Transport Input:"
			bind:value={attributes.transportInput}
		></Dropdown>
	{/if}
</div>
