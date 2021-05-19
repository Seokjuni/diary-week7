from django.shortcuts import get_object_or_404, redirect, render
from .models import diary
# Create your views here.

def 커버(request):
    number = diary.objects.count
    return render(request, '커버.html', {'number':number})

def 목차(request):
    diarys = diary.objects.all()
    return render(request, '목차.html', {'diarys':diarys})

def 상세(request, id):
    일기 = get_object_or_404(diary, pk = id)
    return render(request, '상세.html', {'diary':일기})

def 작성(request):
    return render(request, '작성.html')

def 새로작성(request):
    작성_diary = diary()
    작성_diary.title = request.POST['title']
    작성_diary.body = request.POST["body"]
    작성_diary.save()
    return redirect('상세', 작성_diary.id)

def 수정(request, id):
    수정_diary = diary.objects.get(id = id)
    return render(request, '수정.html', {'diary':수정_diary})

def 업데이트(request, id):
    업데이트_diary = diary.objects.get(id = id)
    업데이트_diary.title = request.POST['title']
    업데이트_diary.body = request.POST["body"]
    업데이트_diary.save()
    return redirect('상세', 업데이트_diary.id)

def 삭제(request, id):
    삭제_diary = diary.objects.get(id = id)
    삭제_diary.delete()
    return redirect('목차')