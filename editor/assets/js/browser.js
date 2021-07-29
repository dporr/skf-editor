//Keep the current state for the history
history = [];
history_pointer = 0;

//Allow child iframe to report its URL
window.addEventListener("message", function(event) {
    if (!window.location.origin) {
      window.location.origin = window.location.protocol + "//" 
          + window.location.hostname 
          + (window.location.port ? ':' + window.location.port: '');
    }
    //updateAddressBar(event.data);
  }, false);

function updateAddressBar(value) {
    var urlbar = document.getElementById('addressBarText');
    urlbar.value = unescape(value);
  }

function openUrl(){
    var urlbar = document.getElementById('addressBarText'); 
    var browserIframe = document.getElementById('browser-iframe');
    //TODO: Validate URL: protocol + FQDN + [:port] + query_string
    browserIframe.src = urlbar.value; //baking our own XSS lol
}

function browseHistory(direction){
  switch(direction){
    case 'forward':
      if(history_pointer < (history.length - 1)) history_pointer++;
      break;
    case 'back':
      if(history_pointer != 0) history_pointer--;
      break;
    default:
      return;
  }
  updateAddressBar(history_pointer[history_pointer]);
  openUrl();
}