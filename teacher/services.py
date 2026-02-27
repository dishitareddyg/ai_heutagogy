
""" from langchain_ollama import OllamaLLM """
from langchain_groq import ChatGroq

# Use mistral or llama3
""" llm = OllamaLLM(model="llama3.1") """
llm = ChatGroq(
    temperature=0.7, 
    groq_api_key="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", 
    model_name="llama-3.3-70b-versatile"
)

def generate_teacher_roadmap(outcomes, num_classes, duration, class_size):
    prompt = f"""
You are an expert instructional designer.

Generate a CLASS WISE TEACHING ROADMAP for a university-level course based on Bloom’s taxonomy.
IMPORTANT RULES:
1. Only use the EXACT course outcomes provided below.
2. DO NOT add topics that are not mentioned by the teacher.
3. DO NOT generate a generic or standard syllabus.
4. Breakdown must strictly follow teacher's outcomes and nothing else
Course Topic: Operating Systems
Course Outcomes:
{outcomes}

Constraints:
- Number of classes: {num_classes}
- Duration per class: {duration} minutes
- Class size: {class_size} students

Requirements:
1. Break the roadmap into Class 1, Class 2, … Class {num_classes}
2. For EACH class include:
   - Bloom’s Level (Remember/Understand/Apply/Analyze/Evaluate/Create)
   - Topic
   - Subtopics
   - Activities (group activities, labs, demos)
   - Time Allocation (total = {duration} minutes)
3. Make the plan progressive (simple → advanced)
4. End with a “Summary of Learning Progression”.

Return result in clean bullet points.
"""

    result = llm.invoke(prompt)
    return result
