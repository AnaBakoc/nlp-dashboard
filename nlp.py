import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
import random
import time
from matplotlib.offsetbox import OffsetImage
import matplotlib.patheffects as path_effects
import plotly.graph_objects as go
import streamlit.components.v1 as components
from streamlit_extras.let_it_rain import rain
from confetti import fire_confetti
import os
#st.markdown('<a id="top"></a>', unsafe_allow_html=True)

st.markdown("""
    <style>
        .main .block-container {
            padding-top: 0rem;
        }
    </style>
""", unsafe_allow_html=True)
scroll_script = """
<script>
window.scrollTo(0, 0);
</script>
"""
st.components.v1.html(scroll_script)
nlp_tips = [
    "🎯 *Postavljanje ciljeva*:\nPostavi cilj koji možeš da vidiš, čuješ ili osetiš – ne samo da 'želiš da budeš srećan', već da 'se smeješ dok šetaš sa prijateljima'.",
    "🌀 *Fleksibilnost*:\nAko komunikacija ne daje rezultat koji želiš, promeni pristup – fleksibilnost je moć.",
    "🗺️ *Percepcija*:\nMapa nije teritorija – pokušaj da vidiš svet iz tuđe perspektive pre nego što reaguješ.",
    "🎤 *Raport*:\nKada želiš da utičeš na nekoga, uskladi ton glasa i tempo govora s njima.",
    "🔁 *Učenje iz grešaka*:\nNeuspeh ne postoji – postoji samo povratna informacija. Prilagodi se, nauči i pokušaj ponovo.",
    "🧠 *Unutrašnji dijalog*:\nTvoj unutrašnji dijalog oblikuje tvoju stvarnost. Obrati pažnju kako razgovaraš sa sobom.",
    "💎 *Resursi*:\nLjudi imaju sve resurse koji su im potrebni – samo treba da ih podsete kako da ih aktiviraju.",
    "🪞 *Ogledalo*:\nAko te neko nervira, zapitaj se: 'Šta me to kod njega podseća na mene samog?'",
    
    # Novi dodati saveti:
    "🔍 *Kalibracija*:\nPre nego što govoriš – gledaj, slušaj, opažaj. Telo često govori više od reči.",
    "💬 *Metamodel*:\nKad čuješ nejasnu izjavu poput 'Nikad me ne slušaju', postavi pitanje: 'Ko tačno?' ili 'Kada se to desilo?'.",
    "🎭 *Reframing*:\nSituacija sama po sebi nema značenje – mi joj dajemo značenje. Promeni okvir i menjaš iskustvo.",
    "🏗️ *Neurologički nivoi*:\nPromena identiteta je dublja i dugotrajnija nego promena ponašanja – pitaj se 'Ko ja postajem time što to radim?'.",
    "🎯 *Motivacija*:\nLjudi se motivišu različito – neki teže ka cilju, neki beže od problema. Prepoznaj šta pokreće tebe i druge.",
    "🧱 *Sidrenje*:\nPoveži fizički pokret sa pozitivnim osećajem. Kasnije ga možeš aktivirati u važnim trenucima.",
    "🌐 *Komunikacija*:\nZnačenje tvoje poruke je u odgovoru koji dobiješ – ne u tvojoj nameri.",
    "👁️ *Reprezentativni sistemi*:\nSlušaj da li ljudi govore 'Vidim šta misliš' ili 'To mi zvuči dobro' – time otkrivaju svoj dominantan sistem."
]


def show_confetti():
    st.balloons()




def get_module_parts(module_num):
    modules = {
        1: module_1_content(),
        2: module_2_content(),
        3: module_3_content(),
        4: module_4_content(),
        5: module_5_content(),
        6: module_6_content(),
        7: module_7_content(),
        8: module_8_content(),
    }
    return modules.get(module_num, None)
# =============================================
# EXERCISE IMPLEMENTATIONS
# =============================================
def chunking_exercise():
    st.markdown("""
    ### 🧱 Vežba: Chunking (Hijerarhija ideja)
    **Cilj:** Promena nivoa apstrakcije u komunikaciji.

    - **Chunking up:** „Zašto ti je to važno?“, „Šta je cilj?“
    - **Chunking down:** „Kako tačno?“, „Ko konkretno?“
    - **Chunking sideways:** „Šta je slično ovome?“

    **Zadatak:**
    1. Izaberi jednu izjavu.
    2. Postavljaj pitanja da se krećeš ka gore, dole ili u stranu u hijerarhiji značenja.
    """)
def metamodel_exercise():
    st.markdown("""
    ### 🎯 Cilj vežbe:
    Prepoznajte i razložite problematične obrasce u komunikaciji korišćenjem **metamodela**.

    ⬇️ Izaberite vrstu obrasca koju želite da vežbate:
    """)

    pattern = st.selectbox("Obrazac koji želite da istražite:", [
        "Brisanje: Neodređene imenice",
        "Brisanje: Neodređeni glagoli",
        "Generalizacije",
        "Izvrtanje: Uzrok - posledica",
        "Izvrtanje: Složena ekvivalencija",
        "Modalni obrasci: Mogućnosti",
        "Modalni obrasci: Neophodnosti",
        "Izgubljena referenca",
        "Nepotpuna poređenja",
        "Nominalizacije",
        "Čitanje misli"
    ])

    if pattern == "Brisanje: Neodređene imenice":
        st.markdown("""
        **Opis:** Govornik ne navodi *ko*, *gde* ili *šta* tačno.

        **Pitanja za preciziranje:**
        - Ko tačno?
        - Gde tačno?
        - Šta konkretno?

        **Primeri za vežbu:**
        - "Niko me ne razume."
        - "Negde će se pojaviti."
        - "Ko te pita da li možeš?"
        """)

    elif pattern == "Brisanje: Neodređeni glagoli":
        st.markdown("""
        **Opis:** Proces ili radnja nije jasno određena.

        **Pitanja:** Kako tačno? Na koji način?

        **Primeri za vežbu:**
        - "Volela bih da to uradimo."
        - "Dogovorili smo se sve."
        - "Sve je pokvario."
        """)

    elif pattern == "Generalizacije":
        st.markdown("""
        **Opis:** Zaključak izveden iz previše malog broja primera.

        **Pitanja:**
        - Baš uvek?
        - Možeš li da se setiš suprotnog primera?

        **Primeri:**
        - "Posao uvek dobijaju oni koji imaju vezu."
        - "Uvek kada te pozovem, nisi dostupan."
        """)

    elif pattern == "Izvrtanje: Uzrok - posledica":
        st.markdown("""
        **Opis:** Verovanje da nečije ponašanje direktno izaziva tuđe emocije.

        **Pitanja:** Kako te to tačno nervira? Kako tačno to utiče na tebe?

        **Primeri:**
        - "Tvoj pogled me nervira."
        - "On me izbacuje iz takta."
        - "Šef me često razbesni."
        """)

    elif pattern == "Izvrtanje: Složena ekvivalencija":
        st.markdown("""
        **Opis:** Dve nepovezane stvari se tretiraju kao isto.

        **Pitanja:** Kako znaš da to znači baš to? Može li značiti nešto drugo?

        **Primeri:**
        - "Kad god me on pozove, uvek bude problema."
        - "On prekida u sred rečenice, što znači da ne poštuje druge."
        """)

    elif pattern == "Modalni obrasci: Mogućnosti":
        st.markdown("""
        **Opis:** Osoba veruje da ne može ili nije moguće.

        **Pitanja:** Šta te sprečava? Kako bi bilo da možeš?

        **Primeri:**
        - "Ne mogu sve odjednom."
        - "Nikad neću imati normalne kolege."
        """)

    elif pattern == "Modalni obrasci: Neophodnosti":
        st.markdown("""
        **Opis:** Postoji unutrašnji pritisak da se nešto mora.

        **Pitanja:** Šta bi se desilo ako to ne uradiš? Zašto baš moraš?

        **Primeri:**
        - "Moram da se javim kući."
        - "Treba da kupim stan."
        """)

    elif pattern == "Izgubljena referenca":
        st.markdown("""
        **Opis:** Izostavljena je osoba koja je iznela tvrdnju.

        **Pitanje:** Ko to kaže?

        **Primeri:**
        - "Loše je spavati dugo."
        - "Prava je ludost dati otkaz."
        """)

    elif pattern == "Nepotpuna poređenja":
        st.markdown("""
        **Opis:** Upoređivanje bez jasne reference.

        **Pitanja:** U odnosu na šta? U odnosu na koga?

        **Primeri:**
        - "Bolja ti je ova ponuda."
        - "Prilično je skupo."
        """)

    elif pattern == "Nominalizacije":
        st.markdown("""
        **Opis:** Apstraktna imenica koju treba konkretizovati.

        **Pitanja:** Šta to znači konkretno? Kako znaš da se dešava?

        **Primeri:**
        - "Zdravlje je najvažnije."
        - "Danas je poštovanje zanemareno."
        """)

    elif pattern == "Čitanje misli":
        st.markdown("""
        **Opis:** Verovanje da znamo šta neko misli ili oseća.

        **Pitanje:** Kako to znaš?

        **Primeri:**
        - "Znam šta je za tebe najbolje."
        - "Šef me ne voli."
        """)
def tri_perspektive_exercise():
    st.markdown("""
    ### 🔁 Vežba: Tri perspektive

    Ova vežba pomaže da sagledaš interpersonalne konflikte iz više uglova i razviješ empatiju i objektivnost u komunikaciji.

    #### ✅ Instrukcije:
    1. **Priseti se neprijatne interakcije** koju si imao/la sa prijateljem, kolegom ili članom porodice.
    2. **Postavi tri oznake na podu** u obliku trougla, na oko 2 metra udaljenosti:
       - 🧍 Ja (1. pozicija)
       - 👤 Druga osoba (2. pozicija)
       - 👁️ Neutralni posmatrač (3. pozicija)

    ---
    #### 🎭 Koraci:
    - **Korak 1: "Ja" pozicija**  
      Stani na prvu oznaku i zapitaj:  
      `Kako ponašanje druge osobe utiče na mene?`

    - **Korak 2: "Druga osoba" zapitaj**  
      Pomeri se na drugu tačku i postani ta osoba.  
      Posmatraj "sebe" i odgovori:  
      `Kako se ja osećam, šta želim, šta pokušavam da postignem?`

    - **Korak 3: "Posmatrač" zapitaj**  
      Stani na treću oznaku i pogledaj situaciju objektivno.  
      `Šta bih preporučio/la osobi iz 1. i 2. pozicije? Šta im nedostaje da bi se bolje razumeli?`

    ---
    🔄 Ponavljaj korake onoliko puta koliko je potrebno da dobiješ uvid koji vodi ka promeni.
    """)

def speak_my_language_exercise():
    st.markdown("""
    ### 🎯 Cilj vežbe:
    Uočite i prilagodite se primarnom **reprezentativnom sistemu** sagovornika kako biste poboljšali međusobno razumevanje i izgradili dublji raport.

    #### 🧪 Instrukcije:
    1. Vodite razgovor sa nekim o njihovom iskustvu.
    2. Pažljivo slušajte *kako* govore – ne samo *šta*.
    3. Identifikujte njihov reprezentativni sistem po rečima koje koriste (predikati).
    4. Prilagodite svoj govor njihovom jeziku.
    """)

    rep_system = st.radio("🧠 Izaberite sistem za vežbu:", 
                          ["Vizuelni", "Auditivni", "Kinestetički"])

    if rep_system == "Vizuelni":
        st.markdown("#### 👁️ Vizuelni sistem")
        st.markdown("**Primeri fraza:**")
        st.info("„Vidim šta misliš“\n„To izgleda dobro“\n„Jasno mi je“")

        st.markdown("**Predikati:**")
        st.code("vidim, slika, jasno, pogledaj, reflektuje, svetlo, tamno, fokus, pogled, prizor, svetla, boje, scena, vizija, jasno")

    elif rep_system == "Auditivni":
        st.markdown("#### 👂 Auditivni sistem")
        st.markdown("**Primeri fraza:**")
        st.info("„Zvuči mi poznato“\n„To volim da čujem“")

        st.markdown("**Predikati:**")
        st.code("čujem, zvuk, ton, govor, slušaj, odzvanja, tišina, reći, ritam, harmonija, pozvati, glasovi, kazati, razgovetno")

    elif rep_system == "Kinestetički":
        st.markdown("#### ✋ Kinestetički sistem")
        st.markdown("**Primeri fraza:**")
        st.info("„Osećam da je to tačno“\n„Imam jak osećaj“\n„Prija mi“")

        st.markdown("**Predikati:**")
        st.code("osećam, dodir, pritisak, toplo, teško, balans, pokret, stisak, grubo, stres, emocija, voleti, kvalitetno")


