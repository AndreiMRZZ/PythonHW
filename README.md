Aplicatia este un microserviciu Python construit cu Flask care ofera calcule matematice precum factorial, fibonacci si pow.
Arhitectura(MVCS) respecta principiile OOP si este structurata pe module: routes (controller), services (logica de calcul), models (Pydantic), storage (SQLite) si utils (cache, auth, log).
Codul este standardizat folosind .flake8.

Accesarea unui API se face printr-un mecanism de tip authenticator cu secret key. Fiecare cerere catre endpoint-urile protejate necesita un token valid pentru acces. Pentru rezultate deja calculate anterior, se foloseste cache in-memory, evitand recalcularea si imbunatatind performanta.

Toate operatiile matematice folosesc o functie centralizata handle_response() care construieste raspunsul JSON, salveaza cererea ca RequestRecord si returneaza un raspuns unificat pentru toate operatiile, cu campuri optionale (y, extra) cand este nevoie.

Datele sunt validate cu Pydantic, logurile sunt centralizate si cererile pot fi salvate in baza de date. Operatiile costisitoare pot fi procesate asincron prin cozi si de asemenea si event log urile sunt trimise prin rabbit mq. Aplicatia este containerizata complet cu Docker, iar docker-compose.yml permite rularea serviciului si a dependintelor. Endpoint-urile disponibile sunt /factorial, /fibonacci, /pow, /history si /health.
