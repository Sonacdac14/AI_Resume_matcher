def calculate_match_score(resume_json, job_description):
    skills = resume_json.get("skills", [])
    work_exp = resume_json.get("work_experience", [])
    education = resume_json.get("education", [])

    explanation = []
    score = 0

    if any("NLP" in skill.upper() or "LLM" in skill.upper() for skill in skills):
        score += 20
        explanation.append("✅ Skills match: NLP/LLM experience found.")
    else:
        explanation.append("❌ Missing key skills in NLP/LLM.")

    if any("machine" in skill.lower() or "ai" in skill.lower() for skill in skills):
        score += 15
        explanation.append("✅ General AI/ML skills present.")

    edu_fields = [e.get("field", "").lower() for e in education]
    if any("artificial" in field or "machine" in field for field in edu_fields):
        score += 10
        explanation.append("✅ Relevant education background in AI.")
    else:
        explanation.append("❌ Education not directly aligned with AI.")

    if any("lead" in exp.get("position", "").lower() or "manager" in exp.get("position", "").lower() for exp in work_exp):
        score += 10
        explanation.append("✅ Leadership/management experience found.")
    else:
        score -= 10
        explanation.append("❌ Lacks leadership/managerial experience.")

    if len(work_exp) >= 3:
        score += 5
        explanation.append("✅ Decent work experience depth.")
    else:
        score -= 5
        explanation.append("⚠️ Limited work experience.")

    final_score = max(0, min(100, score))

    return {
        "match_score": final_score,
        "explanation": "\n".join(explanation)
    }
