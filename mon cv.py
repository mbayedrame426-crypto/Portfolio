import streamlit as st
st.title("Technicien Supérieur Géomaticien")
sidebar=st.sidebar
with sidebar:
    st.image("mbaye.jpeg")
    st.header("Mbaye Dramé")
    st.write["Adresse:Pikine,Dakar"]
    st.write("Tel:785664635")
    st.write("E-mail:mbayedrame426@gmail.com")

    
########################################

st.header("A propos de moi ")
st.write("Passionné par l'informatique et les nouvelles technologies, j'explore le monde du numérique par la geomatique( Gestion numérique des territoires).Je suis technicien supérieur en géomatique,motivé par la compréhension, l’analyse et la planification des territoires.En tant que géomaticien, j’explore l’espace pour révéler ce que l’œil ne voit pas : les zones à fort potentiel, les risques invisibles, les opportunités stratégiques...Rigoureux, analytique et orienté solution, je mets la géomatique au service du développement durable et de la performance territoriale parcque je prends pleinement en compte l'importance et la puissance de l’information géographique pour transformer les défis territoriaux en solutions concrètes et durables  car comprendre un territoire, c’est comprendre son avenir.")

#######################################

st.header("Mon projet")
st.markdown("""En tant que géomaticien, mon ambition est d'accompagner et d'appuyer les collectivités territoriales, les services techniques, les entreprises, les porteurs de projets ou encore les institutions publiques pour transformer chaque projet, qu’il soit dans l’agriculture, l’environnement, l’urbanisme, les infrastructures, l’énergie, la santé, l’éducation ou l’aménagement du territoire en opportunités optimales et décisions stratégiques grâce aux sciences géospatiales et aux nouvelles technologies (drones, capteurs IoT, intelligence artificielle et SIG) pour maximiser et optimiser les investissements, renforcer la maitrise du territoire et la prise de meilleures décisions et enfin promouvoir un développement durable complet, économique, social et environnemental afin de bâtir un Sénégal performant, innovant, emergent et durable sur tous ses fronts en alliant précision et éfficacité dans un monde intelligent où l'Afrique est en avant.""")

#######################################

st.header("Mes diplômes")
st.write(".Brevet de technicien supérieur en géomatique obtenu au Centre d'Entrepreneuriat et de Développement Technique (CEDT-LEG15) avec la «mention Tres Bien»")
st.write(".Baccalauréat en série L2 obtenu au Lycée de Bokhol avec la «mention Bien» ")
st.write(".Certificat en informatique et internet obtenu grâce au programme de la FORCE-N")
st.write(".Certificat en secourisme obtenu a la Croix Rouge sénégalaise")
#########################################

st.header("Mes compétences")

# Création des colonnes pour les trois catégories
col1, col2, col3 = st.columns(3)

# ---- Techniques ----
with col1:
    st.subheader("Techniques")
    techniques =[
        "Production de cartes thématiques professionnelles (santé, environnement, agriculture, infrastructure...)",
        "Collecte et traitement de données",
        "Analyse spatiale (superposition, buffer, intersection...)",
        "Numérisation, géoréférencement et correction de topologie",
        "Création et gestion de bases de données géospatiales",
        "Analyse statistique appliquée au territoire",
        "Maîtrise de l'informatique (suite bureautique, programmation (Python, R, VSCode, JavaScript...))",
        "Geodatascience (prévision des dynamiques spatiales à l'aide de l'IA)",
        "Modélisation spatiale (simulation et visualisation 3D de phénomènes)",
        "Télédétection et imagerie satellite",
        "Topographie",
        "Dessin de plans architecturaux (2D/3D) et cadastraux",
        "Photogrammétrie",
        "Géodésie",
        "Télépilotage de drones",
        "Webmapping (Cartes interactives et dashboards)",
        "Vérification et contrôle de la qualité des données",
        "Maitrise des gestes de premiers secours en cas accident dans le travail"
    ]
    for item in techniques:
        st.write(f"- {item}")

# ---- Aide à la décision ----
with col2:
    st.subheader("Aide à la décision")
    aide_decision = [
        "Rapports techniques et cartographiques",
        "Optimisation des investissements",
        "Détection des changements dans le temps",
        "Suivi et gestion des risques naturels",
        "Gestion et optimisation de l'utilisation des ressources naturelles (eau, engrais, terres...)",
        "Aide au choix des sites d'implantation (forages, infrastructures, cultures...)",
        "Priorisation des zones d'intervention pour les décideurs",
        "Planification et gestion urbaine"
    ]
    for item in aide_decision:
        st.write(f"- {item}")

# ---- Technologies et outils ----
with col3:
    st.subheader("Technologies et outils")
    technologies =[
        "Logiciels SIG (QGIS, ArcGIS, MapInfo, PostGIS, MySQL...)",
         "Logiciels Topo et dessin plan (Autocad/Covadis,Sketchup,Archicad,...)",
        "Logiciels télédétection (ENVI, ERDAS)",
        "Python / R pour données géospatiales",
        "Outils de levées terrain (GPS, GNSS, Stations totales, drones, capteurs IoT...)",
        "Google Earth Engine",
        "Applications mobiles de collecte de données (Mobile Topographer, KoboCollect...)"
    ]
    for item in technologies:
        st.write(f"- {item}")


st.header("Centres d'intérêts")

# Liste des centres d'intérêts avec description
interets = [
    "Randonnée et visite": "Pour explorer la nature et les terrains à cartographier.",
    "Photographie géospatiale": "Pour capturer des paysages ou structures pour analyse ou documentation.",
    "Innovation et nouvelles technologies": "Pour nourrir ma curiosité et mon amour pour les outils numériques et logiciels SIG.",
    "Projets communautaires ou éducatifs": "Pour la transmission et la promotion de la géomatique et la sensibilisation locale."
]

# Affichage
for titre, description in interets.items():
    st.subheader(titre)
    st.write(description)
    
