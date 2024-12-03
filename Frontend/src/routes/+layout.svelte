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
		<SwitchIcon {url}></SwitchIcon>
		<RouterIcon {url}></RouterIcon>
	</div>
	</div>

	<div class="mainDiv">
		<slot />
	</div>
</div>
