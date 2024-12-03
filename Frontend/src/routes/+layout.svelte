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
				<ul><a href="#section1">Console Interface</a></ul>
				<br />
				<ul><a href="#section2">Management Interface</a></ul>
				<br />
				<ul><a href="#vtyMainDiv">VTY Lines</a></ul>
			{/if}

			<SwitchIcon {url}></SwitchIcon>
			{#if url == '/Switchconfig'}
				<ul><a href="#section1">VTP</a></ul>
				<br />
				<ul><a href="#section2">VLANs</a></ul>
				<br />
				<ul><a href="#section3">STP</a></ul>
				<br />
				<ul><a href="#section3">Interfaces</a></ul>
				<br />
				<ul><a href="#section3">Port-Security</a></ul>
				<br />
				<ul><a href="#section3">Etherchannels</a></ul>
			{/if}
			<RouterIcon {url}></RouterIcon>
			{#if url == '/Routerconfig'}
				<ul><a href="#section1">???</a></ul>
			{/if}
		</div>
	</div>

	<div class="mainDiv">
		<slot />
	</div>
</div>
