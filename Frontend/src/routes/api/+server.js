export async function POST({ request }) {
    try {
        const PostData = await request.json();
        console.log(PostData);

        const response = await fetch('http://127.0.0.1:8000/configuration/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(PostData)  // Ensure the body is a string
        });

        // Check if the response is OK (status 200-299)
        if (!response.ok) {
            throw new Error(`Failed to fetch: ${response.statusText}`);
        }

        const ApiData = await response.json();
        return new Response(JSON.stringify(ApiData), { 
            status: 200,
            headers: {
                'Content-Type': 'application/json',
            }
        });
    } catch (error) {
        console.error('Error:', error.message);

        return new Response(JSON.stringify({ error: error.message }), {
            status: 500,
            headers: {
                'Content-Type': 'application/json',
            }
        });
    }
}
