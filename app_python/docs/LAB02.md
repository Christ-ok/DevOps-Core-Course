Contenu du Dockerfile
----------------------
FROM python:3.13-slim

WORKDIR /app

RUN useradd -u 15000 chris

COPY requirements.txt .

RUN pip install --no-cache-dir -r

COPY app.py .

USER 15000

EXPOSE 5000

CMD ["python"  "app.py"]


Contenu du .dockerignore
------------------------
__pycache__/
*.pyc
.venv
venv/
.env
.vscode/
docs/
tests/


Justification d'une phrase par # YOUR TASK
------------------------------------------
RUN ___ # YOUR TASK: create a NUMERIC non-root user (uid >= 10000)
=> RUN useradd -u 15000 chris

J'ai créé un utilisateur avec useradd au lieu de adduser pour pouvoir ajouter manuellement plus d'options dont notamment -u qui permet de définir un uid manuellement pour l'utilisateur



Affichage du docker build
--------------------------
chris@Christok-PC:~/projects/DevOps-Core-Course$ docker build -t devops-info-service:lab02 ./app_python
[+] Building 11.3s (11/11) FINISHED                                                                                                                                                docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                         0.0s
 => => transferring dockerfile: 245B                                                                                                                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.13-slim                                                                                                                          1.8s
 => [internal] load .dockerignore                                                                                                                                                            0.0s
 => => transferring context: 98B                                                                                                                                                             0.0s
 => [1/6] FROM docker.io/library/python:3.13-slim@sha256:8d9d0b8bcf6506481eae4907c18f5e3e7902e629f5f6d684f9e7c32e85e3ddf0                                                                    0.0s
 => => resolve docker.io/library/python:3.13-slim@sha256:8d9d0b8bcf6506481eae4907c18f5e3e7902e629f5f6d684f9e7c32e85e3ddf0                                                                    0.0s
 => [internal] load build context                                                                                                                                                            0.0s
 => => transferring context: 85B                                                                                                                                                             0.0s
 => CACHED [2/6] WORKDIR /app                                                                                                                                                                0.0s
 => CACHED [3/6] RUN useradd -u 15000 chris                                                                                                                                                  0.0s
 => [4/6] COPY requirements.txt .                                                                                                                                                            0.0s
 => [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                 7.2s
 => [6/6] COPY app.py .                                                                                                                                                                      0.1s
 => exporting to image                                                                                                                                                                       2.0s
 => => exporting layers                                                                                                                                                                      1.0s
 => => exporting manifest sha256:f7380d8e2e5f9cfa9b9a6ae0a2ffb1efa20706ebe17faa01ac43fde4be7883fd                                                                                            0.0s
 => => exporting config sha256:9ab04b92ed9e3a262761acf01ece0366f02a08b5747146088bed8f0ee762de44                                                                                              0.0s
 => => exporting attestation manifest sha256:609993dc4f0e6a48bec551e47d6981d6d307fb11bb3deccb4ef12e673761a0d1                                                                                0.1s
 => => exporting manifest list sha256:c7a161bc32402a4dba286dbd5e815fa64cf3f7cf1906784d64e2b3b9fa1bcd37                                                                                       0.0s
 => => naming to docker.io/library/devops-info-service:lab02                                                                                                                                 0.0s
 => => unpacking to docker.io/library/devops-info-service:lab02     



Logs des 10 dernières lignes du journal
----------------------------------------
 => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt                      0.0s
 => CACHED [6/6] COPY app.py .                                                           0.0s
 => exporting to image                                                                   0.1s
 => => exporting layers                                                                  0.0s
 => => exporting manifest sha256:f7380d8e2e5f9cfa9b9a6ae0a2ffb1efa20706ebe17faa01ac43fd  0.0s
 => => exporting config sha256:9ab04b92ed9e3a262761acf01ece0366f02a08b5747146088bed8f0e  0.0s
 => => exporting attestation manifest sha256:8241b670489284a10e740bd3aa710c841f0e71bc5c  0.0s
 => => exporting manifest list sha256:4ac81f6325dc2929be7d00442c14b12d5e05bcd9449e59037  0.0s
 => => naming to docker.io/library/devops-info-service:lab02                             0.0s
 => => unpacking to docker.io/library/devops-info-service:lab02                          0.0s


Les deux JSON 
-------------
chris@Christok-PC:~/projects/DevOps-Core-Course$ curl -s http://localhost:5000/ | jq .
{
  "endpoints": [
    {
      "description": "Service information",
      "method": "GET",
      "path": "/"
    },
    {
      "description": "Health check",
      "method": "GET",
      "path": "/health"
    }
  ],
  "request": {
    "client_ip": "172.17.0.1",
    "method": "GET",
    "path": "/",
    "user_agent": "curl/8.18.0"
  },
  "runtime": {
    "current_time": "2026-09-24T11:30:49.233985+00:00",
    "timezone": "UTC",
    "uptime_human": "0 hours, 0 minutes",
    "uptime_seconds": 38
  },
  "service": {
    "description": "DevOps course info service",
    "framework": "Flask",
    "name": "devops-info-service",
    "version": "1.0.0"
  },
  "system": {
    "architecture": "x86_64",
    "cpu_count": 16,
    "hostname": "c03afd04aa37",
    "platform": "Linux",
    "platform_version": "#1 SMP PREEMPT_DYNAMIC Thu Jun 18 21:54:43 UTC 2026",
    "python_version": "3.13.15"
  }
}

chris@Christok-PC:~/projects/DevOps-Core-Course$ curl -s http://localhost:5000/health | jq -c .
{"status":"healthy","timestamp":"2026-09-24T11:31:22.547254+00:00","uptime_seconds":72}



La ligne id -u 
---------------
chris@Christok-PC:~/projects/DevOps-Core-Course$ docker run --rm devops-info-service:lab02 id -u
15000



Docker images
-------------
chris@Christok-PC:~/projects/DevOps-Core-Course$ docker images devops-info-service:lab02
REPOSITORY            TAG       IMAGE ID       CREATED        SIZE
devops-info-service   lab02     4ac81f6325dc   15 hours ago   197MB



Analyse de la couche la plus importante
---------------------------------------
La couche la plus importante est celle du système d'exploitation car c'est sur elle que repose l'image python, voilà pourquoi elle est celle qui pèse le plus 



Paragraphe de conclusion sur les 2 images
-----------------------------------------
Mon cas est est différent de la norma habituel car l'image mulit-stage est un peu plus légère que la mono-stage, et je trouve plus structuré d'avoir une image multi-stage car cela peut répondre à plusieurs besoin car chaque stage s'occupera d'une tache bien précise rends le tout beaucoup plus ordonné 



Contenu du Dockerfile.multi
---------------------------
# ---------------- Stage 1: Builder -----------------
FROM python:3.13-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ------------------ Stage 2: Runtime ---------------
FROM python:3.13-slim AS runtime
RUN useradd -u 10001 christopher
WORKDIR /app
COPY --from=builder /install .
ENV PATH="/venv/bin:$PATH"
COPY . .
USER 10001
EXPOSE 5000
CMD ["python", "app.py"]


Docker Images des 2 Dockerfile
------------------------------
lab02-multi     183MB
lab02   197MB


Paragraphe sur l'étape de réduction
-----------------------------------
L'étape de réduction multi-stage a diminué légèrement diminué la taille de mon image. Parce-que j'ai récupéré dans le second stage uniquement les éléments importants pour l'image finale et le reste n'a pas été pris en compte, notamment grace à : COPY --from=builder /install .
Tout le reste du premier stage n'a pas été récupéré dans l'image finale ce qui a pu allégé légèrement l'image



Curl dans le container lancé avec l'image multi
--------------------------------------------------
chris@Christok-PC:~/projects/DevOps-Core-Course$ curl -s localhost:5000/health
{"status":"healthy","timestamp":"2026-09-24T12:50:14.217784+00:00","uptime_seconds":4803}


Tableau de gravité
-------------------

| **Gravité** |  *Compter* |
| ----------- | ---------: |
| CRITIQUE    | 0          |
| HAUT        | 44         |
| MOYEN       | 53         |
| FAIBLE      | 57         |
| INCONNU     | 2          |
| **Total**   | **156**    |



Explication d'un constat + comment y remédier
---------------------------------------------
1. setuptools - CVE-2025-47273
2. Parce que le produit utilise des données d'entrée externes pour construire un chemin d'accès destiné à identifier un fichier ou un répertoire situé sous un répertoire parent restreint, mais il ne neutralise pas correctement les éléments spéciaux présents dans le chemin d'accès qui peuvent faire en sorte que celui-ci pointe vers un emplacement situé en dehors du répertoire restreint.
3. Il suffit d'installer une version supérieure qui règle normalement ce problème


Résultat de trivy
-----------------
│                    │ CVE-2026-6791       │          │              │                                   │               │ glibc: Glibc: Denial of Service via stack exhaustion during  │
│                    │                     │          │              │                                   │               │ tilde expansion                                              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-6791                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-77117      │          │              │                                   │               │ glibc: Non-progress DoS in SHIFT_JISX0213 -&gt               │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-77117                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-80489      │          │              │                                   │               │ glibc: Non-progress DoS in EUC_JISX0213 -> UCS-4 conversion  │
│                    │                     │          │              │                                   │               │ state                                                        │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-80489                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-8674       │          │              │                                   │               │ glibc: glibc DNS stub resolver: Denial of Service via long   │
│                    │                     │          │              │                                   │               │ search domain...                                             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-8674                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-86805      │          │              │                                   │               │ glibc: glibc: Privilege escalation and arbitrary code        │
│                    │                     │          │              │                                   │               │ execution via TOCTOU race condition...                       │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-86805                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-89092      │          │              │                                   │               │ glibc: nscd stack overflow leads to degraded DNS resolution  │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-89092                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-95818      │          │              │                                   │               │ glibc: glibc: Local attacker can cause denial of service and │
│                    │                     │          │              │                                   │               │ information disclosure...                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-95818                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2010-4756       │ LOW      │              │                                   │               │ glibc: glob implementation can cause excessive CPU and       │
│                    │                     │          │              │                                   │               │ memory consumption due to...                                 │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2018-20796      │          │              │                                   │               │ glibc: uncontrolled recursion in function                    │
│                    │                     │          │              │                                   │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-1010022    │          │              │                                   │               │ glibc: stack guard protection bypass                         │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-1010023    │          │              │                                   │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                    │                     │          │              │                                   │               │ because of...                                                │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-1010024    │          │              │                                   │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-1010025    │          │              │                                   │               │ glibc: information disclosure of heap addresses of           │
│                    │                     │          │              │                                   │               │ pthread_created thread                                       │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-9192       │          │              │                                   │               │ glibc: uncontrolled recursion in function                    │
│                    │                     │          │              │                                   │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├────────────────────┼─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libc6              │ CVE-2026-18374      │ MEDIUM   │              │                                   │               │ glibc: glibc: Heap buffer overflow via attacker-controlled   │
│                    │                     │          │              │                                   │               │ fopen mode string                                            │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-18374                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-19499      │          │              │                                   │               │ glibc: Buffer Overflow in strfmon right-justification        │
│                    │                     │          │              │                                   │               │ padding                                                      │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-19499                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-19542      │          │              │                                   │               │ glibc: Fix out-of-bounds array write in tdelete              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-19542                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-5435       │          │              │                                   │               │ glibc: glibc: Out-of-bounds write via TSIG record processing │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-5435                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-6238       │          │              │                                   │               │ glibc: glibc: Application crash or uninitialized memory read │
│                    │                     │          │              │                                   │               │ via crafted DNS response...                                  │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-6238                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-6368       │          │              │                                   │               │ glibc: glibc: Process abort due to invalid memory in wordexp │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-6368                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-6791       │          │              │                                   │               │ glibc: Glibc: Denial of Service via stack exhaustion during  │
│                    │                     │          │              │                                   │               │ tilde expansion                                              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-6791                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-77117      │          │              │                                   │               │ glibc: Non-progress DoS in SHIFT_JISX0213 -&gt               │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-77117                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-80489      │          │              │                                   │               │ glibc: Non-progress DoS in EUC_JISX0213 -> UCS-4 conversion  │
│                    │                     │          │              │                                   │               │ state                                                        │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-80489                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-8674       │          │              │                                   │               │ glibc: glibc DNS stub resolver: Denial of Service via long   │
│                    │                     │          │              │                                   │               │ search domain...                                             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-8674                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-86805      │          │              │                                   │               │ glibc: glibc: Privilege escalation and arbitrary code        │
│                    │                     │          │              │                                   │               │ execution via TOCTOU race condition...                       │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-86805                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-89092      │          │              │                                   │               │ glibc: nscd stack overflow leads to degraded DNS resolution  │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-89092                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-95818      │          │              │                                   │               │ glibc: glibc: Local attacker can cause denial of service and │
│                    │                     │          │              │                                   │               │ information disclosure...                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-95818                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2010-4756       │ LOW      │              │                                   │               │ glibc: glob implementation can cause excessive CPU and       │
│                    │                     │          │              │                                   │               │ memory consumption due to...                                 │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2018-20796      │          │              │                                   │               │ glibc: uncontrolled recursion in function                    │
│                    │                     │          │              │                                   │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-1010022    │          │              │                                   │               │ glibc: stack guard protection bypass                         │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-1010023    │          │              │                                   │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                    │                     │          │              │                                   │               │ because of...                                                │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-1010024    │          │              │                                   │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-1010025    │          │              │                                   │               │ glibc: information disclosure of heap addresses of           │
│                    │                     │          │              │                                   │               │ pthread_created thread                                       │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2019-9192       │          │              │                                   │               │ glibc: uncontrolled recursion in function                    │
│                    │                     │          │              │                                   │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ liblastlog2-2      │ CVE-2026-76642      │ HIGH     │              │ 2.41.5-0+deb13u1                  │               │ util-linux: util-linux: failed external mount helper still   │
│                    │                     │          │              │                                   │               │ runs privileged X-mount post-hooks                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78408      │          │              │                                   │               │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
│                    │                     │          │              │                                   │               │ cgroup migration authority                                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78409      │          │              │                                   │               │ util-linux: util-linux: X-mount.subdir detached-tree         │
│                    │                     │          │              │                                   │               │ resolution can escape via intermediate symlinks              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78410      │          │              │                                   │               │ util-linux: util-linux: restricted bind mounts do not pin    │
│                    │                     │          │              │                                   │               │ the source, allowing X-mount.owner/group/mode...             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-3184       │ MEDIUM   │              │                                   │               │ util-linux: util-linux: Access control bypass due to         │
│                    │                     │          │              │                                   │               │ improper hostname canonicalization                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-3184                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2022-0563       │ LOW      │              │                                   │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                    │                     │          │              │                                   │               │ and chsh when compiled...                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ liblzma5           │ TEMP-1147318-639065 │ UNKNOWN  │              │ 5.8.1-1+deb13u1                   │               │ [GHSA-5qpq-xqfv-j9pg: Invalid write if a decoder is          │
│                    │                     │          │              │                                   │               │ reinitialized after allocation failure]                      │
│                    │                     │          │              │                                   │               │ https://security-tracker.debian.org/tracker/TEMP-1147318-63- │
│                    │                     │          │              │                                   │               │ 9065                                                         │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libmount1          │ CVE-2026-76642      │ HIGH     │              │ 2.41.5-0+deb13u1                  │               │ util-linux: util-linux: failed external mount helper still   │
│                    │                     │          │              │                                   │               │ runs privileged X-mount post-hooks                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78408      │          │              │                                   │               │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
│                    │                     │          │              │                                   │               │ cgroup migration authority                                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78409      │          │              │                                   │               │ util-linux: util-linux: X-mount.subdir detached-tree         │
│                    │                     │          │              │                                   │               │ resolution can escape via intermediate symlinks              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78410      │          │              │                                   │               │ util-linux: util-linux: restricted bind mounts do not pin    │
│                    │                     │          │              │                                   │               │ the source, allowing X-mount.owner/group/mode...             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-3184       │ MEDIUM   │              │                                   │               │ util-linux: util-linux: Access control bypass due to         │
│                    │                     │          │              │                                   │               │ improper hostname canonicalization                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-3184                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2022-0563       │ LOW      │              │                                   │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                    │                     │          │              │                                   │               │ and chsh when compiled...                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libncursesw6       │ CVE-2025-69720      │ HIGH     │              │ 6.5+20250216-2                    │               │ ncurses: ncurses: Buffer overflow vulnerability may lead to  │
│                    │                     │          │              │                                   │               │ arbitrary code execution.                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2025-69720                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2025-6141       │ LOW      │              │                                   │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libpam-modules     │ CVE-2026-54411      │ MEDIUM   │              │ 1.7.0-5                           │               │ linux-pam: Plaintext password recovery via timing            │
│                    │                     │          │              │                                   │               │ discrepancy in pam_userdb module                             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-54411                   │
├────────────────────┤                     │          │              │                                   ├───────────────┤                                                              │
│ libpam-modules-bin │                     │          │              │                                   │               │                                                              │
│                    │                     │          │              │                                   │               │                                                              │
│                    │                     │          │              │                                   │               │                                                              │
├────────────────────┤                     │          │              │                                   ├───────────────┤                                                              │
│ libpam-runtime     │                     │          │              │                                   │               │                                                              │
│                    │                     │          │              │                                   │               │                                                              │
│                    │                     │          │              │                                   │               │                                                              │
├────────────────────┤                     │          │              │                                   ├───────────────┤                                                              │
│ libpam0g           │                     │          │              │                                   │               │                                                              │
│                    │                     │          │              │                                   │               │                                                              │
│                    │                     │          │              │                                   │               │                                                              │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsmartcols1      │ CVE-2026-76642      │ HIGH     │              │ 2.41.5-0+deb13u1                  │               │ util-linux: util-linux: failed external mount helper still   │
│                    │                     │          │              │                                   │               │ runs privileged X-mount post-hooks                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78408      │          │              │                                   │               │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
│                    │                     │          │              │                                   │               │ cgroup migration authority                                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78409      │          │              │                                   │               │ util-linux: util-linux: X-mount.subdir detached-tree         │
│                    │                     │          │              │                                   │               │ resolution can escape via intermediate symlinks              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78410      │          │              │                                   │               │ util-linux: util-linux: restricted bind mounts do not pin    │
│                    │                     │          │              │                                   │               │ the source, allowing X-mount.owner/group/mode...             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-3184       │ MEDIUM   │              │                                   │               │ util-linux: util-linux: Access control bypass due to         │
│                    │                     │          │              │                                   │               │ improper hostname canonicalization                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-3184                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2022-0563       │ LOW      │              │                                   │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                    │                     │          │              │                                   │               │ and chsh when compiled...                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsqlite3-0       │ CVE-2026-50812      │ MEDIUM   │              │ 3.46.1-7+deb13u2                  │               │ sqlite: SQLite: Denial of Service via malformed changeset in │
│                    │                     │          │              │                                   │               │ Session Extension                                            │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-50812                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-50813      │          │              │                                   │               │ sqlite: SQLite: Information disclosure via Session Extension │
│                    │                     │          │              │                                   │               │ changeset merge path                                         │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-50813                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2021-45346      │ LOW      │              │                                   │               │ sqlite: crafted SQL query allows a malicious user to obtain  │
│                    │                     │          │              │                                   │               │ sensitive information...                                     │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2021-45346                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2025-70873      │          │              │                                   │               │ sqlite: SQLite: Information Disclosure via Crafted ZIP File  │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2025-70873                   │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsystemd0        │ CVE-2026-16742      │ HIGH     │              │ 257.13-1~deb13u1                  │               │ systemd: systemd-homed: Local privilege escalation via       │
│                    │                     │          │              │                                   │               │ missing home-record signature verification                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-16742                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-15059      │ MEDIUM   │              │                                   │               │ systemd: systemd-oomd: Unprivileged users can terminate      │
│                    │                     │          │              │                                   │               │ arbitrary processes via IPC API                              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-15059                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2013-4392       │ LOW      │              │                                   │               │ systemd: TOCTOU race condition when updating file            │
│                    │                     │          │              │                                   │               │ permissions and SELinux security contexts...                 │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2023-31437      │          │              │                                   │               │ An issue was discovered in systemd 253. An attacker can      │
│                    │                     │          │              │                                   │               │ modify a...                                                  │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2023-31438      │          │              │                                   │               │ An issue was discovered in systemd 253. An attacker can      │
│                    │                     │          │              │                                   │               │ truncate a...                                                │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2023-31439      │          │              │                                   │               │ An issue was discovered in systemd 253. An attacker can      │
│                    │                     │          │              │                                   │               │ modify the...                                                │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-40228      │          │              │                                   │               │ systemd: systemd-journald: Unintended output to user         │
│                    │                     │          │              │                                   │               │ terminals via logger command                                 │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-40228                   │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libtinfo6          │ CVE-2025-69720      │ HIGH     │              │ 6.5+20250216-2                    │               │ ncurses: ncurses: Buffer overflow vulnerability may lead to  │
│                    │                     │          │              │                                   │               │ arbitrary code execution.                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2025-69720                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2025-6141       │ LOW      │              │                                   │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libudev1           │ CVE-2026-16742      │ HIGH     │              │ 257.13-1~deb13u1                  │               │ systemd: systemd-homed: Local privilege escalation via       │
│                    │                     │          │              │                                   │               │ missing home-record signature verification                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-16742                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-15059      │ MEDIUM   │              │                                   │               │ systemd: systemd-oomd: Unprivileged users can terminate      │
│                    │                     │          │              │                                   │               │ arbitrary processes via IPC API                              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-15059                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2013-4392       │ LOW      │              │                                   │               │ systemd: TOCTOU race condition when updating file            │
│                    │                     │          │              │                                   │               │ permissions and SELinux security contexts...                 │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2023-31437      │          │              │                                   │               │ An issue was discovered in systemd 253. An attacker can      │
│                    │                     │          │              │                                   │               │ modify a...                                                  │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2023-31438      │          │              │                                   │               │ An issue was discovered in systemd 253. An attacker can      │
│                    │                     │          │              │                                   │               │ truncate a...                                                │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2023-31439      │          │              │                                   │               │ An issue was discovered in systemd 253. An attacker can      │
│                    │                     │          │              │                                   │               │ modify the...                                                │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-40228      │          │              │                                   │               │ systemd: systemd-journald: Unintended output to user         │
│                    │                     │          │              │                                   │               │ terminals via logger command                                 │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-40228                   │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libuuid1           │ CVE-2026-76642      │ HIGH     │              │ 2.41.5-0+deb13u1                  │               │ util-linux: util-linux: failed external mount helper still   │
│                    │                     │          │              │                                   │               │ runs privileged X-mount post-hooks                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78408      │          │              │                                   │               │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
│                    │                     │          │              │                                   │               │ cgroup migration authority                                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78409      │          │              │                                   │               │ util-linux: util-linux: X-mount.subdir detached-tree         │
│                    │                     │          │              │                                   │               │ resolution can escape via intermediate symlinks              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78410      │          │              │                                   │               │ util-linux: util-linux: restricted bind mounts do not pin    │
│                    │                     │          │              │                                   │               │ the source, allowing X-mount.owner/group/mode...             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-3184       │ MEDIUM   │              │                                   │               │ util-linux: util-linux: Access control bypass due to         │
│                    │                     │          │              │                                   │               │ improper hostname canonicalization                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-3184                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2022-0563       │ LOW      │              │                                   │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                    │                     │          │              │                                   │               │ and chsh when compiled...                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ login              │ CVE-2026-76642      │ HIGH     │              │ 1:4.16.0-2+really2.41.5-0+deb13u1 │               │ util-linux: util-linux: failed external mount helper still   │
│                    │                     │          │              │                                   │               │ runs privileged X-mount post-hooks                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78408      │          │              │                                   │               │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
│                    │                     │          │              │                                   │               │ cgroup migration authority                                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78409      │          │              │                                   │               │ util-linux: util-linux: X-mount.subdir detached-tree         │
│                    │                     │          │              │                                   │               │ resolution can escape via intermediate symlinks              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78410      │          │              │                                   │               │ util-linux: util-linux: restricted bind mounts do not pin    │
│                    │                     │          │              │                                   │               │ the source, allowing X-mount.owner/group/mode...             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-3184       │ MEDIUM   │              │                                   │               │ util-linux: util-linux: Access control bypass due to         │
│                    │                     │          │              │                                   │               │ improper hostname canonicalization                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-3184                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2022-0563       │ LOW      │              │                                   │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                    │                     │          │              │                                   │               │ and chsh when compiled...                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────────┼─────────────────────┤          │              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ login.defs         │ CVE-2007-5686       │          │              │ 1:4.17.4-2                        │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                    │                     │          │              │                                   │               │ the /var/lo ......                                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-56433      │          │              │                                   │               │ shadow-utils: Default subordinate ID configuration in        │
│                    │                     │          │              │                                   │               │ /etc/login.defs could lead to compromise                     │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ TEMP-0628843-DBAD28 │          │              │                                   │               │ [more related to CVE-2005-4890]                              │
│                    │                     │          │              │                                   │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                    │                     │          │              │                                   │               │ AD28                                                         │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ mount              │ CVE-2026-76642      │ HIGH     │              │ 2.41.5-0+deb13u1                  │               │ util-linux: util-linux: failed external mount helper still   │
│                    │                     │          │              │                                   │               │ runs privileged X-mount post-hooks                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78408      │          │              │                                   │               │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
│                    │                     │          │              │                                   │               │ cgroup migration authority                                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78409      │          │              │                                   │               │ util-linux: util-linux: X-mount.subdir detached-tree         │
│                    │                     │          │              │                                   │               │ resolution can escape via intermediate symlinks              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78410      │          │              │                                   │               │ util-linux: util-linux: restricted bind mounts do not pin    │
│                    │                     │          │              │                                   │               │ the source, allowing X-mount.owner/group/mode...             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-3184       │ MEDIUM   │              │                                   │               │ util-linux: util-linux: Access control bypass due to         │
│                    │                     │          │              │                                   │               │ improper hostname canonicalization                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-3184                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2022-0563       │ LOW      │              │                                   │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                    │                     │          │              │                                   │               │ and chsh when compiled...                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-base       │ CVE-2025-69720      │ HIGH     │              │ 6.5+20250216-2                    │               │ ncurses: ncurses: Buffer overflow vulnerability may lead to  │
│                    │                     │          │              │                                   │               │ arbitrary code execution.                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2025-69720                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2025-6141       │ LOW      │              │                                   │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├────────────────────┼─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-bin        │ CVE-2025-69720      │ HIGH     │              │                                   │               │ ncurses: ncurses: Buffer overflow vulnerability may lead to  │
│                    │                     │          │              │                                   │               │ arbitrary code execution.                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2025-69720                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2025-6141       │ LOW      │              │                                   │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├────────────────────┼─────────────────────┤          │              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ passwd             │ CVE-2007-5686       │          │              │ 1:4.17.4-2                        │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                    │                     │          │              │                                   │               │ the /var/lo ......                                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2024-56433      │          │              │                                   │               │ shadow-utils: Default subordinate ID configuration in        │
│                    │                     │          │              │                                   │               │ /etc/login.defs could lead to compromise                     │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ TEMP-0628843-DBAD28 │          │              │                                   │               │ [more related to CVE-2005-4890]                              │
│                    │                     │          │              │                                   │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                    │                     │          │              │                                   │               │ AD28                                                         │
├────────────────────┼─────────────────────┼──────────┼──────────────┼───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ perl-base          │ CVE-2026-9538       │ HIGH     │ fix_deferred │ 5.40.1-6+deb13u1                  │               │ perl-Archive-Tar: perl-Archive-Tar: Denial of Service via    │
│                    │                     │          │              │                                   │               │ crafted tar header with large entry...                       │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-9538                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-15534      │ MEDIUM   │              │                                   │               │ perl: Perl: Arbitrary code execution via out-of-bounds       │
│                    │                     │          │              │                                   │               │ memory access in regular expression...                       │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-15534                   │
│                    ├─────────────────────┤          ├──────────────┤                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-19487      │          │ affected     │                                   │               │ perl: Perl: Incorrect regular expression matching can lead   │
│                    │                     │          │              │                                   │               │ to wrong access or...                                        │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-19487                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2011-4116       │ LOW      │              │                                   │               │ perl: File:: Temp insecure temporary file handling           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2011-4116                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-82560      │ UNKNOWN  │              │                                   │               │ Pod::Text versions before 6.1.1 for Perl allow CPU and       │
│                    │                     │          │              │                                   │               │ memory exhausti ......                                       │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-82560                   │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sysvinit-utils     │ TEMP-0517018-A83CE6 │ LOW      │              │ 3.14-4                            │               │ [sysvinit: no-root option in expert installer exposes        │
│                    │                     │          │              │                                   │               │ locally exploitable security flaw]                           │
│                    │                     │          │              │                                   │               │ https://security-tracker.debian.org/tracker/TEMP-0517018-A8- │
│                    │                     │          │              │                                   │               │ 3CE6                                                         │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ tar                │ CVE-2026-18477      │ MEDIUM   │              │ 1.35+dfsg-3.1                     │               │ tar: tar: TOCTOU in incremental dumpdir 'X' rename handling  │
│                    │                     │          │              │                                   │               │ allows restore path...                                       │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-18477                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-18508      │          │              │                                   │               │ tar: tar: --one-top-level hardlink targets not confined to   │
│                    │                     │          │              │                                   │               │ top-level directory enabling arbitrary...                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-18508                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-5704       │          │              │                                   │               │ tar: tar: Hidden file injection via crafted archives         │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-5704                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2005-2541       │ LOW      │              │                                   │               │ tar: does not properly warn the user when extracting setuid  │
│                    │                     │          │              │                                   │               │ or setgid...                                                 │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2005-2541                    │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ TEMP-0290435-0B57B5 │          │              │                                   │               │ [tar's rmt command may have undesired side effects]          │
│                    │                     │          │              │                                   │               │ https://security-tracker.debian.org/tracker/TEMP-0290435-0B- │
│                    │                     │          │              │                                   │               │ 57B5                                                         │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux         │ CVE-2026-76642      │ HIGH     │              │ 2.41.5-0+deb13u1                  │               │ util-linux: util-linux: failed external mount helper still   │
│                    │                     │          │              │                                   │               │ runs privileged X-mount post-hooks                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-76642                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78408      │          │              │                                   │               │ util-linux: util-linux: nsenter --join-cgroup leaks root     │
│                    │                     │          │              │                                   │               │ cgroup migration authority                                   │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78408                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78409      │          │              │                                   │               │ util-linux: util-linux: X-mount.subdir detached-tree         │
│                    │                     │          │              │                                   │               │ resolution can escape via intermediate symlinks              │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78409                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-78410      │          │              │                                   │               │ util-linux: util-linux: restricted bind mounts do not pin    │
│                    │                     │          │              │                                   │               │ the source, allowing X-mount.owner/group/mode...             │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-78410                   │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-3184       │ MEDIUM   │              │                                   │               │ util-linux: util-linux: Access control bypass due to         │
│                    │                     │          │              │                                   │               │ improper hostname canonicalization                           │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-3184                    │
│                    ├─────────────────────┼──────────┤              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2022-0563       │ LOW      │              │                                   │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                    │                     │          │              │                                   │               │ and chsh when compiled...                                    │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────────┼─────────────────────┼──────────┤              ├───────────────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ zlib1g             │ CVE-2026-27171      │ MEDIUM   │              │ 1:1.3.dfsg+really1.3.1-1+b1       │               │ zlib: zlib: Denial of Service via infinite loop in CRC32     │
│                    │                     │          │              │                                   │               │ combine functions...                                         │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-27171                   │
│                    ├─────────────────────┤          │              │                                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                    │ CVE-2026-85091      │          │              │                                   │               │ zlib versions 1.3.1.2 through 1.3.2 contain a heap buffer    │
│                    │                     │          │              │                                   │               │ overflow vul ......                                          │
│                    │                     │          │              │                                   │               │ https://avd.aquasec.com/nvd/cve-2026-85091                   │
└────────────────────┴─────────────────────┴──────────┴──────────────┴───────────────────────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

Python (python-pkg)

Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 1, HIGH: 2, CRITICAL: 0)

┌────────────┬─────────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────┐
│  Library   │    Vulnerability    │ Severity │ Status │ Installed Version │ Fixed Version │                          Title                          │
├────────────┼─────────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────┤
│ msgpack    │ GHSA-6v7p-g79w-8964 │ HIGH     │ fixed  │ 1.1.2             │ 1.2.1         │ MessagePack for Python: Out-of-bounds read / crash on   │
│            │                     │          │        │                   │               │ Unpacker reuse after a...                               │
│            │                     │          │        │                   │               │ https://github.com/advisories/GHSA-6v7p-g79w-8964       │
├────────────┼─────────────────────┤          │        ├───────────────────┼───────────────┼─────────────────────────────────────────────────────────┤
│ setuptools │ CVE-2025-47273      │          │        │ 70.3.0            │ 78.1.1        │ setuptools: Path Traversal Vulnerability in setuptools  │
│            │                     │          │        │                   │               │ PackageIndex                                            │
│            │                     │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2025-47273              │
│            ├─────────────────────┼──────────┤        │                   ├───────────────┼─────────────────────────────────────────────────────────┤
│            │ CVE-2026-59890      │ MEDIUM   │        │                   │ 83.0.0        │ setuptools: setuptools: MANIFEST.in exclusion bypass in │
│            │                     │          │        │                   │               │ sdist via Unicode normalization collision (NFC/NFD)...  │
│            │                     │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-59890              │




Décisions du Dockerfile
-----------------------
+ FROM python:3.13-slim car cela allège l'image
+ COPY requirements.txt cela permet de stocker la version de python
+ RUN pip install --no-cache-dir ... permet de ne pas garder le cache ce qui allège l'image
+ RUN useradd -u 10001 christopher création d'un utilisateur avec un uid
+ COPY --from=builder /install récupération des paquets installés dans le premier stage de l'image


Résultats multi-étapes
----------------------
devops-info-service   lab02         197MB   (une seule étape)
devops-info-service   lab02-multi   183MB   (multi-étapes)

l'image multi-étapes est légèrement moins lourde que la mono-étape mais à part ça le changement n'est pas si grand que ça


Analyse Trivy
-------------
Total: 2 (HIGH: 2, CRITICAL: 0)

┌────────────┬─────────────────────┬──────────┬────────┬───────────────────┬───────────────┬────────────────────────────────────────────────────────┐
│  Library   │    Vulnerability    │ Severity │ Status │ Installed Version │ Fixed Version │                       Title                          │
├────────────┼─────────────────────┼──────────┼────────┼───────────────────┼───────────────┼────────────────────────────────────────────────────────┤
│ msgpack    │ GHSA-6v7p-g79w-8964 │ HIGH     │ fixed  │ 1.1.2             │ 1.2.1         │ MessagePack for Python: Out-of-bounds read / crash on  │
│            │                     │          │        │                   │               │ Unpacker reuse after a...                              │
│            │                     │          │        │                   │               │ https://github.com/advisories/GHSA-6v7p-g79w-8964      │
├────────────┼─────────────────────┤          │        ├───────────────────┼───────────────┼────────────────────────────────────────────────────────┤
│ setuptools │ CVE-2025-47273      │          │        │ 70.3.0            │ 78.1.1        │ setuptools: Path Traversal Vulnerability in setuptools │
│            │                     │          │        │                   │               │ PackageIndex                                           │
│            │                     │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2025-47273             │
└────────────┴─────────────────────┴──────────┴────────┴───────────────────┴───────────────┴────────────────────────────────────────────────────────┘

chris@Christok-PC:~/projects/DevOps-Core-Course/app_python$   echo $?
1



Preuve de travail
-----------------
1. docker pull
--------------
chris@Christok-PC:~/projects/DevOps-Core-Course/app_python$ docker logout ghcr.io
Removing login credentials for ghcr.io
chris@Christok-PC:~/projects/DevOps-Core-Course/app_python$ docker rmi ghcr.io/christ-ok/devops-info-service:1.0.0
Untagged: ghcr.io/christ-ok/devops-info-service:1.0.0
Deleted: sha256:76785edad9923f2cd83008d31b83f603204d31cc19d3f0ad2d75506ce3a28b0e
chris@Christok-PC:~/projects/DevOps-Core-Course/app_python$ docker pull ghcr.io/christ-ok/devops-info-service:1.0.0
1.0.0: Pulling from christ-ok/devops-info-service
b19aec290dba: Pull complete 
bc42dcc70ffa: Pull complete 
ebde01002665: Pull complete 
6ff4043a00f7: Pull complete 
Digest: sha256:76785edad9923f2cd83008d31b83f603204d31cc19d3f0ad2d75506ce3a28b0e
Status: Downloaded newer image for ghcr.io/christ-ok/devops-info-service:1.0.0
ghcr.io/christ-ok/devops-info-service:1.0.0



2. docker push
--------------
chris@Christok-PC:~/projects/DevOps-Core-Course/app_python$ echo -n "$GHCR_PAT" | wc -c
40
chris@Christok-PC:~/projects/DevOps-Core-Course/app_python$ echo "$GHCR_PAT" | docker login ghcr.io -u Christ-ok --password-stdin
Login Succeeded
chris@Christok-PC:~/projects/DevOps-Core-Course/app_python$ docker push ghcr.io/christ-ok/devops-info-service:1.0.0
The push refers to repository [ghcr.io/christ-ok/devops-info-service]
b19aec290dba: Layer already exists 
264ba3d8ae19: Layer already exists 
bc42dcc70ffa: Layer already exists 
6ff4043a00f7: Layer already exists 
ebde01002665: Layer already exists 
6b37362b3da7: Layer already exists 
4a43a40b039e: Layer already exists 
3d9fb7471420: Layer already exists 
1.0.0: digest: sha256:5c2b1fbe53a204e771ba3f1f0fe071afba3188cb3d40308cc6768329fe5af7fb size: 1812

i Info → Not all multiplatform-content is present and only the available single-platform image was pushed
         sha256:76785edad9923f2cd83008d31b83f603204d31cc19d3f0ad2d75506ce3a28b0e -> sha256:5c2b1fbe53a204e771ba3f1f0fe071afba3188cb3d40308cc6768329fe5af7fb


3. URL du registre
------------------
- Paquet : https://github.com/users/Christ-ok/packages/container/package/devops-info-service
- Pull : `docker pull ghcr.io/christ-ok/devops-info-service:1.0.0`
