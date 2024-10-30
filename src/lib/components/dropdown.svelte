<script>
	export let options;
	export let fieldName;
    export let Heading;
</script>

<div class="dropdownDiv">
	<p>{Heading}</p>
	<select id="dropdown{fieldName}" name="dropdown">
        {#each options as option }
        <option value="option1">{option}</option>
        {/each}

	</select>
</div>
