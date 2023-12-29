
  var BTN = document.querySelector("button");
  var TEXTAREA = document.querySelector("#textSpeech");
  var DIV = document.querySelector("#response_msg");
  var BTN_MIC = document.querySelector("#bMic");

  var recognition = new webkitSpeechRecognition();
  recognition.continuous = false;
  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  // Event listeners
  BTN.addEventListener("click", chatBot);
  BTN_MIC.addEventListener("click", speechToText);

  // Function to send text from TEXTAREA to the backend for analysis
  function chatBot() {
    let text = TEXTAREA.value;
    var url_backend = "http://127.0.0.1:8000/analyse"

    fetch(url_backend, {
      method: "POST",
      body: JSON.stringify({"texte": text}),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => {
        response.json()
          .then(data => {
            console.log(data);
          });
      })
      .catch(error => {
        console.warn(error);
      });
  }

  // Function to start speech-to-text functionality
  function speechToText() {
    alert("Speech to text ready");
    recognition.start();
  }

  // Event handler for speech recognition results
  recognition.onresult = function(event) {
    var message = event.results[0][0].transcript;
    console.log('Result received: ' + message + '.');
    console.log('Confidence: ' + event.results[0][0].confidence);
    TEXTAREA.value = message;
  };

