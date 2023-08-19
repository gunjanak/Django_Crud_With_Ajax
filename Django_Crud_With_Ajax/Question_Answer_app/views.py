from django.shortcuts import render,redirect
from django.http import JsonResponse

from .models import QuestionsAnswer
from .forms import QuestionForm

# Create your views here.

def home(request):
    form = QuestionForm()
    all_questions = QuestionsAnswer.objects.all()
    data = {'form':form,'questions':all_questions}
    return render(request,"home.html",data)

def save_data(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            qid= request.POST.get('queid')
            print("******************")
            print(qid)
            que = request.POST['question']
            ans = request.POST['answer']

            #case when qid is empty, that is new entry
            if(qid==""):
                question = QuestionsAnswer(question=que,answer=ans)
            
            #case when qid is not empty, editing old entry
            else:
                question = QuestionsAnswer(id=qid,question=que,answer=ans)

            question.save()

            question_data = list(QuestionsAnswer.objects.values())

            return JsonResponse({'status':'Save','question_data':question_data})
        
        else:
            return JsonResponse({'status':0})


        
#Delete Data
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get("qid")
        pi = QuestionsAnswer.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    
#Edit Data
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('qid')
        q = QuestionsAnswer.objects.get(pk=id)
        
        data = {"id":q.id,
                "question":q.question,
                "answer":q.answer}
        return JsonResponse(data)