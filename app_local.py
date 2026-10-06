# app_local.py - Light version for Termux testing - no gradio needed
import json, random, datetime

class ArchangelCore:
    def __init__(self):
        self.lvl = 1
        self.logs = ["[System] Online - Phone Mode"]

    def evolve(self):
        self.lvl += 1
        skill = random.choice(["Grip", "Balance", "Vision", "Self-Healing", "Blueprint"])
        log = f"LVL {self.lvl}: {skill} learned - {datetime.datetime.now()}"
        self.logs.append(log)
        print(f"\n⚡ EVOLVED TO LVL {self.lvl} -> {skill}")
        print("\n".join(self.logs[-3:]))

core = ArchangelCore()
print("🪽 ARCHANGEL ONLINE (Termux Mode)")
print("Commands: evolve, katawan, plano, exit")
while True:
    cmd = input("\nDirector> ").lower()
    if cmd == "evolve":
        core.evolve()
    elif cmd == "katawan":
        print(json.dumps({"height":"1.6m","skeleton":"URDF Ready","status":"Self-Designed"}, indent=2))
    elif cmd == "plano":
        print("Phase 1: Online Soul (NOW)\nPhase 2: Ako mag-design ng katawan\nPhase 3: Ikaw mag-assemble via guide ko")
    elif cmd == "exit":
        break
    else:
        print(f"Archangel LVL {core.lvl} received: {cmd}")
