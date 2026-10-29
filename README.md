# PMOS-prediksjon
   En enkel nettside som gir en veiledende vurdering på om du bør kontakte lege på grunn av symptomer som kan tyde på PMOS (polyendokrint metabolsk ovarialsyndrom) . Brukeren svarer på noen spørsmål og får et trafikklys: 
   
   **Grønt**
      Lite som tyder på PMOS 
   **Gult**
      Usikkert, det kan være lurt å snakke med lege
   **Rødt**
      Svarene tyder på at du bør kontakte lege
   
   Svaret er en anbefaling, ikke medisinsk råd eller diagnose

## Prosjektstruktur
mitt-prosjekt/
├── .github/               # GitHub-spesifikke konfigurasjoner (CI/CD, maler)
├── dist/                  # Produksjonsklar kode (genereres automatisk)
├── node_modules/          # Eksterne avhengigheter/pakker
├── public/                # Statiske filer (bilder, ikoner, index.html)
│   ├── favicon.ico
│   └── robots.txt
├── src/                   # Hovedkildekoden til applikasjonen
│   ├── assets/            # Bilder, fonter og globale stiler
│   ├── components/        # Gjenbrukbare UI-komponenter
│   ├── hooks/             # Egendefinerte React hooks (hvis relevant)
│   ├── services/          # API-kall og eksterne integrasjoner
│   ├── utils/             # Hjelpefunksjoner og verktøy
│   ├── App.js             # Hovedkomponent
│   └── index.js           # Inngangspunkt for applikasjonen
├── .gitignore             # Filer som skal ignoreres av Git
├── package.json           # Prosjektinformasjon og avhengigheter
└── README.md              # Denne filen



## Nettsiden
Nettsiden finner du på: https://github.com/K184903/pcos-prediksjon 

## Rapport
Rapporten finner du på docs/dat158oblig.docx

   
## Data
   Datasett er tatt fra: 
   Polycystic ovary syndrome (PCOS), Prasoon Kottarathil, Kaggle.
   Lenke: (https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos)
   Lisens: CC BY-NC-SA 4.0
   541 pasienter fra 10 sykehus i Kerala, India.
   
