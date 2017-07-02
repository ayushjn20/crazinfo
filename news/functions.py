import urllib2, json
from news import models

def get_data(sort, source, request):

	url="https://newsapi.org/v1/articles?source="+source+"&sortBy="+sort+"&apiKey=08aad1a45e184f959986a492a8c8bf76"
	response = urllib2.urlopen(url)
	data = json.loads(response.read())
	if data["status"]=="ok":
		articles=data["articles"]
		#i=0
		if request.user.is_authenticated():
			for i in range(0,len(articles)):
                	      	articles[i]['saved']=models.feed.objects.filter(title = articles[i]["title"], users = request.user).exists()
		#		print str(i) +','+str(articles[i]['saved'])
		return articles
