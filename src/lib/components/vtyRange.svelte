<script>
	import '$lib/stylesheet.css';
	import InputField from '$lib/components/inputField.svelte';
	import Checkbox from '$lib/components/checkbox.svelte';
	export let count;
	export let attributes = {
		startLine: '',
		endLine: '',
		execTimeout: '',
		loggingSyn: '',
		loginLocal: ''
	}	
</script>


<div class="vtyDiv">
<h2 class="subSubHeading">
	Line <input type="text" bind:value={attributes.startLine} /> to
	<input type="text" bind:value={attributes.endLine} />
</h2>
<InputField type="text" placeholder="3600" fieldName="Execution Timeout VTY {count}" bind:value={attributes.execTimeout}></InputField>
<Checkbox name="syn VTY {count}" Heading="Logging Synchronos" bind:isChecked={attributes.loggingSyn}></Checkbox>
<Checkbox name="local {count}" Heading="Login Local" bind:isChecked={attributes.loginLocal}></Checkbox>
</div>
