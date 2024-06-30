document.getElementById('recommendationForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('recommendationResult').innerText = `Recommended Product: ${result.recommended_product}`;
        } else {
            console.error('Failed to fetch recommendations:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching recommendations:', error);
    }
});
