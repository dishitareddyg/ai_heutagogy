
from django.shortcuts import render
import subprocess
import json

from django.shortcuts import render
import subprocess
import json
from .services import generate_teacher_roadmap
from .models import CoursePlan

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import CoursePlan

def view_plans(request):
    plans = CoursePlan.objects.order_by("-created_at")

    paginator = Paginator(plans, 5)  # 5 plans per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "teacher/view_plans.html", {
        "page_obj": page_obj
    })

def plan_detail(request, plan_id):
    plan = get_object_or_404(CoursePlan, id=plan_id)

    return render(request, "teacher/plan_detail.html", {
        "plan": plan
    })



def teacher_dashboard(request):
    return render(request, "teacher/dashboard.html")


def create_plan(request):
    if request.method == "POST":
        
        outcomes = request.POST.get("outcomes", "").strip()
        num_classes = request.POST.get("num_classes")
        duration = request.POST.get("duration")
        class_size = request.POST.get("class_size")

        if not (outcomes and num_classes and duration and class_size):
            return render(request, "teacher/plan.html", {
                "error": "Please fill all fields correctly."
            })

        num_classes = int(num_classes)
        duration = int(duration)
        class_size = int(class_size)

        roadmap = generate_teacher_roadmap(
            outcomes,
            num_classes,
            duration,
            class_size
        )

        CoursePlan.objects.create(
        
        num_classes=num_classes,
        class_duration=duration,
        class_size=class_size,
        course_outcomes=outcomes,
        roadmap=roadmap,
    )

        return render(request, "teacher/roadmap.html", {
            "outcomes": outcomes,
            "roadmap": roadmap
        })

    return render(request, "teacher/plan.html")


import subprocess
from django.shortcuts import render

def call_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.1"],
            input=prompt,
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"Error calling Ollama: {e}"
    



