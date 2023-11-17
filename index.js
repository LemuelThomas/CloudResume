const counter = document.querySelector(".counter-number");

async function updateCounter() {
    try {
        let response = await fetch("https://m27png5uadsacyea66hiiqfzhi0hcwcy.lambda-url.us-east-1.on.aws/");
        let data = await response.json();

        // Update the counter HTML
        counter.innerHTML = `Views: ${data.views}`;
    } catch (error) {
        console.error('Error fetching visitor count:', error);
    }
}

updateCounter();
