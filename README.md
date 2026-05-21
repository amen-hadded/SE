# 🌵 Smart Pot — Système Expert pour Plantes Grasses et Succulentes

**Projet Mini-M1 Intelligence Artificielle** | Système Expert avec Chaînage Avant en Python / Tkinter
<img width="2558" height="1534" alt="image" src="https://github.com/user-attachments/assets/7119b008-a26c-4d94-a3d7-68b562567a93" />

---

## 📋 Vue d'ensemble

**Smart Pot** est un système expert intelligent dédié à la gestion optimale des plantes grasses et succulentes. Face au problème récurrent de l'arrosage lors des absences prolongées, ce système propose une solution logicielle capable de :

1. **Reconnaître automatiquement** une plante à partir de caractéristiques morphologiques
2. **Déterminer les fréquences d'arrosage** adaptées selon la saison
3. **Générer un planning mensuel** des jours d'arrosage recommandés
4. **Déclencher des alertes** en cas de conditions dangereuses (gel, sur-arrosage, infestation, toxicité)

---

## 🎯 Caractéristiques principales

### Base de Connaissances

- **5 espèces référencées** : Aloe Vera, Blue Torch Cactus, Echeveria elegans, Crassula ovata, Sansevieria
- **25 règles de production** réparties en 5 catégories :
  - R01-R05 : Identification
  - R06-R10 : Classification morphologique
  - R11-R15 : Calcul d'arrosage
  - R16-R22 : Alertes critiques
  - R23-R25 : Précautions et entretien
- **Source documentaire** : Royal Horticultural Society (RHS)

### Moteur d'Inférence

- **Chaînage avant** (Forward Chaining) - raisonnement dirigé par les données
- **4 étapes séquentielles** : Identification → Classification → Arrosage → Alertes
- **Résolution de conflits** : Ordre de priorité pour identification, accumulation pour alertes

### Interface Graphique

- **Tkinter** natif (aucune dépendance externe)
- **Panneau gauche** : Saisie intuitive des caractéristiques
- **Panneau droit** : Affichage des résultats structurés
- **3 sections de résultats** :
  - Fiche plante détaillée
  - Planning d'arrosage visuel (30 jours)
  - Alertes classées par criticité (DANGER / ATTENTION / INFO)

---

## 🚀 Démarrage rapide

### Prérequis

- **Python 3.7+**
- Système d'exploitation : Windows, macOS, Linux

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/amehadded/smart-pot.git
cd smart-pot

# Installer les dépendances (optionnel, modules standards seuls)
pip install -r requirements.txt
```

### Utilisation

```bash
python SE.py
```

L'application démarre avec l'interface graphique Tkinter. Remplissez les champs et cliquez sur **« LANCER LE DIAGNOSTIC »** pour obtenir le diagnostic.

---

## 📊 Structure du projet

```
smart-pot/
├── SE.py                    # Application principale (GUI + moteur)
├── requirements.txt         # Dépendances Python
├── README.md               # Ce fichier
└── rapportSystémeExpert.tex # Documentation complète (LaTeX)
```

---

## 🔧 Flux de travail du diagnostic

```
┌─────────────────────────────────────────────────────┐
│  ENTRÉES OBSERVÉES                                  │
│  (Caractéristiques visuelles, conditions ambiantes, │
│   symptômes)                                        │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  ÉTAPE 1 : IDENTIFICATION (R01-R05)                │
│  → Détermine l'espèce de la plante                 │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  ÉTAPE 2 : CLASSIFICATION (R06-R10)                │
│  → Assigne une classe morphologique descriptive     │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  ÉTAPE 3 : ARROSAGE (R11-R15)                      │
│  → Calcule fréquences croissance/dormance          │
│  → Génère planning 30 jours                         │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  ÉTAPE 4 : ALERTES (R16-R25)                       │
│  → Détecte situations dangereuses                   │
│  → Classe par criticité (DANGER/ATTENTION/INFO)    │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
       RÉSULTATS & RECOMMANDATIONS
