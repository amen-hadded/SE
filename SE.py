"""
╔══════════════════════════════════════════════════════════════╗
║         SMART POT — Système Expert en Python / Tkinter       ║
║         Base de connaissances : Cactus & Succulentes         ║
║         Moteur d'inférence par chaînage avant                ║
║         ENTRÉE : Caractéristiques → SORTIE : Identification  ║
╚══════════════════════════════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox
import calendar
from datetime import datetime

# ═══════════════════════════════════════════════════════════════
#  BASE DE FAITS — 5 plantes grasses / succulentes (RHS)
# ═══════════════════════════════════════════════════════════════

PLANTES = {
    "aloe_vera": {
        "nom_commun": "Aloe Vera",
        "nom_scientifique": "Aloe vera",
        "famille": "Asphodelaceae",
        "forme": "rosette",
        "hauteur_max_cm": 100,
        "feuilles_type": "charnues",
        "feuilles_bordure": "epineuse",
        "rusticite_min_c": 5,
        "arrosage_croissance": "modere",
        "arrosage_dormance": "tres_faible",
        "exposition": "plein_soleil",
        "drainage": "excellent",
        "toxique": True,
        "tolere_negligence": False,
        "ravageurs": ["Cochenilles"],
        "floraison": "Printemps-Automne",
        "couleur_fleurs": "Jaune-vert",
        "fertilisation": "mensuelle_mai_aout",
        "temps_adulte_ans": "5-10",
        "emoji": "🌿",
    },
    "pilosocereus": {
        "nom_commun": "Blue Torch Cactus",
        "nom_scientifique": "Pilosocereus pachycladus",
        "famille": "Cactaceae",
        "forme": "colonnaire",
        "hauteur_max_cm": 50,
        "feuilles_type": "epines",
        "feuilles_bordure": "none",
        "rusticite_min_c": 12,
        "arrosage_croissance": "libre",
        "arrosage_dormance": "juste_humide",
        "exposition": "plein_soleil",
        "drainage": "excellent",
        "toxique": False,
        "tolere_negligence": True,
        "ravageurs": ["Cochenilles", "Fourmis"],
        "floraison": "Ete",
        "couleur_fleurs": "Blanc-rouge",
        "fertilisation": "non",
        "temps_adulte_ans": "5-10",
        "emoji": "🌵",
    },
    "echeveria": {
        "nom_commun": "Mexican Snow Ball",
        "nom_scientifique": "Echeveria elegans",
        "famille": "Crassulaceae",
        "forme": "rosette",
        "hauteur_max_cm": 10,
        "feuilles_type": "charnues",
        "feuilles_bordure": "none",
        "rusticite_min_c": 1,
        "arrosage_croissance": "modere",
        "arrosage_dormance": "pas_du_tout",
        "exposition": "plein_soleil",
        "drainage": "excellent",
        "toxique": False,
        "tolere_negligence": True,
        "ravageurs": ["Cochenilles", "Pucerons", "Charancones"],
        "floraison": "Fin-hiver-Printemps",
        "couleur_fleurs": "Rose",
        "fertilisation": "2-3_fois",
        "temps_adulte_ans": "2-5",
        "emoji": "🪴",
    },
    "crassula": {
        "nom_commun": "Jade Plant",
        "nom_scientifique": "Crassula ovata",
        "famille": "Crassulaceae",
        "forme": "buissonnant",
        "hauteur_max_cm": 250,
        "feuilles_type": "charnues",
        "feuilles_bordure": "none",
        "rusticite_min_c": 1,
        "arrosage_croissance": "legerement_humide",
        "arrosage_dormance": "tres_faible",
        "exposition": "plein_soleil",
        "drainage": "excellent",
        "toxique": False,
        "tolere_negligence": True,
        "ravageurs": ["Cochenilles", "Charancones", "Pucerons"],
        "floraison": "Fin-ete",
        "couleur_fleurs": "Blanc-rose",
        "fertilisation": "mensuelle_printemps_ete",
        "temps_adulte_ans": "5-10",
        "emoji": "🍀",
    },
    "sansevieria": {
        "nom_commun": "Langue de belle-mere",
        "nom_scientifique": "Sansevieria trifasciata",
        "famille": "Asparagaceae",
        "forme": "erecte",
        "hauteur_max_cm": 150,
        "feuilles_type": "rigides",
        "feuilles_bordure": "none",
        "rusticite_min_c": 10,
        "arrosage_croissance": "tres_faible",
        "arrosage_dormance": "tres_faible",
        "exposition": "lumiere_filtree",
        "drainage": "excellent",
        "toxique": True,
        "tolere_negligence": True,
        "ravageurs": ["Charancones"],
        "floraison": "Variable",
        "couleur_fleurs": "Vert-blanc",
        "fertilisation": "non",
        "temps_adulte_ans": "2-5",
        "emoji": "🌱",
    },
}

# ═══════════════════════════════════════════════════════════════
#  BASE DE RÈGLES DE PRODUCTION — 20 règles
#  Moteur : Chaînage avant pour déduire PLANTE → CLASSE → ARROSAGE
# ═══════════════════════════════════════════════════════════════

REGLES = [
    # ── IDENTIFICATION PLANTE (basée sur caractéristiques) ──────
    {"id": "R01", "categorie": "Identification",
     "nom": "Pilosocereus pachycladus",
     "description": "Forme colonnaire + épines → Blue Torch Cactus",
     "condition": lambda forme="", feuilles="", **_: forme == "colonnaire" and feuilles == "epines",
     "action": "plante_id", "valeur": "pilosocereus"},

    {"id": "R02", "categorie": "Identification",
     "nom": "Aloe Vera",
     "description": "Rosette + feuilles charnues épineuses → Aloe Vera",
     "condition": lambda forme="", feuilles="", bordure="", **_: forme == "rosette" and feuilles == "charnues" and bordure == "epineuse",
     "action": "plante_id", "valeur": "aloe_vera"},

    {"id": "R03", "categorie": "Identification",
     "nom": "Echeveria elegans",
     "description": "Rosette miniature + feuilles charnues → Mexican Snow Ball",
     "condition": lambda forme="", feuilles="", hauteur=0, **_: forme == "rosette" and feuilles == "charnues" and hauteur < 20,
     "action": "plante_id", "valeur": "echeveria"},

    {"id": "R04", "categorie": "Identification",
     "nom": "Crassula ovata",
     "description": "Forme buissonnante + feuilles charnues → Jade Plant",
     "condition": lambda forme="", feuilles="", **_: forme == "buissonnant" and feuilles == "charnues",
     "action": "plante_id", "valeur": "crassula"},

    {"id": "R05", "categorie": "Identification",
     "nom": "Sansevieria trifasciata",
     "description": "Forme érigée + feuilles rigides marbrées → Langue belle-mère",
     "condition": lambda forme="", feuilles="", **_: forme == "erecte" and feuilles == "rigides",
     "action": "plante_id", "valeur": "sansevieria"},

    # ── CLASSIFICATION PLANTE ───────────────────────────────────
    {"id": "R06", "categorie": "Classification",
     "nom": "Cactus colonnaire épineux",
     "description": "Forme colonnaire → Classe : Cactus colonnaire",
     "condition": lambda p, **_: p["forme"] == "colonnaire",
     "action": "classe", "valeur": "Cactus colonnaire"},

    {"id": "R07", "categorie": "Classification",
     "nom": "Succulente en rosette",
     "description": "Rosette + charnues → Succulente rosette",
     "condition": lambda p, **_: p["forme"] == "rosette" and p["feuilles_type"] == "charnues",
     "action": "classe", "valeur": "Succulente rosette"},

    {"id": "R08", "categorie": "Classification",
     "nom": "Succulente robuste érigée",
     "description": "Érigée + tolérance négligence → Succulente robuste",
     "condition": lambda p, **_: p["forme"] == "erecte" and p["tolere_negligence"],
     "action": "classe", "valeur": "Succulente robuste"},

    {"id": "R09", "categorie": "Classification",
     "nom": "Succulente arbustive",
     "description": "Forme buissonnante → Succulente arbustive",
     "condition": lambda p, **_: p["forme"] == "buissonnant",
     "action": "classe", "valeur": "Succulente arbustive"},

    {"id": "R10", "categorie": "Classification",
     "nom": "Succulente miniature",
     "description": "Hauteur < 20 cm → Succulente miniature",
     "condition": lambda p, **_: p["hauteur_max_cm"] < 20,
     "action": "classe", "valeur": "Succulente miniature"},

    # ── ARROSAGE ────────────────────────────────────────────────
    {"id": "R11", "categorie": "Arrosage",
     "nom": "Cactus arrosage libre",
     "description": "Arrosage libre → tous les 5-7 jours en croissance",
     "condition": lambda p, **_: p["arrosage_croissance"] == "libre",
     "action": "arrosage_croissance", "valeur": 6},

    {"id": "R12", "categorie": "Arrosage",
     "nom": "Succulente modérée",
     "description": "Arrosage modéré → tous les 10-14 jours",
     "condition": lambda p, **_: p["arrosage_croissance"] == "modere",
     "action": "arrosage_croissance", "valeur": 12},

    {"id": "R13", "categorie": "Arrosage",
     "nom": "Plante tolère la négligence",
     "description": "Tolérance négligence → arrosage toutes les 3 semaines",
     "condition": lambda p, **_: p["tolere_negligence"] is True,
     "action": "arrosage_croissance", "valeur": 21},

    {"id": "R14", "categorie": "Arrosage",
     "nom": "Dormance totale — zéro arrosage",
     "description": "Dormance pas_du_tout → suspendre tout arrosage",
     "condition": lambda p, **_: p["arrosage_dormance"] == "pas_du_tout",
     "action": "arrosage_dormance", "valeur": 0},

    {"id": "R15", "categorie": "Arrosage",
     "nom": "Maintien légèrement humide",
     "description": "Arrosage léger → tous les 14 jours en croissance",
     "condition": lambda p, **_: p["arrosage_croissance"] == "legerement_humide",
     "action": "arrosage_croissance", "valeur": 14},

    # ── ALERTES & PRÉCAUTIONS ───────────────────────────────────
    {"id": "R16", "categorie": "Alerte",
     "nom": "Risque de gel",
     "description": "Température < rusticité minimale → danger gel",
     "condition": lambda p, temperature=20, **_: temperature < p["rusticite_min_c"],
     "action": "alerte", "niveau": "DANGER",
     "message": "🥶 Température insuffisante ! Rentrez la plante immédiatement (gel fatal)."},

    {"id": "R17", "categorie": "Alerte",
     "nom": "Surexposition solaire intérieur",
     "description": "Plante lumière filtrée exposée soleil direct → brûlure",
     "condition": lambda p, exposition="normal", **_: p["exposition"] == "lumiere_filtree" and exposition == "direct",
     "action": "alerte", "niveau": "ATTENTION",
     "message": "☀️ Lumière trop directe ! Cette plante préfère une lumière filtrée vive."},

    {"id": "R18", "categorie": "Alerte",
     "nom": "Plante toxique",
     "description": "Toxique → alerter propriétaire (enfants/animaux)",
     "condition": lambda p, **_: p["toxique"] is True,
     "action": "alerte", "niveau": "ATTENTION",
     "message": "☠️ Plante nocive si ingérée ! Hors de portée enfants, chats et chiens."},

    {"id": "R19", "categorie": "Alerte",
     "nom": "Sol à mauvais drainage",
     "description": "Sol retenant l'eau + drainage requis → risque pourriture",
     "condition": lambda p, sol="bien_draine", **_: sol == "retient_eau" and p["drainage"] == "excellent",
     "action": "alerte", "niveau": "DANGER",
     "message": "💧 Sol mal drainant ! Rempotez en substrat cactus + gravier pour éviter la pourriture."},

    {"id": "R20", "categorie": "Alerte",
     "nom": "Cochenilles (taches coton)",
     "description": "Taches blanches cotonneuses → infestation cochenilles",
     "condition": lambda p, symptomes=None, **_: "taches_blanches" in (symptomes or []),
     "action": "alerte", "niveau": "DANGER",
     "message": "🦠 Cochenilles détectées ! Traiter avec alcool isopropylique ou insecticide."},

    {"id": "R21", "categorie": "Alerte",
     "nom": "Manque d'eau",
     "description": "Feuilles plissées/flétries → sous-arrosage",
     "condition": lambda p, symptomes=None, **_: "feuilles_fletries" in (symptomes or []),
     "action": "alerte", "niveau": "ATTENTION",
     "message": "🏜️ Manque d'eau. Arrosez modérément et reprenez le planning normal."},

    {"id": "R22", "categorie": "Alerte",
     "nom": "Sur-arrosage",
     "description": "Feuilles molles/translucides → sur-arrosage",
     "condition": lambda p, symptomes=None, **_: "feuilles_molles" in (symptomes or []),
     "action": "alerte", "niveau": "DANGER",
     "message": "🌊 Sur-arrosage probable ! Suspendez 2-3 semaines. Vérifiez le drainage."},

    {"id": "R23", "categorie": "Précaution",
     "nom": "Manipulation épines",
     "description": "Cactus ou épines → port de gants obligatoire",
     "condition": lambda p, **_: p["feuilles_type"] == "epines",
     "action": "alerte", "niveau": "INFO",
     "message": "🧤 Portez des gants épais pour toute manipulation de cette plante."},

    {"id": "R24", "categorie": "Précaution",
     "nom": "Rappel fertilisation",
     "description": "Fertilisation requise → rappel périodique",
     "condition": lambda p, **_: p["fertilisation"] in ["mensuelle_mai_aout", "mensuelle_printemps_ete", "2-3_fois"],
     "action": "alerte", "niveau": "INFO",
     "message": "🌿 Fertilisez avec engrais liquide cactus/succulentes (mai-août)."},

    {"id": "R25", "categorie": "Précaution",
     "nom": "Hivernage obligatoire",
     "description": "Rusticité < 10°C → hivernage intérieur chauffé",
     "condition": lambda p, **_: p["rusticite_min_c"] < 10,
     "action": "alerte", "niveau": "INFO",
     "message": "🏠 Hivernage à l'intérieur obligatoire (min 10-15°C). Ne jamais exposer au gel."},
]

# ═══════════════════════════════════════════════════════════════
#  MOTEUR D'INFÉRENCE — Chaînage avant
#  Étapes : Caractéristiques → Plante → Classe → Arrosage → Alertes
# ═══════════════════════════════════════════════════════════════

def identifier_plante(forme, feuilles, bordure, hauteur):
    """Étape 1 : Déduire la plante à partir des caractéristiques observées"""
    kwargs = dict(forme=forme, feuilles=feuilles, bordure=bordure, hauteur=hauteur)
    for r in REGLES:
        if r["action"] == "plante_id":
            try:
                if r["condition"](**kwargs):
                    return r["valeur"], r["id"]
            except Exception:
                continue
    return None, "—"

def determiner_classe(plante):
    """Étape 2 : Classer la plante selon ses caractéristiques"""
    for r in REGLES:
        if r["action"] == "classe":
            try:
                if r["condition"](plante):
                    return r["valeur"], r["id"]
            except Exception:
                continue
    return "Succulente non classée", "—"

def calculer_arrosage(plante, saison):
    """Étape 3 : Calculer la fréquence et le planning d'arrosage"""
    freq_cr, freq_do = 12, 30
    for r in REGLES:
        if r["action"] == "arrosage_croissance":
            try:
                if r["condition"](plante):
                    freq_cr = r["valeur"]
                    break
            except Exception:
                continue
    for r in REGLES:
        if r["action"] == "arrosage_dormance":
            try:
                if r["condition"](plante):
                    freq_do = r["valeur"]
                    break
            except Exception:
                continue
    freq = freq_cr if saison == "croissance" else freq_do
    if freq == 0:
        return 0, [], "Aucun arrosage en dormance"
    jours = []
    j = freq
    while j <= 30:
        jours.append(j)
        j += freq
    return freq, jours, f"Arroser tous les {freq} jours"

