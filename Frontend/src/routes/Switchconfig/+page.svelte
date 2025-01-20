<script>
	import '$lib/stylesheet.css';
	import InputField from '../../lib/components/inputField.svelte';
	import Dropdown from '../../lib/components/dropdown.svelte';
	import Checkbox from '../../lib/components/checkbox.svelte';
	import VLAN from '../../lib/components/Switch/vlan.svelte';
	import TrunkInterface from '../../lib/components/Switch/trunk-interface.svelte';
	import Etherchannel from '../../lib/components/Switch/etherchannel.svelte';
	import AccessInterface from '../../lib/components/Switch/access-interface.svelte';
	import StpProcess from '../../lib/components/Switch/stp-process.svelte';
	import PortSecurityInterface from '../../lib/components/Switch/Port-Security-Interface.svelte';
	import { onMount } from 'svelte';
	import { beforeNavigate } from '$app/navigation';
	import { afterNavigate } from '$app/navigation';
	import EdgeInterfaces from '../../lib/components/Switch/edgeInterfaces.svelte';
	import SshCredentials from '../../lib/components/sshCredentials.svelte';

	/* Flags*/

	let enableCheck; /* set to True if the submit button is pressed*/
	let enableConnectivityCheck = false; /* set to True when a connectivity check is performed */
	let enableVTP = false; /* set to true when VTP is enabled */
	let generate = false;
	let showError = false;
	let isInConnectivityCheck = false;
	let script;

	let showScriptLoading = false;

	let buttonClass = 'SSHDivDefault';
	function resetInputs() {
		generate = false;
		showError = false;
		enableConnectivityCheck = false;
		cssClasses = {
			SSH: {},
			VTP: [],
			VLAN: [],
			STP: [],
			EdgePorts: {
				Interfaces: [],
				InterfaceRanges: []
			},
			Trunks: {
				Interfaces: [],
				InterfaceRanges: []
			},
			AccessInterfaces: {
				Interfaces: [],
				InterfaceRanges: []
			},
			Portsecurity: [],
			EtherChannels: []
		};

		userParameter = {
			SSH: {
				ip: '',
				username: '',
				password: ''
			},
			VTP: [],
			VLAN: [],
			STP: [],
			EdgePorts: {
				Interfaces: [],
				InterfaceRanges: []
			},
			Trunks: {
				Interfaces: [],
				InterfaceRanges: []
			},
			AccessInterfaces: {
				Interfaces: [],
				InterfaceRanges: []
			},
			Portsecurity: [],
			EtherChannels: []
		};
	}

	function saveToLocalStorage() {
		localStorage.setItem('enableVTP', JSON.stringify(enableVTP));
		localStorage.setItem('SwitchParams', JSON.stringify(userParameter));
		localStorage.setItem('savedCssClasses', JSON.stringify(cssClasses));
	}

	beforeNavigate(() => {
		saveToLocalStorage();
	});

	afterNavigate(() => {
		const switchParams = localStorage.getItem('SwitchParams');
		const savedcssClasses = localStorage.getItem('savedCssClasses');
		const vtpParam = localStorage.getItem('enableVTP');
		if (switchParams) {
			userParameter = JSON.parse(switchParams);
		}

		if (vtpParam) {
			enableVTP = JSON.parse(vtpParam);
		}
		if (savedcssClasses) {
			cssClasses = JSON.parse(savedcssClasses);
		}
	});
	onMount(() => {
		const savedParams = localStorage.getItem('SwitchParams');
		if (savedParams) {
			userParameter = JSON.parse(savedParams);
		}
	});

	let userParameter = {
		SSH: {
			ip: '',
			username: '',
			password: ''
		},
		VTP: [],
		VLAN: [],
		STP: [],
		EdgePorts: {
			Interfaces: [],
			InterfaceRanges: []
		},
		Trunks: {
			Interfaces: [],
			InterfaceRanges: []
		},
		AccessInterfaces: {
			Interfaces: [],
			InterfaceRanges: []
		},
		Portsecurity: [],
		EtherChannels: []
	};

	let cssClasses = {
		SSH: {
			SSH: {
				ip: '',
				username: '',
				password: '',
				isReachable: ''
			}
		},
		VTP: [],
		VLAN: [],
		STP: [],
		EdgePorts: {
			Interfaces: [],
			InterfaceRanges: []
		},
		Trunks: {
			Interfaces: [],
			InterfaceRanges: []
		},
		AccessInterfaces: {
			Interfaces: [],
			InterfaceRanges: []
		},
		Portsecurity: [],
		EtherChannels: []
	};

	function formatAPIData(data) {
		return [
			{
				SSH: {
					ip: data.SSH.ip || '',
					username: data.SSH.username || '',
					password: data.SSH.password || ''
				}
			},
			{
				VTP: data.VTP.map((vtp) => ({
					version: '3',
					mode: vtp.mode || '',
					domain: vtp.domain || '',
					password: vtp.password || '',
					pruning: vtp.pruning || '',
					is_primary: vtp.is_primary || '',
					vlan: vtp.vlan || ''
				}))
			},
			{
				VLAN: data.VLAN.map((vlan) => ({
					name: vlan.name || '',
					number: vlan.number || ''
				}))
			},
			{
				STP: data.STP.map((stp) => ({
					mode: stp.mode || '',
					priority: stp.priority || '',
					hello_timer: stp.hello_timer || '',
					max_age: stp.max_age || '',
					vlan: stp.vlan.split(',') || [],
					forward_timer: stp.forward_timer || ''
				}))
			},
			{
				EdgePorts: {
					Interfaces: data.EdgePorts.Interfaces.map((interfaceItem) => ({
						name: interfaceItem.name || '',
						portfast: interfaceItem.portfast || '',
						bpduguard: interfaceItem.bpduguard || ''
					})),
					InterfaceRanges: data.EdgePorts.InterfaceRanges.map((range) => ({
						startInterface: range.startInterface || '',
						endInterface: range.endInterface || '',
						portfaste: range.portfaste || '',
						bpduguard: range.bpduguard || ''
					}))
				}
			},
			{
				Trunks: {
					Interfaces: data.Trunks.Interfaces.map((interfaceItem) => ({
						name: interfaceItem.name || '',
						allowed_vlan: interfaceItem.allowed_vlan || '',
						native_vlan: interfaceItem.native_vlan || '',
						encapsulation: interfaceItem.encapsulation || '',
						mode: interfaceItem.mode || '',
						shutdown: interfaceItem.shutdown || ''
					})),
					InterfaceRanges: data.Trunks.InterfaceRanges.map((range) => ({
						startInterface: range.startInterface || '',
						endInterface: range.endInterface || '',
						allowed_vlan: range.allowed_vlan || '',
						native_vlan: range.native_vlan || '',
						encapsulation: range.encapsulation || '',
						mode: range.mode || '',
						shutdown: range.shutdown || ''
					}))
				}
			},
			{
				AccessInterfaces: {
					Interfaces: data.AccessInterfaces.Interfaces.map((interfaceItem) => ({
						name: interfaceItem.name || '',
						allowed_vlan: interfaceItem.allowed_vlan || '',
						native_vlan: interfaceItem.native_vlan || '',
						encapsulation: interfaceItem.encapsulation || '',
						mode: interfaceItem.mode || '',
						shutdown: interfaceItem.shutdown || '',
						vlan: interfaceItem.vlan || ''
					})),
					InterfaceRanges: data.AccessInterfaces.InterfaceRanges.map((range) => ({
						startInterface: range.startInterface || '',
						endInterface: range.endInterface || '',
						allowed_vlan: range.allowed_vlan || '',
						native_vlan: range.native_vlan || '',
						encapsulation: range.encapsulation || '',
						mode: range.mode || '',
						shutdown: range.shutdown || '',
						vlan: range.vlan || ''
					}))
				}
			},
			{
				Portsecurity: data.Portsecurity.map((item) => ({
					interface: item.interface || '',
					maximum: item.maximum || '',
					violation: item.violation || '',
					mac_address: item.mac_address || ''
				}))
			},
			{
				EtherChannels: data.EtherChannels.map((channel) => ({
					Interfaces: channel.Interfaces.map((interfaceItem) => ({
						name: interfaceItem.name || ''
					})),
					InterfaceRanges: channel.InterfaceRanges.map((range) => ({
						startInterface: range.startInterface || '',
						endInterface: range.endInterface || ''
					})),
					mode: channel.mode || '',
					number: channel.number || ''
				}))
			}
		];
	}

	$: console.log(userParameter);

	function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

	function addVLAN() {
		userParameter.VLAN = [...userParameter.VLAN, { name: '', number: '' }];
		cssClasses.VLAN = [...cssClasses.VLAN, { name: 'correct', number: 'correct' }];
	}

	function removeVLAN() {
		if (userParameter.VLAN.length != 0) {
			userParameter.VLAN = userParameter.VLAN.slice(0, -1);
			cssClasses.VLAN = cssClasses.VLAN.slice(0, -1);
		}
	}

	function addSTPProcess() {
		userParameter.STP = [
			...userParameter.STP,
			{
				mode: 'Rapid-PVST',
				priority: '32768',
				hello_timer: '2',
				forward_timer: '15',
				max_age: '20',
				vlan: ''
			}
		];

		cssClasses.STP = [
			...cssClasses.STP,
			{
				priority: 'correct',
				hello_timer: 'correct',
				forward_timer: 'correct',
				max_age: 'correct',
				vlan: 'correct'
			}
		];
	}

	function removeSTPProcess() {
		if (userParameter.STP.length != 0) {
			userParameter.STP = userParameter.STP.slice(0, -1);
			cssClasses.STP = cssClasses.STP.slice(0, -1);
		}
	}

	function addPortSecurityInterface() {
		userParameter.Portsecurity = [
			...userParameter.Portsecurity,
			{
				interface: '',
				maximum: '',
				violation: 'Shutdown',
				mac_address: ''
			}
		];

		cssClasses.Portsecurity = [
			...cssClasses.Portsecurity,
			{
				interface: 'correct',
				maximum: 'correct',
				mac_address: 'correct'
			}
		];
	}

	function removePortSecurityInterface() {
		userParameter.Portsecurity = userParameter.Portsecurity.slice(0, -1);
		cssClasses.Portsecurity = cssClasses.Portsecurity.slice(0, -1);
	}

	function addEtherChannel() {
		userParameter.EtherChannels = [
			...userParameter.EtherChannels,
			{
				Interfaces: [],
				InterfaceRanges: [],
				mode: 'on',
				number: ''
			}
		];

		cssClasses.EtherChannels = [
			...cssClasses.EtherChannels,
			{
				Interfaces: [],
				InterfaceRanges: [],
				number: 'correct'
			}
		];
	}

	function removeEtherChannel() {
		if (userParameter.EtherChannels.length != 0) {
			userParameter.EtherChannels = userParameter.EtherChannels.slice(0, -1);
		}
	}

	$: {
		if (enableVTP) {
			if (userParameter.VTP.length == 0) {
				userParameter.VTP = [
					{
						enabled: false,
						mode: 'Server',
						domain: '',
						password: '',
						pruning: true,
						is_primary: true
					}
				];
			}
			console.log(userParameter.VTP);

			cssClasses.VTP = [
				{
					domain: 'correct',
					password: 'correct'
				}
			];
		} else {
			cssClasses.VTP = [];
			userParameter.VTP = [];
		}
	}

	async function checkConectivity() {
		isInConnectivityCheck = true;
		showError = false;
		enableConnectivityCheck = true;
		let postData = { userParameter: userParameter['SSH'] };
		const response = await fetch('/api/checkConnectivity/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(postData)
		});
		let data = await response.json();
		cssClasses.SSH = data;
		isInConnectivityCheck = false;

		return new Response('', {
			headers: {
				'Content-Type': 'application/json'
			}
		});
	}

	async function generateScript(send) {
		enableCheck = true;
		showScriptLoading = true;

		if (send) {
			await checkConectivity();
		}

		let checkData = { userParameter: userParameter, cssClasses: cssClasses };
		const response = await fetch('/api/parameterChecks/Switchconfig', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(checkData)
		});
		let data = await response.json();
		cssClasses = data.cssClasses;
		if ((data.isCorrect && cssClasses.SSH.isReachable && send) || !send) {
			showError = false;
			generate = true;

			let temp = structuredClone(userParameter);
			if (!send) {
				temp.SSH = {
					ip: '',
					username: '',
					password: ''
				};
			}

			console.log(temp, 'soos');
			script = '';
			let postData = JSON.stringify(formatAPIData(temp));

			/*console.log(postData)*/
			const response = await fetch('/api/', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(postData)
			});
			let ApiData = await response.json();
			console.log(ApiData);
			script = ApiData.split('\\n');
			script[0] = script[0].slice(2);

			script = script
				.filter((item) => /[a-zA-Z]/.test(item))
				.map((item) => item.replace(/","/g, ''));
		} else {
			showError = true;
			generate = false;
		}
		showScriptLoading = false;
	}
	async function sendData() {
		script = '';
		let postData = JSON.stringify(formatAPIData(userParameter));
		/*console.log(postData)*/
		const response = await fetch('/api/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(postData)
		});
		let ApiData = await response.json();
		console.log(ApiData);
		script = ApiData.split('\\n');
		script[0] = script[0].slice(2);

		script = script.filter((item) => /[a-zA-Z]/.test(item)).map((item) => item.replace(/","/g, ''));
		return true;
	}