def metaprogram_exercise():
    st.markdown("""
    **Cilj:** Identifikujte svoje primarne metaprograme
    """)
    
    q1 = st.radio("1. Kada počinjete projekat:", 
                 ["Tražite širu sliku (global)", "Fokusiram se na detalje (specifičan)"])
    
    q2 = st.radio("2. U timskom radu:", 
                 ["Radim bolje sam (nezavisni)", "Volim saradnju (kooperativni)"])
    
    if st.button("Analiziraj moje metaprograme"):
        st.success(f"Vaši primarni metaprogrami:\n1. {q1}\n2. {q2}")

def goal_setting_exercise():
    st.markdown("""
    **Cilj:** Postavite dobro formirani cilj koristeći NLP kriterijume
    """)
    
    goal = st.text_area("Vaš cilj:")
    
    if st.button("Proveri cilj"):
        if goal:
            st.success("""
            Proverite:
            1. Da li je izražen pozitivno?
            2. Da li je pod vašom kontrolom?
            3. Da li možete da ga vidite/čujete/osećate?
            4. Da li je jasno u kom kontekstu?
            """)
        else:
            st.warning("Unesite cilj pre provere")

def calibration_exercise():
    st.markdown("""
    **Cilj:** Vežbajte čitanje nesvesnih signala
    """)
    
    st.video("https://www.youtube.com/watch?v=3LVjOBI7P5s")  # Replace with actual video
    st.markdown("""
    **Instrukcije:**
    1. Gledajte video bez zvuka
    2. Identifikujte emocionalna stanja
    3. Proverite sa zvukom
    """)

def rapport_building_exercise():
    st.markdown("""
    ### 🎯 Cilj vežbe:
    Vežbajte **uspostavljanje raporta** sa sagovornikom kroz verbalno i neverbalno usklađivanje. Raport je stanje međusobne povezanosti koje nastaje kada se osećamo prijatno i usklađeno sa drugom osobom.

    #### 🔑 Ključni elementi raporta:
    - **Verbalni**: govor, izbor reči, tempo govora, boja i jačina glasa  
    - **Neverbalni**: držanje tela, pokreti tela, pokreti očiju, disanje, stisak ruke
    """)

    technique = st.selectbox("🧪 Izaberite tehniku:", [
        "Usklađivanje disanja",
        "Reflektovanje držanja tela",
        "Usklađivanje tempa govora i boje glasa",
        "Govora tela (pokreti ruku, položaj nogu)",
        "Prilagođavanje izbora reči i vokabulara"
    ])

    examples = {
        "Usklađivanje disanja": "Diskretno pratite ritam disanja sagovornika i uskladite svoj. Ovo može povećati osećaj prisutnosti i povezanosti.",
        "Reflektovanje držanja tela": "Ako sagovornik sedi opušteno, vi takođe zauzmite sličan položaj. Izbegavajte očigledno imitiranje – cilj je suptilna usklađenost.",
        "Usklađivanje tempa govora i boje glasa": "Ako sagovornik govori brzo i energično, privremeno preuzmite sličan tempo i intonaciju.",
        "Govora tela (pokreti ruku, položaj nogu)": "Zauzmite sličan stav tela i s vremena na vreme ponovite slične pokrete – ali prirodno.",
        "Prilagođavanje izbora reči i vokabulara": "Obratite pažnju na omiljene reči sagovornika (npr. vizuelni izrazi, ako je sagovornika vizuelac) i uključite ih u svoj govor."
    }

    st.info(f"🔍 **Uputstvo:** {examples[technique]}")



def eye_patterns_exercise():
    st.markdown("""
    **🎯 Cilj:** Prepoznajte obrasce pokreta očiju
    """)

    st.image("eye_patterns.jpeg", width=400)  # relative path

    st.markdown("""
    **Vežba:**
    1. Postavite partneru razna pitanja  
    2. Posmatrajte pokrete očiju  
    3. Zabeležite obrasce
    """)


def perceptual_positions_exercise():
    st.markdown("""
    **🎯Cilj:** Razvijanje fleksibilnosti u percipiranju situacija

    **Instrukcije:**
    1. Zatvorite oči i prisetite se konflikta
    2. Doživite ga iz:
       - Svoje pozicije (1. pozicija)
       - Pogleda druge osobe (2. pozicija)
       - Perspektive posmatrača (3. pozicija)
    3. Zapišite uvide iz svake pozicije
    """)

######################### 4 ######################################
def milton_model_exercise():
    st.markdown("""
    **🎭 Hipnotički izazov – Uloga vodiča promene**

    Zamisli da si coach koji kroz blag i sugestivan jezik treba da inspiriše promenu bez direktnog saveta.

    🧠 **Zadatak:** Osmisli 10 rečenica koje koriste sledeće obrasce:
    - Indirektna sugestija (npr. *„Možda bi bilo dobro da razmisliš o tome...“*)
    - “Da” set (3 pitanja zaredom na koje je odgovor “da”)
    - Skrivena komanda (ugrađena u dužu rečenicu)

    🎯 **Cilj:** Pomozi fiktivnom klijentu u jednoj od sledećih situacija:
    - Motivacija tima na poslu
    - Podrška detetu koje ne želi da uči
    - Partner koji zaboravlja da pomaže

    🧑‍🤝‍🧑 U parovima: Jedan izgovara rečenicu, drugi detektuje obrazac. Menjajte se!
    """)

def submodalities_exercise():
    st.markdown("""
    **🎨 Uređivanje unutrašnjih filmova**


    🧩 **Koraci:**
    1. Priseti se iskustva koje želiš da promeniš (npr. trema pre javnog nastupa).
    2. Opisuj partneru "film" koristeći pitanja: Gde je slika? Koje boje? Koliko je svetla? Ima li zvuk? Pokret?
    3. Partner zapisuje sve "parametre" tvog mentalnog filma.
    4. Menjaj jedan po jedan element i proveravaj: *Kako ti se sada oseća telo?*


    🎯 **Cilj:** Otkrivanje koji unutrašnji elementi imaju najveći uticaj na tvoje emocije.
    """)


def feedback_exercise():
    st.markdown("""
    **Vežba: Feedback u 5 koraka**

    1. Uspostavite raport (zašto vam je važno da kažete osobi ovo)
    2. Opišite ponašanje (šta ste tačno videli/čuli)
    3. Dajte svoj doživljaj (meni to deluje...)
    4. Dajte preporuku za budućnost
    5. Završite u dobrom stanju ("Cenim kod tebe to što...")

    Vežbajte u parovima i rotirajte se nakon svake povratne informacije.
    """)

def anchoring_exercise():
    st.markdown("""
    **⚓ Sidrenje sa tepihčićem**

    🎯 **Cilj:** Aktivirati unutrašnje resurse kroz multisenzorno sidro.

    🧑‍🤝‍🧑 U paru:

    1. B zamišlja buduću situaciju gde mu treba više samopouzdanja, fokusa ili smirenosti.
    2. Priseti se događaja kada je to osećao najintenzivnije – opiši ga partneru (boje, tonovi, osećaji).
    3. Na podu zamisli krug. Kada osećaj dosegne vrhunac – A ga poziva da zakorači u krug.
    4. B uđe u krug, pojača osećaj, A eventualno dodaje dodir/reč kao dodatni stimulus.
    5. Izađi. Uđi ponovo. Ponavljaj dok sidro ne proradi automatski.

    """)


##################################################################
######################### 5 ######################################
def exercise_raspremanje_sadasnjosti():
    st.markdown("""
    ### 🧹 Vežba: Raspremajanje sadašnjosti

    Ova vežba ti pomaže da oslobodiš prostor svoje sadašnjosti od nepotrebnih elemenata iz prošlosti i budućnosti.

    1. 👋 Pokaži rukama gde osećaš da se nalazi tvoja sadašnjost – koliki je taj prostor i kako izgleda?
    2. 🔍 Zamisli da ulaziš u taj prostor da napraviš „inventar“. Proveri šta sve tamo postoji – šta je već prošlo, a šta pripada budućnosti.
    3. 📦 Sve što pripada prošlosti smesti na svoju vremensku liniju iza sebe, na pravo mesto u prošlosti.
    4. 🔄 Proveri još jednom – da li je ostalo nešto što pripada prošlosti? Ako jeste, prenesi i to.
    5. 🎯 Sve što pripada budućnosti premesti unapred na vremensku liniju ispred sebe.
    6. 🧘‍♀️ Kada je prostor sadašnjosti čist, pogledaj ga još jednom i obrati pažnju na to kako se sada osećaš. Usidri novi osećaj jasnoće i prisutnosti.
    """)

def exercise_kreiranje_cilja_po_vremenskoj_liniji():
    st.markdown("""
    ### 🗺️ Vežba: Kreiranje cilja po vremenskoj liniji

    Ova vežba koristi vremensku liniju da bi ti pomogla da sagledaš svoj cilj, izazove, resurse i sledeće korake.

    #### 1. Početna priprema
    - Zatvori oči, udahni duboko i opusti se. 😌
    - Zamisli svoju vremensku liniju – gde se nalazi prošlost, a gde budućnost?
    - Postavi sebi cilj koji želiš da ostvariš. Zapiši ga u pozitivnoj formi i jasno ga definiši.
    - Smesti cilj na odgovarajuće mesto u budućnosti.

    #### 2. Asociirano prekontroliši put do cilja
    - Zakorači svojom vremenskom linijom od sadašnjeg trenutka do cilja.
    - Posmatraj put: da li je jasan ili maglovit? Lagan ili naporan?
    - Obeleži ključne tačke koje deluju izazovno. 📍

    #### 3. Disocirano prekontroliši izazovne deonice
    - Iskorači iz „sebe“ i stani pored vremenske linije. Posmatraj put kao film. 🎞️
    - Uoči konkretne prepreke i izazove. Šta ti tu nedostaje da bi prošao/la lakše?

    #### 4. Disocirano otkrij gde si već imao/la te resurse
    - Kreni unazad vremenskom linijom i pronađi situacije iz prošlosti kada si već imao/la potrebne resurse.
    - Identifikuj ih (npr. odlučnost, jasnoća, podrška, znanje…).

    #### 5. Asociirano proživi te resurse
    - Mentalno se vrati u te događaje i doživi ih: šta si tada video/la, čuo/la, osećao/la? 🧠
    - Oživi svaki resurs pojedinačno.

    #### 6. Integracija resursa u buduće korake
    - Vrati se napred duž vremenske linije do tačaka gde su resursi potrebni.
    - Zamisli kako ih integrišeš u te tačke. 🎯

    #### 7. Kreni iz sadašnjosti sa punim resursima
    - Vrati se u sadašnjost na svojoj vremenskoj liniji.
    - Pogledaj sada put ka cilju – da li ti deluje dostižno?
    - Ako jeste – znaćeš kada je pravo vreme da kreneš. 🚀

    """)

##################################################################

