# Questions

Open questions that block or shape work. When answered: set status, write answer + date, and update linked feature/decision.

| ID | Question | Status | Affects | Answer |
|---|---|---|---|---|
| Q1 | Does the target repo get issues from external users, or only from maintainers? | answered | F03, F05, [D009](decisions/D009-triage-all-issues.md) | 2026-11-06: anyone can open an issue (external users too) |
| Q3 | The dx skills (e.g. `dx-bug-all`) take an ADO/Jira work item. How does a GitHub issue in dx-aem-flow become their input: add GitHub-issue support to the skills, a generic fix prompt for GitHub issues, or phase 3 only on ADO/Jira projects? | answered | F08, D015 | 2026-11-06: `dx-bug-all` was only an example. dx plugins are not used for phase 3 (adapting them to GitHub is too much work for now). Idea kept for later: the plugin fixing its own repo. |
| Q2 | SQLite or Postgres? | answered | [D007](decisions/D007-database.md) | 2026-11-06: SQLite, because of project scope |
