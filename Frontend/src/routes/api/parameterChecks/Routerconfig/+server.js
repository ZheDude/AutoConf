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

    console.log(cssClasses[mappings['Interface']])


    function range(start, end) {
        return Array.from({ length: end - start + 1 }, (_, i) => start + i);
    }
    function checkInterfaceName(name) {
        /*check if an Interface is valid */
        return name.match(/^(g|gi|gig|giga|gigab|gigabi|gigabit|gigabite|gigabitet|gigabithe|gigabither|gigabithernet)\s?([0-9]+\/[0-9]+)$/i) ||
            name.match(/^(f|fa|fas|fast|faste|fastet|fasteth|fastethe|fastether|fastethern|fastetherne|fastethernet)\s?([0-9]+\/[0-9]+)$/i)

    }

    function checkIP(IP){
        return IP.match(/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/)
    }

    for (let i = 0; i < inputParams[mappings['Interface']]['Interface'].length; i++) {
        if (checkInterfaceName(inputParams[mappings['Interface']]['Interface'][i].interface)) {
            cssClasses[mappings['Interface']]['Interface'][i].interface = 'correct'
        } else {
            cssClasses[mappings['Interface']]['Interface'][i].interface = 'error'
            isCorrect = false;
        }

        if (checkIP(inputParams[mappings['Interface']]['Interface'][i].ip_address)){
            cssClasses[mappings['Interface']]['Interface'][i].ip_address = 'correct'
        }else{
            cssClasses[mappings['Interface']]['Interface'][i].ip_address = 'error'
            isCorrect = false;
        }
        



    }










    let apiReturn = { cssClasses: cssClasses, isCorrect: isCorrect }
    return new Response(JSON.stringify(apiReturn), {
        headers: {
            'Content-Type': 'application/json'
        }
    });
}