
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from rag.generator import generate_learning_path
from django.shortcuts import render
""" from langchain_ollama import OllamaLLM """

import re
""" llm = OllamaLLM(model="llama3.1") """
import os
from langchain_groq import ChatGroq

# Setup Cloud LLM
api_key = os.getenv("GROQ_API_KEY", "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")
llm = ChatGroq(
    temperature=0.7, 
    groq_api_key=api_key, 
    model_name="llama-3.3-70b-versatile"
)
from .models import AssessmentResult, Topic, StudentProgress

import markdown
def module1_view(request):
    response = None

    if request.method == "POST":
        request.session["module1_data"] = {
            "topic": request.POST.get("topic"),
            "level": request.POST.get("level"),
            "goal": request.POST.get("goal"),
            "style": request.POST.get("style"),
            "output": request.POST.get("output"),
        }

        response = generate_learning_path(**request.session["module1_data"])

    return render(request, "student/module1.html", {"response": response})

from rag.generator import generate_assessment

def module1_assessment_view(request):
    assessment_output = None
    module1_data = request.session.get("module1_data")

    if request.method == "POST" and module1_data:
        assessment = request.POST.get("assessment")

        assessment_output = generate_assessment(
            topic=module1_data["topic"],
            level=module1_data["level"],
            goal=module1_data["goal"],
            assessment=assessment
        )

    return render(
        request,
        "student/module1_assessment.html",
        {"assessment_output": assessment_output}
    )
    

from rag.generator import generate_resources


def module1_resources_view(request):
    resources = None
    module1_data = request.session.get("module1_data")

    if request.method == "POST" and module1_data:
        resources = generate_resources(
            topic=module1_data["topic"],
            level=module1_data["level"]
        )

    return render(
        request,
        "student/module1_resources.html",
        {"resources": resources}
    )


from rag.generator import generate_reflection_feedback
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def reflection_view(request):
    reflection = None
    ai_feedback = None

    if request.method == "POST":
        reflection_text = f"""
What I learned: {request.POST.get('learning')}
Challenges: {request.POST.get('difficulty')}
Strategy: {request.POST.get('strategy')}
Confidence: {request.POST.get('confidence')}
Next steps: {request.POST.get('next_steps')}
"""

        reflection = reflection_text
        ai_feedback = generate_reflection_feedback(reflection_text)

    return render(request, "student/reflection.html", {
        "reflection": reflection,
        "ai_feedback": ai_feedback
    })



from django.shortcuts import render
import json

def os_graph(request):
    nodes = [
        {"id": "Introduction", "independent": True},
        {"id": "Operating System Structures", "independent": True},
        {"id": "Process", "independent": True},
        {"id": "Threads", "independent": False},
        {"id": "Process Synchronisation", "independent": False},
        {"id": "CPU Scheduling", "independent": False},
        {"id": "Deadlocks", "independent": False},
        {"id": "Main Memory", "independent": True},
        {"id": "Virtual Memory", "independent": False},
        {"id": "Mass Storage Structure", "independent": True},
        {"id": "File System Implementation", "independent": False},
        {"id": "I/O Systems", "independent": True},
        {"id": "Protection", "independent": True},
        {"id": "Security", "independent": True},
    ]

    links = [
        {"source": "Threads", "target": "Process"},
        {"source": "Process Synchronisation", "target": "Process"},
        {"source": "CPU Scheduling", "target": "Process"},
        {"source": "Deadlocks", "target": "Process Synchronisation"},
        {"source": "Virtual Memory", "target": "Main Memory"},
        {"source": "File System Implementation", "target": "Mass Storage Structure"},
    ]

    return render(request, "student/os_graph.html", {
        "nodes": nodes,
        "links": links
    })


from django.shortcuts import render
from rag.generator import generate_one_minute_feedback

def one_minute_paper(request):
    feedback= None

    if request.method == "POST":
        learned = request.POST.get("learned", "").strip()
        question = request.POST.get("question", "").strip()

        if learned:
            feedback = generate_one_minute_feedback(learned, question)
            

        
    return render(
        request,
        "student/one_minute_paper.html",
        {"feedback": feedback}
    )


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rag.generator import generate_story_map_feedback


@csrf_exempt
def story_map_feedback(request):
    # Allow only POST
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed"},
            status=405
        )

    try:
        # Parse JSON body
        data = json.loads(request.body.decode("utf-8"))

        # Required fields for story mapping
        required_fields = [
            "context",
            "actors",
            "problem",
            "events",
            "outcome",
            "reflection"
        ]

        # Check for missing fields
        missing = [field for field in required_fields if field not in data]

        if missing:
            return JsonResponse(
                {
                    "error": "Missing required fields",
                    "missing_fields": missing
                },
                status=400
            )

        # Generate AI feedback
        feedback = generate_story_map_feedback(data)

        return JsonResponse(
            {
                "success": True,
                "feedback": feedback
            },
            status=200
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON format"},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {
                "error": "Internal server error",
                "details": str(e)
            },
            status=500
        )
