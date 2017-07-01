from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
import json
from news import functions, models
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from news.serializers import FeedSerializer,CommentSerializer, UserSerializer 
###############

news_sources=(
	('business-insider','Business Insider'),
	('financial-times','Financial Times'),
	('hacker-news', 'Hacker News'),
	('mtv-news','MTV News'),
	('the-economist','The Economist'),
	('the-hindu','The Hindu'),
	('the-times-of-india', 'TOI'),
)

sortBy=(
	('top','Top',),
	('latest','Latest',),

)


class src_form(forms.Form):
	print 'feed form pass 2 class'
	source = forms.ChoiceField(choices=news_sources)
	#print news_sources
	sort = forms.ChoiceField(choices=sortBy)
@login_required
@csrf_exempt
def feeds(request):
	print request.user
	print 'feed form pass 0'
	if request.method=="POST":
		print request.POST.keys()
		if 'feed_id' in request.POST.keys():
        	        print "pass1"
			num = int(request.POST['feed_id'])
			#print request.POST
			if request.user.is_authenticated():
				data = functions.get_data(request.POST["sort"], request.POST["source"],request)
				if not data[num]['saved']:
					q =  models.feed.objects.filter(title=data[num]['title'])
					if not q.exists():
						reqData=data[num]
						reqData.pop('saved',None)
						f = models.feed(**reqData)
						f.save()
						f.source = request.POST['source']
						f.save()
					else:
						f = q[0]
						print f
						if len(q)>1:
							print "Check DB, more than one feed with same context exist"
					f.users.add(request.user)
				 	print "pass2"

			else:
				print "no user logged in"
				return redirect('/news/login/')
	
		current={'src':request.POST["source"], 'sort':request.POST["sort"]}
		data = functions.get_data(request.POST["sort"], request.POST["source"],request)
		

	else:
		print 'feed form pass 1 initial'
		data = functions.get_data('top','business-insider',request)
		current={'src':'business-insider','sort':'top'}
	feed_form = src_form()

	context = {'data':data, 'feed_form':feed_form, 'current':current}
	return render(request,'news/index.html', context)

###############
@login_required
@csrf_exempt
def discussion(request):
	if request.method == 'POST':
		print "discussion-POST-pass0"
		p = int(request.POST.get('pg','1'))
		nextfeeds = models.feed.objects.all()[(p-1)*5:p*5]
		serializer = FeedSerializer(nextfeeds, many=True)
		print type(serializer.data)
		return JsonResponse(serializer.data, safe=False)
	else:
		print 'discussion-initial'
		return render(request,'news/savedfeeds.html')
@csrf_exempt
def comment(request):
	if request.method == 'POST':
		print 'loading comm feed-'+request.POST['feed_id']
		feed_id = int(request.POST['feed_id'])
		comments = models.comment.objects.filter(key__id = feed_id)
		serializer = CommentSerializer(comments, many=True)
		#print serializer.data
		return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def comment_save(request):
	if request.method == 'POST':
		c = models.comment(comment = request.POST['comment'], key = models.feed.objects.filter(id = int(request.POST['feed_id']))[0], user = request.user)
		c.save()
################

"""
def login_view(request):
	if ( not(request.user.is_authenticated())):
		if request.method=='POST':
			username=request.POST["username"]
			password = request.POST["password"]
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					if request.POST["rme"]=="yes":
						HttpResponse.set_signed_cookie('username',username,salt='',max_age= 60*60*24*365 ,expires=None, path='/',domain=None,secure=None,httponly=True)
					print "2"
					return redirect(feeds)
				else:
					return HttpResponse("Hello "+username+"! Sorry, but your account has been disabled.")
			else:
				return HttpResponse("Invalid Credentials")
		else:
			print"a"
			return render(request,'news/login.html')
	else:
		print"1"
		return redirect(feeds)
"""
##################