############################## 6 ####################################
def exercise_programiranje_po_nln():
    import streamlit as st
    st.markdown("""
    ### 🧠 Vežba: Programiranje cilja po neurologičkim nivoima (NLN)
    Ova vežba povezuje tvoj cilj sa svim nivoima tvoje ličnosti — od ponašanja do identiteta.

    #### 🔹 Priprema prostora:
    Zamisli da prostor ispred tebe ima 5 zona:
    1. 🎯 **Cilj / Okruženje**
    2. 🚶‍♂️ **Ponašanje**
    3. 🛠 **Sposobnosti**
    4. 💡 **Uverenja i Vrednosti**
    5. 🧬 **Identitet**

    Zakorači redom u svaku zonu i postavi sebi sledeća pitanja:

    ---
    #### 🎯 Cilj / Okruženje:
    - Šta tačno želiš da postigneš?
    - Gde se to dešava i kada?
    - Kako izgleda to mesto?

    ---
    #### 🚶‍♂️ Ponašanje:
    - Šta tačno radiš?
    - Kako bi trebalo da se ponašaš?
    - Kako izgledaš dok to postižeš?

    ---
    #### 🛠 Sposobnosti:
    - Koje veštine i strategije koristiš?
    - Kako tačno to radiš?
    - Koja znanja i resurse koristiš?

    ---
    #### 💡 Uverenja i Vrednosti:
    - Šta ti je važno u vezi sa ovim ciljem?
    - U šta veruješ da će se desiti?
    - Šta te pokreće iznutra?

    ---
    #### 🧬 Identitet:
    - Ko si ti kada postižeš ovaj cilj?
    - Koje uloge igraš?
    - Kako se tada ponašaš, kako se osećaš?

    👉 Kada sve povežeš, stani ponovo na početak i pređi ceo put još jednom — sada sa punim identitetom osobe koja već jeste to što želiš da postaneš.
    """)
##################################################################
########################### 7 #######################################
def exercise_disney_strategy():
    st.markdown("""
    ### 🎭 Vežba: Diznijeva strategija kreativnosti
    Koraci ove vežbe predstavljaju tri različite uloge: **Sanjar**, **Realizator** i **Analitičar**. Svaka uloga ima svoju svrhu u procesu donošenja odluka i kreativnog razmišljanja.

    ---
    #### 🪄 1. Pozicija Sanjara
    - Zamisli izazov ili cilj koji želiš da razradiš.
    - Stani na poziciju sanjara. Seti se trenutka kada si bio izuzetno kreativan/a.
    - **Zatvori oči i zamisli:** šta bi bio savršen ishod? Bez ograničenja, pusti mašti na volju.
    - Postavi pitanje: **„Šta sve može biti moguće?“**

    ---
    #### 🛠️ 2. Pozicija Realizatora
    - Fizički se pomeri na drugo mesto (ako radiš uživo).
    - Sada si praktičar/realizator – osoba koja treba da sprovede ideju u delo.
    - Postavi pitanje: **„Kako ovo može da se ostvari? Šta je prvi korak?“**
    - Napravi plan, razmisli o resursima, vremenu, ljudima.

    ---
    #### 🧠 3. Pozicija Analitičara
    - Zauzmi treću poziciju – analitičku.
    - Ocenjuj ideju objektivno – kao da nisi ti to smislio/la.
    - Pitaj se: **„Šta bi moglo da pođe po zlu? Gde imaš rupe u planu? Šta treba poboljšati?“**

    ---
    #### 🔁 Ponavljanje i Integracija
    - Vrati se još jednom kroz sve tri pozicije ako želiš dodatno unapređenje.
    - Na kraju integriši sve uvide i zapiši konkretan plan.

    > „Ako možeš da sanjaš – možeš i da ostvariš.“ 🌟 – *Walt Disney*
                
    """)

def exercise_creating_future_history():
    st.markdown("""
        🕰️ **Creating a Future History** je vežba za unapređenje pregovaračkih veština kroz stvaranje uspešne narativne priče o budućem razgovoru.

        👥 **Uloge**: Dvoje ljudi (A i B), 30 minuta po osobi. Zamenite uloge nakon toga.

        ### 🔄 Koraci:
        1. **B** priča o jednom važnom poslovnom razgovoru koji **nije** prošao uspešno.
        2. **A** postavlja pitanja i pažljivo sluša.
        3. Zatim **A** zamoli **B** da ispriča tu istu priču tako kao da je razgovor **bio uspešan**.
        4. Zajedno istražuju šta je drugačije u toj verziji:
        - Kako se ponašao?
        - Kako je govorio?
        - Koje su reči korišćene?
        - Šta je osećao?
        5. **A** pomaže **B** da izvuče ključne lekcije i uvidi šta može da primeni u budućim pregovorima.

        ### ✍️ Završni zadatak:
        **B** zapisuje razlike i koristi ih za mentalnu pripremu sledećeg važnog razgovora.  
        Opciono: može koristiti **samohipnozu** ili vizualizaciju da dodatno učvrsti promene.

        🎯 Ova vežba pomaže u izgradnji uverenja da uspešan ishod može biti oblikovan i ostvaren!
        """)

##################################################################
def reframing_exercise():
    st.markdown("""
    **🎯Cilj:** Izazvati promenu emocionalne reakcije kod osobe A i proširiti njen pogled na situaciju.
    """)
    st.markdown("""
    **Vežba: Reframing značenja ili konteksta**

    Učesnici rade u trojkama (osoba A, B i C).

    **Koraci:**
    1. Osoba A izgovara neku žalbu ili kritičku izjavu, npr:
        - "Previše bučno priča."
        - "On je lenj."
        - "Moj kolega je previše direktan."

    2. Osobe B i C smišljaju *reframing značenja* ako se izjava odnosi na ličnost (npr. "lenj" → "opušten"),  
       ili *reframing konteksta* ako se izjava odnosi na ponašanje (npr. "previše bučno" → "na zabavi to pravi sjajnu atmosferu").

    3. Kada su spremni, osoba A ponavlja izjavu. Prvo osoba B izgovara svoj reframing, zatim osoba C. Osoba A zatim opisuje kako se oseća nakon svakog preformulisanja.

    4. Uloge se menjaju. Svaka osoba daje 3 izjave i prima povratni reframing.
    
    """)

def smart_goals_exercise():
    st.markdown("""
    **Cilj:** Formulisanje cilja koji zadovoljava SMART NLP kriterijume

    **Instrukcije:**
    1. Napišite jedan cilj koji imate
    2. Proverite da li je:
       - Specifičan (vidljiv, čujan, osetan)
       - Merljiv (kako ćete znati da ste ga postigli?)
       - Ekološki (usaglašen sa vašim vrednostima?)
       - U vašoj kontroli
       - Vremenski određen

    """)
    goal = st.text_area("Unesite vaš cilj:")
    if st.button("Evaluiraj SMART cilj"):
        if goal:
            st.success("Proverite da li vaš cilj zadovoljava sve navedene kriterijume iznad.")
        else:
            st.warning("Molimo unesite cilj pre evaluacije.")

def time_orientation_exercise():
    st.markdown("""
    **Cilj:** Istražiti sopstvenu vremensku orijentaciju

    **Instrukcije:**
    1. Zatvorite oči i zamislite liniju svog života — gde se nalazi prošlost? budućnost?
    2. Odgovorite:
       - Da li su događaji poređani ispred vas ili oko vas?
       - Osećate li se više „u vremenu“ ili „kroz vreme“?

    **Reflektujte kako ta orijentacija utiče na vašu organizaciju, odnose i donošenje odluka**
    """)

def timeline_exercise():
    st.markdown("""
    **Cilj:** Rad sa ličnom vremenskom linijom

    **Instrukcije:**
    1. Vizualizujte vremensku liniju (prošlost - sadašnjost - budućnost)
    2. Postavite pozitivan cilj na budući trenutak
    3. Doživite kako je već ispunjen, pogledajte unazad kako ste ga postigli
    4. Osnažite osećaj poverenja i jasnog pravca

    **Bonus:** Koristite liniju da oslobodite negativna sećanja ili uverenja
    """)

def values_exercise():
    st.markdown("""
    **Cilj:** Otkriti i uskladiti lične vrednosti

    **Instrukcije:**
    1. Odgovorite: Šta je za vas najvažnije u životu/profesiji/odnosima?
    2. Navedite 5 vrednosti i rangirajte ih po važnosti
    3. Zapitajte se: Da li živite u skladu sa tim vrednostima?

    **Napomena:** Usklađene vrednosti = jasnoća i motivacija
    """)

def belief_change_exercise():
    st.markdown("""
    **Cilj:** Promena ograničavajućeg uverenja

    **Instrukcije:**
    1. Identifikujte jedno ograničavajuće uverenje (npr. „Nisam dovoljno dobar“)
    2. Upitajte:
       - Od koga je to uverenje?
       - Da li je istinito u svakom kontekstu?
       - Kako bi izgledao život bez njega?
    3. Zapišite novo podržavajuće uverenje

    **Tehnike:** Reimprinting, vizualizacija
    """)

def neurological_levels_exercise():
    st.markdown("""
    **Cilj:** Razumevanje nivoa promene

    **Instrukcije:**
    1. Izaberite ponašanje koje želite da promenite
    2. Analizirajte na svakom od sledećih nivoa:
       - Okruženje: Gde i kada se dešava?
       - Ponašanje: Šta tačno radite?
       - Sposobnosti: Kako to radite?
       - Uverenja: Zašto to radite?
       - Identitet: Ko to radi?
    3. Promenite jedan viši nivo i reflektujte kako utiče na niže
    """)

def metaprograms_profile_exercise():
    st.markdown("""
    **Cilj:** Upoznati sopstvene metaprograme

    **Instrukcije:**
    1. Odgovorite na sledeće:
       - Da li preduzimate inicijativu ili čekate da vas pozovu?
       - Volite li strukturu ili slobodu izbora?
       - Vidite li širu sliku ili detalje?

    2. Zapišite šta to znači za vaš stil učenja, rada, odnosa
    """)

def creativity_strategy_exercise():
    st.markdown("""
    **Cilj:** Koristiti kreativne strategije na strukturiran način

    **Instrukcije:**
    1. Sanjar: Zapišite ideju bez ograničenja
    2. Realista: Kako biste je sproveli u delo?
    3. Kritičar: Šta bi moglo poći po zlu i kako to preduprediti?

    **Ponovite ciklus dok ideja ne postane izvodljiva**
    """)

def directed_dialogue_exercise():
    st.markdown("""
    **Cilj:** Strukturisati komunikaciju za pozitivni uticaj

    **Instrukcije:**
    1. Prisetite se razgovora gde ste želeli da utičete
    2. Zapišite:
       - Kako ste pokazali razumevanje (pacing)?
       - Kako ste vodili temu?
       - Koje ste ugrađene komande koristili?

    3. Vežbajte ih u budućim razgovorima
    """)

def potential_me_exercise():
    st.markdown("""
    **Cilj:** Kreiranje novih uvida kroz slike i asociacije

    **Instrukcije:**
    1. Pronađite sliku koja vas trenutno najviše privlači 
    2. Zapišite:
       - Šta ta slika predstavlja za vas?
       - Kako se odnosi na vašu trenutnu situaciju?
       - Koji novi uvid dobijate iz toga?

    **Ova tehnika otključava nesvesne uvide**
    """)

def ikigai_exercise():
    st.markdown("""
    **Cilj:** Pronaći tačku svrhe i zadovoljstva

    **Instrukcije:**
    1. Nacrtajte 4 kruga i zapišite za svaki:
       - Šta volite da radite?
       - U čemu ste dobri?
       - Šta svet treba?
       - Za šta vas ljudi plaćaju?

    2. Pronađite presek — to je vaš Ikigai
    """)

def behavior_generator_exercise():
    st.markdown("""
    **Cilj:** Usvajanje novog korisnog ponašanja

    **Instrukcije:**
    1. Identifikujte ponašanje koje biste želeli usvojiti
    2. Prisetite se kada ste to već činili ili vizualizujte osobu koja to radi
    3. Zamislite sebe kako ga uspešno koristite u budućem kontekstu
    4. Pojačajte osećaj uspeha i odlučnosti

    **Dodajte fizičku gestu (sidro) za brzo prisjećanje**
    """)

# Define data functions for various NLP techniques
def rapport_building_exercise_data(selected_month=None):
    return {
        "example": "Na početku sastanka, trener je usklađivao ton glasa i položaj tela sa klijentom kako bi stvorio osećaj poverenja.",
        "exercise": "Tokom sledeće konverzacije, pokušaj da uskladiš brzinu govora, ton i držanje sa sagovornikom i obrati pažnju na efekat koji to ima na komunikaciju."
    }

