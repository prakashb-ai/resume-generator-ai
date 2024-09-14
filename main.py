import os
import traceback
import sys

from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from PyPDF2 import PdfReader
from ai_provider.ai_provider_factory import get_ai_provider

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...), theme: str = "theme1"):
    pdf_reader = PdfReader(file.file)
    pdf_text = "".join([page.extract_text() for page in pdf_reader.pages])
    
    theme_prompts = {
        "theme1": f"""
        Create a polished HTML resume with a professional and corporate style. The design should feature a classic layout with clear headings and sections.The content is as follows: {pdf_text}.
        Structure the resume with clearly defined sections for "Experience," "Education," and "Skills." Use a simple, formal design with a focus on readability and organization.
        """,
        "theme2": f"""
        Design a creative and modern HTML resume that stands out with a dynamic layout.The content is as follows: {pdf_text}.
        Implement a contemporary design with engaging visuals and interactive elements. Highlight sections like "Experience," "Education," and "Skills" with unique design features to make the resume memorable and visually striking.
        """,
        "theme3": f"""
        Generate an elegant and minimalistic HTML resume with a refined and sophisticated appearance.The content is as follows: {pdf_text}.
        Utilize a sleek, minimalist layout with ample white space and a focus on clean typography. Ensure that sections such as "Experience," "Education," and "Skills" are presented in a streamlined and polished manner, emphasizing simplicity and elegance.
        """
    }   

    
    theme_prompt = theme_prompts.get(theme)
    prompt = f"f{theme_prompt}: {pdf_text}"
    
    try:
        ai_provider = get_ai_provider()
        resume_html = ai_provider.generate_text(prompt)
        return JSONResponse(content={"resume_html": resume_html})
    except Exception as e:
        stack_trace = traceback.format_exc()
        print(f"Stack Trace:\n{stack_trace}")
        raise HTTPException(status_code=500, detail=f"Error : {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
