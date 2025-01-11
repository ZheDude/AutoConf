export async function POST({ request }) {
    let postData = await request.json();
    let inputParams = postData.userParameter;
    let cssClasses = postData.cssClasses;
    let isCorrect = true;

    function range(start, end) {
        return Array.from({ length: end - start + 1 }, (_, i) => start + i);
    }


    function checkInterfaceName(name) {
        /*check if an Interface is valid */
        return name.match(/^(g|gi|gig|giga|gigab|gigabi|gigabit|gigabite|gigabitet|gigabithe|gigabither|gigabithernet)\s?([0-9]+\/[0-9]+)$/i) ||
            name.match(/^(f|fa|fas|fast|faste|fastet|fasteth|fastethe|fastether|fastethern|fastetherne|fastethernet)\s?([0-9]+\/[0-9]+)$/i)

    }


    /* validation check for VTP */
    if (inputParams.VTP.length > 0) {
        if (inputParams.VTP[0].password === '') {

            cssClasses.VTP[0].password = 'error';
            isCorrect = false;
        } else {
            cssClasses.VTP[0].password = 'correct';
        }

        if (inputParams.VTP[0].domain === '') {
            cssClasses.VTP[0].domain = 'error';
            isCorrect = false;
        } else {
            cssClasses.VTP[0].domain = 'correct';
        }



    }



    /* validation check for VLANs */
    for (let i = 0; i < inputParams.VLAN.length; i++) {
        if (inputParams.VLAN[i].name === '' || !inputParams.VLAN[i].name.match(/^[A-Za-z0-9_-]{1,32}$/)) {
            cssClasses.VLAN[i].name = 'error';
            isCorrect = false;
        } else {
            cssClasses.VLAN[i].name = 'correct';
        }


        let regex = /^[0-9]+$/
        if (!regex.test(inputParams.VLAN[i].number) || !(parseInt(inputParams.VLAN[i].number, 10) >= 2 && parseInt(inputParams.VLAN[i].number, 10) <= 1001)) {
            cssClasses.VLAN[i].number = 'error';
            isCorrect = false;
        } else {
            cssClasses.VLAN[i].number = 'correct';
        }


    }


    /* validation check for STP */
    for (let i = 0; i < inputParams.STP.length; i++) {
        let regex = /^[0-9]+$/
        if (regex.test(inputParams.STP[i].priority)) {
            let priority = parseInt(inputParams.STP[i].priority, "soos");
            if (priority === 0 || (priority % 4096 === 0 && priority <= 61440)) {
                cssClasses.STP[i].priority = 'correct';

            } else {
                cssClasses.STP[i].priority = 'error';
                isCorrect = false;
            }
        } else {
            cssClasses.STP[i].priority = 'error';
            isCorrect = false;
        }



        if (regex.test(inputParams.STP[i].hello_timer)) {
            let hello_timer = parseInt(inputParams.STP[i].hello_timer);
            if (hello_timer >= 1 && hello_timer <= 10) {
                cssClasses.STP[i].hello_timer = 'correct';
            } else {
                cssClasses.STP[i].hello_timer = 'error';
                isCorrect = false;
            }
        } else {
            cssClasses.STP[i].hello_timer = 'error';
            isCorrect = false;
        }


        if (regex.test(inputParams.STP[i].forward_timer)) {
            let forward_timer = parseInt(inputParams.STP[i].forward_timer);
            if (forward_timer >= 4 && forward_timer <= 30) {
                cssClasses.STP[i].forward_timer = 'correct';
            } else {
                cssClasses.STP[i].forward_timer = 'error';
                isCorrect = false;
            }
        } else {
            cssClasses.STP[i].forward_timer = 'error';
            isCorrect = false;
        }




        if (regex.test(inputParams.STP[i].max_age)) {
            let max_age = parseInt(inputParams.STP[i].max_age);
            if (max_age >= 6 && max_age <= 40) {
                cssClasses.STP[i].max_age = 'correct';
            } else {
                cssClasses.STP[i].max_age = 'error';
                isCorrect = false;
            }
        } else {
            cssClasses.STP[i].max_age = 'error';
            isCorrect = false;
        }
        let vlanRegex = /^\d{1,4}(?:\s*,\s*\d{1,4})*\s*\s*$/

        if (vlanRegex.test(inputParams.STP[i].vlan)) {
            cssClasses.STP[i].vlan = 'correct';


        } else {
            isCorrect = false;
            cssClasses.STP[i].vlan = 'error';
        }

    }


    /* validation check for EdgePorts */
    for (let i = 0; i < inputParams.EdgePorts.Interfaces.length; i++) {
        let currentInterface = inputParams.EdgePorts.Interfaces[i];
        if (checkInterfaceName(currentInterface.name)) {
            cssClasses.EdgePorts.Interfaces[i].name = 'correct'
        } else {
            cssClasses.EdgePorts.Interfaces[i].name = 'error';
            isCorrect = false;
        }
    }





    for (let i = 0; i < inputParams.EdgePorts.InterfaceRanges.length; i++) {
        let currentInterfaceRange = inputParams.EdgePorts.InterfaceRanges[i];
        if (checkInterfaceName(currentInterfaceRange.startInterface)) {
            cssClasses.EdgePorts.InterfaceRanges[i].startInterface = 'correct';
        } else {
            cssClasses.EdgePorts.InterfaceRanges[i].startInterface = 'error';
            isCorrect = false;
        }


        if (checkInterfaceName(currentInterfaceRange.endInterface)) {
            cssClasses.EdgePorts.InterfaceRanges[i].endInterface = 'correct';
        } else {
            cssClasses.EdgePorts.InterfaceRanges[i].endInterface = 'error';
            isCorrect = false;
        }
    }


    /* validation check for Trunks */
    for (let i = 0; i < inputParams.Trunks.Interfaces.length; i++) {

        if (checkInterfaceName(inputParams.Trunks.Interfaces[i].name)) {

            cssClasses.Trunks.Interfaces[i].name = 'correct';
        } else {
            cssClasses.Trunks.Interfaces[i].name = 'error';
            isCorrect = false;
        }


        let vlanRegex = /^\d{1,4}(?:\s*,\s*\d{1,4})*\s*\s*$/

        if (vlanRegex.test(inputParams.Trunks.Interfaces[i].allowed_vlan)) {
            cssClasses.Trunks.Interfaces[i].allowed_vlan = 'correct';
        } else {
            isCorrect = false;
            cssClasses.Trunks.Interfaces[i].allowed_vlan = 'error';
        }


        let regex = /^[0-9]+$/
        if (!regex.test(inputParams.Trunks.Interfaces[i].native_vlan) || !(parseInt(inputParams.Trunks.Interfaces[i].native_vlan, 10) >= 2 && parseInt(inputParams.Trunks.Interfaces[i].native_vlan, 10) <= 1001)) {
            cssClasses.Trunks.Interfaces[i].native_vlan = 'error';
            isCorrect = false;
        } else {
            cssClasses.Trunks.Interfaces[i].native_vlan = 'correct';
        }
    }



    for (let i = 0; i < inputParams.Trunks.InterfaceRanges.length; i++) {

        if (checkInterfaceName(inputParams.Trunks.InterfaceRanges[i].startInterface)) {

            cssClasses.Trunks.InterfaceRanges[i].startInterface = 'correct';
        } else {
            cssClasses.Trunks.InterfaceRanges[i].startInterface = 'error';
            isCorrect = false;
        }

        if (checkInterfaceName(inputParams.Trunks.InterfaceRanges[i].endInterface)) {

            cssClasses.Trunks.InterfaceRanges[i].endInterface = 'correct';
        } else {
            cssClasses.Trunks.InterfaceRanges[i].endInterface = 'error';
            isCorrect = false;
        }


        let vlanRegex = /^\d{1,4}(?:\s*,\s*\d{1,4})*\s*\s*$/

        if (vlanRegex.test(inputParams.Trunks.InterfaceRanges[i].allowed_vlan)) {
            cssClasses.Trunks.InterfaceRanges[i].allowed_vlan = 'correct';
        } else {
            isCorrect = false;
            cssClasses.Trunks.InterfaceRanges[i].allowed_vlan = 'error';
        }


        let regex = /^[0-9]+$/
        if (!regex.test(inputParams.Trunks.InterfaceRanges[i].native_vlan) || !(parseInt(inputParams.Trunks.InterfaceRanges[i].native_vlan, 10) >= 2 && parseInt(inputParams.Trunks.InterfaceRanges[i].native_vlan, 10) <= 1001)) {
            cssClasses.Trunks.InterfaceRanges[i].native_vlan = 'error';
            isCorrect = false;
        } else {
            cssClasses.Trunks.InterfaceRanges[i].native_vlan = 'correct';
        }
    }


    /* validation check for AccessInterfaces */
    for (let i = 0; i < inputParams.AccessInterfaces['Interfaces'].length; i++) {
        if (checkInterfaceName(inputParams.AccessInterfaces.Interfaces[i].name)) {

            cssClasses.AccessInterfaces.Interfaces[i].name = 'correct';
        } else {

            cssClasses.AccessInterfaces.Interfaces[i].name = 'error';
            isCorrect = false;
        }

        let regex = /^[0-9]+$/
        if (!regex.test(inputParams.AccessInterfaces.Interfaces[i].vlan) || !(parseInt(inputParams.AccessInterfaces.Interfaces[i].vlan, 10) >= 2 && parseInt(inputParams.AccessInterfaces.Interfaces[i].vlan, 10) <= 1001)) {
            cssClasses.AccessInterfaces.Interfaces[i].vlan = 'error';
            isCorrect = false;
        } else {
            cssClasses.AccessInterfaces.Interfaces[i].vlan = 'correct';
        }
    }



    for (let i = 0; i < inputParams.AccessInterfaces['InterfaceRanges'].length; i++) {
        if (checkInterfaceName(inputParams.AccessInterfaces.InterfaceRanges[i].startInterface)) {

            cssClasses.AccessInterfaces.InterfaceRanges[i].startInterface = 'correct';
        } else {

            cssClasses.AccessInterfaces.InterfaceRanges[i].startInterface = 'error';
            isCorrect = false;
        }


        if (checkInterfaceName(inputParams.AccessInterfaces.InterfaceRanges[i].endInterface)) {

            cssClasses.AccessInterfaces.InterfaceRanges[i].endInterface = 'correct';
        } else {

            cssClasses.AccessInterfaces.InterfaceRanges[i].endInterface = 'error';
            isCorrect = false;
        }

        let regex = /^[0-9]+$/
        if (!regex.test(inputParams.AccessInterfaces.InterfaceRanges[i].vlan) || !(parseInt(inputParams.AccessInterfaces.InterfaceRanges[i].vlan, 10) >= 2 && parseInt(inputParams.AccessInterfaces.InterfaceRanges[i].vlan, 10) <= 1001)) {
            cssClasses.AccessInterfaces.InterfaceRanges[i].vlan = 'error';
            isCorrect = false;
        } else {
            cssClasses.AccessInterfaces.InterfaceRanges[i].vlan = 'correct';
        }
    }


    /* validation check for PortSecurity */
    for (let i = 0; i < inputParams.Portsecurity.length; i++) {
        if (checkInterfaceName(inputParams.Portsecurity[i].interface)) {
            cssClasses.Portsecurity[i].interface = 'correct';
        } else {
            cssClasses.Portsecurity[i].interface = 'error';
            isCorrect = false;
        }


        let regex = /^[0-9]+$/
        if (!regex.test(inputParams.Portsecurity[i].maximum) || !(parseInt(inputParams.Portsecurity[i].maximum, 10) >= 0 && parseInt(inputParams.Portsecurity[i].maximum, 10) <= 132)) {
            cssClasses.Portsecurity[i].maximum = 'error';
            isCorrect = false;
        } else {
            cssClasses.Portsecurity[i].maximum = 'correct';
        }



        if (inputParams.Portsecurity[i].mac_address === 'sticky' || inputParams.Portsecurity[i].mac_address.match(/^([0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2}$|^[0-9A-Fa-f]{4}([.-])[0-9A-Fa-f]{4}\1[0-9A-Fa-f]{4}$/)) {

            cssClasses.Portsecurity[i].mac_address = 'correct';
        } else {
            cssClasses.Portsecurity[i].mac_address = 'error';
            isCorrect = false;
        }

    }

        /* validation check for EtherChannels */
    for (let i = 0; i < inputParams.EtherChannels.length; i++) {
        if (inputParams.EtherChannels[i].Interfaces.length == 0 && inputParams.EtherChannels[i].InterfaceRanges.length == 0) {
            isCorrect = false;
        }


        let regex = /^[0-9]+$/
        if (!regex.test(inputParams.EtherChannels[i].number) || !(parseInt(inputParams.EtherChannels[i].number, 10) > 0 && parseInt(inputParams.EtherChannels[i].number, 10) <= 8)) {
            cssClasses.EtherChannels[i].number = 'error';
            isCorrect = false;
        } else {
            cssClasses.EtherChannels[i].number = 'correct';
        }


        for (let j = 0; j < inputParams.EtherChannels[i].Interfaces.length; j++) {
            if (checkInterfaceName(inputParams.EtherChannels[i].Interfaces[j].name)) {

                cssClasses.EtherChannels[i].Interfaces[j].name = 'correct';
            } else {
                isCorrect = false;
                cssClasses.EtherChannels[i].Interfaces[j].name = 'error';
            }

        }



        for (let j = 0; j < inputParams.EtherChannels[i].InterfaceRanges.length; j++) {
            if (checkInterfaceName(inputParams.EtherChannels[i].InterfaceRanges[j].startInterface)) {

                cssClasses.EtherChannels[i].InterfaceRanges[j].startInterface = 'correct';
            } else {
                isCorrect = false;
                cssClasses.EtherChannels[i].InterfaceRanges[j].startInterface = 'error';
            }

        }

        for (let j = 0; j < inputParams.EtherChannels[i].InterfaceRanges.length; j++) {
            if (checkInterfaceName(inputParams.EtherChannels[i].InterfaceRanges[j].endInterface)) {

                cssClasses.EtherChannels[i].InterfaceRanges[j].endInterface = 'correct';
            } else {
                isCorrect = false;
                cssClasses.EtherChannels[i].InterfaceRanges[j].endInterface = 'error';
            }

        }



    }

    let apiReturn = { cssClasses: cssClasses, isCorrect: isCorrect }
    return new Response(JSON.stringify(apiReturn), {
        headers: {
            'Content-Type': 'application/json'
        }
    });
}