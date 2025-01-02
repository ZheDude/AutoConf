<script>
	import '$lib/stylesheet.css';
	import InputField from '$lib/components/inputField.svelte';
	import Checkbox from '$lib/components/checkbox.svelte';
	import ExecTimeout from '$lib/components/execTimeout.svelte';
	export let count;
	export let attributes = {
		startLine: '',
		endLine: '',
		loggingSyn: '',
		loginLocal: '',
		execTimeout: {
			minutes: '',
			seconds: '',
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


	<Checkbox name="syn VTY {count}" Heading="Logging Synchronous" bind:isChecked={loggingSyn}
	></Checkbox>
	<Checkbox name="local {count}" Heading="Login Local" bind:isChecked={loginLocal}></Checkbox>
</div>
