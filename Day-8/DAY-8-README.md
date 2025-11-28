# Day 8 – Voice Game Master (D&D-Style Adventure)

## What I Built
For Day 8 of the Murf AI Voice Agents Challenge, I turned my voice agent into an interactive D&D-style Game Master.

The GM:
- Runs a fantasy adventure using only conversation history.
- Describes scenes in vivid detail.
- Ends every message with “What do you do?”
- Remembers past player decisions through chat history.
- Allows a short 5–15 turn mini-arc to play out.

## Files
- backend/agent.py (updated for Day 8)
- Day-8/DAY-8-README.md

## How to Test
1. Start backend + frontend as usual.
2. The game begins automatically:
   - You wake near an ancient forest.
3. Speak actions:
   - “I look around.”
   - “I walk toward the ruins.”
   - “I draw my sword.”
4. The GM will continue the adventure based only on history.
