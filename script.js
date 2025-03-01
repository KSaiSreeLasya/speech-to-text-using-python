// script.js

// Check if the browser supports SpeechRecognition
window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (window.SpeechRecognition) {
    const recognition = new SpeechRecognition();
    const output = document.getElementById("output");
    const startBtn = document.getElementById("start-btn");
    const stopBtn = document.getElementById("stop-btn");
    const resetBtn = document.getElementById("reset-btn");

    recognition.continuous = true;
    recognition.interimResults = true;

    // Start recognition
    startBtn.addEventListener("click", () => {
        recognition.start();
        output.placeholder = "Listening...";
    });

    // Stop recognition
    stopBtn.addEventListener("click", () => {
        recognition.stop();
        output.placeholder = "Speech recognition stopped.";
    });

    // Reset output
    resetBtn.addEventListener("click", () => {
        output.value = "";
        output.placeholder = "Your speech will appear here...";
    });

    // Process speech results
    recognition.addEventListener("result", (event) => {
        const transcript = Array.from(event.results)
            .map(result => result[0].transcript)
            .join("");
        output.value = transcript;
    });

    // Handle recognition errors
    recognition.addEventListener("error", (event) => {
        console.error("Speech recognition error:", event.error);
    });
} else {
    alert("Your browser does not support Speech Recognition. Please try Google Chrome.");
}
