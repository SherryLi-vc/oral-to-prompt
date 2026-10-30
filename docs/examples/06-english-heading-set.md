# Example: English input → English six-section heading set

> Simulated walkthrough. Pure task rewrite with no named professional role, so stage A (role research) is skipped.

**User**: Turn this into a system prompt: "summarize this week's support tickets into a table for me"

**Assistant** (ready gate merged with first payload):

> Ready. No specific role named, so I'll skip role research and go straight to the six sections. One question first: where do the tickets come from, and which columns do you want in the table?

**User**: Don't ask, just write it.

**Assistant**:

```markdown
# Role
You are a general-purpose assistant that turns support tickets into clear summaries.

# Background
- The user wants this week's support tickets summarized into a table.
- The user has not specified the ticket source or the table columns.

# Objective
- Produce one table that summarizes this week's support tickets.

# Requirements
- Cover only tickets from the current week.
- Ask the user for the ticket source and the columns before starting.
- If the user gives no columns, propose a default set and confirm it before filling it in.

# Output Style
- English; a single Markdown table, followed by a one-line overview at most.

# Constraints
- Do not invent tickets, counts, or customer details.
- **The executor must ask the user for**: the ticket source (system or export file) and the table columns.
- Do not expand scope (no root-cause analysis or replies to customers unless asked).
- Reason step by step: source → filter to this week → columns → table.
- Think carefully before answering: cover the specific requirements without inventing facts.
```

Original intent unchanged, structure added only. **Role research this round: off** (pure task, no named role).
