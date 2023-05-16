from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
   
app = FastAPI()
   
@app.get("/")
async def root():
    return {"He":"Uds"}

@app.get("/1")
async def des():
    file_p="./1.py"
    return FileResponse(file_p)

@app.get("/2")
async def des():
    file_p="./2.py"
    return FileResponse(file_p)

@app.get("/2k")
async def des():
    file_p="./2k.py"
    return FileResponse(file_p)

@app.get("/3a")
async def des():
    file_p="./3a.py"
    return FileResponse(file_p)

@app.get("/3b")
async def des():
    file_p="./3b.py"
    return FileResponse(file_p)

@app.get("/4a")
async def des():
    file_p="./4a.py"
    return FileResponse(file_p)

@app.get("/4b")
async def des():
    file_p="./4b.py"
    return FileResponse(file_p)

@app.get("/5a")
async def des():
    file_p="./5a.py"
    return FileResponse(file_p)

@app.get("/5b")
async def des():
    file_p="./5b.py"
    return FileResponse(file_p)

@app.get("/6")
async def des():
    file_p="./6.py"
    return FileResponse(file_p)

@app.get("/7a")
async def des():
    file_p="./7a.py"
    return FileResponse(file_p)

@app.get("/7b")
async def des():
    file_p="./7b.py"
    return FileResponse(file_p)