def evaluer_alertes(plante, temperature, exposition, sol, symptomes):
    """Étape 4 : Évaluer les alertes et précautions"""
    alertes = []
    kwargs = dict(temperature=temperature, exposition=exposition, sol=sol, symptomes=symptomes)
    seen = set()
    for r in REGLES:
        if r["action"] == "alerte" and r["id"] not in seen:
            try:
                if r["condition"](plante, **kwargs):
                    alertes.append({"id": r["id"], "niveau": r["niveau"],
                                    "message": r["message"], "nom": r["nom"]})
                    seen.add(r["id"])
            except Exception:
                continue
    return alertes

def diagnostiquer(forme, feuilles, bordure, hauteur, temperature, saison, exposition, sol, symptomes):
    """Diagnostic complet : Chaînage avant pour déduire la plante et son arrosage"""
    # Étape 1 : Identifier la plante
    plante_id, id_r01 = identifier_plante(forme, feuilles, bordure, hauteur)
    
    if plante_id is None:
        return None  # Plante non identifiée
    
    plante = PLANTES[plante_id]
    
    # Étape 2 : Classer la plante
    classe, r_id_classe = determiner_classe(plante)
    
    # Étape 3 : Calculer l'arrosage
    freq, jours, msg_arrosage = calculer_arrosage(plante, saison)
    freq_cr, jours_cr, _ = calculer_arrosage(plante, "croissance")
    freq_do, jours_do, _ = calculer_arrosage(plante, "dormance")
    
    # Étape 4 : Évaluer les alertes
    alertes = evaluer_alertes(plante, temperature, exposition, sol, symptomes)
    
    return {
        "plante": plante,
        "plante_id": plante_id,
        "classe": classe,
        "classe_regle": r_id_classe,
        "id_regle_identification": id_r01,
        "freq": freq,
        "jours": jours,
        "msg_arrosage": msg_arrosage,
        "freq_cr": freq_cr,
        "jours_cr": jours_cr,
        "freq_do": freq_do,
        "jours_do": jours_do,
        "alertes": alertes,
    }