def speak_my_language_exercise_data(selected_month=None):
    return {
        "example": "Klijent koristi rečenice poput 'Vidim da to ima smisla' – trener koristi vizuelne izraze u odgovoru kako bi izgradio dublje razumevanje.",
        "exercise": "Identifikuj koji reprezentativni sistem koristi osoba sa kojom si danas pričao i prilagodi svoj govor tom sistemu (vizuelni, auditivni, kinestetički)."
    }

def chunking_exercise_data(selected_month=None):
    return {
        "example": "Kada je sagovornik rekao 'Imam previše obaveza', trener je pitao 'Šta ti je tu najvažnije?' (chunking up), a zatim 'Koji tačno zadaci?' (chunking down).",
        "exercise": "Uzmi jednu široku temu (npr. 'produktivnost') i formuliši jedno pitanje za chunking up, jedno za chunking down i jedno za chunking sideways."
    }

def reframing_exercise_data(selected_month=None):
    return {
        "example": "Klijent kaže: 'Stalno se nerviram zbog kašnjenja.' Trener pita: 'U kom kontekstu bi to mogla biti korisna osobina?'",
        "exercise": "Izaberi jednu situaciju koja ti je izazovna i primeni reframing značenja i reframing konteksta na nju."
    }

def metamodel_exercise_data(selected_month=None):
    return {
        "example": "Osoba kaže: 'Svi me kritikuju.' Trener pita: 'Ko tačno? Kada su to uradili?' (preciziranje generalizacije).",
        "exercise": "Zapiši 3 rečenice koje sadrže generalizacije ili brisanja. Za svaku formulisi metamodel pitanje koje razjašnjava smisao."
    }

def calibration_exercise_data(selected_month=None):
    return {
        "example": "Kouč primećuje da klijent počinje da vrti olovku i ubrzava govor kada se spomene određena tema.",
        "exercise": "Tokom sledećeg razgovora, obrati pažnju na 3 fizičke promene kod sagovornika kada menja emocionalno stanje."
    }

def eye_patterns_exercise_data(selected_month=None):
    return {
        "example": "Klijent gleda gore desno kada se trudi da se seti novog scenarija – što ukazuje na vizuelnu konstrukciju.",
        "exercise": "Tokom razgovora, primećuj kuda osoba gleda dok odgovara na pitanja. Zabeleži 2 primera pokreta očiju i poveži ih sa tipom razmišljanja."
    }

def tri_perspektive_exercise_data(selected_month=None):
    return {
        "example": "Tokom rada na konfliktu sa kolegom, klijent je sagledao situaciju iz svoje, kolegine i neutralne pozicije.",
        "exercise": "Uzmi izazovnu situaciju i opiši je iz prve, druge i treće perspektive. Zapiši uvide koje dobijaš iz svake od njih."
    }

def chunking_exercise_data(selected_month=None):
    return {
        "example": "Kouč pita: 'Zašto ti je produktivnost važna?' (chunking up), zatim 'Koje konkretne navike tu pomažu?' (chunking down).",
        "exercise": "Uzmi jednu temu i kreiraj primer pitanja za chunking up, down i sideways."
    }

def milton_model_exercise_data(selected_month=None):
    return {
        "example": "Kouč koristi nejasne izraze: 'Možda ćeš sada pronaći ono što ti je potrebno... na svoj način...'.",
        "exercise": "Sastavi 3 Miltonove rečenice koje uključuju brisanje, nejasnost i otvorenu interpretaciju."
    }

def submodalities_exercise_data(selected_month=None):
    return {
        "example": "Klijent menja mentalnu sliku neugodnog događaja tako što je udaljava i prebacuje u crno-belo.",
        "exercise": "Zamisli prijatno iskustvo i menjaj njegove submodalitete (boja, zvuk, lokacija) i posmatraj uticaj na emociju."
    }

def feedback_exercise_data(selected_month=None):
    return {
        "example": "Umesto 'Loše si to uradio', trener koristi: 'Video sam da si preskočio korak, kako da ti pomognem da ga dodaš sledeći put?'",
        "exercise": "Zapiši primer lošeg i primer dobrog feedback-a koji si dao ili primio i identifikuj razliku u pristupu."
    }

def anchoring_exercise_data(selected_month=None):
    return {
        "example": "Klijent koristi pesmu koja ga podseća na samopouzdanje pre važnih nastupa.",
        "exercise": "Izaberi pozitivno stanje i poveži ga sa fizičkim pokretom (npr. stisak pesnice). Ponavljaj to u tom stanju 5 puta."
    }

def potential_me_exercise_data(selected_month=None):
    return {
        "example": "Kouč koristi sliku iz Points of You da klijent otkrije sopstvene potencijale kroz metaforu.",
        "exercise": "Odaberi jednu inspirativnu sliku. Zapiši 3 reči koje ti padaju na pamet i reflektuj kako se one povezuju s tvojim ciljevima."
    }

def ikigai_exercise_data(selected_month=None):
    return {
        "example": "Klijent spaja ono što voli, u čemu je dobar i za šta može biti plaćen — otkriva smer nove karijere.",
        "exercise": "Ispuni četiri kruga Ikigaija za sebe. Koji je njihov presek? Šta možeš učiniti ove nedelje u skladu s tim?"
    }

def behavior_generator_exercise_data(selected_month=None):
    return {
        "example": "Osoba želi da postane samopouzdan govornik. Vizualizuje sebe kako uspešno drži govor i pojačava unutrašnje stanje sigurnosti.",
        "exercise": "Odaberi jednu osobinu koju želiš. Priseti se kada si je imao, zamisli kako to sada primenjuješ i pojačaj osećaj u telu."
    }

def exercise_disney_strategy_data(selected_month=None):
    return {
        "example": "U kreativnoj radionici koristi se Diznijeva strategija: prvo kao sanjar, zatim realista, pa kritičar.",
        "exercise": "Zamisli cilj koji želiš da ostvariš. Piši kao: 1) sanjar (šta sve možeš), 2) realista (kako to postići), 3) kritičar (šta treba poboljšati)."
    }

def exercise_creating_future_history_data(selected_month=None):
    return {
        "example": "Pregovarač zamišlja kako mediji pišu o uspešnom dogovoru koji su postigli. To mu pomaže da jasno postavi namere i uđe spreman.",
        "exercise": "Zamisli da je pregovor prošao savršeno i da se piše članak o tome. Kako glasi naslov? Koje vrednosti ste uskladili? Zapiši tu priču u 5 rečenica."
    }

def metaphor_exercise_data(selected_month=None):
    return {
        "example": "Klijent koristi priču o planinarenju kao simbol sopstvenog ličnog rasta.",
        "exercise": "Kreiraj metaforu koja simbolizuje tvoj trenutni izazov. Kakva je priča, ko su likovi i šta je rešenje?"
    }

def pregovaranje_i_fleksibilnost_data(selected_month=None):
    return {
        "example": "Tokom pripreme za pregovore, trener je sa klijentom razmatrao koje vrednosti su važne drugoj strani, kako bi došli do obostrano prihvatljivog rešenja.",
        "exercise": "Pre važnog razgovora, napiši koje su tvoje vrednosti i potrebe. Zatim zapiši koje bi mogle biti vrednosti druge strane. Osmisli 2 rešenja koja uključuju fleksibilnost i obostranu dobit."
    }
def generator_ponasanja_data(selected_month=None):
    return {
        "example": "Osoba želi da postane samopouzdan govornik. Vizualizuje sebe kako uspešno drži govor i pojačava unutrašnje stanje sigurnosti.",
        "exercise": "Odaberi jedno ponašanje koje želiš da razviješ. Priseti se kada si ga već imao, zamisli sebe kako ga primenjuješ sada i pojačaj emociju u telu."
    }
def generator_ponasanja_data(selected_month=None):
    return {
        "example": "Osoba želi da postane samopouzdan govornik. Vizualizuje sebe kako uspešno drži govor i pojačava unutrašnje stanje sigurnosti.",
        "exercise": "Odaberi jedno ponašanje koje želiš da razviješ. Priseti se kada si ga već imao, zamisli sebe kako ga primenjuješ sada i pojačaj emociju u telu."
    }
def neurologicki_nivoi_data(selected_month=None):
    return {
        "example": "Klijent radi na promeni navike (ponašanje), ali uz pomoć NLP kouča otkriva da postoji konflikt na nivou identiteta: 'Ja nisam tip koji vežba redovno'.",
        "exercise": "Izaberi cilj i razmisli: 1) Okruženje: Gde i kada? 2) Ponašanje: Šta? 3) Veštine: Kako? 4) Vrednosti: Zašto? 5) Identitet: Ko to radi? 6) Svrha: Šire značenje? Zapiši svoje odgovore."
    }
def raspremanje_sadasnjosti_data(selected_month=None):
    return {
        "example": "Pre nego što sam krenula da planiram narednu nedelju, izdvojila sam 10 minuta da zapišem sve što me mentalno opterećuje. Nakon toga, osetila sam jasnoću i lakše sam se fokusirala.",
        "exercise": "Zatvori oči i zapitaj se: 'Šta sve trenutno nosim u sebi što mi više ne koristi?' Zapiši misli, osećanja, nedovršene obaveze, tuđe poruke koje te opterećuju. Zatim ih simbolično pusti – iscepkaj papir, spali ga (sigurno), ili ga ostavi po strani."
    }

def timeline_goal_programming_data(selected_month=None):
    return {
        "example": "Zamislila sam vremensku liniju svog života ispred sebe, stavila tačno određeni cilj tri meseca u budućnost, i vizualizovala kako ga dostižem. Osetila sam motivaciju da odmah krenem sa prvim koracima.",
        "exercise": "Zatvori oči i zamisli svoju vremensku liniju ispred sebe. Idi do tačke u budućnosti kada si već postigao/la svoj cilj. Oseti šta vidiš, čuješ i osećaš. Zatim se vrati u sadašnjost i zapiši tri koraka koja možeš odmah preduzeti."
    }

def identity_goal_programming_data(selected_month=None):
    return {
        "example": "Kada sam cilj da 'postanem samopouzdan govornik' povezala sa identitetom osobe koja inspiriše druge, osetila sam dublju posvećenost svakodnevnom vežbanju.",
        "exercise": "Zapiši cilj koji želiš da ostvariš. Zatim odgovori na pitanje: 'Ko ja postajem kada ostvarim ovaj cilj?' Opisi tu osobu: kako misli, govori, deluje. Zapiši jednu stvar koju možeš danas uraditi kao ta osoba."
    }

def creating_future_history_data(selected_month=None):
    return {
        "example": "Zapisala sam dnevnički unos kao da je već jun i upravo sam završila javni nastup. Opisala sam kako sam se osećala i koje sam pohvale dobila. Ova vežba mi je pomogla da uvežbam verovanje u sopstveni uspeh.",
        "exercise": "Zamisli da je tvoj cilj već postignut. Napiši kratak tekst iz budućnosti (kao dnevnik): 'Danas sam uradio/la…', opiši šta se desilo, kako si se osećao/la, koga si upoznao/la, šta si naučio/la. Piši u sadašnjem vremenu, kao da se već dogodilo."
    }

