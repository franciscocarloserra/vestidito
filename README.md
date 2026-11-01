# vestidito

A small three.js simulator for learning how to draft the base pattern of a sleeveless dress. Enter the model's measurements, adjust ease, flare and length, and see both the flat pattern (back and front, drafted in 8 steps with the formulas) and the dress in 3D on a dress form built from those measurements, with a simulated skirt drape and a fit heat map.

Live: https://franciscocarloserra.github.io/vestidito/

The UI is in Spanish or English depending on the browser language. It works on mobile.

Run locally:

    python3 serve.py        # http://localhost:7810

No build step. three.js loads from jsdelivr, so it needs internet. When served locally, browser errors are logged to `/tmp/vestidito-console.jsonl`.

Limitations: the bodice is a fixed surface (not simulated), the skirt is frictionless verlet cloth, there are no sleeves and no front bust dart. The pattern is a simplified base draft, meant for understanding how the measurements relate, not for cutting without checking.
