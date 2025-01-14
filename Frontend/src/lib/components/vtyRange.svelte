<script>
	
	import '$lib/stylesheet.css';
	import Checkbox from '$lib/components/checkbox.svelte';
	import ExecTimeout from '$lib/components/execTimeout.svelte';
	import Dropdown from './dropdown.svelte';
	
	export let count;
	export let required = false;
	export let startCssClass = 'correct';
	export let endCssClass = 'correct';
	export let execMinuteClass = 'correct';
	export let execSecondsClass = 'correct';

	export let attributes = {
		startLine: '',
		endLine: '',
		loggingSyn: '',
		loginLocal: '',
		transportInput: '',
		execTimeout: {
			minutes: '0',
			seconds: '0'
		}
		
	};
	

	
</script>

<div class="vtyDiv">
	
	<h2 class="subSubHeading">
		Line <input type="text" bind:value={attributes.startLine} class="{startCssClass}" /> to
		<input class="{endCssClass}" type="text" bind:value={attributes.endLine} />
	</h2>

	<ExecTimeout execMinuteClass={execMinuteClass} execSecondsClass={execSecondsClass} id="execTimeVTY{count}" bind:execTime={attributes.execTimeout}></ExecTimeout>

	<Checkbox name="syn VTY {count}" Heading="Logging Synchronous" bind:isChecked={attributes.loggingSyn}
	></Checkbox>
	{#if !required}
		<Checkbox name="local {count}" Heading="Login Local" bind:isChecked={attributes.loginLocal}></Checkbox>

		<Dropdown
			options={["ssh", "telnet", "ssh telnet"]}
			fieldName="TransportInput{count}"
			Heading="Transport Input:"
			bind:value={attributes.transportInput}
		></Dropdown>
	{/if}
</div>
