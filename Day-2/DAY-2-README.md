# ☕ Day 2 – Coffee Shop Barista Voice Agent

Part of the **Murf AI – 10 Days of Voice Agents Challenge**

---

## 🎯 Objective

Transform the starter voice agent into an interactive coffee shop barista that:
- Talks naturally with users.
- Collects a full coffee order through conversation.
- Maintains a structured order state.
- Saves the completed order to a JSON file.
- Uses **Murf Falcon** for ultra-fast voice responses.

---

## 🧠 Agent Persona

The agent acts as a friendly barista at **Falcon Brew**, a modern specialty coffee brand.

### Requirements:
- Ask questions to fill all fields.
- Confirm choices briefly.
- Call `save_order` tool **only after all fields are known**.
- Speak naturally and conversationally.
- Avoid markdown, emojis, or unnecessary formatting.

---

## 🗂️ Order State Object

The agent must collect the following:

```json
{
  "drinkType": "string",
  "size": "string",
  "milk": "string",
  "extras": ["string"],
  "name": "string"
}
```

### Order Flow:
1. `drinkType`
2. `size`
3. `milk`
4. `extras` (or “none”)
5. `name`

The order is saved to `coffee_order.json`.

---

## 🔧 What I Implemented

### ✔ Updated `agent.py` to:
- Add a barista persona with instructions.
- Maintain order state via conversation.
- Add `save_order` tool using `@function_tool`.
- Automatically generate `coffee_order.json`.
- Confirm the order after saving.

### ✔ Added Tool Logic
Generated a JSON file such as:

```json
{
  "drinkType": "latte",
  "size": "large",
  "milk": "oat",
  "extras": ["caramel"],
  "name": "Saoud"
}
```

### ✔ Full Voice Pipeline Works
- **Deepgram Nova-3** (Speech Recognition)
- **Google Gemini 2.5 Flash** (LLM reasoning)
- **Murf Falcon** (Text-to-speech)
- **LiveKit Turn Detection + VAD**

---

## ▶️ How I Tested It

1. Opened the voice UI at [http://localhost:3000](http://localhost:3000).
2. Connected the microphone.
3. Ordered a coffee using natural speech.
4. Agent asked clarifying questions:
   - “What drink would you like?”
   - “What size?”
   - “What milk?”
   - “Any extras?”
   - “What’s your name?”
5. Order was saved automatically to `coffee_order.json`.
6. Agent verbally confirmed the final order.

---

## 📂 Day 2 Output

- Updated `backend/src/agent.py`.
- Generated `coffee_order.json`.
- Voice interaction working end-to-end.
- Demo video recorded.

---

## 🎥 Demo Video

The demo video (posted on LinkedIn) shows:
- Live agent conversation.
- Order flow completion.
- JSON file generation.
- **Murf Falcon’s** fast responses.

---

## 🎉 Day 2 Completed Successfully

The coffee shop barista agent is fully functional and ready for further improvements in the next days.