</script>

<div id="parameterDivGrundkonfig">
	<div class="mainHeading">
		<h1>Switchconfig</h1>
	</div>

	<SshCredentials
		cssClasses={cssClasses.SSH}
		connectivityCheck={enableConnectivityCheck}
		bind:params={userParameter.SSH}
		showLoadingAnimation={isInConnectivityCheck}
		bind:divClass={buttonClass}
	></SshCredentials>
	<button class="generateSkriptButton {buttonClass}" on:click={checkConectivity}>
		Check Connectivity</button
	>
	<h2 class="subHeading" id="VTP">VTP</h2>
	<Checkbox name="enableVTP" bind:isChecked={enableVTP} Heading="Enable VTP"></Checkbox>
	{#if enableVTP}
		<Dropdown
			options={['Server', 'Client', 'Transparent']}
			bind:value={userParameter.VTP[0]['mode']}
			fieldName="DropdownVTP"
			Heading="Mode:"
		></Dropdown>

		<InputField
			placeholder="corp.at"
			type="text"
			bind:value={userParameter.VTP[0]['domain']}
			fieldName="VTP-Domain"
			id="VTP-Domain"
			cssClass={enableCheck ? cssClasses.VTP[0].domain : 'correct'}
		/>
		<InputField
			placeholder=""
			type="password"
			bind:value={userParameter.VTP[0]['password']}
			fieldName="VTP-Password"
			id="VTP-Password"
			cssClass={enableCheck ? cssClasses.VTP[0].password : 'correct'}
		/>
		<Checkbox
			name="VTP-Pruning"
			bind:isChecked={userParameter.VTP[0]['pruning']}
			Heading="Enable VTP-Pruning"
		></Checkbox>
		{#if userParameter.VTP[0]['mode'] == 'Server'}
			<Checkbox
				name="VTP-Primary"
				bind:isChecked={userParameter.VTP[0]['is_primary']}
				Heading="VTP Primary"
			></Checkbox>
		{/if}
	{/if}

	{#if !enableVTP || userParameter.VTP[0].mode === 'Server'}
		<h2 class="subHeading" id="VLANs">VLANs</h2>
		{#each range(0, userParameter.VLAN.length - 1) as count}
			<VLAN
				cssClasses={cssClasses.VLAN[count]}
				check={enableConnectivityCheck}
				id={count}
				bind:number={userParameter.VLAN[count]['number']}
				bind:name={userParameter.VLAN[count]['name']}
			></VLAN>
		{/each}

		<button class="leftButton" on:click={addVLAN}>Add VLAN</button>
		<button class="rightButton" on:click={removeVLAN}>Remove VLAN</button>
	{/if}

	<h2 class="subHeading" id="STP">STP</h2>
	{#each range(0, userParameter.STP.length - 1) as count}
		<StpProcess
			cssClasses={cssClasses.STP[count]}
			check={enableCheck}
			id={count + 1}
			parameters={userParameter.STP[count]}
		></StpProcess>
	{/each}
	<button class="leftButton" on:click={addSTPProcess}>Add STP Process</button>
	<button class="rightButton" on:click={removeSTPProcess}>Remove STP Process </button>
	<EdgeInterfaces
		check={enableCheck}
		bind:edgeInterfaces={userParameter.EdgePorts}
		InterfaceCssClasses={cssClasses.EdgePorts}
	></EdgeInterfaces>

	<h2 class="subHeading" id="Interfaces">Interfaces</h2>
	<h2 class="subSubHeading">Trunks</h2>
	<TrunkInterface
		check={enableCheck}
		cssClasses={cssClasses.Trunks}
		bind:trunks={userParameter.Trunks}
	></TrunkInterface>

	<h2 class="subSubHeading">Access Interfaces</h2>
	<AccessInterface
		check={enableCheck}
		cssClasses={cssClasses.AccessInterfaces}
		bind:accessInterfaces={userParameter.AccessInterfaces}
	></AccessInterface>
	<br />

	<h2 class="subHeading" id="Port-Security">Port-Security</h2>
	{#each range(0, userParameter.Portsecurity.length - 1) as count}
		<PortSecurityInterface
			check={enableCheck}
			cssClasses={cssClasses['Portsecurity'][count]}
			bind:parameters={userParameter.Portsecurity[count]}
			id={count}
		></PortSecurityInterface>
	{/each}
	<button on:click={addPortSecurityInterface} class="leftButton">Add Interface</button>
	<button on:click={removePortSecurityInterface} class="rightButton">Remove Interface</button>

	<h2 class="subHeading" id="Etherchannels">Etherchannels</h2>
	{#each range(0, userParameter.EtherChannels.length - 1) as count}
		<Etherchannel
			check={enableCheck}
			cssClasses={cssClasses.EtherChannels[count]}
			bind:parameters={userParameter.EtherChannels[count]}
			id={count}
		></Etherchannel>
	{/each}
	<button class="leftButton" on:click={addEtherChannel}>Add Etherchannel</button>
	<button class="rightButton" on:click={removeEtherChannel}>Remove Etherchannel</button>
	<br />
	<button class="generateSkriptButton" id="Submit" on:click={() => generateScript(true)}>
		Submit</button
	>
	<button class="generateRightButton" on:click={() => generateScript(false)}> Show Script</button>
	<button class="generateRightButton" on:click={resetInputs}>Reset Inputs</button>
</div>

{#if generate}
	<div id="textAreaDiv">
		{#if showScriptLoading}
			<br />

			<button
				disabled
				type="button"
				class="btn-loading text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 inline-flex items-center"
			>
				<svg
					aria-hidden="true"
					role="status"
					class="spinner inline w-4 h-4 mr-3 text-white animate-spin"
					viewBox="0 0 100 101"
					fill="none"
					xmlns="http://www.w3.org/2000/svg"
				>
					<path
						d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
						fill="#E5E7EB"
					></path>
					<path
						d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
						fill="currentColor"
					></path>
				</svg>
				Generating Script...
			</button>
		{/if}
		{#if script}
			{#each script as line}
				<p>{line}</p>
			{/each}
		{/if}
	</div>
{/if}

{#if showError}
	<div id="textAreaDiv">
		<h1 style="color: red">Es sind noch nicht alle Felder korrekt ausgefüllt!</h1>
		<p>Bitte überprüfen Sie die rot markierten Felder und füllen Sie diese korrekt aus!</p>
	</div>
{/if}
