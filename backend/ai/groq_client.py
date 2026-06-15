from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama3-70b-8192", temperature=0.7)

def get_study_tips(subject: str, marks: float, total: float) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Student scored {marks}/{total} in {subject}. Give personalized, encouraging study tips."
    )
    chain = prompt | llm
    return chain.invoke({"marks": marks, "total": total, "subject": subject}).content

def get_daily_routine(subject: str, marks: float) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Create a complete daily study routine for a student weak in {subject} with {marks}% score. Include study hours, water intake, breaks, health tips."
    )
    chain = prompt | llm
    return chain.invoke({"subject": subject, "marks": marks}).content