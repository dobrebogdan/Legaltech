function reloadLawResults(outputJSON) {
    const jsonObj = JSON.parse(outputJSON);
    const outputList = jsonObj.response;
    const lawResultsList = document.getElementById("lawResultsList");
    lawResultsList.innerHTML = '';
    for(var i = 0; i < outputList.length; i++) {
        var node = document.createElement('LI');
        var textnode = document.createTextNode(outputList[i]);
        node.appendChild(textnode);
        node.appendChild(document.createElement('HR'))
        lawResultsList.appendChild(node);
    }
}

function reloadCaseResults(outputJSON) {
    const jsonObj = JSON.parse(outputJSON);
    const outputList = jsonObj.response;
    console.log('!!');
    console.log(outputList);
    console.log('--');
    const caseResultsList = document.getElementById("caseResultsList");
    caseResultsList.innerHTML = '';
    for(var i = 0; i < outputList.length; i++) {
        var node = document.createElement('LI');
        var textnode = document.createTextNode(outputList[i]);
        node.appendChild(textnode);
        node.appendChild(document.createElement('HR'))
        caseResultsList.appendChild(node);
    }
}

function sendHttpRequest(theUrl, param, callback)
{
    var xmlHttpRequest = new XMLHttpRequest();
    xmlHttpRequest.onreadystatechange = function() {
        if (xmlHttpRequest.readyState == 4 && xmlHttpRequest.status == 200 && callback != null)
            callback(xmlHttpRequest.responseText);
    }
    xmlHttpRequest.open("POST", theUrl, true);
    xmlHttpRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttpRequest.send("param=" + param);
}


document.addEventListener("DOMContentLoaded", () => {
    const lawSearchButton = document.getElementById("lawSearchButton");
    lawSearchButton.addEventListener("click", () => {
        const lawSearchInput = document.getElementById("lawSearchInput");
        sendHttpRequest("http://127.0.0.1:8000/app/getlaws", lawSearchInput.value, reloadLawResults);
    });
    const caseSearchButton = document.getElementById("caseSearchButton");
    caseSearchButton.addEventListener("click", () => {
        const tribunalInput = document.getElementById("tribunalInput");
        const obiectInput = document.getElementById("obiectInput");
        const input = [obiectInput.value, tribunalInput.value];
        sendHttpRequest("http://127.0.0.1:8000/app/getcases", input, reloadCaseResults);
    });
});
