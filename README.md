# TP Jenkins + SonarQube

Projet Python de demonstration pour le TP d'integration de SonarQube dans Jenkins.

## Contenu
- `app.py`, `test_app.py` : code et tests (version saine)
- `Jenkinsfile` : pipeline (tests + couverture, analyse Sonar, Quality Gate)
- `sonar-project.properties` : configuration du scanner
- `infra/docker-compose.yml` : SonarQube + PostgreSQL
- `scenarios/` : fichiers pour les tests T2 (code defectueux) et T4 (correction)

## Prerequis dans Jenkins
- Plugin "SonarQube Scanner"
- Serveur SonarQube nomme `SonarQube`
- Outil SonarQube Scanner nomme `SonarScanner`
- Webhook SonarQube -> http://IP_VM:8080/sonarqube-webhook/

## Lancer SonarQube
    sudo sysctl -w vm.max_map_count=524288
    cd infra && docker compose up -d

## Scenarios
T2 (echec attendu du Quality Gate) :
    cp scenarios/T2_app_defectueux.py.txt app.py
    git add . && git commit -m "T2 code defectueux" && git push

T4 (retour au vert) :
    cp scenarios/T4_app_corrige.py.txt app.py
    cp scenarios/T4_test_app_corrige.py.txt test_app.py
    git add . && git commit -m "T4 correction" && git push

Retour a la version saine initiale : `git revert` du dernier commit ou
`git checkout <premier_commit> -- app.py test_app.py`.
