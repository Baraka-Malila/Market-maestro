document.getElementById('searchBtn').addEventListener('click', async () => {
    const text = document.getElementById('searchInput').value;
    if (text) {
        try {
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });
            const result = await response.json();
            displayResult(result.prediction);
        } catch (error) {
            console.error('Error:', error);
        }
    }
});

function displayResult(prediction) {
    const articlesDiv = document.getElementById('articles');
    articlesDiv.innerHTML = `<div class="article">Sentiment: ${prediction}</div>`;
}
