<script>
	import '$lib/stylesheet.scss';
	import InputField from '../lib/components/inputField.svelte';
</script>

<div class="mainHeading">
	<h1>Grundkonfig</h1>
</div>
<div id="parameterDivGrundkonfig">
<InputField type="text", fieldName="Hostname"/>
<InputField type="text", fieldName="IP-Domainname"/>
<InputField type="text", fieldName="Adminusername"/>
<InputField type="password", fieldName="Adminpasswort"/>
</div>
