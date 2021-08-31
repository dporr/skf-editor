history_stack = [];
history_pointer = -1;
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

  function openUrl(isKnownUrl){
    var urlbar = document.getElementById('addressBarText');
    if(!isKnownUrl){
      history_stack.push(urlbar.value)
      history_pointer++; 
    }
    var forwardButton = document.getElementById('go-forward');
    var backButton = document.getElementById('go-back');
    forwardButton.disabled = (history_stack.length -1 != history_pointer ) ? false : true;
    backButton.disabled = (history_pointer > 0)? false : true;
    var browserIframe = document.getElementById('browser-iframe');   
    //TODO: Validate URL: protocol + FQDN + [:port] + query_string
    browserIframe.src = urlbar.value; //baking our own XSS lol
}

function iframe_forward(){
  history_pointer++;
  updateAddressBar(history_stack[history_pointer])
  openUrl(true);
}

function iframe_back(){
  history_pointer--;
  updateAddressBar(history_stack[history_pointer])
  openUrl(true);
}