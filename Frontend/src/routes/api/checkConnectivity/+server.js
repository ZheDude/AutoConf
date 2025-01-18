export async function POST({ request }) {
    let inputParams = await request.json();


    let apiReturn = {ip: 'correct', username: 'correct', password: 'correct', isReachable: true}



    const response = await fetch('http://127.0.0.1:8000/metadata/switch?ip=' + inputParams.userParameter.ip+ '&username='
         +inputParams.userParameter.username + '&password=' + inputParams.userParameter.password , {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    });
    
    let returnOfCheck = await response.json();


    apiReturn.isReachable = returnOfCheck[0] == 'Connection successfull';
    console.log(apiReturn.isReachable)
    console.log(returnOfCheck)

    function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}




    if (!inputParams.userParameter.ip.match(
        
        /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/
    ) || inputParams.userParameter.ip === ''){
        apiReturn.ip = 'error';
        apiReturn.isReachable = false;
    }


    if (inputParams.userParameter.username.trim() === '' ){
        apiReturn.username = 'error';
        apiReturn.isReachable = false;
    }

    if (inputParams.userParameter.password.trim() === '' ){
        apiReturn.password = 'error';
        apiReturn.isReachable = false;
    }


    return new Response(JSON.stringify(apiReturn), {
        headers: {
            'Content-Type': 'application/json'
        }
    });

}