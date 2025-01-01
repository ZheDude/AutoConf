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
		managementInterface: '',
		vtyRange1: {}
	};

	let generate = false;

	let cssClasses = {
		hostname: 'correct',
		domain: 'correct',
		adminUser: 'correct',
		adminPassword: 'correct',
		sshVersion: 'correct',
		managementInterface: 'correct',

	}

	$: cssClasses; 

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
		if (checkUserInputs()) {
			generate = true;
		}
	}

	function checkUserInputs() {
		let correct = true;
		if (inputParams.hostname === '') {
			correct = false;
			cssClasses.hostname = 'error';
		}else{
			cssClasses.hostname = 'correct';
		}

		if (inputParams.domain === '') {
			correct = false;
			cssClasses.domain = 'error';
		}else{
			cssClasses.domain = 'correct';
		}

		if (inputParams.adminUser === '') {
			correct = false;
			cssClasses.adminUser = "error";
 		}else{
			cssClasses.adminUser = 'correct';
		}

		if (inputParams.password === '') {
			correct = false;
			cssClasses.password = "error";
		}else{
			cssClasses.password = 'correct';
		}


		if(inputParams.managementInterface === '') {
			correct = false;
			cssClasses.managementInterface = "error";
		}else{
			cssClasses.managementInterface = 'correct';
		}



		let missingInputs = [];
		let missingVTYParams = {};
		for (let [key, value] of Object.entries(inputParams)) {
			if (key.startsWith('vtyRange')) {
				missingInputs[key] = [];
				for (let [vtykey, vtyvalue] of Object.entries(value)) {
					if (vtyvalue === '' || vtyvalue === undefined) {
						missingInputs[key].push(vtykey);
					}
				}
			} else {
				if (value === '') {
					missingInputs.push(key);
				}
			}
		}
		if (missingInputs.length > 0) {
			console.log(missingInputs);
			return false;
		}
		
		return true;
	}
</script>

<div id="parameterDivGrundkonfig">
	<div class="mainHeading">
		<h1>Grundconfig</h1>
	</div>
	<InputField
		placeholder="cisco"
		type="text"
		fieldName="Hostname"
		id="Hostname"
		bind:value={inputParams.hostname}
		bind:cssClass={cssClasses.hostname}
	/>
	<InputField
		placeholder="corp.at"
		type="text"
		fieldName="IP Domain-Name"
		id="IP-Domainname"
		bind:value={inputParams.domain}
		bind:cssClass={cssClasses.domain}
	/>
	<InputField
		placeholder="cisco"
		type="text"
		fieldName="Admin Username"
		id="Adminusername"
		bind:value={inputParams.adminUser}
		bind:cssClass={cssClasses.adminUser}
	/>
	<InputField
		placeholder=""
		type="password"
		fieldName="Admin Password"
		id="Adminpasswort"
		bind:value={inputParams.password}
		bind:cssClass={cssClasses.password}
	/>

	<Dropdown
		options={[1, 2]}
		fieldName="SSH"
		Heading="Choose SSH Version:"
		bind:value={inputParams.sshVersion}
		bind:cssClass={cssClasses.sshVersion}
	></Dropdown>

	<h2 class="subHeading" id="ConsoleInterface">Console Interface</h2>
	<InputField
		type="text"
		placeholder="3600 (default = 0)"
		fieldName="Execution Timeout"
		id="ExecTimeout Console"
		bind:value={inputParams.consoleExecTime}
	></InputField>
	<Checkbox name="syn" Heading="Logging Synchronous" bind:isChecked={inputParams.consoleLoggingSyn}
	></Checkbox>

	<Checkbox name="login" Heading="Login Local" bind:isChecked={inputParams.consoleLoginLocal}
	></Checkbox>

	<h2 class="subHeading" id="ManagementInterface">Management Interface</h2>
	<InputField
		type="text"
		placeholder="vlan 10/ Gig0/0"
		fieldName=""
		id="VLAN-Num"
		bind:value={inputParams.managementInterface}
	></InputField>

	<InputField
		type="text"
		placeholder="192.168.30.254"
		fieldName="IP-Addresse"
		id="Management-IP"
		bind:value={inputParams.ManagementIP}
	></InputField>

	<div id="vtyMainDiv">
		<h2 class="subHeading" id="VTYLines">VTY Lines</h2>

		{#each range(1, count) as number}
			<VtyRange count={number} bind:attributes={inputParams['vtyRange' + number]}></VtyRange>
		{/each}
	</div>

	<button class="leftButton" on:click={addVtyRange}>Add VTY Range</button>
	<button class="rightButton" on:click={removeVtyRange}>Remove VTY Range</button>
	<br />
	<button class="generateSkriptButton" on:click={generateSkript}>Generate Script</button>
</div>

{#if generate}
	<div id="textAreaDiv">
		<h1>Folgendes Skript muss vom User selbst in das Netzwerkgerät eingefügt werden!</h1>
		<p>enable</p>
		<p>configure terminal</p>
		<p>hostname {inputParams.hostname}</p>
		<p>no ip domain-lookup</p>
		<p>ip domain-name {inputParams.domain}</p>
		<p>username {inputParams.adminUser} priv 15</p>
		<p>username {inputParams.adminUser} algorithm-type scrypt secret {inputParams.password}</p>
		<p>crypto key generate rsa usage-keys modulus 1024</p>
		<p>ip ssh version {inputParams.sshVersion}</p>
		<br />
		<p>Interface {inputParams.managementInterface}</p>
		<p>ip address {inputParams.ManagementIP}</p>
		<p>no shut</p>
		<br />
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
