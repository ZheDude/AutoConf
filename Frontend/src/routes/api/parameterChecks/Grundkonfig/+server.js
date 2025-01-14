export async function POST({ request }) {
    let inputParams = await request.json();
    inputParams = inputParams['userInputs']


    function range(start, end) {
		return Array.from({ length: end - start + 1 }, (_, i) => start + i);
	}

    let cssClasses = {
		hostname: 'correct',
		domain: 'correct',
		adminUser: 'correct',
		adminPassword: 'correct',
		managementInterface: 'correct',
		managementIP: 'correct',
		managementMask: 'correct',
		keylength: 'correct',
		consoleExecTime: { minutes: 'correct', seconds: 'correct' },
		vtyRanges: [
			{
				startLine: 'correct',
				endLine: 'correct',
				execMinutes: 'correct',
				execSeconds: 'correct'
			}
		]
	};
    

    let correct = true;
		if (
			inputParams.hostname === '' ||
			!inputParams.hostname.match(/^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$/)
		) {
			correct = false;
			cssClasses.hostname = 'error';
		} else {
			cssClasses.hostname = 'correct';
		}

		if (inputParams.domain === '') {
			correct = false;
			cssClasses.domain = 'error';
		} else {
			cssClasses.domain = 'correct';
		}

		if (
			inputParams.adminUser === '' ||
			!inputParams.adminUser.match(
				/^(?!.*\.\.)(?!.*__)(?!.*--)(?![-_.])[A-Za-z0-9._-]{3,30}(?<![-_.])$/
			)
		) {
			correct = false;
			cssClasses.adminUser = 'error';
		} else {
			cssClasses.adminUser = 'correct';
		}

		if (inputParams.password === '') {
			correct = false;
			cssClasses.password = 'error';
		} else {
			cssClasses.password = 'correct';
		}

		if (inputParams.managementInterface === '') {
			correct = false;
			cssClasses.managementInterface = 'error';
		} else {
			cssClasses.managementInterface = 'correct';
		}

		if (
			inputParams.managementIP === '' ||
			!inputParams.managementIP.match(
				/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/
			)
		) {
			correct = false;
			cssClasses.managementIP = 'error';
		} else {
			cssClasses.managementIP = 'correct';
		}

		if (
			inputParams.managementMask === '' ||
			!inputParams.managementMask.match(
				/^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$/
			)
		) {
			correct = false;
			cssClasses.managementMask = 'error';
		} else {
			cssClasses.managementMask = 'correct';
		}

		range(0, inputParams.vtyRanges.length - 1).forEach((element) => {
			if (
				inputParams.vtyRanges[element].execTimeout.minutes === '' ||
				!inputParams.vtyRanges[element].execTimeout.minutes.match(/^-?\d*\.?\d+$/)
			) {
				correct = false;
				cssClasses.vtyRanges[element].execMinutes = 'error';
			} else {
				cssClasses.vtyRanges[element].execMinutes = 'correct';
			}

			if (
				inputParams.vtyRanges[element].execTimeout.seconds === '' ||
				!inputParams.vtyRanges[element].execTimeout.seconds.match(/^-?\d*\.?\d+$/)
			) {
				correct = false;
				cssClasses.vtyRanges[element].execSeconds = 'error';
			} else {
				cssClasses.vtyRanges[element].execSeconds = 'correct';
			}

			if (
				inputParams.vtyRanges[element].startLine === '' ||
				!inputParams.vtyRanges[element].startLine.match(
					/^(0|([1-9]?[0-9]{1,2}|9[0-1][0-9]|92[0-4]))$/
				)
			) {
				correct = false;
				cssClasses.vtyRanges[element].startLine = 'error';
			} else {
				cssClasses.vtyRanges[element].startLine = 'correct';
			}

			if (
				inputParams.vtyRanges[element].endLine === '' ||
				!inputParams.vtyRanges[element].endLine.match(
					/^(0|([1-9]?[0-9]{1,2}|9[0-1][0-9]|92[0-4]))$/
				)
			) {
				correct = false;
				cssClasses.vtyRanges[element].endLine = 'error';
			} else {
				cssClasses.vtyRanges[element].endLine = 'correct';
			}
		});

		if (
			inputParams.consoleExecTime.minutes === '' ||
			!inputParams.consoleExecTime.minutes.match(/^-?\d*\.?\d+$/)
		) {
			correct = false;
			cssClasses.consoleExecTime.minutes = 'error';
		} else {
			cssClasses.consoleExecTime.minutes = 'correct';
		}

		if (
			inputParams.consoleExecTime.seconds === '' ||
			!inputParams.consoleExecTime.seconds.match(/^-?\d*\.?\d+$/)
		) {
			correct = false;
			cssClasses.consoleExecTime.seconds = 'error';
		} else {
			cssClasses.consoleExecTime.seconds = 'correct';
		}

		if (
			inputParams.keylength === '' ||
			!inputParams.keylength.match(/^(512|768|1024|2048|4096)$/)
		) {
			correct = false;
			cssClasses.keylength = 'error';
		} else {
			cssClasses.keylength = 'correct';
		}




   

        let apiReturn = {correct: correct, cssClasses: cssClasses}
        return new Response(JSON.stringify(apiReturn), {
            headers: {
                'Content-Type': 'application/json'
            }
        });
}