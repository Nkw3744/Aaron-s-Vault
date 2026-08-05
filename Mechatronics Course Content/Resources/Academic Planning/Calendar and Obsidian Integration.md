# Calendar and Obsidian Integration

Return to [[Mechatronics Course Content/Resources/Academic Planning/Academic Planning|Academic Planning]].

## Purpose

This project will make Google Calendar a practical launch point for each class and assessment. Calendar entries should combine authoritative AUT/Canvas timing with a concise preparation summary and quick links to the relevant Canvas source and Obsidian course note.

## Planned improvements

### Canvas Calendar review

The next authenticated Canvas review should inspect the Canvas Calendar as well as Assignments, Pages, Files, Modules, and Announcements. It should capture event descriptions, assessment dates, availability windows, course context, locations, and Canvas URLs, then compare them with the existing incremental ledger before proposing Google Calendar updates.

### Obsidian links in Calendar

A separate investigation will test whether Google Calendar descriptions can reliably open links such as:

`obsidian://open?vault=Aaron%27s%20Vault&file=<URL-encoded-note-path>`

Testing needs to cover Google Calendar on the web, Android, and iPhone. If custom Obsidian links are not clickable on a platform, each event should retain a reliable Canvas or Google Drive link as a fallback.

## Safety

- Canvas remains read-only.
- Calendar changes must be previewed before bulk creation or updates.
- A disposable test event should be used before changing real class entries.
- Stable Canvas IDs and Google Calendar event IDs should be recorded to prevent duplicates.

## Project brief

The implementation brief is stored on Tornado at `/home/aaron/projects/obsidian-calendar-links/BRIEF.md`.

## Feasibility result — 22 July 2026

The read-only investigation is complete: [[Mechatronics Course Content/Resources/Academic Planning/Obsidian Links in Google Calendar - Feasibility|Obsidian Links in Google Calendar — Feasibility Report]].

Google Calendar can store an `obsidian://` URI in an event description, but Google does not guarantee that its web, Android, and iPhone clients will all expose custom URI schemes as clickable links. The recommended production structure is therefore:

1. Keep the authoritative Canvas HTTPS URL in every event.
2. Put a reliable HTTPS note launcher or landing page next.
3. Include the direct `obsidian://open` URI only as a labelled, best-effort shortcut.
4. Test exactly one disposable event across Calendar web, Aaron's Android device, and Aaron's iPhone before using the structure for real university events.

For this vault, the encoded vault name is `Aaron%27s%20Vault`. Each vault-relative note path must be percent-encoded independently, including spaces, apostrophes, and `/` characters.

No Calendar or Canvas records were changed during the investigation.

## iPhone pilot result — 22 July 2026

The approved disposable Calendar event established the following on Aaron's iPhone:

- The Canvas HTTPS control was clickable and opened the main Canvas dashboard, as expected because the pilot deliberately used the harmless root URL `https://canvas.aut.ac.nz/`. Production events use course-, week-, or assignment-specific Canvas URLs.
- The first `obsidian://open` URI successfully launched Obsidian but targeted an Academic Planning note that was not present in the iPhone's current vault copy.
- The event was updated to target [[Thermodynamic Systems and Basic Concepts]], a Week 1 ENME601 note known to be available on the iPhone. That link opened the correct note successfully.

Conclusion: direct Obsidian links work from Google Calendar on Aaron's iPhone when the target exists at the same vault-relative path. Production entries should contain a concise overview of the session, a specific Canvas HTTPS link, and a direct Obsidian link to the relevant note or resource. They should not copy full study notes into Calendar.

## Production rollout — 22 July 2026

Using only the Canvas-derived information already stored on Tornado—without opening or accessing Canvas—the approved rollout:

- updated 135 AUT lecture, tutorial, and lab event instances;
- created eight assessment events: five exact live-assignment timestamps and three clearly labelled provisional overview dates;
- added concise descriptions of what each session covers, what to attempt or bring where known, specific Canvas links, and verified Obsidian links;
- used conservative course-level wording for unsupported later recurrences rather than inventing topics;
- recorded stable managed source IDs for repeat-safe updates.

Independent Google Calendar readback verified all 135 class descriptions and all eight assessment events. No personal-event description changed, and every managed event contains both Canvas and Obsidian links.

Future revisions may use newer Canvas information only during a session for which Aaron explicitly authorizes Canvas access. Canvas must never be opened or refreshed automatically.
