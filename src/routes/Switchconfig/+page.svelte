<script>
	import '$lib/stylesheet.css';
	import InputField from '../../lib/components/inputField.svelte';
	import Dropdown from '../../lib/components/dropdown.svelte';
	import Checkbox from '../../lib/components/checkbox.svelte';
	import VLAN from '../../lib/components/Switch/vlan.svelte'
	import TrunkInterface  from '../../lib/components/Switch/trunk-interface.svelte';
	import Etherchannel from "../../lib/components/Switch/etherchannel.svelte"
</script>

<div id="parameterDivGrundkonfig">
	<div class="mainHeading">
		<h1>Switchconfig</h1>
	</div>
	<h2 class="subHeading">VLANs</h2>
	<VLAN id=1></VLAN>

	<button class="VtyButton">Add VLAN</button>

	<h2 class="subHeading">Interfaces</h2>
	<h2 class="subHeading">Trunks</h2>
	<TrunkInterface id=1 interfaceRange=true></TrunkInterface>
	
	<br />
	<button class="VtyButton">Add Interface</button>
	<button class="VtyButton">Add Interface Range</button>

	<h2 class="subHeading">Access Interfaces</h2>
	<InputField
		placeholder="Gig0/1"
		type="text"
		fieldName="Access-Interface:"
		id="Access-Interface 1:"
	/>

	<InputField
	placeholder="VLAN 10" type="text"  fieldName="VLAN" id></InputField>
	<br />
	<button class="VtyButton">Add Interface</button>
	<button class="VtyButton">Add Interface Range</button>

	<h2 class="subHeading">Etherchannels</h2>
	<Etherchannel></Etherchannel>



	<br />
	<button class="VtyButton">Add Interface</button>
	<button class="VtyButton" id="uniqueRight">Add Interface Range</button>


</div>
