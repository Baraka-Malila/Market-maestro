//script.js

document.getElementById('searchBtn').addEventListener('click', function() {
    const searchInput = document.getElementById('searchInput').ariaValueMax;
    // Calling my sentiment analysis function or API with the search input
    console.log('Searching for:', searchInput)
})