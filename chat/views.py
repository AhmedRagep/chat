import json
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
  if not request.user.is_authenticated:
    return redirect('login')
  else:
    user = request.user.profile
    frinds = user.frinds.all()
    
    context = {
      'user':user,
      'frinds':frinds
    }
  return render(request,'index.html',context)


def detail(request,pk):
  user = request.user.profile
  frind = Frind.objects.get(profile_id=pk)
  profile = Profile.objects.get(id=frind.profile.id)
  chats = ChatMessage.objects.all()
  rec_msg = ChatMessage.objects.filter(sender=profile,reciever=user)
  rec_msg.update(read=True)
  form = ChatForm()
  if request.POST:
    form = ChatForm(request.POST)
    if form.is_valid():
      new_form = form.save(commit=False)
      new_form.sender = user
      new_form.reciever = profile
      new_form.save()
      return redirect('detail', frind.profile.id)
  return render(request,'detail.html',{'frind':frind,'num':rec_msg.count(),'profile':profile,'user':user,'form':form,'chats':chats})




def frinds(request):
  user = request.user.profile

  friends = request.user.profile.frinds.all()
  friends_ids = [friend.id for friend in friends]
  non_friends = Profile.objects.exclude(Q(id__in=friends_ids) | Q(user=request.user))
  # print(non_friends)
  context = {
    'all_frinds':non_friends,
    'user':user
  }
  return render(request,'frinds.html',context)


def add_frinds(request,pk):
  user = request.user
  profile_user = get_object_or_404(Profile, user=user)         # Profile صاحب الطلب
  profile_friend = get_object_or_404(Profile, id=pk)           # Profile اللي هيبقى صديق
  friend_obj, created = Frind.objects.get_or_create(profile=profile_friend)  # نتأكد إن عنده Frind

  profile_user.frinds.add(friend_obj)   # نضيفه كصديق
  return JsonResponse({'success': f'{profile_friend.name} تمت إضافته كصديق ✅'})



def sendMessage(request,pk):
  user = request.user.profile
  frind = Frind.objects.get(profile_id=pk)
  profile = Profile.objects.get(id=frind.profile.id)
  data = json.loads(request.body)
  new_chat = data["msg"]
  create_message = ChatMessage.objects.create(body=new_chat, sender=user, reciever=profile,read=False)
  return JsonResponse(create_message.body ,safe=False)




def receiveMessage(request, pk):
  user = request.user.profile
  frind = Frind.objects.get(profile_id=pk)
  profile = Profile.objects.get(id=frind.profile.id)
  arr=[]
  messages = ChatMessage.objects.filter(sender=profile,reciever=user)
  for msg in messages:
    arr.append(msg.body)
  return JsonResponse(arr, safe=False)




def getNotification(request):
  user = request.user.profile
  friends = user.frinds.all()
  arr = []
  for friend in friends:
    chat = ChatMessage.objects.filter(sender__id=friend.profile.id,reciever=user,read=False)
    arr.append(chat.count())
  return JsonResponse(arr, safe=False)



from django.contrib.auth import logout
def logoutview(request):
  logout(request)
  return redirect('login')