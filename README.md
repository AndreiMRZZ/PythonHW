Aplicatia este un microserviciu Python construit cu Flask care ofera calcule matematice precum factorial, fibonacci si pow.
Arhitectura respecta principiile OOP si este structurata pe module: routes (controller), services (logica de calcul), models (Pydantic), storage (SQLite) si utils (cache, auth, logging).
Codul este standardizat folosind .flake8.

Autentificarea API se face printr-un mecanism personalizat de tip authenticator cu secret key. Fiecare cerere catre endpoint-urile protejate necesita un token valid pentru acces. Pentru rezultate deja calculate anterior, se foloseste cache in-memory, evitand recalcularea si imbunatatind performanta.

Datele sunt validate cu Pydantic, logurile sunt centralizate si cererile pot fi salvate in baza de date. Operatiile costisitoare pot fi procesate asincron prin cozi si de asemenea si event log urile sunt trimise prin rabbit mq. Aplicatia este containerizata complet cu Docker, iar docker-compose.yml permite rularea serviciului si a dependintelor. Endpoint-urile disponibile sunt /factorial, /fibonacci, /pow, /history si /health.
