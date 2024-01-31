from fastapi import FastAPI, HTTPException
from PDF_reader import PDF_reader
from BOT import BOT
import uvicorn


pdf = PDF_reader('pdfs/black_hole.pdf')
bot = BOT()
app = FastAPI()


@app.get('/response')
def response(query: str):
    try:
        return bot.answer(query=query,content=pdf.get_relevant_chunks(query)[0],page_no=pdf.get_relevant_chunks(query)[1])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/summary')
def summary():
    try:
       return bot.summarize(pdf.large_chunks)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
