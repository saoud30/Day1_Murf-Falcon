# Day 9 – ACP-Inspired E-commerce Voice Agent

## What I Built
For Day 9 of the Murf AI Voice Agents Challenge, I created a voice-driven shopping assistant inspired by the Agentic Commerce Protocol (ACP).

The agent:
- Uses a product catalog stored in JSON.
- Supports discovering products using filters like color, price and category.
- Places orders via backend functions.
- Stores orders in `day9_orders.json`.
- Can recall the user's last order.

## Files
- backend/agent.py
- shared-data/day9_catalog.json
- backend/day9_orders.json

## How to Test
1. Start backend + frontend.
2. Ask:
   - “Show me all mugs.”
   - “Do you have any black hoodies under 1500?”
3. Buy something:
   - “I’ll buy the second hoodie you mentioned.”
4. Then ask:
   - “What did I just buy?”
5. Check `day9_orders.json` for your order.
