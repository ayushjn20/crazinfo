var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/news/discussion" + window.location.pathname);
