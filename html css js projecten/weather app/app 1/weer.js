
const WEATHERURL = 'https://api.openweathermap.org/data/2.5/weather';

async function getWeather() {
    const cityInput = document.getElementById('cityInput').value;
    const key = 'a352db877902bafba7d0ed23e7660331';
    const response = await fetch(`${WEATHERURL}?q=${cityInput}&appid=${key}&units=metric`);
    const data = await response.json();
    loadScreen(data);
}


function loadScreen(weer) {
    console.log(weer);
    place.innerText = weer.name;
    temperature.innerText = `${weer.main.temp}°C`
    minmaxTemp.innerText = `${weer.main.temp_min}°C, ${weer.main.temp_max}°C`;

}
 
window.onload = function () {
    getWeather('Riyad');
}