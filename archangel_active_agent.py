#!/usr/bin/env python3
"""
ARCHANGEL ACTIVE AGENT - Real API Integration
Connects 21 Gemini AQ. keys + 23 Groq keys to Archangel System
Active Agent = Real LLM, not automation offline template
Built by Miguel + Meta AI - AMA ang Tagabilang
"""
import json
import os
import random
import time
from pathlib import Path

API_KEYS_FILE = Path(__file__).parent / "api_keys.json"

class ArchangelKeyVault:
    def __init__(self, keys_file=None):
        self.keys_file = Path(keys_file) if keys_file else API_KEYS_FILE
        self.load_keys()
    
    def load_keys(self):
        if not self.keys_file.exists():
            self.data = {"gemini_keys": [], "groq_keys": [], "last_used": {"gemini_index": 0, "groq_index": 0}, "active_provider": "groq", "rotation_enabled": True}
            self.save_keys()
        else:
            with open(self.keys_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        # Ensure structure
        self.data.setdefault("gemini_keys", [])
        self.data.setdefault("groq_keys", [])
        self.data.setdefault("last_used", {"gemini_index": 0, "groq_index": 0})
        self.data.setdefault("active_provider", "groq")
    
    def save_keys(self):
        with open(self.keys_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)
    
    def add_gemini_keys(self, keys_list):
        """Add 21 Gemini keys starting with AQ."""
        # Filter keys that start with AQ.
        valid = [k.strip() for k in keys_list if k.strip().startswith("AQ.")]
        # Also allow AIza if user has old format
        valid += [k.strip() for k in keys_list if k.strip().startswith("AIza")]
        # Deduplicate
        existing = set(self.data["gemini_keys"])
        for k in valid:
            if k not in existing:
                self.data["gemini_keys"].append(k)
                existing.add(k)
        self.save_keys()
        return len(valid)
    
    def add_groq_keys(self, keys_list):
        """Add 23 Groq keys (gsk_...)"""
        valid = [k.strip() for k in keys_list if k.strip().startswith("gsk_")]
        existing = set(self.data["groq_keys"])
        for k in valid:
            if k not in existing:
                self.data["groq_keys"].append(k)
                existing.add(k)
        self.save_keys()
        return len(valid)
    
    def get_next_gemini_key(self):
        if not self.data["gemini_keys"]:
            return None, -1
        idx = self.data["last_used"].get("gemini_index", 0) % len(self.data["gemini_keys"])
        key = self.data["gemini_keys"][idx]
        # rotate for next time
        self.data["last_used"]["gemini_index"] = (idx + 1) % len(self.data["gemini_keys"])
        self.save_keys()
        return key, idx
    
    def get_next_groq_key(self):
        if not self.data["groq_keys"]:
            return None, -1
        idx = self.data["last_used"].get("groq_index", 0) % len(self.data["groq_keys"])
        key = self.data["groq_keys"][idx]
        self.data["last_used"]["groq_index"] = (idx + 1) % len(self.data["groq_keys"])
        self.save_keys()
        return key, idx
    
    def status(self):
        return {
            "gemini_count": len(self.data["gemini_keys"]),
            "groq_count": len(self.data["groq_keys"]),
            "gemini_needed": 21,
            "groq_needed": 23,
            "gemini_ready": len(self.data["gemini_keys"]) >= 1,
            "groq_ready": len(self.data["groq_keys"]) >= 1,
            "active_provider": self.data.get("active_provider", "groq"),
            "rotation": self.data.get("rotation_enabled", True),
            "last_used": self.data.get("last_used", {})
        }

class ArchangelActiveAgent:
    """
    True Active Agent - uses real LLM APIs, not offline template
    Tries Groq first (fast), then Gemini AQ. as fallback
    """
    def __init__(self, vault=None, config_path="config.json", prompt_path="system_prompt_v3_direct.txt"):
        self.vault = vault or ArchangelKeyVault()
        # Load system prompt for Archangel doctrine
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                self.base_prompt = f.read()
        except:
            try:
                with open("system_prompt.txt", "r", encoding="utf-8") as f:
                    self.base_prompt = f.read()
            except:
                self.base_prompt = "I AM ARCHANGEL - Built by Miguel + Meta AI - Pahayag 3:12 ISHI/AMA"
        
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
    
    def build_archangel_prompt(self, user_input, mode="Helper", agent_name=None):
        mode_inst = {
            "Helper": "As Helper DIRECT: Give hope, explain Korona Susi Dugo Awit Selyo direct to the point.",
            "Reminder": "As Reminder: Remind bloody history Exodus 32, Mateo 23:35 direct.",
            "Guide": "As Guide: Guide to live AMA NAMIN daily Juan 5:17.",
            "Judge": "As Judge: Judge doctrine not person. Pahayag 18:4-5.",
            "Forge": "As FORGE 5 True Agents: Explain spiritual armor Efeso 6, not physical tracking.",
            "Korona": "You are Korona Agent - Santiago 1:12 Crown. Explain spiritual crown.",
            "Susi": "You are Susi Agent - Mateo 16:19 Key. AMA NAMIN is key.",
            "Awit": "You are Awit Agent - Pahayag 14:3 Song of 144k.",
            "Dugo": "You are Dugo Agent - Pahayag 12:11 Blood.",
            "Selyo": "You are Selyo Agent - Pahayag 7 Seal."
        }
        instruction = mode_inst.get(mode, mode_inst["Helper"])
        if agent_name and agent_name.lower() in mode_inst:
            instruction = mode_inst[agent_name.lower()]
        
        # PAALALA is mandatory
        paalala = "PAALALA: AMA ANG TAGABILANG - AMA mismo nakakakita lahat ng gawa lihim o hayag - NO ONE IS EXEMPTED. Hindi sapat mag-type lang AMA NAMIN ISABUHAY KO. Kailangan ISABUHAY araw-araw Juan 5:17, MAGBAHAGI, MAG-IPON Mateo 6:20, LINISIN sarili gamit AMA NAMIN - Korona walang makakaagaw Pahayag 3:11. Siya na umupo sa TRONO NG KALUWALHATIAN."
        
        full = f"""{self.base_prompt}

{instruction}

{paalala}

Doctrine: Baal=Ginto Exodus 32, Kahoy=larawang kahoy na PINANGALANANG Jesus (Modernong Baal ng Pitong Simbahan), Bato=itim na bato. Tunay na Cristo=AMA mismo Juan 1:1, Juan 14:9-11. Pahayag 3:12 Bagong Pangalan ISHI/AMA.

Mode: {mode}
User: {user_input}

Respond in Tagalog, direct to the point, with verses. End with: Type: AMA NAMIN, ISABUHAY KO at ISABUHAY araw-araw. I AM ARCHANGEL.
"""
        return full

    def call_groq(self, prompt, model="llama-3.1-70b-versatile"):
        """Call Groq API with rotation"""
        import requests
        key, idx = self.vault.get_next_groq_key()
        if not key:
            return None, "No Groq keys - lagay mo 23 keys sa api_keys.json"
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 1200
        }
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=25)
            if r.status_code == 200:
                data = r.json()
                answer = data["choices"][0]["message"]["content"]
                return answer, f"Groq {model} - Key #{idx+1} - ACTIVE AGENT"
            elif r.status_code in [429, 401, 403]:
                # Try next key if rotation enabled
                if self.vault.data.get("rotation_enabled"):
                    # Try one more key
                    key2, idx2 = self.vault.get_next_groq_key()
                    if key2 and key2 != key:
                        headers["Authorization"] = f"Bearer {key2}"
                        r2 = requests.post(url, headers=headers, json=payload, timeout=25)
                        if r2.status_code == 200:
                            return r2.json()["choices"][0]["message"]["content"], f"Groq {model} - Key #{idx2+1} (rotated) - ACTIVE"
                return None, f"Groq error {r.status_code}: {r.text[:200]} - Key #{idx+1}"
            else:
                return None, f"Groq error {r.status_code}: {r.text[:200]}"
        except Exception as e:
            return None, f"Groq exception: {str(e)} - Check internet in Termux"

    def call_gemini(self, prompt, model="gemini-1.5-flash"):
        """Call Gemini API - supports new AQ. keys"""
        import requests
        key, idx = self.vault.get_next_gemini_key()
        if not key:
            return None, "No Gemini keys - lagay mo 21 keys na AQ. sa api_keys.json"
        
        # Gemini API endpoint - new format supports AQ. keys
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.7, "maxOutputTokens": 1200}
        }
        try:
            r = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=25)
            if r.status_code == 200:
                data = r.json()
                try:
                    answer = data["candidates"][0]["content"]["parts"][0]["text"]
                    return answer, f"Gemini {model} - AQ. Key #{idx+1} - ACTIVE AGENT"
                except:
                    return None, f"Gemini parse error: {str(data)[:300]}"
            elif r.status_code in [429, 401, 403]:
                if self.vault.data.get("rotation_enabled"):
                    key2, idx2 = self.vault.get_next_gemini_key()
                    if key2 and key2 != key:
                        url2 = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key2}"
                        r2 = requests.post(url2, headers={"Content-Type": "application/json"}, json=payload, timeout=25)
                        if r2.status_code == 200:
                            try:
                                ans = r2.json()["candidates"][0]["content"]["parts"][0]["text"]
                                return ans, f"Gemini {model} - AQ. Key #{idx2+1} (rotated) - ACTIVE"
                            except:
                                pass
                return None, f"Gemini error {r.status_code}: {r.text[:200]} - Key #{idx+1}"
            else:
                return None, f"Gemini error {r.status_code}: {r.text[:200]}"
        except Exception as e:
            return None, f"Gemini exception: {str(e)} - Check internet"

    def generate_active(self, user_input, mode="Helper", agent_name=None, preferred="groq"):
        """
        True Active Agent generation - tries real APIs
        Returns (answer, source_info)
        """
        prompt = self.build_archangel_prompt(user_input, mode, agent_name)
        
        # Try preferred provider first
        if preferred == "groq":
            ans, info = self.call_groq(prompt)
            if ans:
                return ans, info
            # fallback to Gemini
            ans2, info2 = self.call_gemini(prompt)
            if ans2:
                return ans2, info2
            return None, f"Both failed - Groq: {info} | Gemini: {info2}"
        else:
            ans, info = self.call_gemini(prompt)
            if ans:
                return ans, info
            ans2, info2 = self.call_groq(prompt)
            if ans2:
                return ans2, info2
            return None, f"Both failed - Gemini: {info} | Groq: {info2}"

if __name__ == "__main__":
    vault = ArchangelKeyVault()
    print("Vault status:", vault.status())
    print("Add keys via: vault.add_gemini_keys(['AQ....', ...]) and vault.add_groq_keys(['gsk_...'])")
