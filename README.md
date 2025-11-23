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

### 🔹 Day 3 – Coming soon…
- *(Will update daily)*

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