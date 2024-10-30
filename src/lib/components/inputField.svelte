
<script>
    export let type = "text";
    export let fieldName;
    export let placeholder;
</script>

<div class="inputFieldDiv">
<label for="{fieldName}">{fieldName}</label>
<input placeholder="{placeholder}" id="{fieldName}" type="{type}">

</div>