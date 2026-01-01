
from django.shortcuts import render
from rag.generator import generate_learning_path

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
    feedback = None

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
