<script>
    import InputField from '../../lib/components/inputField.svelte';
    export let params = {
        ip: '',
        username: '',
        password: ''
    }
</script>

<InputField
		placeholder="192.168.10.10"
		type="text"
		bind:value={params.ip}
		fieldName="SSH-IP"
		id="SSH-IP"
	/>

	<InputField
		placeholder="cisco"
		type="text"
		bind:value={params.username}
		fieldName="SSH-Username"
		id="SSH-Username"
	/>

	<InputField
		placeholder=""
		type="password"
		bind:value={params.password}
		fieldName="SSH-Password"
		id="SSH-Password"
	/>
