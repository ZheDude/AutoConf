<script>
	import '$lib/stylesheet.scss';
	import InputField from '$lib/components/inputField.svelte';
	import Checkbox from '$lib/components/checkbox.svelte';

</script>


<div class="vtyDiv">
<h2 class="subSubHeading">
	Line <input type="text" /> to
	<input type="text" />
</h2>
<InputField type="text" placeholder="3600" fieldName="Execution Timeout"></InputField>
<Checkbox name="syn" Heading="Logging Synchronos"></Checkbox>
<Checkbox name="local" Heading="Login Local"></Checkbox>
</div>
