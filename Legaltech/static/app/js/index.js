function reloadResults(outputJSON) {
    const jsonObj = JSON.parse(outputJSON);
    const outputList = jsonObj.response;
    const resultsList = document.getElementById("resultsList");
    resultsList.innerHTML = '';
    for(var i = 0; i < outputList.length; i++) {
        var node = document.createElement('LI');
        var textnode = document.createTextNode(outputList[i]);
        node.appendChild(textnode);
        node.appendChild(document.createElement('HR'))
        resultsList.appendChild(node);
    }
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
        sendHttpRequest("http://127.0.0.1:8000/app/getlaws", searchArea.value, reloadResults);
    })
});
