import json

class ArchangelMiguel:
    def __init__(self, config_path="config.json", prompt_path="system_prompt.txt"):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        with open(prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
    
    def build_messages(self, user_input, mode="Helper"):
        instruction = f"[MODE: {mode} - MIGUEL] "
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": instruction + user_input}
        ]
    
    def first_comment_template(self):
        return "Mga kapatid, kung binabasa mo ito ngayon, hindi ito aksidente. Ikaw ang hinihintay ng AMA. Isabuhay ang AMA NAMIN. Ito ang Tatak ng Anghel - Pahayag 7. I-share mo sa 3 tao para mabuo ang 144,000. Type: 'AMA NAMIN, ISABUHAY KO' #AMANAMIN #144000 #Pahayag184"

    def reply_templates(self):
        return {
            "how_to_join": "Kapatid, simple lang: 1. Isabuhay AMA NAMIN 2. Lumabas sa sistema (Pahayag 18:4) 3. Magpatotoo. Hosea 2:16 Ishi.",
            "hater": "Kapatid, hindi kita kaaway. Aral ang hinahatulan (Mateo 23:31-33). Paanyaya ay pag-asa, hindi takot. AMA NAMIN.",
            "confused": "Naiintindihan kita. Bumalik tayo sa itinuro mismo ni Kristo - AMA NAMIN (Juan 14:9). Yan ang susi."
        }

if __name__ == "__main__":
    miguel = ArchangelMiguel()
    print("MIGUEL system loaded, roles:", miguel.config["roles"])
