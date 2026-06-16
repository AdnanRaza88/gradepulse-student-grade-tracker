from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama3-70b-8192", temperature=0.7)

def get_study_tips(subject: str, marks: float, total: float) -> str:
    prompt = ChatPromptTemplate.from_template(
        "A student scored {marks} out of {total} in {subject}. "
        "Provide clear, practical and encouraging study advice to help improve performance."
    )
    chain = prompt | llm
    response = chain.invoke({"marks": marks, "total": total, "subject": subject})
    return response.content

def get_daily_routine(subject: str, marks: float) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Create a realistic daily study schedule for a student who scored {marks}% in {subject}. "
        "Include study time, breaks, revision methods and basic health suggestions."
    )
    chain = prompt | llm
    response = chain.invoke({"marks": marks, "subject": subject})
    return response.content