core_techniques = {
    "Raport": {
        "icon": "🤝",
        "description": "Izgradnja poverenja kroz verbalno i neverbalno usklađivanje.",
        "function": rapport_building_exercise_data
    },
    "Reprezentativni sistemi": {
        "icon": "👁️👂🤲",
        "description": "Razumevanje i korišćenje dominantnih čulnih sistema u komunikaciji.",
        "function": speak_my_language_exercise_data
    },
    "Kalibracija": {
        "icon": "🔍",
        "description": "Zapažanje suptilnih promena u ponašanju i izrazu lica sagovornika.",
        "function": calibration_exercise_data
    },
    "Očni obrasci": {
        "icon": "👀",
        "description": "Praćenje pokreta očiju radi identifikacije misaonih procesa.",
        "function": eye_patterns_exercise_data
    },
    "Chunking – Hijerarhija ideja": {
        "icon": "🧠",
        "description": "Kretanje kroz nivoe apstrakcije u komunikaciji.",
        "function": chunking_exercise_data
    },
    "Reframing": {
        "icon": "🖼️",
        "description": "Promena značenja i konteksta za drugačiji pogled na situaciju.",
        "function": reframing_exercise_data
    },
    "Metamodel": {
        "icon": "🔍🗣️",
        "description": "Postavljanje preciznih pitanja za razotkrivanje nejasnih izjava.",
        "function": metamodel_exercise_data
    },
    "Miltonov model": {
        "icon": "🌀",
        "description": "Upotreba neodređenog jezika za rad sa nesvesnim umom.",
        "function": milton_model_exercise_data
    },
    "Submodaliteti": {
        "icon": "🎨🎧🤲",
        "description": "Rad sa finim nijansama unutrašnjih slika, zvukova i osećaja.",
        "function": submodalities_exercise_data
    },
    "Feedback": {
        "icon": "💬",
        "description": "Veština davanja i primanja korisne povratne informacije.",
        "function": feedback_exercise_data
    },
    "Sidrenje": {
        "icon": "⚓",
        "description": "Povezivanje emocionalnih stanja sa specifičnim stimulusima.",
        "function": anchoring_exercise_data
    },
    "Pregovaranje i fleksibilnost": {
        "icon": "🤝",
        "description": "Pregovaranje u NLP-u nije borba, već saradnja. U centru su razumevanje i usaglašavanje vrednosti i potreba obe strane.",
        "function": pregovaranje_i_fleksibilnost_data
    },
    "Metafore": {
        "icon": "📖",
        "description": "Metafore govore direktno nesvesnom umu i pomažu u osvetljavanju problema i resursa na kreativan način.",
        "function": metaphor_exercise_data
    },
    "Points of You": {
        "icon": "🖼️",
        "description": "Metoda koja koristi slike i ključne reči za introspektivno razmišljanje i osvešćivanje unutrašnjih resursa.",
        "function": potential_me_exercise_data
    },
    "Ikigai": {
        "icon": "🌸",
        "description": "Japanski koncept pronalaženja svrhe kroz ono što voliš, u čemu si dobar i šta svet treba.",
        "function": ikigai_exercise_data
    }
}

additional_techniques = {
    "Tri perceptualne pozicije": {
        "icon": "🔄",
        "desc": "Sagledavanje situacije iz svoje, tuđe i neutralne pozicije radi boljeg razumevanja konflikata.",
        "exercise": tri_perspektive_exercise_data()
    },
    "Raspremanje sadašnjosti": {
        "icon": "🧹",
        "desc": "Vežba osvešćivanja i otpuštanja mentalnog nereda i emocionalnih ostataka iz svakodnevice.",
        "exercise": raspremanje_sadasnjosti_data()
    },
    "Programiranje cilja na vremenskoj liniji": {
        "icon": "🕒",
        "desc": "Tehnika za postavljanje cilja u budućnost i njegovo 'upisivanje' na vremensku liniju.",
        "exercise": timeline_goal_programming_data()
    },
    "Programiranje cilja pomoću identiteta": {
        "icon": "🧬",
        "desc": "Postavljanje cilja u skladu sa ličnim vrednostima i identitetom.",
        "exercise": identity_goal_programming_data()
    },
    "Creating Future History": {
        "icon": "📜",
        "desc": "Kreiranje pozitivne budućnosti kao da se već dogodila kako bi se lakše ostvarila u stvarnosti.",
        "exercise": creating_future_history_data()
    },
    "Diznijeva strategija kreativnosti": {
        "icon": "🎭",
        "desc": "Kreativna tehnika u kojoj koristiš tri uloge: sanjar, realista i kritičar.",
        "exercise": exercise_disney_strategy_data()
    },
    "Generator budućeg ponašanja": {
        "icon": "🚀",
        "desc": "Tehnika za modeliranje i pripremu željenog ponašanja u budućim izazovnim situacijama.",
        "exercise": generator_ponasanja_data()
    }
}

import streamlit as st

def render_techniques():
    st.header("🧰 NLP Tehnike i Vežbe")

    st.subheader("🔹Teme")
    cols = st.columns(2)
    for i, (name, data) in enumerate(core_techniques.items()):
        with cols[i % 2]:
            with st.expander(f"{data['icon']} {name}"):
                st.markdown(f"**Opis:** {data['description']}")
                result = data["function"]()
                st.markdown(f"**🧪 Primer:** {result['example']}")
                st.markdown(f"**✍️ Vežba:** {result['exercise']}")

    st.subheader("🔸 Tehnike")
    cols = st.columns(2)
    for i, (name, data) in enumerate(additional_techniques.items()):
        with cols[i % 2]:
            with st.expander(f"{data['icon']} {name}"):
                st.markdown(f"**Opis:** {data['desc']}")
                exercise = data["exercise"]
                if isinstance(exercise, dict):
                    st.markdown(f"**🧪 Primer:** {exercise['example']}")
                    st.markdown(f"**✍️ Vežba:** {exercise['exercise']}")
                else:
                    st.markdown(f"**✍️ Vežba:** {exercise}")

# =============================================
# MODULE CONTENT FUNCTIONS
# =============================================

def module_1_content() -> dict:
    return {
        "title": "Osnove NLP-a",
        "sections": [
            ("🧠 Šta je NLP?", """
            NLP (Neuro-Lingvističko Programiranje) je metodologija koja proučava uspešne ljude i strategije koje koriste, kako bi se te strategije mogle preneti i primeniti u raznim oblastima života. 
            
            Tri stuba NLP uspeha su:
            - **Ciljevi** – Jasno postavljanje ciljeva kao osnove za napredak.
            - **Otvorenost čula** – Svesno obraćanje pažnje na signale iz okoline i tela.
            - **Fleksibilnost** – Prilagodljivost ponašanja kako bi se došlo do željenog cilja.
             
            NLP su razvili Ričard Bandler i Džon Grinder 70-ih godina na Univerzitetu Santa Kruz, analizom uspešnih terapeuta poput Miltona Eriksona, Frica Perlza i Virdžinije Satir.

            Kroz modelovanje njihovih komunikacionih obrazaca, stvorili su sistem koji pomaže ljudima da postižu izuzetne rezultate u komunikaciji, terapiji i ličnom razvoju.
            """, None),

            ("📜 NLP Aksiomi", """
            - **Mapa nije teritorija** – Naša mentalna mapa stvarnosti nije isto što i sama stvarnost.
            - **Ljudi zasnivaju svoje ponašanje na najboljoj opciji koju imaju u tom trenutku** – Iza svakog ponašanja stoji pozitivna namera.
            - **Ljudi već poseduju sve resurse koji su im potrebni da bi napravili željenu promenu**.
            - **Ako nešto ne funkcioniše, probaj nešto drugo**.
            - **Ne postoji neuspeh – postoji samo povratna informacija**.
            - **Mi ne možemo ne komunicirati** – Čak i ćutanje je oblik komunikacije.
            - **Značenje komunikacije je odgovor koji dobijemo** – Ne ono što smo hteli da kažemo, već kako je poruka primljena.
            - **Rešenje je uvek unutar sistema** – Promene treba da se dešavaju iznutra ka spolja.
            - **Ako neko može nešto da uradi, svako može da nauči kako** – Modeliranjem tuđeg ponašanja moguće je naučiti veštine.
            - **Ako želiš nešto da razumeš – primeni to**.
            - **Ljudski um, telo i emocije čine celinu** – Sve je povezano.
            - **Reakcija sagovornika zavisi i od nas** – Mi učestvujemo u kreiranju interakcije.
            - **Ukoliko nešto funkcioniše, to znači da je sistem u ravnoteži**.
            - **Ljudima nisu potrebne velike promene – dovoljan je mali pomak**.
            - **Ljudi koji nas okružuju su naše ogledalo** – Ono što nas nervira u drugima, često je i u nama.
            - **Pojedinačna iskustva nisu fiksni identitet** – Ljudi nisu njihova prošlost; mogu se menjati.
            """, None),

            ("📊 Mehrabianov model komunikacije", """
            Prema ovom modelu, komunikacija se sastoji od:  
            - 55% govor tela  
            - 38% ton glasa  
            - 7% same reči  

            To ukazuje na značaj neverbalnih signala u interakciji.
            """, None),

            ("🤝 Raport i Usklađivanje", """
            Raport je stanje međusobne povezanosti i poverenja koje gradimo kroz verbalno i neverbalno usklađivanje sa sagovornikom (držanje tela, disanje, tempo govora, izbor reči...).

            Uspešna komunikacija počiva na stvaranju raporta.
            """, None),

            ("👁️ Reprezentativni sistemi", """
            NLP prepoznaje tri glavna sistema putem kojih percipiramo svet:  
            - Vizuelni  
            - Auditivni  
            - Kinestetički  

            Prepoznavanje dominantnog sistema sagovornika pomaže u efikasnijoj komunikaciji.
            """, None),

            ("🧩 Metaprogrami", """
            Metaprogrami su nesvesni obrasci mišljenja koji filtriraju informacije koje primamo.  
            Oni određuju naše preferencije, ponašanje i motivaciju.

            Primeri:
            - Prema / Od
            - Sličnosti / Razlike
            - Interni / Eksterni
            - Ljudi / Zadaci
            - Opšta slika / Detalji
            """, None),

            ("🎯 Postavljanje ciljeva", """
            Cilj nije isto što i želja, zadatak ili vizija.

            Dobar NLP cilj je:
            - **P**oseban
            - **O**ročen
            - **K**reativan
            - **R**ealan
            - **E**kološki
            - **N**ajbolji mogući ishod
            - **I**nspirativan
            - **S**istemski
            - **E**fikasan

            NLP koristi jasnu metodologiju za definisanje i ostvarenje ciljeva koji vode ka dugoročnom uspehu.
            """, None)
        ],
        "exercises": [
            ("🤝 Raport", rapport_building_exercise),
            ("👁️ Reprezentativni sistemi", speak_my_language_exercise)
        ]
    }


def module_2_content():
    return {
        "title": "Komunikacija i Raport",
        "sections": [
            ("🕵️ Kalibracija", """
            Kalibracija je veština primećivanja suptilnih promena u fiziologiji, glasu i ponašanju drugih ljudi. Pomaže nam da razumemo emocionalno stanje sagovornika i uspostavimo dublji nivo komunikacije.
            
            Šta možemo primetiti:
            - Izraz lica
            - Pokrete očiju
            - Promene u tonu, brzini, jačini glasa
            - Držanje tela, gestikulaciju, disanje
            """, None),

            ("🌉 Raport", """
            Raport je stanje međusobne usklađenosti koje se stvara kada se dvoje ljudi nalaze „na istoj talasnoj dužini“. U NLP-u, raport gradimo tehnikama:
            - Pacing (praćenje): usklađivanje s fiziologijom, govorom, ponašanjem druge osobe
            - Matching (ogledanje): oponašanje tempa, položaja tela, tona glasa
            - Leading (vođenje): uvodimo promene kad imamo uspostavljen raport

            Raport je preduslov za uspešnu komunikaciju, jer stvara poverenje i otvorenost.
            """, None),

            ("👀 Očni obrasci", """
            NLP povezuje pokrete očiju s tipom razmišljanja. Prateći gde neko gleda, možemo pretpostaviti da li se priseća ili konstruiše vizuelne, auditivne ili kinestetičke informacije:

            - Gore levo: vizuelno sećanje
            - Gore desno: vizuelna konstrukcija
            - Levo u stranu: auditivno sećanje
            - Desno u stranu: auditivna konstrukcija
            - Dole desno: kinestetičko (osećaji)
            - Dole levo: unutrašnji dijalog
            """, None),

            ("⚖️ Kongruentnost i nekongruentnost", """
            Kongruentnost znači sklad između misli, reči i ponašanja. Kada su osoba i njeni postupci usklađeni – ona deluje sigurno, jasno i uverljivo.

            Nekongruentnost je nesklad – osoba može govoriti jedno, ali ponašanjem slati drugu poruku (npr. reći "sve je u redu" dok pokazuje znake nervoze). U NLP-u učimo da prepoznamo i uskladimo se s ovim razlikama, ali i da ih korigujemo kod sebe.
            """, None),

            ("✂️ Separator", """
            Separator je tehnika prekidanja obrasca ponašanja – koristi se kada želimo da zaustavimo negativnu spiralu razmišljanja ili prekinemo neželjeni tok komunikacije.

            Može biti fizički pokret (npr. promena položaja, aplauz, udarac rukom o sto), promena tona glasa ili teme razgovora. Ključ je da razbije tok misli i otvori prostor za novu perspektivu.
            """, None),

            ("🔁 Tri perspektive", "Vežba za sagledavanje konflikta iz pozicije sebe, druge osobe i neutralnog posmatrača", None)
        ],
        "exercises": [
            ("🕵️ Kalibracija", calibration_exercise),
            ("🌉 Raport", rapport_building_exercise),
            ("👀 Očni obrasci", eye_patterns_exercise),
            ("🔁 Tri perspektive", tri_perspektive_exercise)
        ]
    }


