var BTN=document.querySelector("button")
var TEXTAREA=document.querySelector("textarea")
var DIV=document.querySelector("#response_msg")

//EVENT
BTN.addEventListener("click", ChatBot)


//Main function

function ChatBot(){

    console.log("Button clicked")
    let text=TEXTAREA.value
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    
    var raw = JSON.stringify({
      "text": text
    });
    
    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      // redirect: 'follow'
    };
    
    fetch("http://127.0.0.1:8000/analyse", requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
}