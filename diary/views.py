from django.shortcuts import get_object_or_404, redirect, render
from .models import diary
from django.contrib.auth.decorators import login_required
# Create your views here.

def 커버(request):
    number = diary.objects.count() #all().__len__()
    return render(request, '커버.html', {'number':number})

@login_required(login_url='/account/login/')
def 목차(request):
    diarys = diary.objects.all()
    return render(request, '목차.html', {'diarys':diarys})

@login_required(login_url='/account/login/')
def 상세(request, id):
    일기 = get_object_or_404(diary, pk = id)
    return render(request, '상세.html', {'diary':일기})

@login_required(login_url='/account/login/')
def 작성(request):
    return render(request, '작성.html')

@login_required(login_url='/account/login/')
def 새로작성(request):
    작성_diary = diary()
    작성_diary.title = request.POST['title']
    작성_diary.body = request.POST["body"]
    작성_diary.save()
    return redirect('상세', 작성_diary.id)

@login_required(login_url='/account/login/')
def 수정(request, id):
    수정_diary = diary.objects.get(id = id)
    return render(request, '수정.html', {'diary':수정_diary})

@login_required(login_url='/account/login/')
def 업데이트(request, id):
    업데이트_diary = diary.objects.get(id = id)
    업데이트_diary.title = request.POST['title']
    업데이트_diary.body = request.POST["body"]
    업데이트_diary.save()
    return redirect('상세', 업데이트_diary.id)

@login_required(login_url='/account/login/')
def 삭제(request, id):
    삭제_diary = diary.objects.get(id = id)
    삭제_diary.delete()
    return redirect('목차')