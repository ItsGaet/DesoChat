import streamlit as st
import streamlit_authenticator as stauth
import yaml
import cohere
from yaml.loader import SafeLoader
from st_pages import Page, Section, show_pages, add_page_title
from pyexpat.errors import messages
from yaml import serialize

with open('config/utenti.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()

if st.session_state["authentication_status"]:
    add_page_title()
    show_pages([
        Page("login.py", "C-AGE", "😶‍🌫️"),
        Page("story.py", "About Us", ":books:")
    ])  
    st.caption("🚀 Chabot based on Cohere and RAG 🚀")
    authenticator.logout()
    co = cohere.Client('crAvP7FvQ4yVLw7pju7nAHBy9FZmRB5uY6bxgSFB')

    preamble_override = "You are Cage, an expert IT consultant and trainer"

    deso_tech_connector = {
        "id": "web-search",
        "options": {
            "site": "deso.tech/en"
        }
    }

    # Initialize session state variables
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    connectors = [deso_tech_connector]
    
    # Process user input
    if prompt := st.chat_input("What is up?"):
        # Display user input in the chat
        with st.chat_message("user"):
            st.markdown(prompt)

        # Make request to Cohere API
        cohere_response = co.chat(
        model="command",
        message="Info aggiuntive DSH306?",
        preamble_override="Sei un Chatbot per il supporto alla vendita di corsi, rispondi in modo professionale.",
        documents=[
                {"name":"DSH306","description":"Advanced giorno Istio\n\nIl corso si concentra sulla piattaforma di service mesh open source Istio. Gli argomenti coperti includono l’installazione di Istio, la sua iniezione in un cluster Kubernetes, la gestione del traffico di ingresso ed uscita, la sicurezza, il monitoraggio, la distribuzione Blue Green e Canary, l’aggiunta di autenticazione JWT, l’uso di strumenti diagnostici e altro ancora. Il corso include demo dal trainer e laboratori per fornire un’esperienza pratica con Istio. I partecipanti impareranno ad utilizzare Istio per migliorare l’affidabilità, la sicurezza e la visibilità delle loro applicazioni su Kubernetes."},
                {"name":"DSH306","description":"Metodologia didattica\nIl corso prevede laboratori didattici in cui ciascuno studente potrà lavorare ai fini di portare a termine esercizi formativi che forniranno esperienza pratica nell’utilizzo dello strumento, per ciascuno degli argomenti affrontati durante il corso."},
                {"name":"DSH306","description":"Informazioni aggiuntive\nLingua\n• Formatore: Italiano\n• Laboratori e Slide: Inglese\n• Connessione Internet stabile"},
                {"name":"DSH306","description":"Contenuti del corso\nProgramma didattico\n• Install Istio\n• Istio Injection\n• Controlling Ingress Traffic\n• Install Jaeger\n• Install Prometheus and Grafana\n• Install Kiali\n• Routing\n• Blue Green and Canary Deployments\n• Controlling Egress Traffic\n• Deploy Hipster App in Kubernetes.\n• Fault Delay Injection\n• Circuit Breaker\n• Retry\n• Security\n• Mirroring\n• Authorization on Ingress Gateway\n• Add End-User JWT Authentication"},
                {"name":"DSH306","description":"Obiettivi del corso\nConoscenze in uscita\n• Installare Istio e iniettarlo in un cluster Kubernetes\n• Gestire il traffico di ingresso ed uscita utilizzando Istio\n• Utilizzare strumenti come Jaeger, Prometheus, Grafana e Kiali per il monitoraggio\n• Impostare e utilizzare la distribuzione Blue Green e Canary\n• Utilizzare Istio per migliorare la sicurezza delle applicazioni su Kubernetes\n• Aggiungere autenticazione JWT per l’autenticazione degli utenti finali\n• Utilizzare strumenti diagnostici per la risoluzione dei problemi."},
                {"name":"DSH309","description":"Advanced giorno Kubernetes Troubleshooting\n\nIn questo corso avviene una simulazione dove gli studenti dovranno risolvere dei ticket (richieste di supporto) all’interno di un’organizzazione. Il corso è completamente pratico, e si scontra con dei problemi reali. Il docente sarà a disposizione per illustrare le procedure di diagnostica, workflow da seguire per arrivare all’individuazione del problema e alla conseguente risoluzione dello stesso."},
                {"name":"DSH309","description":"Metodologia didattica\nIl corso prevede laboratori didattici in cui ciascuno studente potrà lavorare ai fini di portare a termine esercizi formativi che forniranno esperienza pratica nell’utilizzo dello strumento, per ciascuno degli argomenti affrontati durante il corso."},
                {"name":"DSH309","description":"Informazioni aggiuntive\nLingua\n• Formatore: Italiano\n• Laboratori e Slide: Inglese\n• Connessione Internet stabile"},
                {"name":"DSH309","description":"Contenuti del corso\nProgramma didattico\n• Introduction\n• Scheduling\n• Network\n• Terminating state\n• Cluster Component #1\n• Cluster Component #2\n• Cluster Component #3\n• Cluster Component #4\n• Cluster Component #5"},
                {"name":"DSH309","description":"Obiettivi del corso\nConoscenze in uscita\nTeoria\n• Comprendere la procedura per individuare una problematica e arrivare alla risoluzione della stessa\n\nPratica\n• Risoluzione di ticket che richiamano problemi reali"},
                {"name":"DSK401","description":"Advanced giorno CKA Exam Prep\n\nIl corso di preparazione all’esame CKA è progettato per fornirti le competenze e le conoscenze necessarie per partecipare all’esame Certified Kubernetes Administrator. Al termine del corso, sarai preparato per affrontare l’esame CKA e dimostrare la tua abilità nell’amministrazione di cluster Kubernetes in un ambiente reale. Ottenere la certificazione, CKA riconosciuta a livello internazionale, attesterà le tue competenze come amministratore qualificato di Kubernetes, aprendo nuove opportunità di carriera nel campo dell’orchestrazione dei container. Preparati per un’esperienza di apprendimento coinvolgente e stimolante, guidata da esperti del settore, che ti fornirà gli strumenti necessari per affrontare le sfide di un ambiente Kubernetes sempre più complesso."},
                {"name":"DSK401","description":"Metodologia didattica\nIl corso prevede laboratori didattici in cui ciascuno studente potrà lavorare ai fini di portare a termine esercizi formativi che forniranno esperienza pratica nell’utilizzo dello strumento, per ciascuno degli argomenti affrontati durante il corso."},
                {"name":"DSK401","description":"Informazioni aggiuntive\nLingua\n• Formatore: Italiano\n• Laboratori e Slide: Inglese\n• Connessione Internet stabile"},
                {"name":"DSK401","description":"Contenuti del corso\n\nChi dovrebbe partecipare\nQuesto corso si rivolge a un pubblico di professionisti del settore IT, nello specifico agli amministratori di Kubernetes, agli amministratori cloud e a tutti coloro che sono responsabili della gestione di istanze Kubernetes. L’obiettivo principale di questo percorso formativo è consentire ai partecipanti di certificare le proprie competenze acquisendo la qualifica di Certified Kubernetes Administrator (CKA). Attraverso un approccio completo e approfondito, il corso fornisce le conoscenze e le competenze necessarie per affrontare con successo gli aspetti complessi e le sfide legate all’amministrazione di ambienti Kubernetes. I partecipanti saranno guidati attraverso argomenti chiave, acquisendo una comprensione approfondita delle best practice, delle procedure e delle competenze pratiche fondamentali per eccellere nel ruolo di amministratori di Kubernetes. La certificazione CKA ottenuta al termine di questo corso costituirà un riconoscimento ufficiale delle competenze acquisite e rappresenterà un importante passo avanti nella carriera di coloro che aspirano a eccellere nella gestione avanzata di Kubernetes."},
                {"name":"DSK401","description":"Metodologia didattica\nIl corso prevede laboratori didattici in cui ciascuno studente potrà lavorare ai fini di portare a termine esercizi formativi che forniranno esperienza pratica nell’utilizzo dello strumento, per ciascuno degli argomenti affrontati durante il corso."},
                {"name":"DSK401","description":"Informazioni aggiuntive\nLingua\n• Formatore: Italiano\n• Laboratori e Slide: Inglese\n• Connnessione Internet stabile"}
                ]
                                )

        # Display assistant's response in the chat
        with st.chat_message("assistant"):
            st.markdown(cohere_response.text)

        # Update session state with both user input and assistant's response
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": cohere_response.text})
      
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')