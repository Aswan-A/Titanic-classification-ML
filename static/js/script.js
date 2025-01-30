const facts = [
    "Titanic's first-class suites cost over $2,500, a fortune at the time.",
    "The ship had a real-life 'unsinkable' reputation before its fateful voyage.",
    "Titanic carried over 2,200 passengers and crew but had lifeboats for only 1,178.",
    "Titanic's iceberg collision took just 37 seconds to sink the ship.",
    "The ship's band played on even as Titanic sank, trying to keep passengers calm."
];

let currentFactIndex = 0;

function updateFact() {
    document.getElementById("fact-text").textContent = facts[currentFactIndex];
    currentFactIndex = (currentFactIndex + 1) % facts.length;
}

setInterval(updateFact, 5000);
updateFact();

function validateForm() {
    const age = document.getElementById("Age").value;
    const fare = document.getElementById("Fare").value;

    if (age < 0 || fare < 0) {
        alert("Age and Fare cannot be negative.");
        return false;
    }

    return true;
}
