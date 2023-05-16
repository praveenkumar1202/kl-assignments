from fastapi import FastAPI
import uvicorn
from scripts.services.book_services import library_router


app_main = FastAPI()
app_main.include_router(library_router)

if __name__ == "__main__":
    uvicorn.run("main:app_main")
