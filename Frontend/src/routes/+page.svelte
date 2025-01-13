<script>
	import '$lib/stylesheet.css';
	import InputField from '../lib/components/inputField.svelte';
	import Dropdown from '../lib/components/dropdown.svelte';
	import Checkbox from '../lib/components/checkbox.svelte';
	import VtyRange from '../lib/components/vtyRange.svelte';
	import ExecTimeout from '../lib/components/execTimeout.svelte';
	import { onMount, onDestroy } from 'svelte';
	import { browser } from '$app/environment';

	import { beforeNavigate } from '$app/navigation';
	import { afterNavigate } from '$app/navigation';

	let inputParams = {
		hostname: '',
		domain: '',
		domainLookup: false,
		adminUser: '',
		password: '',
		sshVersion: '2',
		consoleExecTime: { minutes: '0', seconds: '0' },
		consoleLoggingSyn: false,
		consoleLoginLocal: false,
		managementInterface: '',
		managementIP: '',
		managementMask: '',
		keylength: '1024',
		vtyRanges: [
			{
				startLine: '',
				endLine: '',
				execTimeout: { minutes: '0', seconds: '0' },
				loggingSyn: false,
				loginLocal: false,
				required: true,
				transportInput: 'ssh'
			}
		]
	};

	let cssClasses = {
		hostname: 'correct',
		domain: 'correct',
		adminUser: 'correct',
		adminPassword: 'correct',
		managementInterface: 'correct',
		managementIP: 'correct',
		managementMask: 'correct',
		keylength: 'correct',
		consoleExecTime: { minutes: 'correct', seconds: 'correct' },
		vtyRanges: [
			{
				startLine: 'correct',
				endLine: 'correct',
				execMinutes: 'correct',
				execSeconds: 'correct'
			}
		]
	};

	onMount(() => {
		const savedParams = localStorage.getItem('grundconfigParams');

		const savedCssClasses = localStorage.getItem('grundConfigCssClasses');

		if (savedParams) {
			inputParams = JSON.parse(savedParams);
		}

		if (savedCssClasses) {
			cssClasses = JSON.parse(savedCssClasses);
		}
	});

	function saveToLocalStorage() {
		localStorage.setItem('grundconfigParams', JSON.stringify(inputParams));
		localStorage.setItem('grundConfigCssClasses', JSON.stringify(cssClasses));
	}

	beforeNavigate(() => {
		saveToLocalStorage();
	});

	let generate = false;
	let showError = false;

	$: cssClasses;

	function addVtyRange() {
		inputParams.vtyRanges = [
			...inputParams.vtyRanges,
			{
				startLine: '',
				endLine: '',
				execTimeout: { minutes: '0', seconds: '0' },
				loggingSyn: false,
				loginLocal: false,
				required: false,
				transportInput: 'ssh'
			}
		];

		cssClasses.vtyRanges = [
			...cssClasses.vtyRanges,
			{
				startLine: 'correct',
				endLine: 'correct',
				execMinutes: 'correct',
				execSeconds: 'correct'
			}
		];
	}

	function removeVtyRange() {
		if (inputParams.vtyRanges.length > 1) {
			inputParams.vtyRanges = inputParams.vtyRanges.slice(0, -1);
			cssClasses.vtyRanges = cssClasses.vtyRanges.slice(0, -1);
		}
	}

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

	async function generateSkript() {
		if (await checkUserInputs()) {
			generate = true;
		} else {
			generate = false;
			showError = true;
		}
	}

	async function checkUserInputs() {
		let postData = {userInputs: inputParams};
		showError = false;
		const response = await fetch('/api/parameterChecks/Grundkonfig/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(postData)
		});
		let data = await response.json();
		console.log(data);
		cssClasses = data['cssClasses']
		return data['correct']
	}

	function resetInputs() {
		generate = false;
		showError = false;

		inputParams = {
			hostname: '',
			domain: '',
			domainLookup: false,
			adminUser: '',
			password: '',
			sshVersion: '2',
			consoleExecTime: { minutes: '0', seconds: '0' },
			consoleLoggingSyn: false,
			consoleLoginLocal: false,
			managementInterface: '',
			managementIP: '',
			managementMask: '',
			keylength: '1024',
			vtyRanges: [
				{
					startLine: '',
					endLine: '',
					execTimeout: { minutes: '0', seconds: '0' },
					loggingSyn: false,
					loginLocal: false,
					required: true,
					transportInput: 'ssh'
				}
			]
		};

		cssClasses = {
			hostname: 'correct',
			domain: 'correct',
			adminUser: 'correct',
			adminPassword: 'correct',
			managementInterface: 'correct',
			managementIP: 'correct',
			managementMask: 'correct',
			keylength: 'correct',
			consoleExecTime: { minutes: 'correct', seconds: 'correct' },
			vtyRanges: [
				{
					startLine: 'correct',
					endLine: 'correct',
					execMinutes: 'correct',
					execSeconds: 'correct'
				}
			]
		};
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
		required="true"
	/>

	<InputField
		placeholder="corp.at"
		type="text"
		fieldName="IP Domain-Name"
		id="IP-Domainname"
		bind:value={inputParams.domain}
		bind:cssClass={cssClasses.domain}
		required="true;"
	/>

	<Checkbox
		name="domainLookup"
		Heading="Enable 'No IP Domain Lookup'"
		bind:isChecked={inputParams.domainLookup}
	></Checkbox>

	<InputField
		placeholder="cisco"
		type="text"
		fieldName="Admin Username"
		id="Adminusername"
		bind:value={inputParams.adminUser}
		bind:cssClass={cssClasses.adminUser}
		required="true;"
	/>

	<InputField
		placeholder=""
		type="password"
		fieldName="Admin Password"
		id="Adminpasswort"
		bind:value={inputParams.password}
		bind:cssClass={cssClasses.password}
		required="true;"
	/>

	<InputField
		placeholder="1024"
		type="text"
		fieldName="Keylength"
		id="Keylength"
		bind:value={inputParams.keylength}
		cssClass={cssClasses.keylength}
	/>

	<Dropdown
		options={[1, 2]}
		fieldName="SSH"
		Heading="Choose SSH Version:"
		bind:value={inputParams.sshVersion}
		bind:cssClass={cssClasses.sshVersion}
	></Dropdown>

	<h2 class="subHeading" id="ManagementInterface">Management Interface</h2>
	<InputField
		type="text"
		placeholder="vlan 10/ Gig0/0"
		fieldName="Interface"
		id="VLAN-Num"
		bind:value={inputParams.managementInterface}
		required="true"
		cssClass={cssClasses.managementInterface}
	></InputField>

	<InputField
		type="text"
		placeholder="192.168.30.254"
		fieldName="IP-Addresse"
		id="Management-IP"
		bind:value={inputParams.managementIP}
		required="true"
		cssClass={cssClasses.managementIP}
	></InputField>

	<InputField
		type="text"
		placeholder="255.255.255.0"
		fieldName="Subnetmask"
		id="Management-Mask"
		bind:value={inputParams.managementMask}
		cssClass={cssClasses.managementMask}
		required="true"
	></InputField>

	<h2 class="subHeading" id="ConsoleInterface">Console Interface</h2>
	<ExecTimeout
		id="execTimeVTY{inputParams.vtyRanges.length}"
		bind:execTime={inputParams.consoleExecTime}
		execMinuteClass={cssClasses.consoleExecTime.minutes}
		execSecondsClass={cssClasses.consoleExecTime.seconds}
	></ExecTimeout>

	<Checkbox name="syn" Heading="Logging Synchronous" bind:isChecked={inputParams.consoleLoggingSyn}
	></Checkbox>

	<Checkbox name="login" Heading="Login Local" bind:isChecked={inputParams.consoleLoginLocal}
	></Checkbox>

	<div id="vtyMainDiv">
		<h2 class="subHeading" id="VTYLines">VTY Lines</h2>
		<h2 class="subSubHeading">Note: At least on vty range is required!</h2>

		{#each range(0, inputParams.vtyRanges.length - 1) as number}
			<VtyRange
				execMinuteClass={cssClasses.vtyRanges[number].execMinutes}
				execSecondsClass={cssClasses.vtyRanges[number].execSeconds}
				bind:attributes={inputParams.vtyRanges[number]}
				count={number}
				required={inputParams.vtyRanges[number].required}
				startCssClass={cssClasses.vtyRanges[number].startLine}
				endCssClass={cssClasses.vtyRanges[number].endLine}
			></VtyRange>
		{/each}
	</div>
	<button class="leftButton" on:click={addVtyRange}>Add VTY Range</button>
	<button class="rightButton" on:click={removeVtyRange}>Remove VTY Range</button>
	<br />
	<button class="generateSkriptButton" on:click={generateSkript}>Generate Script</button>
	<button class="generateSkriptButton" on:click={resetInputs}>Reset Inputs</button>
</div>

{#if generate}
	<div id="textAreaDiv">
		<h1>Folgendes Skript muss vom User selbst in das Netzwerkgerät eingefügt werden!</h1>
		<p>enable</p>
		<p>configure terminal</p>
		<p>hostname {inputParams.hostname}</p>
		{#if inputParams.domainLookup}
			<p>no ip domain-lookup</p>
		{/if}
		<p>ip domain-name {inputParams.domain}</p>
		<p>username {inputParams.adminUser} priv 15</p>
		<p>username {inputParams.adminUser} algorithm-type scrypt secret {inputParams.password}</p>
		<p>crypto key generate rsa usage-keys modulus {inputParams.keylength}</p>
		<p>ip ssh version {inputParams.sshVersion}</p>
		<br />
		<p>Interface {inputParams.managementInterface}</p>
		<p>ip address {inputParams.managementIP} {inputParams.managementMask}</p>
		<p>no shut</p>
		<br />
		<p>line con 0</p>
		<p>exec-timeout {inputParams.consoleExecTime.minutes} {inputParams.consoleExecTime.seconds}</p>
		<p>{inputParams.consoleLoggingSyn ? 'logging syn' : ''}</p>
		<p>{inputParams.consoleLoginLocal ? 'login local' : ''}</p>

		<br />

		{#each inputParams.vtyRanges as range}
			<p>line vty {range.startLine} {range.endLine}</p>
			{#if range.required}
				<p>transport input ssh</p>
				<p>login local</p>
			{/if}
			<p>exec-timeout {range.execTimeout.minutes} {range.execTimeout.seconds}</p>
			<p>{range.loggingSyn ? 'logging syn' : ''}</p>
			<p>{range.loginLocal ? 'login local' : ''}</p>
			<br />
		{/each}
	</div>
{/if}

{#if showError}
	<div id="textAreaDiv">
		<h1 style="color: red">Es sind noch nicht alle Felder korrekt ausgefüllt!</h1>
		<p>Bitte überprüfen Sie die rot markierten Felder und füllen Sie diese korrekt aus!</p>
	</div>
{/if}
