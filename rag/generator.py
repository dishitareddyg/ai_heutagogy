
import subprocess

def run_llama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3.1"],
        input=prompt,
        capture_output=True,
        text=True
    )
    return result.stdout
def generate_learning_path(topic, level, goal, style, output):
    prompt = f"""
You are an AI co-creator using **heutagogical learning theory**.

Learner profile:
- Topic: {topic}
- Level: {level}
- Goal: {goal}
- Learning style: {style}
- Output preference: {output}

Create a self-determined learning path with:
- Choice points
- Exploration prompts
- Capability development
- Reflection questions
"""
    return run_llama(prompt)
def generate_assessment(topic, level, goal, assessment):
    prompt = f"""
You are an AI assessor following **heutagogy**.

Learner details:
- Topic: {topic}
- Level: {level}
- Goal: {goal}
- Preferred assessment: {assessment}

Generate assessment accordingly:

If Quiz:
- 5 MCQs with answers

If Short answer:
- 4 applied questions with key points

If Mini project:
- Problem statement
- Deliverables
- Evaluation criteria

End with reflection questions.
"""
    return run_llama(prompt)

def generate_resources(topic, level):
    prompt = f"""
You are an AI learning curator following heutagogical principles.

Learner details:
- Topic: {topic}
- Level: {level}

Generate diverse learning resources with brief descriptions:

1. BOOKS (2–3)
   - Author + why it is useful

2. ARTICLES / BLOGS (2–3)
   - Prefer open-access or well-known sources

3. RESEARCH PAPERS (1–2)
   - Foundational or survey papers (mention year)

4. YOUTUBE / OPEN VIDEOS (2–3)
   - Reputable educational channels

Focus on learner autonomy and exploration.
Do NOT hallucinate exact URLs — just names and sources.
"""

    return run_llama(prompt)

import subprocess
import json

def generate_reflection_feedback(reflection_text):
    prompt = f"""
You are a learning coach following heutagogical principles.

Given the student's reflection below, provide:
- Encouraging feedback
- 2 reflective questions
- 1 suggested next learning action

Student reflection:
{reflection_text}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3.1"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()

import subprocess


# rag/generator.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1"

def generate_one_minute_feedback(learned, question):
    prompt = f"""
You are an AI learning coach based on heutagogical principles.

A student completed a One-Minute Paper.

Most important thing learned:
{learned}

Remaining question or confusion:
{question if question else "None mentioned"}

Respond with:
• Encouraging tone
• Gentle clarification if needed
• ONE self-directed next learning step
• No grading, no judgment
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]
# rag/generator.py
import subprocess

def generate_story_map_feedback(story_map):
    prompt = f"""
You are a learning coach following active learning and heutagogical principles.

Given the student's story map below:
- Give encouraging feedback
- Point out 1 strong connection
- Suggest 1 improvement
- Ask 1 reflective question

Story Map:
Context: {story_map['context']}
Actors: {story_map['actors']}
Problem: {story_map['problem']}
Events: {story_map['events']}
Outcome: {story_map['outcome']}
Reflection: {story_map['reflection']}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3.1"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