from django.shortcuts import render

def story_map_page(request):
    """
    Renders the Story Mapping active learning activity page.
    """
    return render(request, "student/story_map.html")


def learning_video(request):
    return render(request, "student/video_page.html")



from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now
from .models import Topic, StudentProgress

@login_required
def mark_topic_completed(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    progress, created = StudentProgress.objects.get_or_create(
        student=request.user,
        topic=topic
    )

    progress.completed = True
    progress.completed_at = now()
    progress.save()

    return redirect('student:progress')
@login_required
def student_progress(request):
    topics = Topic.objects.all()
    progress = StudentProgress.objects.filter(student=request.user)

    completed_topics = {p.topic_id for p in progress if p.completed}

    return render(request, 'student/progress.html', {
        'topics': topics,
        'completed_topics': completed_topics
    })


from django.shortcuts import render
from rag.generator import generate_muddiest_point_explanation

def muddiest_point_view(request):
    explanation_html = None

    if request.method == "POST":
        muddiest_point = request.POST.get("muddiest_point")

        explanation = generate_muddiest_point_explanation(
            muddiest_point
        )
        #
        explanation_html = markdown.markdown(
            explanation,
            extensions=["extra", "nl2br"]
        )
    return render(
        request,
        "student/muddiest_point.html",
        {
            "explanation": explanation_html
        }
    )



def get_prompt(topic, qtype):
    if qtype == "mcq":
        return f"""
Generate 3 multiple choice questions on "{topic}".

Format STRICTLY like:
Q1. question
A) option
B) option
C) option
D) option
Answer: A
"""
    if qtype == "true_false":
        return f"""
Generate 3 True or False questions on "{topic}".

Format:
Q1. statement
Answer: True
"""

    if qtype == "fill_blanks":
        return f"""
Generate 3 fill in the blank questions on "{topic}".

Format:
Q1. statement with ___
Answer: correct word
"""

    if qtype == "short_answer":
        return f"""
Generate 3 short answer questions on "{topic}".

Format:
Q1. question
Answer: short answer
"""

def parse_questions(text, qtype):
    blocks = re.split(r"\nQ\d+\.", text)[1:]
    questions = []

    for block in blocks:
        lines = block.strip().split("\n")
        q_text = lines[0].strip()
        answer_line = [l for l in lines if l.startswith("Answer")][0]
        answer = answer_line.split(":", 1)[1].strip()

        q = {"question": q_text, "answer": answer}

        if qtype == "mcq":
            q["options"] = [l[3:] for l in lines if l.startswith(("A)", "B)", "C)", "D)"))]

        questions.append(q)

    return questions

def assessment(request):
    if request.method == "POST":
        topic = request.POST["topic"]
        qtype = request.POST["qtype"]

        prompt = get_prompt(topic, qtype)
        """ response = llm.invoke(prompt) """
        response_obj = llm.invoke(prompt)
        response = response_obj.content

        questions = parse_questions(response, qtype)

        request.session["questions"] = questions
        request.session["qtype"] = qtype

        return render(request, "student/assessment.html", {
            "questions": questions,
            "qtype": qtype
        })

    return render(request, "student/assessment.html")

def submit_assessment(request):
    questions = request.session["questions"]
    qtype = request.session["qtype"]

    score = 0
    results = []

    for i, q in enumerate(questions):
        user_ans = request.POST.get(f"q{i}", "").strip()
        correct = q["answer"]

        is_correct = user_ans.lower() == correct.lower()
        if is_correct:
            score += 1

        results.append({
            "question": q["question"],
            "your": user_ans,
            "correct": correct,
            "is_correct": is_correct
        })

    return render(request, "student/assessment.html", {
        "results": results,
        "score": score,
        "total": len(questions),
        "show_results": True
    })


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def media_library(request):
    videos = [
        {
            "title": "Process Creation",
            "file": "/media/videos/Process Creation.mp4"
        },
        {
            "title": "Deadlocks",
            "file": "/media/videos/Deadlocks.mp4"
        },
        {
            "title": "FCFS vs RR",
            "file": "/media/videos/FCFS vs RR.mp4"
        },
        {
            "title": "Virtual Memory",
            "file": "/media/videos/Virtual Memory.mp4"
        },
        {
            "title": "File Permissions",
            "file": "/media/videos/File Permissions.mp4"
        },
    ]

    audios = [
        {
            "title": "File Permissions",
            "file": "/media/audios/File Permissions Audio.mp4"
        },
        {
            "title": "Virtual Memory",
            "file": "/media/audios/Virtual Memory Audio.mp4"
        },
        {
            "title": "Deadlocks",
            "file": "/media/audios/Deadlocks Audio.mp4"
        },
        {
            "title": "FCFS vs RR",
            "file": "/media/audios/FCFS vs RR Audio.mp4"
        },
        {
            "title": "Process Creation",
            "file": "/media/audios/Process Creation Audio.mp4"
        },
    ]

    return render(request, "student/media_library.html", {
        "videos": videos,
        "audios": audios
    })
