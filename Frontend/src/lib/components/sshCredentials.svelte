<script>
    import InputField from '../../lib/components/inputField.svelte';
	export let connectivityCheck;
    export let params = {
        ip: '',
        username: '',
        password: ''
    }

	export let cssClasses = {
		}

	let divClass = '';
	$:{

		
	if (cssClasses['ip'] != 'correct' || cssClasses['username'] != 'correct' || cssClasses['password'] != 'correct'){
		divClass = 'SSHDivDefault';
	}else if (cssClasses['isReachable'] === true){
		divClass = 'SSHDivCorrect';
	}else{
		divClass = 'SSHDivError';
	}

}

</script>
<div class={divClass}> 


<InputField
		placeholder="192.168.10.10"
		type="text"
		bind:value={params.ip}
		fieldName="SSH-IP"
		id="SSH-IP"
		cssClass={connectivityCheck ? cssClasses['ip'] : 'correct'}
	/>

	<InputField
		placeholder="cisco"
		type="text"
		bind:value={params.username}
		fieldName="SSH-Username"
		id="SSH-Username"
		cssClass={connectivityCheck ? cssClasses['username'] : 'correct'}
	/>

	<InputField
		placeholder=""
		type="password"
		bind:value={params.password}
		fieldName="SSH-Password"
		id="SSH-Password"
		cssClass={connectivityCheck ? cssClasses['password'] : 'correct'}
	/>
</div>