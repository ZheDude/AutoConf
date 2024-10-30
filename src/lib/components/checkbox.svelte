<script>
    export let Heading
    export let name
    export let isChecked
</script>

<div class="checkboxDiv">
<label  for="{name}">{Heading}</label>
<input type="checkbox" id="{name}" name="{name}" bind:checked={isChecked}/>
</div>