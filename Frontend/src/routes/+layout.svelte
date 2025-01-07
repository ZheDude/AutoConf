<script>
	import '$lib/stylesheet.css';
	/*
	import IconContainer from '$lib/Icons/Navbar/iconContainer.svelte';
    */
	import { afterNavigate } from '$app/navigation';
	import GrundkonfigIcon from '$lib/components/icons/GrundkonfigIcon.svelte';
	import RouterIcon from '$lib/components/icons/RouterIcon.svelte';
	import SwitchIcon from '$lib/components/icons/SwitchIcon.svelte';
	import GrundkonfigPage from '/src/routes/+page.svelte';
	import SwitchPage from '/src/routes/Switchconfig/+page.svelte';
	import RouterPage from '/src/routes/Routerconfig/+page.svelte';

	let url = '/';
	afterNavigate((navigation) => {
		url = navigation.to.url.pathname.toString();
		console.log(url);
	});
</script>

<div class="pageDiv">
	<div id="navbar">
		<div id="NavbarContent">
			<GrundkonfigIcon {url}></GrundkonfigIcon>
			{#if url == '/'}
				<ul><a href="#ConsoleInterface">Console Interface</a></ul>
				<br />
				<ul><a href="#ManagementInterface">Management Interface</a></ul>
				<br />
				<ul><a href="#VTYLines">VTY Lines</a></ul>
			{/if}

			<SwitchIcon {url}></SwitchIcon>
			{#if url == '/Switchconfig'}
				<ul><a href="#VTP">VTP</a></ul>
				<br />
				<ul><a href="#VLANs">VLANs</a></ul>
				<br />
				<ul><a href="#STP">STP</a></ul>
				<br />
				<ul><a href="#Interfaces">Interfaces</a></ul>
				<br />
				<ul><a href="#Port-Security">Port-Security</a></ul>
				<br />
				<ul><a href="#Etherchannels">Etherchannels</a></ul>
				<br />
				<ul><a href="#Submit"><strong>Submit</strong></a></ul>
			{/if}
			<RouterIcon {url}></RouterIcon>
			{#if url == '/Routerconfig'}
				<ul><a href="#Interfaces">Interfaces</a></ul>
				<br />
				<ul><a href="#Key-Chains">Key-Chains</a></ul>
				<br />
				<ul><a href="#OSPF">OSPF</a></ul>
				<br />
				<ul><a href="#RIP">RIP</a></ul>
				<br />
				<ul><a href="#BGP">BGP</a></ul>
				<br />
				<ul><a href="#StaticRoutes">Static Routes</a></ul>
				<br />
				<ul><a href="#GRE-Tunnels">GRE-Tunnels</a></ul>
				<br />
				<ul><a href="#HSRP">HSRP</a></ul>
				<br />
				<ul><a href="#DHCP">DHCP</a></ul>
			{/if}
		</div>
	</div>

	<div class="mainDiv">
		<slot />
	</div>
</div>
