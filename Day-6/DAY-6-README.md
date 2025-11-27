# Day 6 – Fraud Alert Voice Agent (Primary Goal)

## What I Built
For Day 6 of the Murf AI Voice Agents Challenge, I built a voice-based Fraud Alert Agent for a fictional Indian bank called Horizon Bank.

The agent:
- Loads a fraud case from a JSON “database”
- Verifies the customer with a safe, non-sensitive question
- Reads out a suspicious transaction
- Asks whether the customer made it
- Marks the case as safe or fraudulent
- Writes the updated status back to the database

## Files
- backend/agent.py – Fraud voice agent
- shared-data/day6_fraud_cases.json – Fake fraud case database
- Day-6/DAY-6-README.md – this file

## How it Works
1. Start a voice session
2. Agent asks for user’s first name
3. Loads matching fraud case
4. Performs verification
5. Reads suspicious transaction
6. Asks “Did you make this?”
7. Updates database with result

## JSON Database Output Example
```json
{
  "status": "confirmed_safe",
  "outcomeNote": "Customer confirmed the transaction as legitimate."
}
