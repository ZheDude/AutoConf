
<script>
    export let type = "text";
    export let fieldName;
    export let placeholder;
    export let value = ''; 
</script>

<div class="inputFieldDiv">
<label for="{fieldName}">{fieldName}</label>

{#if type=== "text"}
<input  bind:value={value} placeholder="{placeholder}" id="{fieldName}" type="text" >
{:else}
<input  bind:value={value} placeholder="{placeholder}" id="{fieldName}" type="password" >
{/if}
</div>