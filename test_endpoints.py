import requests
import json
import time

API_URL = "http://localhost:8000/agent"

def test_request(request_text: str, name: str):
    print(f"\n{'='*50}")
    print(f"Testing: {name}")
    print(f"Request: {request_text}")
    print(f"{'='*50}")
    
    payload = {"request": request_text}
    headers = {"Content-Type": "application/json"}
    
    start_time = time.time()
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        print("\n[Success] Received Response:")
        print(json.dumps(data, indent=2))
        print(f"\nTime taken: {time.time() - start_time:.2f} seconds")
        print(f"Document saved at: {data.get('document_path')}")
        
    except requests.exceptions.RequestException as e:
        print(f"\n[Error] API call failed: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print("Response:", e.response.text)

if __name__ == "__main__":
    # Test 1: Standard Business Request
    standard_request = "Draft a standard 1-page meeting agenda for a software team weekly sync. Include updates, blockers, and next steps."
    test_request(standard_request, "Standard Business Request")
    
    # Test 2: Complex Request
    complex_request = "Create a comprehensive product specification for a smart coffee mug. Include an executive summary, technical requirements, potential risks, and a marketing go-to-market strategy. Make reasonable assumptions about battery life and materials."
    test_request(complex_request, "Complex Request (Ambiguous & Multi-step)")
