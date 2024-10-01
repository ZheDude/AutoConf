<script>
	import '$lib/stylesheet.scss';
    /*
	import IconContainer from '$lib/Icons/Navbar/iconContainer.svelte';
    */
	import { afterNavigate } from '$app/navigation';

	let url = '/';
	afterNavigate((navigation) => {
		url = navigation.to.url.pathname.toString();
	});
</script>

<div class="pageDiv">
	<div id="navbar">
		<div class="navbarTextDiv">
			<a class={url === '/' ? 'aSelected' : 'aDefault'} href="/">Grundkonfig</a>
			<a class={url.startsWith('/Switchconfig') ? 'aSelected' : 'aDefault'} href="/Switchconfig">Switchconfig</a>
			<a class={url.startsWith('/Routerconfig') ? 'aSelected' : 'aDefault'} href="/Routerconfig">Routerconfig</a>
		</div>
	</div>
	<div class="mainDiv">
		<slot />
	</div>
</div>
