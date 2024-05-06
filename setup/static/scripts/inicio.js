document.getElementById('start-scraping').addEventListener('click', ()=> {
    window.location.href = '{% url "login" %}';
});
