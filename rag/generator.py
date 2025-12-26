
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
