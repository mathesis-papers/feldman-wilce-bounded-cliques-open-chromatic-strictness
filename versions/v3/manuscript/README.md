# A deleted-square answer to Feldman–Wilce's bounded-clique question

Haobo Ma — ChronoAI Pte Ltd, Singapore  
Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore

License: Creative Commons Attribution 4.0 International (CC BY 4.0).

## Mathematical contents

`note.tex` proves that `D(βℕ)=(βℕ)²∖Δ` has the bounded-clique property,
where relations are closed in the whole square, but its swap relation has
no countable open independent cover. It extends the conditional example of
Brandsma, van Hartskamp and van Mill (1997). It also gives an explicit higher
power that is not countably compact, with the earlier general-space existence
consequence of Ortiz-Castillo, Rodrigues and Tomita (2017/2018) credited
separately, and derives the sphere lower bound five from Holmsen–Lee's theorem.
The compactness mechanism is credited to Protasov–Pym–Strauss (2000),
with the compact F-space countable-power consequence given as a written deduction.

The exact posing locator is Feldman–Wilce, *A Note on Compactness and Clique
Size*, arXiv:2608.13320v1, Section 5, Question 2, printed page 11.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a TeX distribution with `amsmath`, `amssymb`, `amsthm`,
`geometry`, `microtype` and `hyperref`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is contained in `note.tex`; no BibTeX database or external
figure is required. `metadata.json` gives the author order, license, claim
identity and a pinned scientific source link. `SHA256SUMS` lists the source
package members and their hashes.

## Coverage of the mathematical evidence

The PDF's Verification scope section maps declarations in both pinned Lean
files to their statements. The countable-power compactness, bounded-clique
criterion and finite-open-cover obstruction are represented there. The
topological corollaries, uncountable chromatic bound, higher-power example
and sphere bound are written proofs. The sphere deduction uses the cited
Holmsen–Lee theorem, and the historical higher-power comparison uses the
cited hyperspace results.

`verify.py` uses Python 3's standard library and exact integer arithmetic:

```sh
python3 verify.py > verification.actual.json
cmp verification.actual.json verification.json
```

The computation checks swap graphs on ground sets of size 0 through 9,
and all directional membership-pattern pairs for 0 through 8 cover indices
(87,381 pairs in total). These finite graph identities are distinct from the
infinite topological theorems proved in the note. The script's JSON output
is the expected content of `verification.json`.
