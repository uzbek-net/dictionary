---
name: 💡 Feature Request / Improvement
about: Suggest an idea, enhancement, or new feature for the dictionary structure, tooling, or process.
title: "[Feature]: <Brief summary of the feature>"
labels: enhancement, planning
assignees: ''

---

### What is the Feature or Improvement?

Provide a clear and concise explanation of the requested feature or improvement.

*Example: "Add a new mandatory field, `example_sentence_en`, to hold an English usage example for every term."*

---

### Why is this needed? (Problem Statement)

Describe the problem or limitation you are currently facing that this feature would solve.

*Example: "Translators often struggle to understand the exact context of a new term, leading to inaccurate translations. Having an example sentence would drastically reduce translation errors."*

---

### Proposed Solution

Describe exactly how you envision this feature working.

* **If it's a data structure change (e.g., adding a new field):** How should the new field be named, and what kind of data should it contain?
* **If it's a tooling change (e.g., a script):** What should the tool do, and what should the output be?
* **If it's a process change:** What steps should be added or removed from the current workflow?

---

### Examples (Optional)

If possible, provide a quick example of the proposed feature in action or how a TOML entry might look with the change.

```toml
# Example of a new field:
[[translations]]
# ... other fields
example_sentence_en = "The system ensures the function is **idempotent** by checking the transaction ID."