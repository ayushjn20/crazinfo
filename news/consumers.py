import json
from channels import Group
from channels.sessions import channel_session
from channels.auth import http_session,channel_session_user, channel_session_user_from_http
from .models import comment, reply, Room, feed
from .serializers import CommentSerializer

@channel_session_user_from_http
def ws_connect(message):
	print "ws_connect"
	print message.user
	label = message['path'].replace('/news/','')
	print label
	#prefix, label = message['path']
	#room = Room.objects.get(label=label)
	#print room
	message.reply_channel.send({"accept": True})
	Group('comment-' + label).add(message.reply_channel)
	message.channel_session['room'] = label
	
@channel_session_user
def ws_receive(message):
	label = message.channel_session['room']
	#room = Room.objects.get(label=label)
	data = json.loads(message['text'])
	print "data-receive-channel-"
	print data['feed_id']
	c = comment(comment = data['comment'], key = feed.objects.filter(id = int(data['feed_id']))[0], user = message.user)
	c.save()
	serializer = CommentSerializer(c)
	print type(serializer.data)
	Group('comment-'+data['feed_id']).send({'text':json.dumps(serializer.data),})

@channel_session_user
def ws_disconnect(message):
	label = message.channel_session['room']
	Group('comment-'+label).discard(message.reply_channel)