def module_3_content():
    return {
        "title": "🧠 Jezičke strukture i promene perspektive",
        "sections": [
            ("🧠 Chunking – Hijerarhija ideja", """
            🧠 **Cilj:** Razvijanje fleksibilnosti u komunikaciji prelaskom između različitih nivoa apstrakcije.

            - 🔼 **Chunking up:** uopštavanje (Zašto ti je to važno? Šta ti to znači?)
            - 🔽 **Chunking down:** konkretizacija (Šta tačno? Ko? Kada?)
            - ↔️ **Chunking sideways:** alternativna kategorija (Šta je još sličan primer?)
            """, None),

            ("🔍 Metamodel", """
            🔍 **Cilj:** Oslobađanje od jezičkih ograničenja i nepreciznosti kroz postavljanje preciznih pitanja.

            **Obuhvaćeni obrasci:**
            - ❌ Brisanje (neodređene imenice, glagoli)
            - 🔁 Generalizacije (univerzalne, složene ekvivalencije)
            - 🔄 Izvrtanje (uzrok-posledica, čitanje misli)
            - 🔐 Neophodnost / Mogućnost
            - ❓ Izgubljena referenca
            - 📏 Nepotpuna poređenja
            - 🌀 Nominalizacije
            """, None),

            ("🖼️ Reframing", """
            🖼️ **Cilj:** Promena percepcije kroz preformulisanje značenja ili konteksta neke izjave.

            - ✨ **Reframing značenja:** Šta još ovo može da znači? Kako bi ovo moglo da bude korisno?
            - 🌍 **Reframing konteksta:** U kom kontekstu bi ovo bilo pozitivno ili korisno?
            """, None)
        ],
        "exercises": [
            ("🧠 Chunking – Hijerarhija ideja", chunking_exercise),
            ("🔍 Metamodel", metamodel_exercise),
            ("🖼️ Reframing", reframing_exercise)
        ]
    }


def module_4_content():
    return {
        "title": "🌀 Nesvesni jezik i unutrašnja reprezentacija",
        "sections": [
            ("🌀 Miltonov model", """
            🌀 **Cilj:** Razumevanje kako Miltonov model koristi nejasan i sugestivan jezik za rad sa nesvesnim umom.

            - 🔮 Jezik je uopšten, ubacuje u trans
            - 🧭 Usmeren ka opštem razumevanju
            - 👁️‍🗨️ Fokusira osobu ka unutra i nesvesnim resursima
            """, None),

            ("🎨 Submodaliteti", """
            🧩 **Cilj:** Istražiti strukturu mentalnih predstava koje stvaraju značenja.

            - 🎨 Vizuelni: mesto, veličina, boja, jasnost
            - 🎧 Auditivni: ton, visina, kontinuitet, glasnoća
            - 🤲 Kinestetički: temperatura, pokret, pritisak, intenzitet
            """, None),

            ("💬 Feedback", """
            💬 **Cilj:** Razvijanje veštine davanja i primanja feedback-a u svrhu razvoja i rasta.

            - 🪟 Johari prozor i slepa mrlja
            - ✅ Pravila za feedback
            - 📑 Struktura: raport → ponašanje → doživljaj → preporuka → zatvaranje
            """, None),

            ("⚓ Sidrenje", """
            ⚓ **Cilj:** Naučiti kako da povežemo određeno emocionalno stanje sa spoljnim ili unutrašnjim stimulusom.

            - 👁️/👂/🤝 Sidra po modalitetima
            - 🔁 Krug izvrsnosti
            - 🧷 Efikasno sidrenje: jasno stanje, jak stimulus, ponavljanje
            """, None)
        ],
        "exercises": [
            ("🌀 Miltonov model", milton_model_exercise),
            ("🎨 Submodaliteti", submodalities_exercise),
            ("💬 Feedback", feedback_exercise),
            ("⚓ Sidrenje", anchoring_exercise)
        ]
    }


def module_5_content():
    return {
        "title": "🎯 Lični ciljevi, vreme i uspeh",
        "sections": [
            ("🏆 Šta je uspeh i kako pobediti strah od neuspeha", """
            🏆 **Uspeh** je subjektivan — u NLP-u, meri se ostvarenjem sopstvenih ciljeva u skladu sa ličnim vrednostima.

            😨 **Strah od neuspeha** često se zasniva na:
            - negativnim iskustvima iz prošlosti
            - tuđim očekivanjima
            - nesvesnim uverenjima o sebi

            💡 **Promena perspektive:** neuspeh je povratna informacija, a ne kraj puta.
            """, None),

            ("🎯 Šta cilj jeste, a šta nije", """
            🎯 Cilj nije isto što i:
            - ❌ Želja (nedovoljno precizna)
            - 🌫 Vizija (preširoka)
            - 📋 Zadatak (ne motiviše)

            ✅ Pravi cilj je:
            - **P**oseban
            - **O**ročen
            - **K**reativan
            - **R**ealan
            - **E**kološki
            - **N**ajbolji mogući ishod
            - **I**nspirativan
            - **S**istemski
            - **E**fikasan
            """, None),

            ("⏳ Odnos prema vremenu", """
            ⏳ NLP razlikuje dva osnovna odnosa prema vremenu:
            - 🌀 **U vremenu**: žive u trenutku, spontani, ne planiraju, skloni stresu
            - 📅 **Kroz vreme**: planeri, organizovani, orijentisani na prošlost i budućnost

            🧭 Razumevanje sopstvene vremenske linije pomaže boljem planiranju i emocionalnoj ravnoteži.
            """, None)
        ],
        "exercises": [
            ("🧹 Raspremanje sadašnjosti", exercise_raspremanje_sadasnjosti),
            ("🕒 Kreiranje cilja po vremenskoj liniji", exercise_kreiranje_cilja_po_vremenskoj_liniji)
        ]
    }


def module_6_content():
    return {
        "title": "💡 Vrednosti, uverenja i dubinska promena",
        "sections": [
            ("🎯 Vrednosti", """
            **Rad sa vrednostima:**
            1. Elicitacija — otkrivanje ključnih vrednosti
            2. Hijerarhija — koji prioritet imaju
            3. Usaglašavanje — poravnanje sa ciljevima

            **Vrednosti utiču na motivaciju, ponašanje i identitet**

            - Naše vrednosti oblikuju odluke i ponašanje.
            - Vrednosti su emocionalno doživljene i menjive.
            - One su osnovni kriterijumi po kojima merimo dobro i loše u životu.
            """, None),

            ("🧠 Uverenja", """
            **Moć uverenja**  
            Naša uverenja kreiraju realnost u kojoj živimo.

            - 🧲 Ograničavajuća uverenja nas drže u obrascima nepoverenja i straha.  
            - 🔓 Podržavajuća uverenja otvaraju prostor za akciju i razvoj.

            NLP tretira uverenje kao *izbor*, a ne kao činjenicu.

            **Lingvistika uverenja**  
            Jezik otkriva dublja uverenja:

            - "To je nemoguće" → Ograničavajuće uverenje  
            - "Ja sam takva osoba" → Identifikacija sa uverenjem  
            - "Ne mogu jer..." → Implicitna granica

            NLP koristi pitanja i preformulisanje da oslobodi potencijal.

            **Elicitacija uverenja**  
            🎯 Cilj: Prepoznati skrivena nesvesna uverenja.

            - Ponavljanje ključnih izjava i traženje značenja ("Šta ti to znači?")  
            - Identifikovanje uverenja u vezi s ciljevima  
            - Praćenje emocionalnih reakcija na izazove

            👉 Uverenja se najčešće otkrivaju kroz pažljiv dijalog i refleksiju.
            """, None),

            ("📉 Kriva promene", """
            **Faze promene:**
            - Šok 😵
            - Strah 😨
            - Cenkаnje 🤔
            - Pretnje 😠
            - Dno 😔
            - Prihvatanje realnosti 😌
            - Odvezivanje 🎯
            - Nove navike 💪

            Promena je proces koji vodi od otpora do integracije novih ponašanja.
            """, None),

            ("🎭 Dramski trougao", """
            **Uloge u Dramskom trouglu:**
            - Žrtva 😢 — oseća se nemoćno, prepušteno drugima
            - Progonitelj 😠 — kritikuje, optužuje, napada
            - Spasilac 😇 — pokušava da reši tuđe probleme, često bez poziva

            **Rešenje:** Izaći iz kruga uloga i preuzeti odgovornost za svoje stanje.

            Ovaj obrazac često dovodi do toksičnih odnosa i narušene komunikacije.
            """, None),

            ("🏗️ Neurologički nivoi", """
            Model neurologičkih nivoa (NLN), koji su definisali Gregory Bateson i Robert Dilts, opisuje kako promene i motivacija funkcionišu na više nivoa ljudskog postojanja:

            1. 🌍 Okruženje – Gde i sa kim nešto radimo?
            2. 🔄 Ponašanje – Šta tačno radimo?
            3. 🛠️ Sposobnosti – Kako to radimo?
            4. 💡 Uverenja i vrednosti – Zašto to radimo?
            5. 👤 Identitet – Ko to radi?
            6. 🌟 Viša svrha – Kome/čemu pripadamo?

            Razumevanje i rad sa ovim nivoima omogućava dublju i trajniju promenu.
            """, None)
        ],
        "exercises": [
            ("🧬 Programiranje cilja kroz NLN", exercise_programiranje_po_nln)
        ]
    }


def render_metaprogram_selector():
    metaprogram_options = {
                "🎯 Smer delovanja: Prema / Od": """
        - *Prema* motivacija — usmerena ka nagradama i ciljevima  
        - *Od* motivacija — usmerena ka izbegavanju neprijatnih situacija  
        🔍 Pomaže u otkrivanju stvarnih pokretača ponašanja.
        """,
                "🔍 Percepcija: Sličnosti / Razlike": """
        - 👯 *Sličnosti* — ljudi brzo pronalaze povezanost  
        - 🔎 *Razlike* — fokus na ono što ne štima  
        🧩 Korisno u rešavanju problema i izgradnji timova.
        """,
                "🕰️ Vremenski fokus: Prošlost / Sadašnjost / Budućnost": """
        - 🕵️ *Prošlost* — refleksija i iskustvo  
        - 🎁 *Sadašnjost* — improvizacija i spontanost  
        - 📅 *Budućnost* — planiranje i organizacija
        """,
                "🖼️ Opšta slika / Detalji": """
        - 🌐 *Opšta slika* — fokus na celinu i viziju  
        - 🧷 *Detalji* — preciznost i tačni koraci  
        ✅ Timski balans je ključ.
        """,
                "🧭 Opcija / Procedura": """
        - 🌀 *Opcija* — fleksibilnost, kreativnost  
        - 📈 *Procedura* — sled koraka, struktura  
        🎯 Korisno za dizajn procesa i rad sa klijentima.
        """,
                "⚙️ Način delovanja: Preaktivni / Aktivni / Reaktivni / Neaktivni": """
        - 🧨 *Preaktivni* — sve planiraju unapred  
        - 🔋 *Aktivni* — rade na vreme  
        - ⏰ *Reaktivni* — reaguju kad zatreba  
        - 💤 *Neaktivni* — često odlažu
        """,
                "🤝 Organizacija: Zadaci / Ljudi": """
        - 📊 *Zadaci* — usmereni na rezultat i efikasnost  
        - 🧑‍🤝‍🧑 *Ljudi* — fokus na odnose i saradnju  
        🤹 Idealno je imati balans u timu.
        """,
                "💡 Izvor motivacije: Interni / Eksterni": """
        - 🔋 *Interni* — samopokretanje i samovrednovanje  
        - 📢 *Eksterni* — potreba za potvrdom od drugih  
        🔑 Svest o ovome pomaže u radu sa motivacijom i ciljevima.
        """
            }

    selected = st.selectbox("📌 Izaberi metaprogram za istraživanje:", list(metaprogram_options.keys()))
    st.markdown("### " + selected)
    st.markdown(metaprogram_options[selected])

