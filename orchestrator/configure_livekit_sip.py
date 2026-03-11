#!/usr/bin/env python3
"""Configure LiveKit SIP Trunking for Zadarma"""

import asyncio
from livekit.api import LiveKitAPI
from livekit.protocol.sip import (
    CreateSIPInboundTrunkRequest,
    CreateSIPDispatchRuleRequest
)

LIVEKIT_URL = "http://localhost:7880"
LIVEKIT_API_KEY = "openclaw-54990a102ce72a4e"
LIVEKIT_API_SECRET = "e60d2b7fe4e493123f71251e29dc4b1752d18d983a0ee8b41058b18b9b168ba9"

async def configure_sip():
    api = LiveKitAPI(url=LIVEKIT_URL, api_key=LIVEKIT_API_KEY, api_secret=LIVEKIT_API_SECRET)
    
    print("🎤 Configurando SIP Trunking para Zadarma...")
    
    try:
        # 1. Crear SIP Inbound Trunk
        print("\n1. Creando SIP Inbound Trunk...")
        trunk = await api.sip.create_inbound_trunk(
            CreateSIPInboundTrunkRequest(
                trunk={
                    "name": "Zadarma-Inbound",
                    "metadata": "Zadarma PSTN → LiveKit",
                    "numbers": ["+34919935163"],
                    "allowed_addresses": ["46.224.204.126"],
                    "auth_username": "livekit",
                    "auth_password": "livekit"
                }
            )
        )
        print(f"   ✅ Trunk ID: {trunk.sip_trunk_id}")
        
        # 2. Crear Dispatch Rule
        print("\n2. Creando Dispatch Rule...")
        rule = await api.sip.create_dispatch_rule(
            CreateSIPDispatchRuleRequest(
                rule={
                    "trunk_ids": [trunk.sip_trunk_id],
                    "rule": {"dispatch_rule_direct": {"room_prefix": "call-", "pin": ""}}
                }
            )
        )
        print(f"   ✅ Rule ID: {rule.id}")
        
        await api.aclose()
        
        print("\n✅ SIP CONFIGURADO!")
        print("   📞 Zadarma → LiveKit: 46.224.204.126:5060")
        print("   🏠 Rooms: call-{caller_id}")
        print("   🔐 Auth: livekit/livekit")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        await api.aclose()

if __name__ == "__main__":
    asyncio.run(configure_sip())
