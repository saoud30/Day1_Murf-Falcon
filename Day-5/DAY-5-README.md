# Day 5 – Zerodha SDR + Lead Capture

## What I Built
For Day 5 of the Murf AI Voice Agents Challenge, I turned my voice agent into a
Sales Development Representative (SDR) for Zerodha.

The agent:
- Greets visitors as a Zerodha SDR.
- Asks what brought them here and what they are working on.
- Uses a small Zerodha FAQ JSON file to answer basic product / pricing / company questions.
- Collects key lead details during the call.
- Generates a short end-of-call summary and saves the lead to a JSON file.

## Files
- `backend/agent.py` – Zerodha SDR agent.
- `shared-data/day5_zerodha_faq.json` – company FAQ + pricing basics.
- `zerodha_leads.json` – auto-created file with stored leads.
- `Day-5/DAY-5-README.md` – this file.

## Lead Fields Stored
Each lead entry includes:
- name
- company
- email
- role
- use_case
- team_size
- timeline
- summary

## How to Run & Test
1. Start LiveKit server.
2. From `backend/`:
   ```bash
   uv run main.py