```

---

## 📝 Entrées utilisateur

### Caractéristiques morphologiques

- **Forme** : Rosette, Colonnaire, Érigée, Buissonnante
- **Type de feuilles** : Charnues, Épines, Rigides
- **Bordure des feuilles** : Épineuse, Lisse
- **Hauteur estimée** : Valeur en cm

### Conditions ambiantes

- **Saison** : Croissance (printemps-été) ou Dormance (automne-hiver)
- **Température** : -5°C à 45°C (curseur)
- **Exposition lumineuse** : Normale, Directe, Ombre
- **Type de sol** : Bien drainé, Retient l'eau, Sableux

### Symptômes observés

- Taches blanches (cochenilles)
- Feuilles flétries (manque d'eau)
- Feuilles molles (sur-arrosage)

---

## 📤 Sorties du système

### Fiche Plante

- Nom commun et scientifique
- Famille botanique
- Classe morphologique
- Règle d'identification déclenchée
- Attributs détaillés (hauteur, rusticité, exposition, drainage, toxicité, etc.)

### Planning d'Arrosage

- Fréquence en période de croissance
- Fréquence en période de dormance
- Nombre d'arrosages par mois
- Calendrier visuel avec jours d'arrosage marqués

### Alertes & Précautions

- **DANGER** : Risques critiques (gel, sur-arrosage, pourriture)
- **ATTENTION** : Risques importants (toxicité, infestation)
- **INFO** : Conseils d'entretien (manipulation, fertilisation)

---

## 💾 Dépendances

### Standards Python (inclus)

- `tkinter` : Interface graphique
- `calendar` : Gestion des calendriers
- `datetime` : Gestion des dates

**Aucune dépendance externe requise !**

---

## 📚 Cas d'usage

### Exemple 1 : Identification d'une Echeveria elegans

1. Sélectionner : Forme = Rosette, Feuilles = Charnues, Hauteur = 15 cm
2. Cliquer « LANCER LE DIAGNOSTIC »
3. Système identifie : **Echeveria elegans** (Succulente miniature)
4. Recommande : Arrosage tous les 14 jours en croissance, arrêt complet en dormance
5. Génère planning et alertes pertinentes

### Exemple 2 : Détection de surexposition

1. Sélectionner : Aloe Vera, Exposition = Directe (au soleil intense)
2. Système déclenche alerte ATTENTION : "Risque de brûlure foliaire"
3. Recommande : Exposition filtrée ou ombre partielle

---

## 🔬 Méthodologie

### Sources documentaires

- **Royal Horticultural Society (RHS)** - [https://www.rhs.org.uk/plants](https://www.rhs.org.uk/plants)
- Fiches techniques détaillées pour chaque espèce
- Données de rusticité, arrosage, fertilisation vérifiées

### Spécifications du projet

- Base de faits : 5 espèces de succulentes
- Base de règles : 25 règles de production
- Moteur : Chaînage avant
- Interface : Tkinter
- Langage : Python 3

---

## 👤 Auteur

**Amen Allah Hadded**  
Mini-Projet M1 — Master 1 Informatique  
Année Universitaire 2025/2026

---

## 📄 Licence

Ce projet est fourni à titre éducatif. Libre d'utilisation et de modification.

---

## 📞 Support

Pour toute question ou suggestion, consultez la documentation complète du rapport (rapportSystémeExpert.tex) ou contactez l'auteur.

---

## 🌱 Améliorations futures

- [ ] Extension à 15+ espèces
- [ ] Intégration de capteurs matériels (humidité, lumière, température)
- [ ] Système d'arrosage automatisé
- [ ] API REST pour intégration externe
- [ ] Application mobile multiplateforme
- [ ] Machine Learning pour amélioration des règles

---

**Smart Pot** — Prenez soin de vos plantes, même en vacances ! 🌿
