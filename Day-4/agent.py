import logging
import json
from pathlib import Path

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    WorkerOptions,
    cli,
    metrics,
    tokenize,
    function_tool,
    RunContext,
)
from livekit.plugins import murf, silero, google, deepgram, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

logger = logging.getLogger("agent")

load_dotenv(".env.local")

# Tutor conten
CONTENT_PATH = Path("shared-data/day4_tutor_content.json")


def load_content():
    try:
        with CONTENT_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


class TutorAgent(Agent):
    def __init__(self):
        self.content = load_content()

        base = (
            "You are an Active Recall Coach with three modes:\n"
            "1) learn – explain a concept clearly.\n"
            "2) quiz – ask questions and wait for user answers.\n"
            "3) teach_back – ask the user to teach the concept back and give simple, encouraging feedback.\n\n"
            "Rules:\n"
            "- Always ask the user which mode they want.\n"
            "- User can switch modes anytime (e.g., 'switch to quiz mode').\n"
            "- Keep responses short and conversational.\n"
            "- Use NO emojis or formatting.\n"
            "- Change TTS voice based on mode:\n"
            "   learn: Matthew\n"
            "   quiz: Alicia\n"
            "   teach_back: Ken\n"
            "- Pull explanations and quiz questions from the JSON file.\n"
            "- Let the user choose the concept when needed.\n"
        )

        super().__init__(instructions=base)

    # -------------------------
    # TOOLS
    # -------------------------

    @function_tool
    async def tutor_learn(self, ctx: RunContext, concept_id: str) -> str:
        """Explain a concept using learn mode voice."""
        concept = next((c for c in self.content if c["id"] == concept_id), None)
        if not concept:
            return "I could not find that concept."

        # switch voice
        ctx.session.tts.update_voice("en-US-matthew")

        return f"Here is a simple explanation of {concept['title']}: {concept['summary']}"

    @function_tool
    async def tutor_quiz(self, ctx: RunContext, concept_id: str) -> str:
        """Ask a quiz question in quiz mode (Alicia)."""
        concept = next((c for c in self.content if c["id"] == concept_id), None)
        if not concept:
            return "This concept is not available."

        ctx.session.tts.update_voice("en-US-alicia")

        return f"Here is a question: {concept['sample_question']}"

    @function_tool
    async def tutor_teach_back(self, ctx: RunContext, concept_id: str) -> str:
        """Ask the user to teach back the concept using Ken's voice."""
        concept = next((c for c in self.content if c["id"] == concept_id), None)
        if not concept:
            return "I cannot find that concept."

        ctx.session.tts.update_voice("en-US-ken")

        return (
            f"Please explain the concept {concept['title']} in your own words. "
            "Take your time. After you explain, I will give feedback."
        )


# ---------------------------
# LiveKit setup
# ---------------------------

def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    ctx.log_context_fields = {"room": ctx.room.name}

    session = AgentSession(
        stt=deepgram.STT(model="nova-3"),
        llm=google.LLM(model="gemini-2.5-flash"),
        tts=murf.TTS(
            voice="en-US-matthew",
            style="Conversation",
            tokenizer=tokenize.basic.SentenceTokenizer(),
            text_pacing=True,
        ),
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
        preemptive_generation=True,
    )

    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on(ev: MetricsCollectedEvent):
        usage_collector.collect(ev.metrics)

    async def log_usage():
        logger.info(usage_collector.get_summary())

    ctx.add_shutdown_callback(log_usage)

    await session.start(
        agent=TutorAgent(),
        room=ctx.room,
        room_input_options=RoomInputOptions(noise_cancellation=noise_cancellation.BVC()),
    )

    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
