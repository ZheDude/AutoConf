<script>
	import '$lib/stylesheet.css';
    import InputField from '../../lib/components/inputField.svelte';
	import Dropdown from '../../lib/components/dropdown.svelte';
	import Checkbox from '../../lib/components/checkbox.svelte';
	
</script>

<div id="parameterDivGrundkonfig">
	<div class="mainHeading">
		<h1>Switchconfig</h1>
	</div>

    <h2 class="subHeading">VLANs</h2>
    <InputField
    placeholder="10"
    type="text"
    fieldName="VLAN"
    id = "VLAN1"
    />
    <InputField
    placeholder="Management"
    type="text"
    fieldName="Name"
    id = "VLAN1"
    />
    <button>Add VLAN</button>



    <h2 class="subHeading">Interfaces</h2>
    <h2 class="subHeading">Trunks</h2>
    <InputField
    placeholder="Gig0/0"
    type="text"
    fieldName="Trunk-Interface:"
    id ="Trunk-Interface 1"/>
    <br>
    <button>Add Interface</button>
    <button>Add Interface Range</button>

    <h2 class="subHeading">Access Interfaces</h2>
    <InputField
    placeholder="Gig0/1"
    type="text"
    fieldName="Access-Interface:"
    id ="Access-Interface 1:"/>
    <br>
    <button>Add Interface</button>
    <button>Add Interface Range</button>
	

    <h2 class="subHeading">Etherchannels</h2>
    <InputField
    placeholder="1"
    type="text"
    fieldName="Channel-Group:"
    id ="Etherchannel 1"/>


    <InputField
    placeholder="Gig0/2"
    type="text"
    fieldName="Interface"
    id ="Etherchannel-Interface 1 "/>
    <br>
    <button>Add Interface</button>
    <button>Add Interface Range</button>

</div>


