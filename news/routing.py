from news import consumers
channel_routing = {
	'websocket.connect':consumers.ws_connect,
	'websocket.receive':consumers.ws_receive,
	'wensocket.diconnect':consumers.ws_disconnect,
}
