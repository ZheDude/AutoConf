<script>
	import '$lib/stylesheet.css';
	import InputField from '../lib/components/inputField.svelte';
	import Dropdown from '../lib/components/dropdown.svelte';
	import Checkbox from '../lib/components/checkbox.svelte';
	import VtyDiv from '../lib/components/checkbox.svelte';
	import VtyRange from '../lib/components/vtyRange.svelte';
	import { get } from 'svelte/store';

	let inputParams = {
		hostname: '',
		domain: '',
		adminUser: '',
		password: '',
		sshVersion: '',
		consoleExecTime: '',
		consoleLoggingSyn: false,
		consoleLoginLocal: false,
		vtyRange1: {}
	};

	let generate = false;

	let count = 1;
	function addVtyRange() {
		count += 1;
		let rangeName = 'vtyRange' + count;
		Object.assign(inputParams, { rangeName: {} });
	}

	function removeVtyRange() {
		if (count !== 1) {
			count -= 1;
			delete inputParams['vtyRange' + count];
		}
	}

	function getVtyRanges() {
		let range = [];
		for (let i = 1; i <= count; i++) {
			range.push('vtyRange' + i);
		}
		return range;
	}

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

	function generateSkript() {
		generate = true;
	}
</script>

<div id="parameterDivGrundkonfig">
	<div class="mainHeading">
		<h1>Grundkonfig</h1>
	</div>
	<InputField
		placeholder="cisco"
		type="text"
		fieldName="Hostname"
		bind:value={inputParams.hostname}
	/>
	<InputField
		placeholder="corp.at"
		type="text"
		fieldName="IP-Domainname"
		bind:value={inputParams.domain}
	/>
	<InputField
		placeholder="cisco"
		type="text"
		fieldName="Adminusername"
		bind:value={inputParams.adminUser}
	/>
	<InputField
		placeholder=""
		type="password"
		fieldName="Adminpasswort"
		bind:value={inputParams.password}
	/>

	<Dropdown
		options={[1, 2]}
		fieldName="SSH"
		Heading="Choose SSH Version:"
		bind:value={inputParams.sshVersion}
	></Dropdown>

	<h2 class="subHeading">Console Interface</h2>
	<InputField
		type="text"
		placeholder="3600"
		fieldName="Execution Timeout"
		bind:value={inputParams.consoleExecTime}
	></InputField>
	<Checkbox name="syn" Heading="Logging Synchronous" bind:isChecked={inputParams.consoleLoggingSyn}
	></Checkbox>
	<Checkbox name="login" Heading="Login Local" bind:isChecked={inputParams.consoleLoginLocal}
	></Checkbox>

	<div id="vtyMainDiv">
		<h2 class="subHeading">VTY Lines</h2>

		{#each range(1, count) as number}
			<VtyRange count={number} bind:attributes={inputParams['vtyRange' + number]}></VtyRange>
		{/each}
	</div>

	<button on:click={addVtyRange}>Add VTY Range</button>
	<button on:click={removeVtyRange}>Remove VTY Range</button>
	<br />
	<button on:click={generateSkript}>Generate Script</button>
</div>

{#if generate}
	<div id="textAreaDiv">
		<h1>Folgendes Skript muss vom User selbst in das Netzwerkgeräte eingefügt werden!</h1>
		<p>enable</p>
		<p>configure terminal</p>
		<p>hostname {inputParams.hostname}</p>
		<p>no ip domain-lookup</p>
		<p>ip domain-name {inputParams.domain}</p>
		<p>username {inputParams.adminUser} priv 15</p>
		<p>username {inputParams.adminUser} algorithm-type scrypt secret {inputParams.password}</p>
		<p>crypto key generate rsa usage-keys modulus 1024</p>
		<p>ip ssh version {inputParams.sshVersion}</p>

		<p>line con 0</p>
		<p>exec-timeout {inputParams.consoleExecTime}</p>
		<p>{inputParams.consoleLoggingSyn ? 'logging syn' : ''}</p>
		<p>{inputParams.consoleLoginLocal ? 'login local' : ''}</p>

		{#each getVtyRanges() as range}
			<p>line vty {inputParams[range].startLine} {inputParams[range].endLine}</p>
			<p>exec-timeout {inputParams[range].execTimeout}</p>
			<p>{inputParams[range].loggingSyn ? 'logging syn' : ''}</p>
			<p>{inputParams[range].loginLocal ? 'login local' : ''}</p>
			<br />
		{/each}
	</div>
{/if}
