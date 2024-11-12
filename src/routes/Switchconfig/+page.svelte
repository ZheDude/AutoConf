<script>
	import '$lib/stylesheet.css';
	import InputField from '../../lib/components/inputField.svelte';
	import Dropdown from '../../lib/components/dropdown.svelte';
	import Checkbox from '../../lib/components/checkbox.svelte';
	import VLAN from '../../lib/components/Switch/vlan.svelte';
	import TrunkInterface from '../../lib/components/Switch/trunk-interface.svelte';
	import Etherchannel from '../../lib/components/Switch/etherchannel.svelte';
	import AccessInterface from '../../lib/components/Switch/access-interface.svelte';
</script>

<div id="parameterDivGrundkonfig">
	<div class="mainHeading">
		<h1>Switchconfig</h1>
	</div>
	<h2 class="subHeading">VTP</h2>
	<Checkbox name="enableVTP" Heading="Enable VTP"></Checkbox>
	<Dropdown options={['Server', 'Client', 'Transparent']} fieldName="DropdownVTP" Heading="Mode:"
	></Dropdown>

	<InputField placeholder="corp.at" type="text" fieldName="VTP-Domain" id="VTP-Domain" />
	<InputField placeholder="" type="password" fieldName="VTP-Password" id="VTP-Password" />

	<InputField placeholder="corp.at" type="text" fieldName="VTP-Domain" id="VTP-Domain" /><InputField
		placeholder="corp.at"
		type="text"
		fieldName="VTP-Domain"
		id="VTP-Domain"
	/>
	<Checkbox name="VTP-Pruning" Heading="Enable VTP-Pruning"></Checkbox>

	<Checkbox name="VTP-Primary" Heading="VTP Primary"></Checkbox>
	<h2 class="subHeading">VLANs</h2>
	<VLAN id="1"></VLAN>

	<button class="VtyButton">Add VLAN</button>

	<h2 class="subHeading">Interfaces</h2>
	<h2 class="subHeading">Trunks</h2>
	<TrunkInterface id="1" interfaceRange="true"></TrunkInterface>

	<br />
	<button class="VtyButton">Add Interface</button>
	<button class="VtyButton">Add Interface Range</button>

	<h2 class="subHeading">Access Interfaces</h2>
	<AccessInterface id="1" interfaceRange="true"></AccessInterface>
	<br />
	<button class="VtyButton">Add Interface</button>
	<button class="VtyButton">Add Interface Range</button>


	<h2 class="subHeading">Etherchannels</h2>
	<Etherchannel id={1} interfaceRange=false></Etherchannel>

	<br />
</div>
