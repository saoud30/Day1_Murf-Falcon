# 📅 Day 1 – Getting the Starter Voice Agent Running

Today I completed **Day 1** of the **Murf AI – 10 Days of Voice Agents Challenge**.

The goal was to set up the provided starter repository, run the backend and frontend, connect to the LiveKit server, and have a working conversation with an agent powered by **Murf Falcon TTS**.

---

## ✅ What I Accomplished Today

### 1. Set Up & Ran LiveKit Server
- Installed and configured LiveKit Server in development mode.
- Exposed WebSocket endpoint at `ws://localhost:7880`.
- Verified server logs & system connectivity.
- Ensured networking + firewall access for RTC ports.

### 2. Configured and Ran Backend (Python Agent)
- Installed all dependencies using `uv`.
- Downloaded required models (Deepgram, Google, Silero, Murf Falcon).
- Created `.env.local` with:
  ```
  LIVEKIT_URL
  LIVEKIT_API_KEY
  LIVEKIT_API_SECRET
  MURF_API_KEY
  ```
- Successfully launched the agent using:
  ```bash
  uv run python src/agent.py dev
  ```
- Backend connected to LiveKit immediately and began listening for sessions.

### 3. Ran the Frontend (Next.js + LiveKit Components)
- Installed dependencies using `pnpm`.
- Created `.env.local`.
- Started local dev server with:
  ```bash
  pnpm dev
  ```

### 🎙️ 4. First Conversation Test
- Opened the UI at `http://localhost:3000`.
- Clicked **Connect**, allowed microphone permissions, and initiated my first conversation.
- The agent responded instantly using **Murf Falcon** — extremely fast TTS with very low latency.

This completed the core requirement of Day 1.

### 🎥 5. Recorded My Demo Video
- Recorded a short screen capture showing:
  - Running frontend.
  - Voice interaction.
  - Real-time responses with Murf Falcon.

### 🔗 6. Posted on LinkedIn
- Shared my Day-1 update with video and tagged:
  - **@Murf AI**
- Used hashtags:
  - `#MurfAIVoiceAgentsChallenge`
  - `#10DaysofAIVoiceAgents`

---

## 📁 Project Commands Used Today

### Start LiveKit Server
```bash
.\livekit-server.exe --dev
```

### Backend
```bash
cd backend
uv sync
cp .env.example .env.local
uv run python src/agent.py download-files
uv run python src/agent.py dev
```

### Frontend
```bash
cd frontend
pnpm install
cp .env.example .env.local
pnpm dev
```

---

## 🚀 Day 1 Completed Successfully

Everything is running end-to-end:
- **LiveKit (RTC Server)** ✔
- **Backend Agent** ✔
- **Frontend UI** ✔
- **Murf Falcon TTS** ✔
- **Successful conversation** ✔
- **GitHub repo updated** ✔
- **LinkedIn post uploaded** ✔

Ready for **Day 2**!