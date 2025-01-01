<script>
	export let type = 'text';
	export let fieldName;
	export let placeholder;
	export let value = '';
	export let id = '';
	export let cssClass = 'correct';
	$: cssClass; 

</script>

<div class="inputFieldDiv">
	<label for={id}>{fieldName}</label>

	{#if type === 'text'}
		<input bind:value {placeholder} {id} class={cssClass} type="text" />
	{:else}
		<input bind:value {placeholder} {id} class={cssClass} type="password" />
	{/if}
</div>
