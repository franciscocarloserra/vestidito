# vestidito
- `index.html`: todo (UI, maniquí, molde SVG, sim de falda). Constantes al principio del módulo.
- `serve.py`: estático + `POST /log` → `/tmp/vestidito-console.jsonl` (leerlo en vez de preguntar). Puerto 7810.
- Fuente única: `draft()` calcula el molde; `effW()` da el ancho efectivo (pinzas cerradas) por profundidad desde la nuca y alimenta tanto el SVG como el 3D.
- i18n: Spanish strings are the keys, `EN` dict + `tr()` translate when `navigator.language` isn't es. New UI text → add to `EN`.
- Body is a procedural dress form (torso shell + stand), no legs; skirt collides with the torso only.
- Deploy: GitHub Pages from `main` root (franciscocarloserra/vestidito). Telemetry only posts on localhost.
