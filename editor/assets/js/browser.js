var backSteps = 0;
//Allow child iframe to report its URL
window.addEventListener("message", function(event) {
    if (!window.location.origin) {
      window.location.origin = window.location.protocol + "//" 
          + window.location.hostname 
          + (window.location.port ? ':' + window.location.port: '');
    }
    updateAddressBar(event.data);
  }, false);

function updateAddressBar(value) {
    var urlbar = document.getElementById('addressBarText');
    urlbar.value = unescape(value);
  }

function openUrl(){
    var urlbar = document.getElementById('addressBarText'); 
    var browserIframe = document.getElementById('browser-iframe');
    if(browserIframe.src != urlbar.value){
      backSteps++;
      browserIframe.src = urlbar.value;
    }
    
    //TODO: Validate URL: protocol + FQDN + [:port] + query_string
     //baking our own XSS lol
}

function iframe_forward(){
  var browserIframe = document.getElementById('browser-iframe');
  if(backSteps < (browserIframe.contentWindow.history.length - 1)){
    backSteps++;
    browserIframe.contentWindow.history.forward();
  }

}

function iframe_back(){
  var browserIframe = document.getElementById('browser-iframe');
  if(backSteps <= 1) return;
  backSteps--;
  browserIframe.contentWindow.history.back();
}