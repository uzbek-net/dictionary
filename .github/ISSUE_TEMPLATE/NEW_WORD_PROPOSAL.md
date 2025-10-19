---
name: ✨ New Word Proposal
about: Propose a new English technical term and its official Uzbek translation for the dictionary.
title: "[New Term]: <English Term>"
labels: enhancement, new-term, needs-translation
assignees: ''

---

### English Term Details

* **English Term:** (e.g., `idempotence`, `marshalling`)
* **Part of Speech (`part_of_speech`):** (e.g., `noun`, `verb`, `adjective`)
* **Context:** (Where is this term typically used? e.g., "API design," "Data serialization," "Database transactions.")

---

### Proposed Uzbek Translation and Definition

Provide the proposed translation and the full entry data using the TOML format.

* **Proposed Uzbek Translation (`uz`):** (e.g., `o'zgarmaslik`, `marshalizatsiya`)
* **Proposed Description (`description` - Uzbek):** A brief explanation of what the term means in Uzbek.
* **Proposed Pronunciation (`pronunciation_uz`):** (How should the Uzbek term be pronounced? e.g., `mar-sha-li-za-tsi-ya`)
* **Similar Terms (`similar`):** (List any similar or related English terms, e.g., `["concurrency", "mutability"]`)

### Proposed TOML Entry

Please fill out the fields below to create the initial entry:

```toml
[[translations]]
en = "<English Term>"
uz = "<Proposed Uzbek Translation>"
part_of_speech = "<Part of Speech>"
description = "<Proposed Description>"
pronunciation_uz = "<Proposed Pronunciation>"
similar = ["<Similar Term 1>", ""] # Add any similar terms
status = "Pending review" # Always start as 'Pending review'