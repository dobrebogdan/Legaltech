function reloadResults(outputJSON) {
    const jsonObj = JSON.parse(outputJSON);
    const outputText = jsonObj.response;
    console.log(outputText);
}

function sendHttpRequest(theUrl, input, callback)
{
    var xmlHttpRequest = new XMLHttpRequest();
    xmlHttpRequest.onreadystatechange = function() {
        if (xmlHttpRequest.readyState == 4 && xmlHttpRequest.status == 200 && callback != null)
            callback(xmlHttpRequest.responseText);
    }
    xmlHttpRequest.open("POST", theUrl, true);
    xmlHttpRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttpRequest.send("param=" + input);
}




document.addEventListener("DOMContentLoaded", () => {
    const searchButton = document.getElementById("searchButton");
    searchButton.addEventListener("click", () => {
        const searchArea = document.getElementById("searchInput");
        sendHttpRequest("http://127.0.0.1:8000/app/getevents", searchArea.value, reloadResults);
    })
});
