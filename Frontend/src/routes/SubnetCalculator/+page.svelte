<script>
	import '$lib/stylesheet.css';
	import InputField from '../../lib/components/inputField.svelte';
	import Dropdown from '../../lib/components/dropdown.svelte';
    import { onMount } from 'svelte';
	import { beforeNavigate } from '$app/navigation';
	let ip = '';
	let subnetmask = '0.0.0.0 /0';
    let showError = false;
    let calculatedInfos = {};
    let displayInfos = false;
	const subnetMasks = [
		'0.0.0.0 /0',
		'128.0.0.0 /1',
		'192.0.0.0 /2',
		'224.0.0.0 /3',
		'240.0.0.0 /4',
		'248.0.0.0 /5',
		'252.0.0.0 /6',
		'254.0.0.0 /7',
		'255.0.0.0 /8',
		'255.128.0.0 /9',
		'255.192.0.0 /10',
		'255.224.0.0 /11',
		'255.240.0.0 /12',
		'255.248.0.0 /13',
		'255.252.0.0 /14',
		'255.254.0.0 /15',
		'255.255.0.0 /16',
		'255.255.128.0 /17',
		'255.255.192.0 /18',
		'255.255.224.0 /19',
		'255.255.240.0 /20',
		'255.255.248.0 /21',
		'255.255.252.0 /22',
		'255.255.254.0 /23',
		'255.255.255.0 /24',
		'255.255.255.128 /25',
		'255.255.255.192 /26',
		'255.255.255.224 /27',
		'255.255.255.240 /28',
		'255.255.255.248 /29',
		'255.255.255.252 /30',
		'255.255.255.254 /31',
		'255.255.255.255 /32'
	];


    function saveToLocalStorage() {
		localStorage.setItem('ip', JSON.stringify(ip));
        localStorage.setItem('subnet', JSON.stringify(subnetmask));
	}


	beforeNavigate(() => {
		saveToLocalStorage();
	
	});

	onMount(() => {
		const savedIP = localStorage.getItem('ip');
        const savedSubnetMask = localStorage.getItem('subnet')
		if (savedIP) {
			ip = JSON.parse(savedIP);
		}

        if(savedSubnetMask){
            subnetmask = JSON.parse(savedSubnetMask);
        }
	});

	function isValidIPv4(ip) {
        const ipv4Regex = /^(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})\.(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})\.(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})\.(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})$/;
		return ipv4Regex.test(ip);
	}
	function calculateSubnetInfo(prefixLength, ipAddress) {
        displayInfos = false;
		if (!isValidIPv4(ipAddress)){
            showError = true;
            return;
        }
		
			// Convert IP to binary
			const ipToBinary = (ip) =>
				ip
					.split('.')
					.map((octet) => parseInt(octet, 10).toString(2).padStart(8, '0'))
					.join('');

			const binaryToIP = (binary) =>
				binary
					.match(/.{8}/g)
					.map((b) => parseInt(b, 2))
					.join('.');

			// Generate subnet mask from prefix
			const subnetMaskBinary = '1'.repeat(prefixLength).padEnd(32, '0');
			const subnetMask = binaryToIP(subnetMaskBinary);

			// Calculate network address
			const ipBinary = ipToBinary(ipAddress);
			const networkBinary = (BigInt('0b' + ipBinary) & BigInt('0b' + subnetMaskBinary))
				.toString(2)
				.padStart(32, '0');
			const networkAddress = binaryToIP(networkBinary);

			// Calculate broadcast address
			const broadcastBinary = (
				BigInt('0b' + networkBinary) |
				BigInt('0b' + '1'.repeat(32 - prefixLength).padStart(32, '0'))
			)
				.toString(2)
				.padStart(32, '0');
			const broadcastAddress = binaryToIP(broadcastBinary);

			// Calculate the number of possible hosts
			const hostBits = 32 - prefixLength;
			const numHosts = Math.max(2 ** hostBits - 2, 0); // Subtract 2 for network & broadcast

			calculatedInfos = {
				number_of_hosts: numHosts,
				network_address: networkAddress,
				broadcast_address: broadcastAddress
			};
            showError = false;
            displayInfos = true;
	}

</script>

<div id="parameterDivGrundkonfig">
	<div class="mainHeading">
		<h1>SubnetCalculator</h1>
	</div>
	<InputField
		placeholder="192.168.30.10"
		type="text"
		fieldName="IP-Address"
		id="IP-Address"
		bind:value={ip}
        cssClass={showError ? 'error' : 'correct'}
	/>
    {#if showError}
        <p style="color: red">Please provide a Valid IP-Address</p>
    {/if}

	<Dropdown options={subnetMasks} fieldName="subnetMask" Heading="Subnet:" bind:value={subnetmask}
	></Dropdown>
	<button
		class="generateSkriptButton"
		on:click={calculateSubnetInfo(subnetmask.split('/')[1].trim(), ip)}>Calculate</button
	>


  
</div>
{#if displayInfos && !showError}
<div id="textAreaDiv">

    <p>Netzaddresse: {calculatedInfos.network_address}</p>
    <p>Broadcastaddresse: {calculatedInfos.broadcast_address}</p>
    <p>Anzahl der möglichen Hosts: {calculatedInfos.number_of_hosts}</p>
</div>

{/if}
