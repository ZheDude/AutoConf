<script>
	export let type = 'text';
	export let fieldName;
	export let placeholder;
	export let value = '';
	export let id = '';
	export let cssClass = 'correct';
	export let required = false;
	$: cssClass; 

	if(required){

		fieldName += "*";
	}

</script>

<div class="inputFieldDivRight">
	<label for={id}>{fieldName}</label>

	{#if type === 'text'}
		<input bind:value {placeholder} {id} class={cssClass} type="text" />
	{:else}
		<input bind:value {placeholder} {id} class={cssClass} type="password" />
	{/if}

	{#if required}
		<p class>* This field is required</p>
	{/if}
</div>
