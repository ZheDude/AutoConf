<script>
	import '$lib/stylesheet.css';
	/*
	import IconContainer from '$lib/Icons/Navbar/iconContainer.svelte';
    */
	import { afterNavigate } from '$app/navigation';
	import GrundkonfigIcon from '$lib/components/icons/GrundkonfigIcon.svelte';
	import RouterIcon from '$lib/components/icons/RouterIcon.svelte';
	import SwitchIcon from '$lib/components/icons/SwitchIcon.svelte';

	let url = '/';
	afterNavigate((navigation) => {
		url = navigation.to.url.pathname.toString();
		console.log(url)
	});


</script>

<div class="pageDiv">
	<div id="navbar">
		<div class="navbarTextDiv">
			<a class={url === '/' ? 'aSelected' : 'aDefault'} href="/">Grundkonfig</a>
			<a class={url.startsWith('/Switchconfig') ? 'aSelected' : 'aDefault'} href="/Switchconfig">Switchconfig</a>
			<a class={url.startsWith('/Routerconfig') ? 'aSelected' : 'aDefault'} href="/Routerconfig">Routerconfig</a>
		</div>
		<div id="iconDiv">
			<a href="/">
				<GrundkonfigIcon color={url === '/' ? '#A9DFD8' : '#87888C'}></GrundkonfigIcon>
			</a>
			<a href="/Switchconfig">
				<SwitchIcon color={url === '/Switchconfig' ? '#A9DFD8' : '#87888C'}></SwitchIcon>
			</a>
			<a href="/Routerconfig">
			<RouterIcon color={url === '/Routerconfig' ? '#A9DFD8' : '#87888C'}></RouterIcon>
			</a>
		</div>
	</div>

	<div class="mainDiv">
		<slot />
	</div>
</div>
