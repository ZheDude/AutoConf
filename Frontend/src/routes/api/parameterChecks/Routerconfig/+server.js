export async function POST({ request }) {
    let postData = await request.json();
    let inputParams = postData.userParameter;
    let cssClasses = postData.cssClasses;
    let isCorrect = true;
    const mappings = {
        OSPF: 1,
        'Key-Chain': 2,
        RIP: 3,
        BGP: 4,
        Interface: 0,
        'Static-Routes': 5,
        GRE: 6,
        HSRP: 7,
        DHCP: 8,
        SSH: 9
    };



    function range(start, end) {
        return Array.from({ length: end - start + 1 }, (_, i) => start + i);
    }
    function checkInterfaceName(name) {
        /*check if an Interface is valid */
        return name.match(/^(g|gi|gig|giga|gigab|gigabi|gigabit|gigabite|gigabitet|gigabithe|gigabither|gigabithernet)\s?([0-9]+\/[0-9]+)$/i) ||
            name.match(/^(f|fa|fas|fast|faste|fastet|fasteth|fastethe|fastether|fastethern|fastetherne|fastethernet)\s?([0-9]+\/[0-9]+)$/i) ||
            name.match(/^(l|lo|loo|loop|loopb|loopba|loopbac|loopback)\s?([0-9]+)$/i)

    }

    function checkIP(IP) {
        return IP.match(/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/)
    }

    function checkSubnetMask(mask) {
        return mask.match((/^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$/))
    }


    /* Interface validation */
    for (let i = 0; i < inputParams[mappings['Interface']]['Interface'].length; i++) {
        if (checkInterfaceName(inputParams[mappings['Interface']]['Interface'][i].interface)) {
            cssClasses[mappings['Interface']]['Interface'][i].interface = 'correct'
        } else {
            cssClasses[mappings['Interface']]['Interface'][i].interface = 'error'
            isCorrect = false;
        }

        if (checkIP(inputParams[mappings['Interface']]['Interface'][i].ip_address)) {
            cssClasses[mappings['Interface']]['Interface'][i].ip_address = 'correct'
        } else {
            cssClasses[mappings['Interface']]['Interface'][i].ip_address = 'error'
            isCorrect = false;
        }


        if (checkSubnetMask(inputParams[mappings['Interface']]['Interface'][i].subnetmask)) {
            cssClasses[mappings['Interface']]['Interface'][i].subnetmask = 'correct'
        } else {
            cssClasses[mappings['Interface']]['Interface'][i].subnetmask = 'error'
            isCorrect = false;
        }

        if (inputParams[mappings['Interface']]['Interface'][i].description != '') {
            cssClasses[mappings['Interface']]['Interface'][i].description = 'correct';
        } else {
            cssClasses[mappings['Interface']]['Interface'][i].description = 'error'
            isCorrect = false;
        }


        if (inputParams[mappings['Interface']]['Interface'][i].ospf != undefined) {

            if (inputParams[mappings['Interface']]['Interface'][i].ospf.area_id.match(/\d+$/)) {
                cssClasses[mappings['Interface']]['Interface'][i].ospf.area_id = 'correct'
            } else {
                cssClasses[mappings['Interface']]['Interface'][i].ospf.area_id = 'error';
                isCorrect = false;
            }

            if (inputParams[mappings['Interface']]['Interface'][i].ospf.cost.match(/\d+$/) &&
                (parseInt(inputParams[mappings['Interface']]['Interface'][i].ospf.cost) > 0
                    && parseInt(inputParams[mappings['Interface']]['Interface'][i].ospf.cost) <= 65535)) {
                cssClasses[mappings['Interface']]['Interface'][i].ospf.cost = 'correct'
            } else {
                cssClasses[mappings['Interface']]['Interface'][i].ospf.cost = 'error';
                isCorrect = false;
            }


            if (inputParams[mappings['Interface']]['Interface'][i].ospf.priority.match(/\d+$/) &&
                (parseInt(inputParams[mappings['Interface']]['Interface'][i].ospf.priority) >= 0
                    && parseInt(inputParams[mappings['Interface']]['Interface'][i].ospf.priority) <= 255)) {
                cssClasses[mappings['Interface']]['Interface'][i].ospf.priority = 'correct'
            } else {
                cssClasses[mappings['Interface']]['Interface'][i].ospf.priority = 'error';
                isCorrect = false;
            }

            if (inputParams[mappings['Interface']]['Interface'][i].ospf.authentication != undefined) {
                if (inputParams[mappings['Interface']]['Interface'][i].ospf.authentication.key_chain != '') {
                    cssClasses[mappings['Interface']]['Interface'][i].ospf.authentication.key_chain = 'correct';
                } else {
                    cssClasses[mappings['Interface']]['Interface'][i].ospf.authentication.key_chain = 'error';
                    isCorrect = false;
                }

            }
        }


    }
    /* Key Chain validation */
    for (let i = 0; i < inputParams[mappings['Key-Chain']]['Key-Chain'].length; i++) {
        if (inputParams[mappings['Key-Chain']]['Key-Chain'][i].number.match(/\d+$/)) {
            cssClasses[mappings['Key-Chain']]['Key-Chain'][i].number = 'correct';
        } else {
            cssClasses[mappings['Key-Chain']]['Key-Chain'][i].number = 'error';
            isCorrect = false;
        }


        if (inputParams[mappings['Key-Chain']]['Key-Chain'][i].name != '') {
            cssClasses[mappings['Key-Chain']]['Key-Chain'][i].name = 'correct';
        } else {
            cssClasses[mappings['Key-Chain']]['Key-Chain'][i].name = 'error';
            isCorrect = false;
        }

        if (inputParams[mappings['Key-Chain']]['Key-Chain'][i].password != '') {
            cssClasses[mappings['Key-Chain']]['Key-Chain'][i].password = 'correct';
        } else {
            cssClasses[mappings['Key-Chain']]['Key-Chain'][i].password = 'error';
            isCorrect = false;
        }
    }


    /* OSPF validation */
    for (let i = 0; i < inputParams[mappings['OSPF']]['OSPF'].length; i++) {
        if (inputParams[mappings['OSPF']]['OSPF'][i].process_id.match(/\d+$/)) {
            cssClasses[mappings['OSPF']]['OSPF'][i].process_id = 'correct';
        } else {
            cssClasses[mappings['OSPF']]['OSPF'][i].process_id = 'error';
            isCorrect = false;
        }


        if (checkIP(inputParams[mappings['OSPF']]['OSPF'][i].router_id)) {
            cssClasses[mappings['OSPF']]['OSPF'][i].router_id = 'correct'
        } else {
            cssClasses[mappings['OSPF']]['OSPF'][i].router_id = 'error'
            isCorrect = false;
        }


        if (inputParams[mappings['OSPF']]['OSPF'][i]['timer_dead'].match(/\d+$/)) {
            cssClasses[mappings['OSPF']]['OSPF'][i].timer_dead = 'correct';
        } else {
            cssClasses[mappings['OSPF']]['OSPF'][i].timer_dead = 'error';
            isCorrect = false;
        }

        if (inputParams[mappings['OSPF']]['OSPF'][i]['timer_hello'].match(/\d+$/)) {
            cssClasses[mappings['OSPF']]['OSPF'][i].timer_hello = 'correct';
        } else {
            cssClasses[mappings['OSPF']]['OSPF'][i].timer_hello = 'error';
            isCorrect = false;
        }

        for (let j = 0; j < inputParams[mappings['OSPF']]['OSPF'][i]['passive_interfaces'].length; j++) {
            if (checkInterfaceName(inputParams[mappings['OSPF']]['OSPF'][i].passive_interfaces[j])) {
                cssClasses[mappings['OSPF']]['OSPF'][i].passive_interfaces[j] = 'correct'
            } else {
                cssClasses[mappings['OSPF']]['OSPF'][i].passive_interfaces[j] = 'error'
                isCorrect = false;
            }
        }

        console.log(cssClasses[mappings['OSPF']]['OSPF'][i].passive_interfaces)


        for (let j = 0; j < inputParams[mappings['OSPF']]['OSPF'][i].networks.length; j++) {
            if (checkIP(inputParams[mappings['OSPF']]['OSPF'][i].networks[j].network)) {
                cssClasses[mappings['OSPF']]['OSPF'][i].networks[j].network = 'correct'
            } else {
                cssClasses[mappings['OSPF']]['OSPF'][i].networks[j].network = 'error'
                isCorrect = false;
            }

            if (inputParams[mappings['OSPF']]['OSPF'][i].networks[j].area_id.match(/\d+$/)) {
                cssClasses[mappings['OSPF']]['OSPF'][i].networks[j].area_id = 'correct';
            } else {
                cssClasses[mappings['OSPF']]['OSPF'][i].networks[j].area_id = 'error';
                isCorrect = false;
            }

            if (checkIP(inputParams[mappings['OSPF']]['OSPF'][i].networks[j].wildcard)) {
                cssClasses[mappings['OSPF']]['OSPF'][i].networks[j].wildcard = 'correct';
            } else {
                cssClasses[mappings['OSPF']]['OSPF'][i].networks[j].wildcard = 'error';
                isCorrect = false;
            }
        }


    }

    /* RIP validation */


    if (inputParams[mappings['RIP']]['RIP'].timer_update != undefined) {
        if (inputParams[mappings['RIP']]['RIP'].timer_update.match((/\d+$/))) {
            cssClasses[mappings['RIP']]['RIP'].timer_update = 'correct';
        } else {
            cssClasses[mappings['RIP']]['RIP'].timer_update = 'error';
            isCorrect = false;
        }

        for (let i = 0; i < inputParams[mappings['RIP']]['RIP'].networks.length; i++) {
            if (checkIP(inputParams[mappings['RIP']]['RIP'].networks[i].network)) {
                cssClasses[mappings['RIP']]['RIP'].networks[i].network = 'correct';

            } else {
                cssClasses[mappings['RIP']]['RIP'].networks[i].network = 'error';
                isCorrect = false;
            }
        }

    }


    /* BGP validation */
    console.log((inputParams[mappings['BGP']]))
    if (inputParams[mappings['BGP']]['BGP'].local_as != undefined) {

        if (inputParams[mappings['BGP']]['BGP'].local_as.match((/\d+$/))) {
            cssClasses[mappings['BGP']]['BGP'].local_as = 'correct';
        } else {
            cssClasses[mappings['BGP']]['BGP'].local_as = 'error';
            isCorrect = false;
        }


        if (inputParams[mappings['BGP']]['BGP'].hold_time.match((/\d+$/))) {
            cssClasses[mappings['BGP']]['BGP'].hold_time = 'correct';
        } else {
            cssClasses[mappings['BGP']]['BGP'].hold_time = 'error';
            isCorrect = false;
        }


        for (let i = 0; i < inputParams[mappings['BGP']]['BGP'].neighbor.length; i++) {
            if (checkIP(inputParams[mappings['BGP']]['BGP'].neighbor[i].ip_of_neighbor)) {
                cssClasses[mappings['BGP']]['BGP'].neighbor[i].ip_of_neighbor = 'correct';
            } else {

                cssClasses[mappings['BGP']]['BGP'].neighbor[i].ip_of_neighbor = 'error';
                isCorrect = false;
            }


            if (inputParams[mappings['BGP']]['BGP'].neighbor[i].as.match(/\d+$/)) {
                cssClasses[mappings['BGP']]['BGP'].neighbor[i].as = 'correct';
            } else {

                cssClasses[mappings['BGP']]['BGP'].neighbor[i].as = 'error';
                isCorrect = false;
            }


            if (checkInterfaceName(inputParams[mappings['BGP']]['BGP'].neighbor[i].update_source)) {
                cssClasses[mappings['BGP']]['BGP'].neighbor[i].update_source = 'correct';
            } else {
                cssClasses[mappings['BGP']]['BGP'].neighbor[i].update_source = 'error';
                isCorrect = false;
            }
        }

        for (let i = 0; i < inputParams[mappings['BGP']]['BGP'].networks.length; i++) {
            if (checkIP(inputParams[mappings['BGP']]['BGP'].networks[i].network)) {
                cssClasses[mappings['BGP']]['BGP'].networks[i].network = 'correct';
            } else {

                cssClasses[mappings['BGP']]['BGP'].networks[i].network = 'error';
                isCorrect = false;
            }


            if (checkSubnetMask(inputParams[mappings['BGP']]['BGP'].networks[i].subnetmask)) {
                cssClasses[mappings['BGP']]['BGP'].networks[i].subnetmask = 'correct';
            } else {

                cssClasses[mappings['BGP']]['BGP'].networks[i].subnetmask = 'error';
                isCorrect = false;
            }
        }
    }


    /* static route check */

    console.log(inputParams[mappings['Static-Routes']]['Static-Routes'])
    for (let i = 0; i < inputParams[mappings['Static-Routes']]['Static-Routes'].length; i++) {
        if (checkIP(inputParams[mappings['Static-Routes']]['Static-Routes'][i].source)) {
            cssClasses[mappings['Static-Routes']]['Static-Routes'][i].source = 'correct';

        } else {
            isCorrect = false;
            cssClasses[mappings['Static-Routes']]['Static-Routes'][i].source = 'error';
        }


        if (checkSubnetMask(inputParams[mappings['Static-Routes']]['Static-Routes'][i].mask)) {
            cssClasses[mappings['Static-Routes']]['Static-Routes'][i].mask = 'correct';

        } else {
            isCorrect = false;
            cssClasses[mappings['Static-Routes']]['Static-Routes'][i].mask = 'error';
        }


        if (inputParams[mappings['Static-Routes']]['Static-Routes'][i].distance.match(/\d+$/) &&
            (parseInt(inputParams[mappings['Static-Routes']]['Static-Routes'][i].distance) > 0) &&
            parseInt(inputParams[mappings['Static-Routes']]['Static-Routes'][i].distance) <= 255) {
            cssClasses[mappings['Static-Routes']]['Static-Routes'][i].distance = 'correct'
        } else {
            cssClasses[mappings['Static-Routes']]['Static-Routes'][i].distance = 'error';
            isCorrect = false;
        }



        if (inputParams[mappings['Static-Routes']]['Static-Routes'][i].destination == '' && inputParams[mappings['Static-Routes']]['Static-Routes'][i].interface == '') {
            isCorrect = false;
            cssClasses[mappings['Static-Routes']]['Static-Routes'][i].destination = 'error';
            cssClasses[mappings['Static-Routes']]['Static-Routes'][i].interface = 'error';
        } else {

            if (checkIP(inputParams[mappings['Static-Routes']]['Static-Routes'][i].destination) || inputParams[mappings['Static-Routes']]['Static-Routes'][i].destination == '') {
                cssClasses[mappings['Static-Routes']]['Static-Routes'][i].destination = 'correct';
            } else {
                cssClasses[mappings['Static-Routes']]['Static-Routes'][i].destination = 'error';
                isCorrect = false;
            }


            if (checkInterfaceName(inputParams[mappings['Static-Routes']]['Static-Routes'][i].interface) || inputParams[mappings['Static-Routes']]['Static-Routes'][i].interface == '') {
                cssClasses[mappings['Static-Routes']]['Static-Routes'][i].interface = 'correct';
            } else {
                cssClasses[mappings['Static-Routes']]['Static-Routes'][i].interface = 'error';
                isCorrect = false;
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










