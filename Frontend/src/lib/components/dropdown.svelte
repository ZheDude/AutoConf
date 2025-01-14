<script>
	export let options;
	export let fieldName;
	export let Heading;
	export let value;
	export let cssClass = 'correct';
	$: cssClass; 
</script>

<div class="dropdownDiv">
	<p>{Heading}</p>
	<select id="dropdown{fieldName}" name="dropdown" bind:value class={cssClass}>
		{#each options as option}
			{#if option === options[0]}
			<option value={option} selected>{option}</option>
			{:else}
			<option value={option}>{option}</option>
			{/if}
		{/each}
	</select>
</div>
