# Day 4 – Teach-the-Tutor: Active Recall Coach

For Day 4 of the Murf AI Voice Agents Challenge, I built an Active Recall Coach
with three learning modes driven by JSON course content.

## Features
- Modes:
  - learn → explains concepts (Matthew voice)
  - quiz → asks questions (Alicia voice)
  - teach_back → asks user to explain (Ken voice)
- User can switch modes anytime.
- Content comes from:
  shared-data/day4_tutor_content.json
- Works fully via voice in the browser.

## Files
- backend/agent.py (updated)
- shared-data/day4_tutor_content.json
- Day-4/DAY-4-README.md

## How to Test
1. Start LiveKit server.
2. Run backend:
   uv run main.py
3. Run frontend:
   pnpm dev
4. Test the three modes:
   - “I want learn mode with variables”
   - “Switch to quiz mode for loops”
   - “Switch to teach back mode for variables”
5. Confirm voices switch correctly:
   - Learn: Matthew
   - Quiz: Alicia
   - Teach-back: Ken

You have completed Day 4
