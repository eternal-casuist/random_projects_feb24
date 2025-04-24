function startDictation() {
    const inputField = document.getElementById("input");
    if (window.SpeechRecognition || window.webkitSpeechRecognition) {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            inputField.value = transcript;
        };

        recognition.onerror = function(event) {
            console.error('Error occurred in recognition: ', event.error);
        };

        recognition.start();
    } else {
        alert("Sorry, your browser does not support speech recognition.");
    }
}