# ═══════════════════════════════════════════════════════════════
#  INTERFACE TKINTER
# ═══════════════════════════════════════════════════════════════

# ── Palette de couleurs ──────────────────────────────────────
C = {
    "bg":        "#1a2e1c",
    "bg2":       "#243328",
    "bg3":       "#2d4030",
    "panel":     "#1e3422",
    "green":     "#4caf50",
    "green_dk":  "#2e7d32",
    "green_lt":  "#a5d6a7",
    "accent":    "#81c784",
    "white":     "#e8f5e9",
    "muted":     "#7aab7e",
    "danger":    "#ef5350",
    "danger_bg": "#2c1515",
    "warning":   "#ffb74d",
    "warn_bg":   "#2c2010",
    "info":      "#64b5f6",
    "info_bg":   "#102040",
    "water":     "#29b6f6",
    "water_bg":  "#0d2a38",
    "border":    "#3a5c3e",
    "text":      "#e8f5e9",
    "text2":     "#a5d6a7",
}

class SmartPotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🪴  Smart Pot — Système Expert Plantes")
        self.configure(bg=C["bg"])
        self.resizable(True, True)
        self.minsize(1000, 680)

        # Fonts
        self.ft_title  = font.Font(family="Helvetica", size=20, weight="bold")
        self.ft_h2     = font.Font(family="Helvetica", size=13, weight="bold")
        self.ft_h3     = font.Font(family="Helvetica", size=11, weight="bold")
        self.ft_body   = font.Font(family="Helvetica", size=10)
        self.ft_mono   = font.Font(family="Courier",   size=10)
        self.ft_badge  = font.Font(family="Helvetica", size=9,  weight="bold")
        self.ft_big    = font.Font(family="Helvetica", size=18, weight="bold")

        # Variables - Caractéristiques d'entrée
        self.var_forme    = tk.StringVar()
        self.var_feuilles = tk.StringVar()
        self.var_bordure  = tk.StringVar()
        self.var_hauteur  = tk.DoubleVar(value=50)
        
        # Variables - Conditions
        self.var_saison    = tk.StringVar(value="croissance")
        self.var_temp      = tk.DoubleVar(value=20)
        self.var_expo      = tk.StringVar(value="normal")
        self.var_sol       = tk.StringVar(value="bien_draine")
        self.var_s_taches  = tk.BooleanVar()
        self.var_s_fletri  = tk.BooleanVar()
        self.var_s_molles  = tk.BooleanVar()

        self._build_ui()
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        w, h = 1100, 720
        x = (self.winfo_screenwidth()  - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    # ── Build UI ─────────────────────────────────────────────
    def _build_ui(self):
        self._build_header()
        main = tk.Frame(self, bg=C["bg"])
        main.pack(fill="both", expand=True, padx=14, pady=(0, 14))
        main.columnconfigure(0, weight=0, minsize=320)
        main.columnconfigure(1, weight=1)
        main.rowconfigure(0, weight=1)

        self._build_left(main)
        self._build_right(main)

    def _build_header(self):
        hdr = tk.Frame(self, bg=C["bg2"], pady=12)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🪴  Smart Pot", font=self.ft_title,
                 bg=C["bg2"], fg=C["white"]).pack(side="left", padx=20)
        tk.Label(hdr, text="Système Expert · Cactus & Succulentes · IA par chaînage avant",
                 font=self.ft_body, bg=C["bg2"], fg=C["muted"]).pack(side="left", padx=4)
        tk.Label(hdr, text=f"  {len(REGLES)} règles  |  {len(PLANTES)} plantes  ",
                 font=self.ft_badge, bg=C["green_dk"], fg=C["white"],
                 relief="flat", padx=8, pady=3).pack(side="right", padx=20)

    # ── LEFT PANEL ───────────────────────────────────────────
    def _build_left(self, parent):
        left = tk.Frame(parent, bg=C["panel"], relief="flat",
                        highlightbackground=C["border"], highlightthickness=1)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=10)

        self._section(left, "CARACTÉRISTIQUES OBSERVÉES")
        
        # Forme
        tk.Label(left, text="Forme de la plante", font=self.ft_badge,
                 bg=C["panel"], fg=C["muted"]).pack(anchor="w", padx=14, pady=(0, 2))
        cb_forme = ttk.Combobox(left, textvariable=self.var_forme, state="readonly",
                               values=["rosette", "colonnaire", "buissonnant", "erecte"],
                               font=self.ft_body, width=34)
        cb_forme.pack(padx=14, pady=(0, 10), fill="x")
        self._apply_combo_style(cb_forme)
        
        # Type de feuilles
        tk.Label(left, text="Type de feuilles", font=self.ft_badge,
                 bg=C["panel"], fg=C["muted"]).pack(anchor="w", padx=14, pady=(0, 2))
        cb_feuilles = ttk.Combobox(left, textvariable=self.var_feuilles, state="readonly",
                                  values=["charnues", "epines", "rigides"],
                                  font=self.ft_body, width=34)
        cb_feuilles.pack(padx=14, pady=(0, 10), fill="x")
        self._apply_combo_style(cb_feuilles)
        
        # Bordure des feuilles
        tk.Label(left, text="Bordure des feuilles", font=self.ft_badge,
                 bg=C["panel"], fg=C["muted"]).pack(anchor="w", padx=14, pady=(0, 2))
        cb_bordure = ttk.Combobox(left, textvariable=self.var_bordure, state="readonly",
                                 values=["epineuse", "lisse", "none"],
                                 font=self.ft_body, width=34)
        cb_bordure.pack(padx=14, pady=(0, 10), fill="x")
        self._apply_combo_style(cb_bordure)
        
        # Hauteur estimée
        tk.Label(left, text="Hauteur estimée (cm)", font=self.ft_badge,
                 bg=C["panel"], fg=C["muted"]).pack(anchor="w", padx=14, pady=(0, 2))
        frm_h = tk.Frame(left, bg=C["panel"])
        frm_h.pack(padx=14, fill="x", pady=(0, 12))
        self.lbl_hauteur = tk.Label(frm_h, text="50 cm", font=self.ft_mono,
                                     bg=C["green_dk"], fg=C["white"], width=8, relief="flat")
        self.lbl_hauteur.pack(side="right", padx=(6, 0))
        sl_h = ttk.Scale(frm_h, from_=5, to=250, orient="horizontal",
                        variable=self.var_hauteur, command=self._on_hauteur)
        sl_h.pack(side="left", fill="x", expand=True)

        self._section(left, "SAISON & CONDITIONS")
        
        # Saison
        tk.Label(left, text="Saison", font=self.ft_badge,
                 bg=C["panel"], fg=C["muted"]).pack(anchor="w", padx=14, pady=(0, 2))
        frm_s = tk.Frame(left, bg=C["panel"])
        frm_s.pack(padx=14, pady=(0, 12), fill="x")
        for label, val in [("🌱 Croissance", "croissance"), ("❄️  Dormance", "dormance")]:
            tk.Radiobutton(frm_s, text=label, variable=self.var_saison, value=val,
                           bg=C["panel"], fg=C["white"], selectcolor=C["green_dk"],
                           activebackground=C["panel"], font=self.ft_body).pack(side="left", padx=4)

        # Température slider
        tk.Label(left, text="Température ambiante (°C)", font=self.ft_badge,
                 bg=C["panel"], fg=C["muted"]).pack(anchor="w", padx=14, pady=(0, 2))
        frm_t = tk.Frame(left, bg=C["panel"])
        frm_t.pack(padx=14, fill="x", pady=(0, 12))
        self.lbl_temp = tk.Label(frm_t, text="20°C", font=self.ft_mono,
                                  bg=C["green_dk"], fg=C["white"], width=5, relief="flat")
        self.lbl_temp.pack(side="right", padx=(6, 0))
        sl = ttk.Scale(frm_t, from_=-5, to=45, orient="horizontal",
                       variable=self.var_temp, command=self._on_temp)
        sl.pack(side="left", fill="x", expand=True)

        # Exposition
        tk.Label(left, text="Exposition lumineuse", font=self.ft_badge,
                 bg=C["panel"], fg=C["muted"]).pack(anchor="w", padx=14, pady=(0, 2))
        cb_expo = ttk.Combobox(left, textvariable=self.var_expo, state="readonly",
                               values=["normal", "direct", "ombre"],
                               font=self.ft_body, width=34)
        cb_expo.pack(padx=14, pady=(0, 8), fill="x")
        self._apply_combo_style(cb_expo)

        # Sol
        tk.Label(left, text="Type de sol", font=self.ft_badge,
                 bg=C["panel"], fg=C["muted"]).pack(anchor="w", padx=14, pady=(0, 2))
        cb_sol = ttk.Combobox(left, textvariable=self.var_sol, state="readonly",
                              values=["bien_draine", "retient_eau", "sableux"],
                              font=self.ft_body, width=34)
        cb_sol.pack(padx=14, pady=(0, 10), fill="x")
        self._apply_combo_style(cb_sol)

        self._section(left, "SYMPTÔMES OBSERVÉS")
        frm_sy = tk.Frame(left, bg=C["panel"])
        frm_sy.pack(padx=14, pady=(0, 14), fill="x")
        for text, var in [
            ("🦠 Taches blanches ", self.var_s_taches),
            ("🍂 Feuilles flétries ", self.var_s_fletri),
            ("💧 Feuilles molles ",  self.var_s_molles),
        ]:
            tk.Checkbutton(frm_sy, text=text, variable=var,
                           bg=C["panel"], fg=C["white"], selectcolor=C["green_dk"],
                           activebackground=C["panel"], font=self.ft_body).pack(anchor="w", pady=2)

        # Button
        tk.Button(left, text="🔍  LANCER LE DIAGNOSTIC",
                  font=self.ft_h3, bg=C["green_dk"], fg=C["white"],
                  activebackground=C["green"], activeforeground=C["white"],
                  relief="flat", pady=10, cursor="hand2",
                  command=self.lancer_diagnostic).pack(padx=14, pady=12, fill="x")

        # Rules button
        tk.Button(left, text="📋  Voir toutes les règles",
                  font=self.ft_badge, bg=C["bg3"], fg=C["muted"],
                  activebackground=C["bg2"], activeforeground=C["text"],
                  relief="flat", pady=6, cursor="hand2",
                  command=self.afficher_regles).pack(padx=14, pady=(0, 14), fill="x")

    # ── RIGHT PANEL ──────────────────────────────────────────
    def _build_right(self, parent):
        right = tk.Frame(parent, bg=C["bg"])
        right.grid(row=0, column=1, sticky="nsew", pady=10)
        right.columnconfigure(0, weight=1)
        right.rowconfigure(2, weight=1)

        # ── Fiche plante ────────────────────────────────────
        self.frm_fiche = tk.Frame(right, bg=C["bg2"],
                                   highlightbackground=C["border"], highlightthickness=1)
        self.frm_fiche.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        self.lbl_empty = tk.Label(self.frm_fiche,
            text="🌵  Remplissez les caractéristiques et lancez le diagnostic",
            font=self.ft_h2, bg=C["bg2"], fg=C["muted"], pady=28)
        self.lbl_empty.pack()

        # ── Planning ────────────────────────────────────────
        self.frm_planning = tk.Frame(right, bg=C["bg2"],
                                      highlightbackground=C["border"], highlightthickness=1)
        self.frm_planning.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        self.frm_planning.grid_remove()  # Hidden at startup

        # ── Alertes ─────────────────────────────────────────
        self.frm_alertes = tk.Frame(right, bg=C["bg2"],
                                     highlightbackground=C["border"], highlightthickness=1)
        self.frm_alertes.grid(row=2, column=0, sticky="nsew")
        self.frm_alertes.grid_remove()  # Hidden at startup

    # ── Helpers ──────────────────────────────────────────────
    def _section(self, parent, title):
        frm = tk.Frame(parent, bg=C["bg3"])
        frm.pack(fill="x", padx=0, pady=(6, 8))
        tk.Label(frm, text=f"  {title}", font=self.ft_badge,
                 bg=C["bg3"], fg=C["accent"], pady=5).pack(anchor="w")

    def _apply_combo_style(self, cb):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox",
                        fieldbackground="#1a1a1a", 
                        background="#1a1a1a",
                        foreground="#000000",
                        selectbackground=C["green_dk"],
                        arrowcolor=C["green"],
                        relief="solid",
                        borderwidth=1)

    def _on_temp(self, val):
        t = int(float(val))
        self.lbl_temp.config(text=f"{t}°C")

    def _on_hauteur(self, val):
        h = int(float(val))
        self.lbl_hauteur.config(text=f"{h} cm")

    def _clear(self, frame):
        for w in frame.winfo_children():
            w.destroy()

    # ── Diagnostic ───────────────────────────────────────────
    def lancer_diagnostic(self):
        # Récupérer les caractéristiques observées
        forme = self.var_forme.get()
        feuilles = self.var_feuilles.get()
        bordure = self.var_bordure.get()
        hauteur = int(self.var_hauteur.get())
        
        if not forme or not feuilles or not bordure:
            messagebox.showwarning("Smart Pot", 
                "Veuillez sélectionner toutes les caractéristiques de la plante.")
            return
        
        # Récupérer les symptômes
        symptomes = []
        if self.var_s_taches.get(): symptomes.append("taches_blanches")
        if self.var_s_fletri.get(): symptomes.append("feuilles_fletries")
        if self.var_s_molles.get(): symptomes.append("feuilles_molles")
        
        # Lancer le diagnostic avec chaînage avant
        res = diagnostiquer(
            forme=forme,
            feuilles=feuilles,
            bordure=bordure,
            hauteur=hauteur,
            temperature=int(self.var_temp.get()),
            saison=self.var_saison.get(),
            exposition=self.var_expo.get(),
            sol=self.var_sol.get(),
            symptomes=symptomes,
        )
        
        if res is None:
            messagebox.showerror("Smart Pot",
                "Plante non identifiée.\nVérifiez vos observations ou consultez le guide.")
            return
        
        self.lbl_empty.pack_forget()  # Hide empty message
        self.frm_planning.grid()      # Show planning section
        self.frm_alertes.grid()       # Show alertes section
        self._afficher_fiche(res)
        self._afficher_planning(res)

    # ── Fiche plante ────────────────────────────────────────
    def _afficher_fiche(self, res):
        self._clear(self.frm_fiche)
        p = res["plante"]
        frm = self.frm_fiche

        # Bandeau titre
        top = tk.Frame(frm, bg=C["green_dk"])
        top.pack(fill="x")
        tk.Label(top, text=p["emoji"], font=font.Font(size=32),
                 bg=C["green_dk"], pady=8).pack(side="left", padx=14)
        info = tk.Frame(top, bg=C["green_dk"])
        info.pack(side="left", pady=8)
        tk.Label(info, text=p["nom_commun"], font=self.ft_h2,
                 bg=C["green_dk"], fg=C["white"]).pack(anchor="w")
        tk.Label(info, text=p["nom_scientifique"], font=font.Font(family="Helvetica", size=10, slant="italic"),
                 bg=C["green_dk"], fg=C["green_lt"]).pack(anchor="w")
        tk.Label(info, text=f"  Classe : {res['classe']}  ",
                 font=self.ft_badge, bg=C["accent"], fg=C["bg"],
                 padx=6, pady=2).pack(anchor="w", pady=4)
        tk.Label(info, text=f"  [Règle: {res['id_regle_identification']}]  ",
                 font=font.Font(family="Helvetica", size=8),
                 bg=C["green_dk"], fg=C["green_lt"]).pack(anchor="w")

        # ── PLANNING D'ARROSAGE ─────────────────────────────────
        plan_frm = tk.Frame(frm, bg=C["water_bg"])
        plan_frm.pack(fill="x", padx=0, pady=(10, 0))
        tk.Label(plan_frm, text="📅 Planning d'arrosage — 30 jours",
                 font=self.ft_h3, bg=C["water_bg"], fg=C["water"],
                 pady=8, padx=12).pack(fill="x")
        
        # Stats
        stats = tk.Frame(frm, bg=C["bg2"])
        stats.pack(fill="x", padx=12, pady=8)
        for saison_key, label, jours_arrosage, nb in [
            ("croissance", "🌱 Croissance", res["freq_cr"], len(res["jours_cr"])),
            ("dormance",   "❄️  Dormance",  res["freq_do"], len(res["jours_do"])),
        ]:
            box = tk.Frame(stats, bg=C["bg3"], padx=10, pady=8)
            box.pack(side="left", expand=True, fill="both", padx=4)
            tk.Label(box, text=label, font=self.ft_badge,
                     bg=C["bg3"], fg=C["muted"]).pack()
            freq_txt = f"/{jours_arrosage}j" if jours_arrosage > 0 else "STOP"
            tk.Label(box, text=freq_txt, font=self.ft_big,
                     bg=C["bg3"], fg=C["water"]).pack()
            tk.Label(box, text=f"{nb} arrosages/mois", font=self.ft_badge,
                     bg=C["bg3"], fg=C["text2"]).pack()
        
        # Calendrier
        saison = self.var_saison.get()
        jours = res["jours_cr"] if saison == "croissance" else res["jours_do"]
        self._draw_calendar(frm, jours)

        # ── ALERTES DIRECTES ────────────────────────────────────
        alertes = res["alertes"]
        if alertes:
            alertes_frm = tk.Frame(frm, bg=C["danger_bg"])
            alertes_frm.pack(fill="x", padx=0, pady=(10, 0))
            
            tk.Label(alertes_frm, text="⚠️  ALERTES & PRÉCAUTIONS",
                     font=self.ft_h3, bg=C["danger_bg"], fg=C["danger"],
                     pady=8, padx=12).pack(fill="x")
            
            niveau_cfg = {
                "DANGER":    (C["danger"],   C["danger_bg"],  "🔴"),
                "ATTENTION": (C["warning"],  C["warn_bg"],    "🟡"),
                "INFO":      (C["info"],     C["info_bg"],    "🔵"),
            }
            for a in alertes:
                fg, bg, ico = niveau_cfg.get(a["niveau"], (C["white"], C["bg3"], "⚪"))
                row = tk.Frame(alertes_frm, bg=bg, pady=4, padx=10)
                row.pack(fill="x", padx=0, pady=2)
                tk.Label(row, text=ico, font=font.Font(size=12),
                         bg=bg).pack(side="left", padx=(0, 8))
                txt_frm = tk.Frame(row, bg=bg)
                txt_frm.pack(side="left", fill="x", expand=True)
                tk.Label(txt_frm, text=f"{a['nom']}",
                         font=self.ft_badge, bg=bg, fg=fg).pack(anchor="w")
                tk.Label(txt_frm, text=a["message"],
                         font=self.ft_body, bg=bg, fg=C["white"],
                         wraplength=500, justify="left").pack(anchor="w")

        # Grille de données
        grid = tk.Frame(frm, bg=C["bg2"])
        grid.pack(fill="x", padx=12, pady=10)
        items = [
            ("Famille",       p["famille"]),
            ("Forme",         p["forme"].capitalize()),
            ("Feuilles",      f"{p['feuilles_type']} → {p['feuilles_bordure']}"),
            ("Hauteur max",   f"{p['hauteur_max_cm']} cm"),
            ("Temp. min.",    f"{p['rusticite_min_c']} °C"),
            ("Floraison",     p["floraison"]),
            ("Fleurs",        p["couleur_fleurs"]),
            ("Ravageurs",     ", ".join(p["ravageurs"])),
            ("Multiplication", p["multiplication"]),
            ("Adulte en",     p["temps_adulte_ans"]),
            ("Toxique",       "⚠️ Oui" if p["toxique"] else "✅ Non"),
        ]
        for i, (lbl, val) in enumerate(items):
            r, c = divmod(i, 2)
            cell = tk.Frame(grid, bg=C["bg3"], padx=8, pady=5)
            cell.grid(row=r, column=c, padx=4, pady=3, sticky="ew")
            grid.columnconfigure(c, weight=1)
            tk.Label(cell, text=lbl, font=self.ft_badge,
                     bg=C["bg3"], fg=C["muted"]).pack(anchor="w")
            tk.Label(cell, text=val, font=self.ft_body,
                     bg=C["bg3"], fg=C["white"], wraplength=200).pack(anchor="w")

    # ── Planning ────────────────────────────────────────────
    def _afficher_planning(self, res):
        self._clear(self.frm_planning)
        frm = self.frm_planning

        hdr = tk.Frame(frm, bg=C["water_bg"])
        hdr.pack(fill="x")
        tk.Label(hdr, text="📅  Planning d'arrosage — 30 jours", font=self.ft_h2,
                 bg=C["water_bg"], fg=C["water"], pady=8, padx=12).pack(side="left")

        # Stats row
        stats = tk.Frame(frm, bg=C["bg2"])
        stats.pack(fill="x", padx=12, pady=8)
        for saison_key, label, jours_arrosage, nb in [
            ("croissance", "🌱 Croissance", res["freq_cr"], len(res["jours_cr"])),
            ("dormance",   "❄️  Dormance",  res["freq_do"], len(res["jours_do"])),
        ]:
            box = tk.Frame(stats, bg=C["bg3"], padx=10, pady=8)
            box.pack(side="left", expand=True, fill="both", padx=4)
            tk.Label(box, text=label, font=self.ft_badge,
                     bg=C["bg3"], fg=C["muted"]).pack()
            freq_txt = f"/{jours_arrosage}j" if jours_arrosage > 0 else "STOP"
            tk.Label(box, text=freq_txt, font=self.ft_big,
                     bg=C["bg3"], fg=C["water"]).pack()
            tk.Label(box, text=f"{nb} arrosages/mois", font=self.ft_badge,
                     bg=C["bg3"], fg=C["text2"]).pack()

        # Légende
        leg = tk.Frame(frm, bg=C["bg2"])
        leg.pack(fill="x", padx=12, pady=(0, 4))
        tk.Label(leg, text="● Jours d'arrosage :", font=self.ft_badge,
                 bg=C["bg2"], fg=C["water"]).pack(side="left")
        saison = self.var_saison.get()
        jours = res["jours_cr"] if saison == "croissance" else res["jours_do"]
        tk.Label(leg, text=f"  {', '.join(f'J.{j}' for j in jours) or 'Aucun'}",
                 font=self.ft_mono, bg=C["bg2"], fg=C["white"]).pack(side="left")

        # Calendrier visuel 30 jours
        self._draw_calendar(frm, jours)

    def _draw_calendar(self, parent, water_days):
        cal_frm = tk.Frame(parent, bg=C["bg2"])
        cal_frm.pack(fill="x", padx=12, pady=(4, 12))
        water_set = set(water_days)
        cols = 10
        for d in range(1, 31):
            r, c = divmod(d - 1, cols)
            is_water = d in water_set
            bg   = C["water"]     if is_water else C["bg3"]
            fg   = C["bg"]        if is_water else C["muted"]
            txt  = "💧"           if is_water else str(d)
            cell = tk.Label(cal_frm, text=txt, font=self.ft_badge,
                            bg=bg, fg=fg, width=3, pady=5,
                            relief="flat")
            cell.grid(row=r, column=c, padx=2, pady=2, sticky="ew")
            cal_frm.columnconfigure(c, weight=1)
            if is_water:
                cell.config(relief="groove")
            # Tooltip
            cell.bind("<Enter>", lambda e, day=d, iw=is_water:
                      e.widget.config(text=f"J.{day}" if iw else str(day),
                                      bg=C["green"] if iw else C["border"]))
            cell.bind("<Leave>", lambda e, day=d, iw=is_water:
                      e.widget.config(text="💧" if iw else str(day),
                                      bg=C["water"] if iw else C["bg3"]))

    # ── Alertes ─────────────────────────────────────────────
    def _afficher_alertes(self, res):
        self._clear(self.frm_alertes)
        frm = self.frm_alertes
        alertes = res["alertes"]

        nb_danger = sum(1 for a in alertes if a["niveau"] == "DANGER")
        nb_warn   = sum(1 for a in alertes if a["niveau"] == "ATTENTION")
        nb_info   = sum(1 for a in alertes if a["niveau"] == "INFO")

        # Header
        hdr_bg = C["danger_bg"] if nb_danger else C["warn_bg"] if nb_warn else C["info_bg"]
        hdr_fg = C["danger"]    if nb_danger else C["warning"] if nb_warn else C["info"]
        hdr = tk.Frame(frm, bg=hdr_bg)
        hdr.pack(fill="x")
        summary = f"🔴 {nb_danger} danger   🟡 {nb_warn} attention   🔵 {nb_info} info"
        tk.Label(hdr, text=f"⚠️  Alertes & Précautions   |   {summary}",
                 font=self.ft_h3, bg=hdr_bg, fg=hdr_fg, pady=8, padx=12).pack(side="left")
        tk.Label(hdr, text=f"  {len(alertes)} règles déclenchées  ",
                 font=self.ft_badge, bg=C["green_dk"], fg=C["white"], padx=6).pack(side="right", padx=12)

        # Scrollable alerts
        canvas = tk.Canvas(frm, bg=C["bg2"], highlightthickness=0, height=180)
        sb = ttk.Scrollbar(frm, orient="vertical", command=canvas.yview)
        scroll_frm = tk.Frame(canvas, bg=C["bg2"])
        scroll_frm.bind("<Configure>",
                        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frm, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side="left", fill="both", expand=True, padx=0)
        sb.pack(side="right", fill="y")

        # Bind mousewheel
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

        if not alertes:
            tk.Label(scroll_frm, text="✅  Aucune alerte pour ces conditions.",
                     font=self.ft_body, bg=C["bg2"], fg=C["accent"],
                     pady=20).pack(padx=14)
            return

        niveau_cfg = {
            "DANGER":    (C["danger"],   C["danger_bg"],  "🔴"),
            "ATTENTION": (C["warning"],  C["warn_bg"],    "🟡"),
            "INFO":      (C["info"],     C["info_bg"],    "🔵"),
        }
        for a in alertes:
            fg, bg, ico = niveau_cfg.get(a["niveau"], (C["white"], C["bg3"], "⚪"))
            row = tk.Frame(scroll_frm, bg=bg, pady=6, padx=10)
            row.pack(fill="x", padx=8, pady=4)
            tk.Label(row, text=ico, font=font.Font(size=14),
                     bg=bg).pack(side="left", padx=(0, 8))
            txt_frm = tk.Frame(row, bg=bg)
            txt_frm.pack(side="left", fill="x", expand=True)
            tk.Label(txt_frm, text=f"{a['id']} — {a['nom']}",
                     font=self.ft_badge, bg=bg, fg=fg).pack(anchor="w")
            tk.Label(txt_frm, text=a["message"],
                     font=self.ft_body, bg=bg, fg=C["white"],
                     wraplength=560, justify="left").pack(anchor="w")

    # ── Fenêtre toutes les règles ────────────────────────────
    def afficher_regles(self):
        win = tk.Toplevel(self)
        win.title("📋 Base de règles — Smart Pot")
        win.configure(bg=C["bg"])
        win.geometry("740x520")
        win.grab_set()

        tk.Label(win, text="📋  Base de Règles de Production",
                 font=self.ft_title, bg=C["bg2"], fg=C["white"],
                 pady=12).pack(fill="x")
        tk.Label(win, text=f"  {len(REGLES)} règles au total — Moteur : chaînage avant",
                 font=self.ft_badge, bg=C["bg3"], fg=C["muted"],
                 pady=6).pack(fill="x")

        # Table
        cols = ("ID", "Catégorie", "Nom", "Description")
        tree = ttk.Treeview(win, columns=cols, show="headings", height=20)
        style = ttk.Style()
        style.configure("Treeview",
                        background=C["bg3"], foreground=C["white"],
                        fieldbackground=C["bg3"], rowheight=28,
                        font=("Helvetica", 9))
        style.configure("Treeview.Heading",
                        background=C["green_dk"], foreground=C["white"],
                        font=("Helvetica", 9, "bold"))
        style.map("Treeview", background=[("selected", C["green_dk"])])

        widths = [50, 100, 160, 360]
        for col, w in zip(cols, widths):
            tree.heading(col, text=col)
            tree.column(col, width=w, minwidth=40, anchor="w")

        cat_colors = {
            "Identification": C["accent"],
            "Arrosage":       C["water"],
            "Alerte":         C["danger"],
            "Précaution":     C["warning"],
        }
        for i, r in enumerate(REGLES):
            tag = r["categorie"]
            tree.insert("", "end", values=(r["id"], r["categorie"], r["nom"], r["description"]),
                        tags=(tag,))
        for cat, clr in cat_colors.items():
            tree.tag_configure(cat, foreground=clr)

        vsb = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        tree.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        vsb.pack(side="right", fill="y", pady=8)

        tk.Button(win, text="Fermer", font=self.ft_body,
                  bg=C["green_dk"], fg=C["white"], relief="flat",
                  pady=6, command=win.destroy).pack(pady=8)


# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = SmartPotApp()
    app.mainloop()