def login_view(request):
	print "pass login-view-0"
	if request.user.is_authenticated():
		return redirect(feeds) 
	else:
		if request.method=="POST":
			print "pass login-views-1-POST"
			if not request.POST.get('rem_me',None):
				request.session.set_expiry(0)
		return auth_views.login(request)

##################
"""
def signup_view(request):
	print request.user
	print 1
	if(not(request.user.is_authenticated())):
		if request.method=='POST':
			if request.POST["password"]==request.POST["conf_password"]:
				name=request.POST["name"]
				namearr= name.split(' ',2)
				print 2
				print namearr
				user=User.objects.create_user( request.POST["username"] , request.POST["email"] , request.POST["password"] )
				user.first_name=namearr[0]
				user.last_name=namearr[1]
				user.save()
				login(request, user)
				#return redirect(profile)
				#print "User created successfully"
				return HttpResponse("User created successfully")
			else:
				return HttpResponse("Passwords do not match")
		else:
			return render(request,'news/signup.html')
	else:
		return redirect(feeds)
"""
###############

def signup_form(request):
	if request.method=='POST':
		print "pass signup-0-POST"
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
			login(request, user)
			return HttpResponse("User created successfully")
		else:
			return HttpResponse("Failed")
	else:
		form = UserCreationForm()
	return render(request,'news/signup2.html',{'form':form})	

#################
class UserProfileForm(forms.ModelForm):
	class Meta:
		model=models.UserProfile
		exclude=('user',)
		#fields=('dp','phoneNo', 'Bio')

	
def register(request):	
	print request.user
	print "pass-signu-0"
	print models.UserProfile._meta.get_fields()

	if request.user.is_authenticated():
		return redirect(feeds)
	
	elif request.method=="POST" or request.method=="FILES":
		print "pass-signup-1-POST"
		ucf=UserCreationForm(request.POST, prefix="usercreate")
		#uf=UserForm(request.POST, prefix='user')
		upf=UserProfileForm(request.POST, request.FILES, prefix='userprofile')
		print ucf.is_valid()
		print upf.is_valid()
		if ucf.is_valid() and upf.is_valid():
			print "pass-signup-2-valid"
			user=ucf.save()
			#user=uf.save(commit="false")
			userprofile = upf.save(commit="False")
			userprofile.user=user
			userprofile.save()
			user.first_name=request.POST["first_name"]
			user.last_name=request.POST["last_name"]
			user.email=request.POST["email"]
			user.save()
			g = Group.objects.get(name="Common")
			g.user_set.add(user)
			#user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
                        #login(request, user)
			return HttpResponse("User created successfully")
	else:
		#uf=UserForm(prefix='user')
		upf=UserProfileForm(prefix='userprofile')
		ucf=UserCreationForm(prefix='usercreate')
	context = {
	#'form_u':uf,
	'form_up':upf,
	'form_ucf':ucf,
	}
	return render(request,'news/signup.html',context)

###############

def profile(request, username):
	print "profile-"+username			
	user = get_object_or_404(User, username = username)
	serializer = UserSerializer(user)
	print True if request.user.username==username else False 
	###
	if request.method=='POST' and request.user.username==username and authenticate(username=username, password = request.POST['password']) is not None:
		print request.POST.keys()
		print type(request.POST)
		ign = ['csrfmiddlewaretoken','password']
		gen = (key for key in request.POST if key not in ign)
		for key in gen:
			#print key +'-' +request.POST[key]
			try:
				setattr(user, key ,request.POST[key])
				user.save(update_fields=[key])
			except:
				try:
					setattr(user.userprofile, key, request.POST[key])
					user.userprofile.save(update_fields=[key])
				except:
					print 'error'
					raise
					return None
		return render(request,'news/user_profile.html', {'data':serializer.data,'auth':True if request.user.username==username else False, 'notify':'user_profile_updated_successfully!'})
	else:
		return render(request,'news/user_profile.html', {'data':serializer.data,'auth':True if request.user.username==username else False})
