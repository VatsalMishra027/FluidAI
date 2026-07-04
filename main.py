from fastapi import FastAPI, HTTPException
import uvicorn
from models import AgentRequest, AgentResponse
from agent import run_agent

app = FastAPI(
    title="Autonomous AI Agent API",
    description="An API that runs an autonomous agent to fulfill requests and generate Word documents.",
    version="1.0.0"
)

@app.post("/agent", response_model=AgentResponse)
async def process_agent_request(request: AgentRequest):
    if not request.request.strip():
        raise HTTPException(status_code=400, detail="Request string cannot be empty.")
        
    print(f"\n[API] Received request: {request.request}")
    
    # Run the autonomous agent workflow
    result = run_agent(request.request)
    
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
        
    return AgentResponse(
        status=result["status"],
        message=result["message"],
        document_path=result["document_path"],
        plan=result["plan"]
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
