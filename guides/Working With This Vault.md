# Working With This Vault

This vault is built for AI prompt crafting and operational runbooks. Use the guidelines below to keep contributions consistent and easy to navigate.

## Quick Start Checklist
1. Start new prompts or runbooks from the templates in `Templates/` to match the expected style and front matter.
2. Cross-link related material with `[[double bracket]]` links so Obsidian builds backlinks automatically.
3. Tag each note with `#prompt`, `#runbook`, and domain tags (for example `#incident-response`) to power Dataview queries and search.
4. Capture references, research, or snippets in `Resources/` and link them back to the primary prompt or runbook.
5. Automate new note creation with `Scripts/new_note.sh` when you need a fresh scaffold quickly.

## Organize And Maintain
- Keep folders aligned with their purpose (`Prompts/`, `Runbooks/`, `Guides/`, `[[double bracket]]`00) so related content stays grouped in the file browser.
- Use the metadata blocks provided in the templates; they are already tuned for Dataview and dashboards.
- When you retire or supersede a prompt, update backlinks so dependent notes point at the latest version.

## Automation
- Run `[[double bracket]]`11 to scaffold a note from the right template. Usage: `[[double bracket]]`22.
- The script fills in titles and timestamps, creates any missing folders, and saves the note where Obsidian will pick it up immediately.

## Recommended Obsidian Plugins
- Core: Templates, Daily Notes, Outgoing Links.
- Community: Dataview (dashboards), Templater (advanced templating), QuickAdd (fast capture), Commander (custom command palette).

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/

