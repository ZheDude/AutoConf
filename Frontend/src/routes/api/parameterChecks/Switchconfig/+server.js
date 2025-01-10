export async function POST({ request }) {
    let postData = await request.json();
    let inputParams = postData.userParameter;
    let cssClasses = postData.cssClasses;
    let isCorrect = true;
    function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

    if (inputParams.VTP.length > 0){
        if (inputParams.VTP[0].password === ''){

            console.log('soss')
            cssClasses.VTP[0].password = 'error';
            isCorrect = false;
        }else{
            cssClasses.VTP[0].password = 'true';
        }

        if (inputParams.VTP[0].domain === ''){
            cssClasses.VTP[0].domain = 'error';
            isCorrect = false;
        }else{
            cssClasses.VTP[0].domain = 'true';
        }



    }

    if (inputParams.VLAN.length > 0){
        for(let i = 0; i < inputParams.VLAN.length; i++){
        if (inputParams.VLAN[i].name === '' || !inputParams.VLAN[i].name.match(/^[A-Za-z0-9_-]{1,32}$/)){
            cssClasses.VLAN[i].name = 'error';
            isCorrect = false;
        }


        let regex = /^[0-9]+$/
        if (!regex.test(inputParams.VLAN[i].number) || !parseInt(inputParams.VLAN[i].number, 10) >= 2 || !parseInt(inputParams.VLAN[i].number, 10) <= 1001) {
            cssClasses.VLAN[i].number = 'error';
            isCorrect = false;
        }

    }

    }
   
        let apiReturn = {cssClasses: cssClasses, isCorrect: false}
        return new Response(JSON.stringify(apiReturn), {
            headers: {
                'Content-Type': 'application/json'
            }
        });
}