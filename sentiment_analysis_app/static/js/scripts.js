document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('searchBtn').addEventListener('click', async () => {
        const text = document.getElementById('searchInput').value;
        if (text) {
            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: text })
                });
                
                if (!response.ok) {
                    throw new Error(`Server error: ${response.status}`);
                }

                const result = await response.json();
                if (result.prediction) {
                    displayResult(result.prediction);
                } else {
                    displayResult('Error: Could not process the prediction.');
                }
            } catch (error) {
                console.error('Error:', error);
                displayResult('An error occurred while fetching the prediction.');
            }
        } else {
            displayResult('Please enter some text to analyze.');
        }
    });

    function displayResult(prediction) {
        const articlesDiv = document.getElementById('articles');
        articlesDiv.innerHTML = `<div class="article">Sentiment: ${prediction}</div>`;
    }
});
