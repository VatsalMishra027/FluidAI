# Autonomous AI Agent - 60 Minute Build Challenge

## Overview
This repository contains a FastAPI-based autonomous AI agent built to fulfill the requirements of the 60-Minute Build Challenge. The agent takes a natural language request, plans the necessary sections for a business document, drafts the content, reviews it (self-reflection), and outputs a polished Microsoft Word (`.docx`) document.

## Architecture
- **FastAPI**: Provides the REST API endpoint (`POST /agent`).
- **LangGraph**: Orchestrates the autonomous agent workflow using a state machine.
- **LangChain & Gemini API**: Powers the LLM intelligence for planning, drafting, and reviewing.
- **python-docx**: Generates the final `.docx` output.

## Real Engineering Improvement: Reflection / Self-Check
I implemented **Reflection/self-check** in the agent's workflow using a dedicated `reviewer_node` in LangGraph.

**How it works**:
1. The **Planner** breaks down the task.
2. The **Drafter** writes the initial content.
3. The **Reviewer** reads the drafted content and compares it to the *original user request*. 
4. If the Reviewer finds missing information or poor quality, it generates critical feedback and sends the state back to the Drafter. 
5. The loop continues until the Reviewer approves the content or the recursion limit is hit.

**Why I chose it and how it improves the agent**:
Autonomous agents often hallucinate or lazily skip requirements. By adding a distinct "Reviewer" step, we enforce a quality control gate. The agent literally critiques its own work, drastically improving reliability, adherence to complex instructions, and final document quality without requiring human intervention.

## Setup Instructions

1. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**:
   A `.env` file is already provided with the Gemini API key. Ensure it looks like this:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

3. **Run the API Server**:
   ```bash
   python main.py
   ```
   *The server will start on `http://0.0.0.0:8000`*

4. **Run the Tests**:
   In a new terminal window, run the provided test script to hit the API with both standard and complex requests:
   ```bash
   python test_endpoints.py
   ```

## API Endpoint Reference

**`POST /agent`**
- **Body**: `{"request": "string"}`
- **Response**: 
  ```json
  {
    "status": "success",
    "message": "Document generated successfully.",
    "document_path": "outputs/Generated_Document_123456789.docx",
    "plan": ["Section 1", "Section 2"]
  }
  ```
