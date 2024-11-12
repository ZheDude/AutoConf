<script>
	export let type = 'text';
	export let fieldName;
	export let placeholder;
	export let value = '';
	export let id = '';
</script>

<div class="inputFieldDiv">
	<label for={id}>{fieldName}</label>

	{#if type === 'text'}
		<input bind:value {placeholder} {id} type="text" />
	{:else}
		<input bind:value {placeholder} {id} type="password" />
	{/if}
</div>
