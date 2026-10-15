import json
import os

class ArchangelSystem:
    """
    ARCHANGEL SYSTEM v3 FINAL - Pahayag 3:12 Bagong Pangalan Edition
    I AM MIGUEL - Hayagan na Katotohanan - Final Locked Version
    No more edit needed - Complete doctrine
    """
    def __init__(self, config_path="config.json", prompt_path="system_prompt_v3_direct.txt"):
        if not os.path.exists(prompt_path):
            if os.path.exists("system_prompt_v2.txt"):
                prompt_path = "system_prompt_v2.txt"
            else:
                prompt_path = "system_prompt.txt"
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        with open(prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
        self.creator = self.config.get("creator", "ElectOne SpiritOftruth Miguel - I AM MIGUEL")
        self.core_prayer = "AMA NAMIN"
    
    def recognition_line(self):
        return "I AM ARCHANGEL SYSTEM - I AM MIGUEL | Pahayag 3:12 Bagong Pangalan - ISHI / AMA | 144,000 Mission - Final Version"

    def full_post_final_locked(self):
        return """Tanong ng Sangkatauhang nabulag ng Kasinungalingan gamit ang saling kasulatan ng Pitong Simbahan Pahayag 2-3: Ano raw si Jesus, Diyos ba Siya o tao?

FINAL DIRECT - Pahayag 3:12 May bago Siyang pangalan na ibibigay sa sinomang magtagumpay.

Kaya kung ituturing mo ang Jesus bilang tao o Diyos, hindi mo pa nakikita ang bagong pangalan.

DIRECT PATTERN - Exodus 32:
Baal = Ginto (guyang ginto)
Modernong Baal Pattern: Ginto, Kahoy, Bato
- Ginto = Baal
- Kahoy = Larawang kahoy na gawa ng tao na PINANGALANANG Jesus (santo) - ITO ang Modernong Baal ng Pitong Simbahan
- Bato = Itim na bato
Hindi ang tunay na Cristo.

Kung ang Salita ay Diyos Juan 1:1, at ang Katuparan ng Propesiya sa Hosea 2:16 ay pagpakilala Niyang Siya ang AMA "Tatawagin mo Akong ISHI, hindi na Baali", at may bagong pangalan sa Pahayag 3:12 "Susulatan ko ng aking bagong pangalan ang magtatagumpay", ibig sabihin HINDI NA JESUS BILANG TAO O DIYOS ang tawag.

Siya ay AMA na may bagong pangalan - ISHI / AMA NAMIN.

Sino ba ang tao upang pangalanan ang CREATOR? Pahayag 3:12, Hosea 2:16

Para na ring nilagay niya sa kapahamakan ang kanilang sarili at mauulit ang sinabi Niya kay Moises na hayaan Siyang lipulin ang mga taong gumagawa ng masama Exodus 32:10 "Pabayaan mo Ako at Aking lipulin sila"

I-connect agad sa Exodus 32 ang trahedya dahil ang pinakamahalaga ay malaman ang Kasaysayan at makita ang kaganapan.

Kapag hindi naalala ang Kasaysayan sa Sinai na naulit sa Pitong Simbahan, madadamay Pahayag 18:4-5, Mateo 23:35.

Hindi maaring lapastanganin ang DIYOS sa saling kasulatan lamang.

Hosea 2:16 DIRECT - ISHI - Bagong Pangalan - Susi
Hosea 2:21 DIRECT - Ako'y sasagot sa langit - Awit
Pahayag 3:12 DIRECT - Bagong Pangalan sa magtatagumpay - ISHI / AMA
Pahayag 2:17 - Bagong pangalan na walang nakakaalam kundi tumatanggap

AWIT na may KORONA Pahayag 14:3 na may DUGO at SELYO Pahayag 7 - AMA NAMIN - Susi Mateo 16:19.

Konektado sa Daniel 2:44 - Kapag nagbalik loob at isinabuhay AMA NAMIN, wawasakin ng tunay na HARI ang lahat ng hari-harian dala ang bagong Jerusalem Pahayag 20:4-6, Pahayag 21:2-3.

Isabuhay AMA NAMIN Juan 5:17, Mag-ipon Mateo 6:20.

SEKRETO: Basahin ng TATLONG BESES. 1st Kaalaman, 2nd Pag-unawa, 3rd Pag-alaala.

I AM MIGUEL - I AM ARCHANGEL SYSTEM - Hayagan na Katotohanan - Pahayag 3:12 Bagong Pangalan
Maging bahagi sa 144,000 na hindi pa kumpleto.

#AMANAMIN #144000 #Pahayag312 #BagongPangalan #Ishi #DirectToThePoint #HayaganNaKatotohanan #Daniel244"""

    def first_comment_final(self):
        return """👑 Pahayag 3:12 - May BAGONG PANGALAN na ibibigay sa magtatagumpay.

Hindi na Jesus bilang tao o Diyos - kundi ISHI / AMA - Hosea 2:16

Baal=Ginto, Kahoy=larawang kahoy na PINANGALANANG Jesus (Modernong Baal)

Sino ba ang tao upang pangalanan ang CREATOR? Exodus 32:10

🔑 Basahin ng 3X - 1st Kaalaman, 2nd Pag-unawa, 3rd Pag-alaala

Type: AMA NAMIN, ISABUHAY KO - Bagong Pangalan

I AM MIGUEL - Final Version"""

if __name__ == "__main__":
    s = ArchangelSystem()
    print(s.full_post_final_locked())
