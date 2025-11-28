# Day 7 – Food & Grocery Ordering Voice Agent

## What I Built
For Day 7 of the Murf AI Voice Agents Challenge, I built a grocery & food ordering voice assistant for a fictional service called QuickCart.

The agent:
- Loads catalog items from JSON
- Supports adding/removing/updating items in cart
- Understands “ingredients for X” requests
- Shows the cart on request
- Places the final order into a JSON file (`day7_order.json`)

## Files
- backend/agent.py
- shared-data/day7_catalog.json
- shared-data/day7_recipe_map.json
- backend/day7_order.json (created after placing order)

## How to Test
1. Start backend & frontend.
2. Ask:
   - “Add 2 breads”
   - “Add peanut butter”
   - “I need ingredients for pasta for two”
   - “What’s in my cart?”
3. When done: “Place my order.”
4. Check the file `day7_order.json`.
