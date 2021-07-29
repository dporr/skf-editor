//Report our URL to the parent
//This should be called from all iframed labs
parent.postMessage(window.location.toString(), "*");