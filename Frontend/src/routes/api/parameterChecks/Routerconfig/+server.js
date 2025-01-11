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

    console.log(cssClasses[mappings['Interface']]['Interface'][0].ospf)


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
    
    function checkSubnetMask(mask){
        return mask.match((/^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$/))
    }


    /* Interface validaiton */
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
        

        if (checkSubnetMask(inputParams[mappings['Interface']]['Interface'][i].subnetmask)){
            cssClasses[mappings['Interface']]['Interface'][i].subnetmask = 'correct'
        }else{
            cssClasses[mappings['Interface']]['Interface'][i].subnetmask = 'error'
            isCorrect = false;
        }

        if (inputParams[mappings['Interface']]['Interface'][i].description != ''){
            cssClasses[mappings['Interface']]['Interface'][i].description = 'correct';
        }else{
            cssClasses[mappings['Interface']]['Interface'][i].description = 'error'
            isCorrect = false;
        }


        if(inputParams[mappings['Interface']]['Interface'][i].ospf != undefined){
            
            if (inputParams[mappings['Interface']]['Interface'][i].ospf.area_id.match(/\d+$/)){
                cssClasses[mappings['Interface']]['Interface'][i].ospf.area_id = 'correct'
            }else{
                cssClasses[mappings['Interface']]['Interface'][i].ospf.area_id = 'error';
                isCorrect = false;
            }

            if (inputParams[mappings['Interface']]['Interface'][i].ospf.cost.match(/\d+$/) && 
            (parseInt(inputParams[mappings['Interface']]['Interface'][i].ospf.cost) > 0 
            && parseInt(inputParams[mappings['Interface']]['Interface'][i].ospf.cost)  <= 65535)){
                cssClasses[mappings['Interface']]['Interface'][i].ospf.cost = 'correct'
            }else{
                cssClasses[mappings['Interface']]['Interface'][i].ospf.cost = 'error';
                isCorrect = false;
            }


            if (inputParams[mappings['Interface']]['Interface'][i].ospf.priority.match(/\d+$/) && 
            (parseInt(inputParams[mappings['Interface']]['Interface'][i].ospf.priority) >= 0 
            && parseInt(inputParams[mappings['Interface']]['Interface'][i].ospf.priority)  <= 255)){
                cssClasses[mappings['Interface']]['Interface'][i].ospf.priority = 'correct'
            }else{
                cssClasses[mappings['Interface']]['Interface'][i].ospf.priority = 'error';
                isCorrect = false;
            }

            if (inputParams[mappings['Interface']]['Interface'][i].ospf.authentication != undefined){
                if (inputParams[mappings['Interface']]['Interface'][i].ospf.authentication.key_chain != ''){
                    cssClasses[mappings['Interface']]['Interface'][i].ospf.authentication.key_chain = 'correct'; 
                }else{
                    cssClasses[mappings['Interface']]['Interface'][i].ospf.authentication.key_chain = 'error'; 
                    isCorrect = false;
                }

            }


        }

        for(let i = 0; i < inputParams[mappings['Key-Chain']]['Key-Chain'].length; i++){
            if (inputParams[mappings['Key-Chain']]['Key-Chain'][i].number.match(/\d+$/)){
                cssClasses[mappings['Key-Chain']]['Key-Chain'][i].number = 'correct';
            }else{
                cssClasses[mappings['Key-Chain']]['Key-Chain'][i].number = 'error';
                isCorrect = false;
            }


            if (inputParams[mappings['Key-Chain']]['Key-Chain'][i].name != ''){
                cssClasses[mappings['Key-Chain']]['Key-Chain'][i].name = 'correct';
            }else{
                cssClasses[mappings['Key-Chain']]['Key-Chain'][i].name = 'error';
                isCorrect = false;
            }

            if (inputParams[mappings['Key-Chain']]['Key-Chain'][i].password != ''){
                cssClasses[mappings['Key-Chain']]['Key-Chain'][i].password = 'correct';
            }else{
                cssClasses[mappings['Key-Chain']]['Key-Chain'][i].password = 'error';
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