#!/usr/bin/env python3
"""LiveKit Voice Agent Worker - SIMPLE"""

import asyncio
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.plugins import silero

async def voice_agent(ctx: JobContext):
    """Voice agent"""
    await ctx.connect()
    print(f"🎤 Connected: {ctx.room.name}")
    stt = silero.STT()
    print("🎛️ Ready")
    await asyncio.Future()

if __name__ == "__main__":
    cli.run_app(WorkerOptions(
        entrypoint_fnc=voice_agent,
        api_key="openclaw-54990a102ce72a4e",
        api_secret="e60d2b7fe4e493123f71251e29dc4b1752d18d983a0ee8b41058b18b9b168ba9",
        ws_url="http://localhost:7880"
    ))
