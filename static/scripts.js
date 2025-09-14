async function updateData() {
    const response = await fetch('/data');
    const data = await response.json();

  
    document.getElementById('ldr').innerText = data.ldr;
    document.getElementById('temp').innerText = data.temperature + " °C";
    document.getElementById('humidity').innerText = data.humidity + " %";

  
    document.getElementById('mq2').innerText = data.mq2;
    document.getElementById('mq2v').innerText = data.mq2_voltage + " V";


    document.getElementById('ldr-gauge').style.width = (data.ldr / 1023 * 100) + '%';
    document.getElementById('temp-gauge').style.width = (data.temperature !== "--" ? (data.temperature / 50 * 100) : 0) + '%';
    document.getElementById('humidity-gauge').style.width = (data.humidity !== "--" ? data.humidity : 0) + '%';
    document.getElementById('mq2-gauge').style.width = (data.mq2 / 1023 * 100) + '%';
}

setInterval(updateData, 2000);
updateData();