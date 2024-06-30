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
            document.getElementById('recommendationResult').innerHTML = `<div class="result-item">Recommended Product: <strong>${result.recommended_product}</strong></div>`;
        } else {
            console.error('Failed to fetch recommendations:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching recommendations:', error);
    }
});

document.getElementById('nlpForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const nlpInput = document.getElementById('nlpInput').value;

    try {
        const response = await fetch('/nlp_predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: nlpInput }),
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('nlpResult').innerHTML = Object.entries(result).map(([key, value]) => 
                `<div class="result-item"><strong>${key.replace(/_/g, ' ')}:</strong> ${value}</div>`
            ).join('');
            
            await predict(result);

        } else {
            console.error('Failed to extract circumstances:', response.statusText);
        }
    } catch (error) {
        console.error('Error extracting circumstances:', error);
    }
});

async function predict(jsonResult) {
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(jsonResult),
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('nlpResult2').innerHTML = `<div class="result-item">Recommended Product: <strong>${result.recommended_product}</strong></div>`;
        } else {
            console.error('Failed to fetch product recommendation:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching product recommendation:', error);
    }
}
