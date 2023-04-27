from django.shortcuts import render,HttpResponse,redirect
from pytube import YouTube

def mainn(request):
	return render(request,"index.html")
def returnn(request):
	return redirect("/")
def yourvid(request):
	if request.method=="POST":
		try:
			ur=request.POST.get("ur")
			va=request.POST.get("type")
			yt=YouTube(ur)
			print("Title : ",yt.title)
			print("Thumbnail Url : ",yt.thumbnail_url)
			context={
				"title":yt.title,
				"thum":yt.thumbnail_url
			}
			if va=="vid":
				st=yt.streams.filter(file_extension='mp4',res="360p")
			else:
				st=yt.streams.filter(file_extension='mp4',only_audio=True)
			vid=list(enumerate(st))
			if len(vid)==0:
				return render(request,"index.html",context)
			context["pppp"]=st[0].url
			# st[0].download(r'C:/Users/DELL/Desktop/Yedekh',filename="yourfile.webm")
			print("HO GAYA....")
			return render(request,"index0.html",context)
		except:
			print("Kuch Bhi.....")
			return redirect("/")
	return HttpResponse("Nikal")