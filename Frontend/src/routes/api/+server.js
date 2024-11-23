
export async function POST({ request }) {
    const PostData = await request.json();
    const response = await fetch('127.0.0.1:8000/configuration/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(PostData)
    });
    ApiData = await response.json();
    return true;
}