def module_7_content():
    return {
        "title": "Metaprogrami i Pregovaranje",
        "sections": [
            ("🧠 Uvod u Metaprograme", """
            Metaprogrami su nesvesni filteri kroz koje percipiramo stvarnost.  
            Oni utiču na naše odluke, ponašanja i način komunikacije.

            Kao što operativni sistem povezuje hardver i softver,  
            metaprogrami povezuju naš um sa ponašanjem.
            """, None),

            ("🎛️ Izaberi metaprogram", None, render_metaprogram_selector),

            ("🤝 Pregovaranje umesto ubeđivanja", """
            Pregovaranje je veština nalaženja zajedničkih rešenja, zasnovana na razumevanju, fleksibilnosti i uvažavanju interesa obe strane.

            🔹 **Društvena kompetencija**  
            Ključ uspeha je sposobnost prilagođavanja i izgradnje odnosa — veština koja je neophodna i u profesionalnim i u ličnim pregovorima.

            🔹 **Priprema je ključ**  
            Najvažniji alat dobrih pregovarača je priprema. Bez nje, improvizacija je rizična.

            🔹 **Ciljevi i namere**  
            Pregovori nisu nadmudrivanje. Dobro pitanje: *Šta želim da postignem ovim razgovorom?*
            """, None),

            ("📋 Principi efikasnog pregovaranja", """
            ✅ Predlog treba da bude *poziv na dijalog*, a ne gotovo rešenje.  
            ✅ Potrebno je ostaviti prostor za *fleksibilnost i zajedničko oblikovanje rešenja*.  
            ✅ Sagovorniku treba ponuditi *njegovu ideju u vašem rešenju*.  
            ✅ Tražite *feedback*, ne odmah odluku.  
            ✅ Učinite sagovornika *kreatorom rešenja* — tada ga neće lako odbiti.

            Ovi principi osnažuju i vas i osobu s kojom pregovarate.
            """, None)
        ],
        "exercises": [
            ("🎭 Diznijeva strategija kreativnosti", exercise_disney_strategy),
            ("🕊️Creating Future History", exercise_creating_future_history)
        ]
    }


def module_8_content():
    return {
        "title": "Meta-Stanja i Napredne Primene",
        "sections": [
            ("🖼️ Points of You", """
            **Points of You** metodologija koristi slike i reči za introspekciju i promenu perspektive.

            🔧 **Alati:**
            - 🎲 *The Coaching Game* — slike + reči za nove uvide  
            - 🧩 *Punctum* — rad sa emocijama kroz fotografije  
            - 🌟 *The Potential Me* — razvoj potencijala i vizije

            🧠 Koristi se u koučingu, treningu i ličnom razvoju.
            """, None),

            ("🌸 Ikigai – Svrha života", """
            **Ikigai** je japanski model smislenog života koji kombinuje strast, misiju i profesiju.

            🔄 **Četiri sfere:**
            1. ❤️ Ono što voliš  
            2. 🧠 U čemu si dobar  
            3. 🌍 Šta svet treba  
            4. 💰 Za šta možeš biti plaćen

            🎯 Presek svih sfera = tvoja svrha.
            """, None),

            ("🧠 Generator ponašanja", """
            **Tehnika za usvajanje korisnih ponašanja i navika**

            🪜 **Koraci:**
            1. 🎯 Identifikuj ponašanje koje želiš  
            2. 🔍 Priseti se trenutka kad si to već radio ili zamisli uzor  
            3. 🧘 Vizualizuj sebe kako to uspešno primenjuješ  

            💡 Ključ: pojačaj stanje sigurnosti, odlučnosti i samopouzdanja.
            """, None),

            ("🌀 Metafore", """
            **Metafore** su snažno sredstvo za promenu stanja, perspektive i ponašanja.

            ✨ Koriste se u NLP-u za:
            - Obilazak otpora i nesvesnih blokada  
            - Lakšu integraciju promena kroz simboliku  
            - Aktivaciju unutrašnjih resursa

            📖 Efikasne metafore su jednostavne, emocionalne i povezane s realnim izazovima klijenta.
            """, None)
        ],
        "exercises": [
            ("🎯 Points of You", potential_me_exercise),
            ("🌸 Ikigai", ikigai_exercise),
            ("🧠 Generator ponašanja", behavior_generator_exercise)
        ]
    }
default_diary_entries = {
    1: """🧠 Mesec 1 – Osnove NLP-a

Ovaj mesec sam prvi put čula za NLP i njegove temelje. Posebno mi se dopala ideja da "Mapa nije teritorija" – shvatila sam koliko često reagujem na svoju interpretaciju stvarnosti, a ne na stvarnost samu.

Vežbanje raporta mi je pomoglo da poboljšam odnos sa bliskim osobama. Postala sam svesnija govora tela i kako utiče na komunikaciju.

Zapis: Šta za mene znači imati fleksibilnost u razmišljanju?
""",

    2: """📦 Mesec 2 – Chunking i struktura razmišljanja

Naučila sam kako da razlažem probleme i teme na manje delove (chunk down), i kako da ih sagledam u širem kontekstu (chunk up).

U svakodnevnoj komunikaciji koristim ovu veštinu da bih postavljala jasnija pitanja.

Zapis: Gde u životu mogu primeniti više 'chunkovanja' da bih se organizovala?
""",

    3: """🖼️ Mesec 3 – Preokviravanje

Ovaj mesec sam naučila koliko moćna može biti promena perspektive. Vežbala sam kako da negativne situacije posmatram iz ugla korisnog učenja.

Rečenica "nije neuspeh – već povratna informacija" mi odzvanja u glavi.

Zapis: Koji događaj bih mogla preokviriti da dobijem više snage iz njega?
""",

    4: """🗣️ Mesec 4 – Meta-model komunikacije

Počela sam da uviđam koliko u svakodnevnom govoru koristimo generalizacije, brisanja i distorzije. Vežbala sam da postavljam preciznija pitanja.

U razgovoru sa koleginicom sam prvi put primetila kada neko koristi 'ne mogu' kao generalizaciju.

Zapis: Kada sam poslednji put izgovorila nešto neprecizno, a mogla sam postaviti moćnije pitanje?
""",

    5: """🧙‍♀️ Mesec 5 

Ova je bila zahtevna tema – naučiti kako preoblikovati ograničavajuća uverenja pomoću jezičkih obrazaca.

Vežbala sam da odgovaram na izjave poput: "To nije za mene." Naučila sam nekoliko novih načina da pokrenem promenu kod sagovornika – ili kod sebe.

Zapis: Koje je moje trenutno najveće ograničavajuće uverenje?
""",

    6: """🎭 Mesec 6 – Napredni obrasci

Upoznavanje sa tehnikama poput submodaliteta i prekidanja obrazaca bilo je uzbudljivo.

Pokušala sam da promenim unutrašnji doživljaj jednog neprijatnog sećanja – menjajući boje, udaljenost i zvukove u svom umu. I stvarno se nešto promenilo!

Zapis: Koji obrasci ponašanja mi više ne služe – i kako ih mogu "prekinuti"?
""",

    7: """🌀 Mesec 7 – Integracija

Ovde sam se bavila delovima sebe koji se nekad ne slažu. Vežba integracije delova mi je otvorila novi pogled na unutrašnje konflikte.

Primila sam poruku iznutra da ne moram birati između uspeha i opuštenosti – mogu imati oba.

Zapis: Koji unutrašnji konflikti me koče, i šta svaki deo želi da zaštiti?
""",

    8: """🌈 Mesec 8 – Meta-stanja i identitet

Rad sa meta-stanjima mi je pokazao kako emocije mogu biti slojevite – i kako nad-stanja mogu pojačati ili ublažiti druga stanja.

U ovom periodu sam se često pitala: "Šta bi bilo kada bih imala više samopouzdanja u ovoj situaciji?"

Zapis: Koja meta-stanja mogu pojačati moju kreativnost, mir ili hrabrost?
""",

    9: """🏆 Mesec 9 – Majstorstvo

Ovaj mesec je bio posvećen integraciji svega naučenog. Razmišljala sam o svom NLP putu, i gde sam sada u odnosu na početak.

Zamišljam sebe kako prenosim naučeno drugima – možda kroz koučing, ili neformalnu podršku bliskima.

Zapis: Koji aspekt NLP-a je najviše transformisao moj život do sada?
"""
}


