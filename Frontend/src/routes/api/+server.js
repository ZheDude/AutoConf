export async function POST({ request }) {
    let inputParams = await request.json();
    function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}




    console.log(inputParams)
    const response = await fetch('http://127.0.0.1:8000/configuration/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: inputParams 
    });
    
    let returnOfResponse = await response.text();
    console.log(returnOfResponse)


    return new Response(JSON.stringify(returnOfResponse), {
        headers: {
            'Content-Type': 'application/json'
        }
    });

}