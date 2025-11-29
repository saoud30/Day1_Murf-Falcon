# 🎙️ Murf AI – 10 Days of Voice Agents Challenge

This repository contains all my work for the **Murf Falcon 10-Day Voice Agent Challenge**, where I build one new voice agent every day using:

- **LiveKit Agents**
- **Deepgram STT**
- **Gemini LLM**
- **Murf Falcon TTS** (fastest TTS API)
- Custom personas, tools, state machines, and more.

Each day has its own folder and documentation.

---

## 📅 Daily Progress

### 🔹 Day 1 – Starter Voice Agent
- Setup backend, frontend, LiveKit server.
- Connected and had first conversation.
- **Folder**: `Day-1/`
- **README**: `Day-1\DAY-1-README.md`

### 🔹 Day 2 – Coffee Shop Barista Agent
- Created a persona-driven barista.
- Implemented order state machine.
- Added `save_order` tool to generate `coffee_order.json`.
- Voice-driven ordering via browser.
- **Folder**: `Day-2/`
- **README**: `Day-2\DAY-2-README.md`

### 🔹 Day 3 – Health & Wellness Voice Companion
- Built a wellness companion agent.
- Checks in on mood, energy, and daily goals.
- Saves check-ins to `wellness_log.json`.
- References past sessions for continuity.
- **Folder**: `Day-3/`
- **README**: `Day-3\DAY-3-README.md`

### 🔹 Day 4 – Teach-the-Tutor Active Recall Coach
- Built an active recall coach with 3 learning modes:
  - **Learn mode** (Matthew voice).
  - **Quiz mode** (Alicia voice).
  - **Teach-back mode** (Ken voice).
- Content sourced from a small JSON file.
- Users can switch modes anytime.
- Instant voice-switching powered by **Murf Falcon**.
- **Folder**: `Day-4/`
- **README**: `Day-4\DAY-4-README.md`

### 🔹 Day 5 – Zerodha SDR + Lead Capture
- Built a Sales Development Representative (SDR) agent for Zerodha.
- Greets visitors and asks about their needs.
- Uses a small Zerodha FAQ JSON file to answer product/pricing questions.
- Collects key lead details during the call.
- Generates an end-of-call summary and saves the lead to `zerodha_leads.json`.
- **Folder**: `Day-5/`
- **README**: `Day-5\DAY-5-README.md`

### 🔹 Day 6 – Fraud Alert Voice Agent
- Built a voice-based Fraud Alert Agent for Horizon Bank.
- Loads a fraud case from a JSON “database”.
- Verifies the customer with a safe, non-sensitive question.
- Reads out a suspicious transaction and asks if the customer made it.
- Marks the case as safe or fraudulent and updates the database.
- **Folder**: `Day-6/`
- **README**: `Day-6\DAY-6-README.md`

### 🔹 Day 7 – Fitness Tracker Voice Agent
- Built a fitness tracker agent to log workouts and provide fitness tips.
- Tracks workout type, duration, and intensity.
- Provides motivational tips and fitness advice based on user input.
- Saves workout logs to `fitness_log.json`.
- References past workouts to suggest improvements or consistency.
- **Folder**: `Day-7/`
- **README**: `Day-7\DAY-7-README.md`

### 🔹 Day 8 – Voice Game Master (D&D-Style Adventure)
- Built an interactive D&D-style Game Master agent.
- Runs a fantasy adventure using only conversation history.
- Describes scenes in vivid detail and ends every message with “What do you do?”
- Remembers past player decisions and allows a short 5–15 turn mini-arc.
- **Folder**: `Day-8/`
- **README**: `Day-8\DAY-8-README.md`

### 🔹 Day 9 – ACP-Inspired E-commerce Voice Agent
- Created a voice-driven shopping assistant inspired by the Agentic Commerce Protocol (ACP).
- Uses a product catalog stored in JSON.
- Supports discovering products using filters like color, price, and category.
- Places orders via backend functions and stores them in `day9_orders.json`.
- Can recall the user's last order.
- **Folder**: `Day-9/`
- **README**: `Day-9\DAY-9-README.md`

---

## 🚀 Tech Stack

- **LiveKit Agents** (STT, LLM, TTS pipeline)
- **Deepgram Nova-3** (Speech-to-text)
- **Google Gemini 2.5 Flash** (LLM reasoning)
- **Murf Falcon** (Ultra-fast streaming text-to-speech)
- **Silero VAD + BVC** (Noise Cancellation)
- **Next.js frontend**
- **Python backend**

---

## ▶️ How to Run Locally

1. **Run LiveKit Server**
   ```bash
   .\livekit-server.exe --dev
   ```

2. **Start Backend**
   ```bash
   cd backend
   uv run python src/agent.py dev
   ```

3. **Start Frontend**
   ```bash
   cd frontend
   pnpm dev
   ```

4. **Open**:
   👉 [http://localhost:3000](http://localhost:3000)

---

## 📹 Daily LinkedIn Posts

Each day I post a small video demo on LinkedIn showcasing progress.  
Follow along on my profile!

---

## ⭐ About This Challenge

This challenge is hosted by **Murf AI**, creators of the lightning-fast **Falcon TTS engine**.  
The goal: build **10 functional voice agents in 10 days** with increasing complexity.

❤️ Thanks for visiting the project!  
More updates coming daily.