export async function POST({ request }) {
    let inputParams = await request.json();

    function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

    let apiReturn = {ip: 'correct', username: 'correct', password: 'correct', isReachable: true}


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