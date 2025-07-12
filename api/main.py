from fastapi import FastAPI
 
from .routers.states import router as stateRouter
app = FastAPI()
 
app.get('/home')
async def root():
    return {"intro": "Hello-World"}

                   
app.include_router(stateRouter)