def interactive_timeline(selected_month=None):
    # Realistični naslovi i tehnike po mesecima
    month_data = {
        1: {
            "title": "Osnove NLP-a",
            "techniques": ["Ciljevi", "Raport", "Reprezentativni sistemi", "NLP Aksiomi"]
        },
        2: {
            "title": "Komunikacija i Raport",
            "techniques": ["Kalibracija", "Očni obrasci", "Kongruentnost", "Separator", "Tri perspektive"]
        },
        3: {
            "title": "Chunking i Metamodel",
            "techniques": ["Chunking", "Metamodel", "Upravljanje pitanjima"]
        },
        4: {
            "title": "Reframing i Submodaliteti",
            "techniques": ["Reframing značenja i konteksta", "Submodaliteti", "Swish obrazac"]
        },
        5: {
            "title": "Neurologički nivoi i vrednosti",
            "techniques": ["Neurologički nivoi", "Vrednosti", "Ciljevi po vremenskoj liniji"]
        },
        6: {
            "title": "Napredne jezičke tehnike",
            "techniques": ["Milton model", "Metafore"]
        },
        7: {
            "title": "Strategije i ponašanja",
            "techniques": ["Disney strategija", "Generator ponašanja", "Ikigai"]
        },
        8: {
            "title": "Integracija i promena",
            "techniques": ["Modelovanje", "Integracija delova", "Meta-stanja"]
        },
        9: {
            "title": "Sertifikacija",
            "techniques": [" "]
        }
    }
    
    # Create figure
    fig = go.Figure()
    
    # Add timeline line
    fig.add_trace(go.Scatter(
        x=list(month_data.keys()),
        y=[0]*9,
        mode='lines',
        line=dict(color='#6a5acd', width=2, dash='dot'),
        hoverinfo='none'
    ))
    
    # Add bubbles with hover animation
    for month, data in month_data.items():
        fig.add_trace(go.Scatter(
            x=[month],
            y=[0],
            mode='markers+text',
            marker=dict(
                size=30,
                color='#ff6b6b' if month == selected_month else '#6a5acd',
                opacity=0.7,
                line=dict(width=2, color='white')
            ),
            text=[str(month)],  # Number inside bubble
            textposition="middle center",
            textfont=dict(color='white', size=14),
            hovertext=(
                f"<b>{data['title']}</b><br>" +
                f"<br>".join(data['techniques'])
            ),
            hoverinfo="text",  # Show only the hovertext
            customdata=[month],
            name=f"Mesec {month}",
            textfont_size=14
        ))
    
    # Add month labels below the timeline
    fig.add_trace(go.Scatter(
        x=list(month_data.keys()),
        y=[-0.1]*9,
        mode='text',
        text=[f"Mesec {m}" for m in month_data.keys()],
        textposition='bottom center',
        hoverinfo='none',
        showlegend=False,
        textfont=dict(size=10)
    ))
    
    # Layout adjustments
    fig.update_layout(
        showlegend=False,
        xaxis=dict(
            range=[0.5, 9.5],
            showgrid=False,
            showticklabels=False,
            zeroline=False
        ),
        yaxis=dict(
            range=[-0.15, 0.15],
            showgrid=False,
            showticklabels=False,
            zeroline=False
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        height=300,
        margin=dict(l=0, r=0, t=0, b=50),
        hovermode='closest',
        hoverlabel=dict(
            bgcolor='white',
            font_size=14,
            font_family="Arial",
            bordercolor='#6a5acd',
            align='left'
        )
    )
    
    # Display the plot
    selected = st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # Handle clicks
    if selected:
        click_data = st.session_state.get('plotly_click', None)
        if click_data:
            clicked_month = click_data['points'][0]['customdata']
            if isinstance(clicked_month, list):
                clicked_month = clicked_month[0]
            st.session_state.selected_month = clicked_month
            st.rerun()
monthly_curriculum = {
    1: {
        "title": "",
        "techniques": [
            "Ciljevi", 
            "Otvorenost čula", 
            "Fleksibilnost", 
            "Raport", 
            "Reprezentativni Sistemi", 
            "Mehrabianov Model", 
            "NLP Aksiomi"
        ],
        "exercises": [
            "Kreirajte 3 cilja koristeći NLP kriterijume (pozitivno, merljivo, u vašoj kontroli)",
            "Vežbajte usklađivanje u razgovoru (disanje, ton, tempo govora)",
            "Identifikujte reprezentativni sistem sagovornika i prilagodite svoj",
            "Posmatrajte neverbalnu komunikaciju u 3 različita razgovora",
            "Zapišite i reflektujte 5 NLP aksioma u dnevnim situacijama"
        ],
        "milestones": [
            "Razumevanje osnova NLP-a i njegove primene",
            "Prvi pokušaj svesnog usklađivanja sa sagovornikom",
            "Prepoznat dominantan reprezentativni sistem kod sebe i drugih",
            "Uspešno postavljen prvi NLP cilj",
            "Primena barem 3 NLP aksioma u praksi"
        ]
    },
    2: {
        "title": "",
        "techniques": ["Chunking", "Usklađivanje"],
        "exercises": [
            "Razbijte 3 problema na manje delove",
            "Vežba senzorne oštrine (posmatrajte obrasce pokreta očiju kod drugih)",
            "Vežba usklađivanja sa partnerom (držanje, gestovi, disanje)"
        ],
        "milestones": [
            "Primenjen chunking u procesu učenja",
            "Prepoznati primarni reprezentacioni sistemi",
            "Uspešno nesvesno usklađivanje sa nekim"
        ]
    },
    3: {
        "title": "",
        "techniques": ["Preokviravanje", "Kalibracija"],
        "exercises": [
            "Dnevna vežba preokviravanja (3 situacije)",
            "Posmatranje mikro-izraza na videu",
            "Vežba kalibracije sa prijateljima (pogodite njihovo stanje)"
        ],
        "milestones": [
            "Preokvirene 3 negativne situacije",
            "Prepoznati osnovne mikro-izraze",
            "Poboljšana tačnost kalibracije za 30%"
        ]
    },
    4: {
        "title": "",
        "techniques": ["Meta-Model"],
        "exercises": [
            "Dnevnik meta-modela (analizirajte svoj unutrašnji dijalog)",
            "Snimite i analizirajte razgovore za obrasce",
            "Vežbajte precizna pitanja dnevno"
        ],
        "milestones": [
            "Identifikovani lični jezički obrasci",
            "Pomogli nekome da razjasni svoje razmišljanje",
            "Razvijen refleks meta-modela"
        ]
    },
    5: {
        "title": "",
        "techniques": ["a"],
        "exercises": [
            "Vežbajte 3 obrasca promene uverenja dnevno",
            "Analizirajte političke govore za obrasce",
            "Napravite preokvire za uobičajena ograničavajuća uverenja"
        ],
        "milestones": [
            "Promenjeno jedno lično ograničavajuće uverenje",
            "Prepoznati sleight of mouth obrasce u medijima",
            "Primenjeni obrasci u razgovoru"
        ]
    },
    6: {
        "title": "",
        "techniques": ["Prekidi Obrasca", "Submodaliteti"],
        "exercises": [
            "Kreirajte prekide obrasca za navike",
            "Eksperimenti sa promenom submodaliteta",
            "Integracija svih naučenih tehnika"
        ],
        "milestones": [
            "Prekinuta 3 lična obrasca",
            "Promenjen emocionalni intenzitet sećanja",
            "Kreiran lični proces promene"
        ]
    },
    7: {
        "title": "",
        "techniques": ["Swish Obrazac", "Integracija Delova"],
        "exercises": [
            "Modelirajte nečiju izvrsnu veštinu",
            "Rešite jedan unutrašnji konflikt",
            "Dizajnirajte lične swish obrasce"
        ],
        "milestones": [
            "Ekstrahovan jedan model izvrsnosti",
            "Integrisana dva konfliktna dela",
            "Kreiran efektan swish obrazac"
        ]
    },
    8: {
        "title": "",
        "techniques": ["Meta-Stanja"],
        "exercises": [
            "Primenite meta-stanja na izazove",
            "Dizajnirajte plan upravljanja stanjima",
            "Podučite jednu tehniku nekome"
        ],
        "milestones": [
            "Upravljanje izazovnim emocionalnim stanjem",
            "Kreiran lični alat za stanja",
            "Uspešno podučena jedna tehnika"
        ]
    },
    9: {
        "title": "Sertifikacija",
        "techniques": [],
        "exercises": [
            "Napravite lični NLP priručnik",
            "Dizajnirajte coaching proces",
            "Završni integracioni projekat"
        ],
        "milestones": [
            "Završen lični priručnik",
            "Coachirali nekog kroz proces",
            "Dostignut nivo sertifikacije"
        ]
    }
}
def show_month_details(month):
    if month == 9:
        st.subheader("🎓 Mesec 9 – Završni modul: Sertifikacija i slavlje")
        st.image("svi_mi2.jpeg", caption="NLP tim – svi mi zajedno!", use_container_width =True)
        st.image("svi_mi1.jpeg", caption="NLP tim – svi mi zajedno!", use_container_width =True)
        st.image("svi_mi3.jpeg", caption="NLP tim – svi mi zajedno!", use_container_width =True)
        return

    data = monthly_curriculum.get(month, {})

    if not data:
        st.warning("Nema dostupnih podataka za ovaj mesec")
        return

    st.subheader(f"📅 Mesec {month} {data.get('title', '')}")
    st.progress(min(month * 11, 100))
    st.markdown("---")

    tab1, tab2 = st.tabs(["Teme", "Vežbe"])

    with tab1:
        module = get_module_parts(st.session_state.selected_month)
        if module:
            for title, theory, custom_renderer in module["sections"]:
                with st.expander(f"🔹 {title}"):
                    if theory:
                        st.markdown(theory)
                    if callable(custom_renderer):
                        custom_renderer()
                    if not theory and not callable(custom_renderer):
                        st.info("Nema dodatnog sadržaja.")
        else:
            st.info("Još uvek nema unosa za ovaj mesec.")

    with tab2:
        module = get_module_parts(st.session_state.selected_month)
        if module and module.get("exercises"):
            exercise_tabs = st.tabs([title for title, _ in module["exercises"]])
            for (title, func), tab in zip(module["exercises"], exercise_tabs):
                with tab:
                    func()
        elif module:
            # Fallback ako su vežbe samo u sections (stariji moduli)
            for title, _, exercise in module["sections"]:
                if exercise:
                    with st.expander(f"🧪 {title}"):
                        exercise()
        else:
            st.info("Vežbe još uvek nisu dostupne.")


# Define module_3_content, module_4_content, etc. here (omitted for brevity)

# =============================================
# MODULE RENDERING HELPERS
# =============================================

def display_section_content(content, exercise_func=None):
    st.markdown(content)
    if exercise_func:
        with st.container():
            st.subheader("Vežba")
            exercise_func()


def show_module(module_num):
    modules = {
        1: module_1_content(),
        2: module_2_content(),
        3: module_3_content(),
        4: module_4_content(),
        5: module_5_content(),
        6: module_6_content(),
        7: module_7_content(),
        8: module_8_content(),
    }
    module = modules.get(module_num, {})
    if not module:
        st.warning("Modul još uvek nije dostupan")
        return
    st.header(f"📚 Modul {module_num}: {module['title']}")
    for section in module['sections']:
        with st.expander(f"🔹 {section[0]}"):
            display_section_content(section[1], section[2] if len(section) > 2 else None)

def generate_wordcloud(text):
    wc = WordCloud(width=800, height=400, background_color='white',
                   colormap='viridis', contour_width=1, contour_color='steelblue').generate(text)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
    plt.close(fig)

# =============================================
# =============================================
# MAIN APP LAYOUT
# =============================================

# Initialize session state
if 'selected_month' not in st.session_state:
    st.session_state.selected_month = 1
if 'current_section' not in st.session_state:
    st.session_state.current_section = "Vremenska Linija"
if 'random_tip' not in st.session_state:
    st.session_state.random_tip = ""

# Sidebar with navigation
with st.sidebar:
    st.title("🧠 NLP Putovanje")
    # Month selection dots
    cols = st.columns(9)
    for i, col in enumerate(cols, 1):
        with col:
            if st.session_state.selected_month == i:
                st.markdown(f"<div style='text-align: center; font-size: 18px; color: #ff6b6b;'>•</div>", 
                        unsafe_allow_html=True)
                if i == 9:
                    show_confetti()
            else:
                if st.button(str(i), key=f"month_{i}"):
                    st.session_state.selected_month = i
                    st.rerun()
    
    # Main navigation
    st.markdown("---")
    st.markdown("**Glavni Delovi**")
    
    if st.button("📅 Vremenska Linija"):
        st.session_state.current_section = "Vremenska Linija"
    if st.button("🔍 NLP Istraživač"):
        st.session_state.current_section = "NLP Istraživač"
    if st.button("📖 Moj Dnevnik"):
        st.session_state.current_section = "Moj Dnevnik"
    if st.button("📚 Resursi"):
        st.session_state.current_section = "Resursi"
        
    
    st.markdown("---")
    if st.button("🎲 Nasumični NLP Savet"):
        st.session_state.current_section = "Nasumični Savet"
        st.session_state.random_tip = random.choice(nlp_tips)
    

    
    st.markdown("---")

# Main content area
st.title("Moje NLP putovanje")

# Section routing
if st.session_state.current_section == "Vremenska Linija":
    st.markdown("### 📚 Vremenska Linija")
    
    # Display the interactive timeline
    interactive_timeline(st.session_state.selected_month)
    
    # Show details for the selected month
    show_month_details(st.session_state.selected_month)


elif st.session_state.current_section == "NLP Istraživač":
    render_techniques()



elif st.session_state.current_section == "Moj Dnevnik":
    st.markdown(f"### 📖 Moj NLP Dnevnik – Mesec {st.session_state.selected_month}")

    file_path = f"moj_dnevnik/mesec_{st.session_state.selected_month}.txt"
    if not os.path.exists("moj_dnevnik"):
        os.makedirs("moj_dnevnik")

    # Ako fajl ne postoji ili je prazan, ubaci početni sadržaj
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(default_diary_entries.get(st.session_state.selected_month, ""))

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    edited_content = st.text_area("📝 Unesi svoje misli i uvide:", value=content, height=300)

    if st.button("💾 Sačuvaj belešku"):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(edited_content)
        st.success("Dnevnik je sačuvan ✅")


elif st.session_state.current_section == "Resursi":
    st.markdown("### 📚 Preporučena literatura i materijali")

    st.markdown("""
    #### 📖 Knjige
    - *Stvorite novo JA* – Joe Dispenza  
    - *Biologija verovanja* – Bruce Lipton  
    - *Spontano lečenje uverenja* – Gregg Braden  
    - *Dete u tebi mora da pronađe svoj zavičaj* – Stefanie Stahl  
    - *Živeti bez igara* – Stephen Karpman  
    - *Koju igru igraš?* – Eric Berne  
    - *Frogs Into Princes* – Richard Bandler & John Grinder  
    - *The Structure of Magic* – Richard Bandler & John Grinder  
    """)


elif st.session_state.current_section == "Nasumični Savet":
    st.markdown("### 🎲 Nasumični NLP Savet")
    st.success(st.session_state.random_tip)

    if st.button("Novi Savet"):
        st.session_state.random_tip = random.choice(nlp_tips)
        st.rerun()
