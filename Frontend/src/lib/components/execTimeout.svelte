<script>
	
	import InputField from './inputField.svelte';


    export let execTime = {
		minutes: '',
		seconds: ''
	};

	export let execMinuteClass = 'correct';
	export let execSecondsClass = 'correct';
	
    export let id; 
</script>

<h2 class="subSubHeading">Execution Timeout</h2>
<div class = execTimeoutDiv id="execTimeoutDiv{id}">
<InputField
	type="text"
	placeholder="0 (default)"
	fieldName="Minutes"
	id="execTimeoutMinutes{id}"
	bind:value={execTime.minutes}
	cssClass={execMinuteClass}
></InputField>


<InputField
	type="text"
	placeholder="0 (default)"
	fieldName="Seconds"
	id="execTimeoutSeconds{id}"
	bind:value={execTime.seconds}
	cssClass={execSecondsClass}

></InputField>

</div>
