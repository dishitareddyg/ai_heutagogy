from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rag_pipeline.rag import get_rag_response

def generate_student_roadmap(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        outcomes = request.POST.get("outcomes")

        query = f"Generate a learning roadmap for topic '{topic}' \
                   with desired outcomes: {outcomes}. Include \
                   visual learning elements and step-by-step activities."

        roadmap = get_rag_response(query)

        return render(request, "student/roadmap.html", {"roadmap": roadmap})
    return render(request, "student/form.html")



def learn(request):
    return render(request, "student/learn.html")

