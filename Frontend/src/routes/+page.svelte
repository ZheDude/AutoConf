<script>
	import '$lib/stylesheet.css';
	import InputField from '../lib/components/inputField.svelte';
	import Dropdown from '../lib/components/dropdown.svelte';
	import Checkbox from '../lib/components/checkbox.svelte';
	import VtyRange from '../lib/components/vtyRange.svelte';
	import ExecTimeout from '../lib/components/execTimeout.svelte';
	import { onMount, onDestroy } from 'svelte';
	import { browser } from '$app/environment';


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
				execTimeout: { minutes: '', seconds: '' },
				loggingSyn: false,
				loginLocal: false,
				required: true
			}
		]
	};

	$: console.log(inputParams);


/*

  function saveBeforeUnload() {
    localStorage.setItem('userInputs', inputParams);
    localStorage.setItem('cssClasses', cssClasses);
  }


  function loadVariables() {
    inputParams = localStorage.getItem('userInputs');
    cssClasses = localStorage.getItem('cssClasses');
    
  }


  browser.window.addEventListener('beforeunload', saveBeforeUnload);


  onMount(() => {
    loadVariables();
  });


  onDestroy(() => {+
    window.removeEventListener('beforeunload', saveBeforeUnload);
  });
*/
	

	let generate = false;
	let showError = false;

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

	$: cssClasses;

	function addVtyRange() {
		inputParams.vtyRanges = [
			...inputParams.vtyRanges,
			{
				startLine: '',
				endLine: '',
				execTimeout: { minutes: '', seconds: '' },
				loggingSyn: false,
				loginLocal: false,
				required: false
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

	function generateSkript() {
		if (checkUserInputs()) {
			generate = true;
		} else {
			showError = true;
		}
	}

	function checkUserInputs() {
		let correct = true;
		if (
			inputParams.hostname === '' ||
			!inputParams.hostname.match(/^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$/)
		) {
			correct = false;
			cssClasses.hostname = 'error';
		} else {
			cssClasses.hostname = 'correct';
		}

		if (
			inputParams.domain === ''
		) {
			correct = false;
			cssClasses.domain = 'error';
		} else {
			cssClasses.domain = 'correct';
		}

		if (
			inputParams.adminUser === '' ||
			!inputParams.adminUser.match(
				/^(?!.*\.\.)(?!.*__)(?!.*--)(?![-_.])[A-Za-z0-9._-]{3,30}(?<![-_.])$/
			)
		) {
			correct = false;
			cssClasses.adminUser = 'error';
		} else {
			cssClasses.adminUser = 'correct';
		}

		if (inputParams.password === '') {
			correct = false;
			cssClasses.password = 'error';
		} else {
			cssClasses.password = 'correct';
		}

		if (inputParams.managementInterface === '') {
			correct = false;
			cssClasses.managementInterface = 'error';
		} else {
			cssClasses.managementInterface = 'correct';
		}

		if (inputParams.managementIP === '' || !inputParams.managementIP.match(/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/)) {
			correct = false;
			cssClasses.managementIP = 'error';
		} else {
			cssClasses.managementIP = 'correct';
		}

		if (
			inputParams.managementMask === '' ||
			!inputParams.managementMask.match(
				/^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$/
			)
		) {
			correct = false;
			cssClasses.managementMask = 'error';
		} else {
			cssClasses.managementMask = 'correct';
		}

		range(0, inputParams.vtyRanges.length - 1).forEach((element) => {
			if (
				inputParams.vtyRanges[element].execTimeout.minutes === '' ||
				!inputParams.vtyRanges[element].execTimeout.minutes.match(/^-?\d*\.?\d+$/)
			) {
				console.log(element);
				correct = false;
				cssClasses.vtyRanges[element].execMinutes = 'error';
			} else {
				cssClasses.vtyRanges[element].execMinutes = 'correct';
			}

			if (
				inputParams.vtyRanges[element].execTimeout.seconds === '' ||
				!inputParams.vtyRanges[element].execTimeout.seconds.match(/^-?\d*\.?\d+$/)
				)
			 {
				correct = false;
				cssClasses.vtyRanges[element].execSeconds = 'error';
			} else {
				cssClasses.vtyRanges[element].execSeconds = 'correct';
			}


			if (
				inputParams.vtyRanges[element].startLine === '' ||
				!inputParams.vtyRanges[element].startLine.match(
					/^(0|([1-9]?[0-9]{1,2}|9[0-1][0-9]|92[0-4]))$/
				)
			) {
				console.log(element);
				correct = false;
				cssClasses.vtyRanges[element].startLine = 'error';
			} else {
				cssClasses.vtyRanges[element].startLine = 'correct';
			}

			if (
				inputParams.vtyRanges[element].endLine === '' ||
				!inputParams.vtyRanges[element].endLine.match(
					/^(0|([1-9]?[0-9]{1,2}|9[0-1][0-9]|92[0-4]))$/
				)
			) {
				correct = false;
				cssClasses.vtyRanges[element].endLine = 'error';
			} else {
				cssClasses.vtyRanges[element].endLine = 'correct';
			}
		});


		if (
			inputParams.consoleExecTime.minutes === '' ||
			!inputParams.consoleExecTime.minutes.match(/^-?\d*\.?\d+$/)
		) {
			correct = false;
			cssClasses.consoleExecTime.minutes = 'error';
		} else {
			cssClasses.consoleExecTime.minutes = 'correct';
		}


		if (
			inputParams.consoleExecTime.seconds === '' ||
			!inputParams.consoleExecTime.seconds.match(/^-?\d*\.?\d+$/)
		) {
			correct = false;
			cssClasses.consoleExecTime.seconds = 'error';
		} else {
			cssClasses.consoleExecTime.seconds = 'correct';
		}


		if (inputParams.keylength === '' || !inputParams.keylength.match(/^(512|768|1024|2048|4096)$/)) {
			correct = false;
			cssClasses.keylength = 'error';
		} else {
			cssClasses.keylength = 'correct';
		}

		return correct;
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
		placeholder="1024 (default)"
		type="text"
		fieldName="Keylength"
		id="Keylength"
		bind:value={inputParams.keylength}
		cssClass={cssClasses.keylength}
	/>

	<Dropdown
		options={[1, 2]}
		fieldName="SSH"
		Heading="Choose SSH Version (Default = 2):"
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
		
		{#each inputParams.vtyRanges as range}
			<p>line vty {range.startLine} {range.endLine}</p>
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
