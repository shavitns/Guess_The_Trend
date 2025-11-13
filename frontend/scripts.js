// 🎮 Guess The Trend – Frontend Logic

document.addEventListener("DOMContentLoaded", async () => {
    console.log("🚀 Guess The Trend frontend loaded");

    // Draw graphs when page is loaded
    await drawCharts();
});

async function drawCharts() {
    try {
        // Fetch data from Flask server
        const cryptoRes = await fetch("http://127.0.0.1:5000/api/trend?type=crypto&coin=bitcoin");
        console.log("✅ got cryptoRes", cryptoRes.status);
        const cryptoData = await cryptoRes.json();
        console.log("💰 cryptoData:", cryptoData);  // ← הדפסה


        const weatherRes = await fetch("http://127.0.0.1:5000/api/trend?type=weather&lat=31.78&lon=35.22&period=day");
        console.log("✅ got weatherRes", weatherRes.status);
        const weatherData = await weatherRes.json();
        console.log("🌤️ weatherData:", weatherData); // ← הדפסה


        // Draw charts
        createLineChart("chart1", cryptoData, "Bitcoin Price", "#10B981");
        createLineChart("chart2", weatherData, "Jerusalem Temperature", "#3B82F6");

        const randomTrend = Array.from({ length: 10 }, () => 50 + Math.random() * 10 - 5);
        createLineChart("chart3", randomTrend, "Random Trend", "#EF4444");

    } catch (error) {
        console.error("❌ Error fetching data:", error);
    }
}

function createLineChart(canvasId, data, label, color) {
    const ctx = document.getElementById(canvasId).getContext("2d");

    let values = Array.isArray(data) ? data : data.values || [];
    if (data.previous !== undefined && data.today !== undefined) {
        values = [data.previous, data.today];
    } else if (Array.isArray(data)) {
        values = data;
    } else {
        values = data.values || [0];
    }

    let labels = Array.from({ length: values.length }, (_, i) => i + 1);

    new Chart(ctx, {
        type: "line",
        data: {
            labels,
            datasets: [
                {
                    label,
                    data: values,
                    borderColor: color,
                    tension: 0.3,
                    borderWidth: 2,
                    fill: false,
                },
            ],
        },
        options: {
            scales: {
                x: {
                    ticks: { color: "#E2E8F0" },
                    grid: { color: "#1E293B" },
                },
                y: {
                    ticks: { color: "#E2E8F0" },
                    grid: { color: "#1E293B" },
                },
            },
            plugins: {
                legend: {
                    labels: { color: "#E2E8F0" },
                },
            },
        },

    });


}
