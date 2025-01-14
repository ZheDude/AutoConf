<script>
	
	import InputField from './inputField.svelte';


    export let execTime = {
		minutes: '0',
		seconds: '0'
	};

	export let execMinuteClass = 'correct';
	export let execSecondsClass = 'correct';
	
    export let id; 
</script>

<h2 class="subSubHeading">Execution Timeout</h2>
<div class = execTimeoutDiv id="execTimeoutDiv{id}">
<InputField
	type="text"
	placeholder="0 "
	fieldName="Minutes"
	id="execTimeoutMinutes{id}"
	bind:value={execTime.minutes}
	cssClass={execMinuteClass}
></InputField>


<InputField
	type="text"
	placeholder="0 "
	fieldName="Seconds"
	id="execTimeoutSeconds{id}"
	bind:value={execTime.seconds}
	cssClass={execSecondsClass}

></InputField>

</div>
