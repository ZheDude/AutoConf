<script>
	import '$lib/stylesheet.scss';
	import InputField from '../lib/components/inputField.svelte';
	import Dropdown from '../lib/components/dropdown.svelte';
	import Checkbox from '../lib/components/checkbox.svelte';
	import VtyDiv from '../lib/components/checkbox.svelte';
	import VtyRange from '../lib/components/vtyRange.svelte';

	let count = 1
	function addVtyRange(){
		count += 1;
		console.log(count)
	}
</script>


<div class="mainHeading">
	<h1>Grundkonfig</h1>
</div>
<div id="parameterDivGrundkonfig">
<InputField placeholder="cisco" type="text" fieldName="Hostname"/>
<InputField placeholder="corp.at" type="text" fieldName="IP-Domainname"/>
<InputField placeholder="cisco" type="text" fieldName="Adminusername"/>
<InputField type="password" fieldName="Adminpasswort"/>

<Dropdown options={[1,2]} fieldName='SSH'Heading='Choose SSH Version:'  ></Dropdown>


<h2 class="subHeading">Console Interface</h2>
<InputField type="text" placeholder="3600" fieldName="Execution Timeout"></InputField>
<Checkbox name="syn" Heading="Logging Synchronos"></Checkbox>
<Checkbox name="login" Heading="Login Local"></Checkbox>

<div id="vtyMainDiv">
<h2 class="subHeading">VTY Lines</h2>
{#each count as number }
<VtyRange></VtyRange>
{/each}

</div>

<button on:click={addVtyRange}>Add VTY Range</button>
</div>



