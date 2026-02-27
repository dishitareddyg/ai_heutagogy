import os
from langchain_groq import ChatGroq

# Setup Cloud LLM
api_key = os.getenv("GROQ_API_KEY", "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")
llm = ChatGroq(
    temperature=0.7, 
    groq_api_key=api_key, 
    model_name="llama-3.3-70b-versatile"
)

def ask_ai(prompt):
    """Replaces the old run_llama subprocess method"""
    result = llm.invoke(prompt)
    return result.content

# 1. Generate Learning Path
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
    return ask_ai(prompt)

# 2. Generate Assessment
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
    return ask_ai(prompt)

# 3. Generate Resources
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
    return ask_ai(prompt)

# 4. Generate Reflection Feedback (FIXED to use ask_ai)
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
    return ask_ai(prompt)

# 5. Generate One Minute Feedback (FIXED to use ask_ai)
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
    return ask_ai(prompt)

# 6. Generate Story Map Feedback (FIXED to use ask_ai)
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
    return ask_ai(prompt)

# 7. Generate Muddiest Point (FIXED to use ask_ai)
def generate_muddiest_point_explanation(muddiest_point):
    prompt = f"""
You are an expert operating systems tutor.

A student has identified the following concept as their muddiest point:

"{muddiest_point}"

Explain this concept clearly in simple language.
Use examples if helpful.
Avoid jargon where possible.
Keep the explanation concise and student-friendly.
"""
    return ask_ai(prompt)