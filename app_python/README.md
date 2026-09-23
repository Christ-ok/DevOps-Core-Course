1. Aperçu : Ce projet qui consiste à créer un serveur HTTP avec quelques routes, l'étape 1 consiste à écrire le code et dans l'étape suivante nous fairons plusieurs autres choses dont notamment de la conteneurisation de l'orchestration ...


2. Prérequis : Python 3.14.4
               Flask 3.1.3


3. Installation : - python3 -m venv venv
                  - source venv/bin/activate
                  - pip install flask

4. Execution : python3 app.py (hote = "0.0.0.0", port = 5000)


5. Configuration : 
    Variables d'environnements : 
        - host = os.getenv("HOST", "0.0.0.0")
        - port = int(os.getenv("PORT", "5000"))
        - debug = os.getenv("DEBUG", "False").lower() == "true"
