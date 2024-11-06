document.getElementById('searchBtn').addEventListener('click', async () => {
    const text = document.getElementById('searchInput').value;
    if (text) {
        try {
            console.log("Sending request to API with text:", text);  // Debugging log
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            const result = await response.json();
            console.log("API response:", result);  // Debugging log
            displayResult(result.prediction);
        } catch (error) {
            console.error('Error:', error);
        }
    }
});

function displayResult(prediction) {
    const articlesDiv = document.getElementById('articles');
    articlesDiv.innerHTML = `<div class="article">${prediction}</div>`;
}
