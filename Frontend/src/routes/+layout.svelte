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
				<ui><a href="#section1">Console Interface</a></ui>
				<ui><a href="#section2">Management Interface</a></ui>
				<ui><a href="#vtyMainDiv">VTY Lines</a></ui>
			{/if}

			<SwitchIcon {url}></SwitchIcon>
			{#if url == '/Switchconfig'}
				<ui><a href="#section1">VTP</a></ui>
				<br />
				<ui><a href="#section2">VLANs</a></ui>
				<br />
				<ui><a href="#section3">STP</a></ui>
				<br />
				<ui><a href="#section3">Interfaces</a></ui>
				<br />
				<ui><a href="#section3">Port-Security</a></ui>
				<br />
				<ui><a href="#section3">Etherchannels</a></ui>
			{/if}
			<RouterIcon {url}></RouterIcon>
			{#if url == '/Routerconfig'}
				<ui><a href="#section1">???</a></ui>
			{/if}
		</div>
	</div>

	<div class="mainDiv">
		<slot />
	</div>
</div>
