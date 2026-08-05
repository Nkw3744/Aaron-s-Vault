# Obsidian Links in Google Calendar: Feasibility Report

Investigated: 2026-07-22 (Pacific/Auckland)

## Executive conclusion

Google Calendar can **store** an Obsidian URI in an event description, but the available authoritative documentation does not guarantee that Calendar will preserve and expose an `obsidian://` URI as a clickable link on Calendar web, Android, or iPhone. The Calendar API defines `description` as a writable string and says it can contain HTML, but it does not document which HTML, URI schemes, or links each Calendar client will render or permit [1].

Therefore:

- Use an `obsidian://open` URI only as a **best-effort secondary link**.
- Always include a normal `https://` link as the primary reliable action or fallback.
- Do not roll deep links into real university events until one disposable event has been tested on Calendar web, Aaron's Android device, and Aaron's iPhone.
- Keep the authoritative Canvas URL in every event regardless of the Obsidian result.

No Google Calendar event was created, edited, or deleted during this investigation. Canvas was not accessed or modified.

## What is documented

### Google Calendar description storage

The Google Calendar API's Event resource defines `description` as a writable string: “Description of the event. Can contain HTML. Optional.” [1] This establishes that the event resource can carry the text or HTML representation of a link. It does **not** establish that every Google Calendar client will render every URI scheme as an active hyperlink. Google does not document a cross-client guarantee for custom schemes such as `obsidian:`.

An important distinction is therefore:

1. **Stored:** the URI survives in the event's description value.
2. **Rendered:** the client displays it as a hyperlink.
3. **Routed:** tapping it is handed to Obsidian by the operating system.
4. **Resolved:** Obsidian finds the intended vault and note.

Success at one stage does not prove the next.

### Obsidian URI syntax

Obsidian officially supports a custom URI protocol for opening notes and other actions [2]. Its documented form is:

```text
obsidian://action?param1=value&param2=value
```

For opening a note, Obsidian documents:

```text
obsidian://open?vault=my%20vault&file=my%20note
```

The `vault` value may be a vault name or vault ID. The `file` value may be a filename or a path from the vault root; the `.md` extension is optional [2].

Obsidian explicitly requires URI encoding and gives `/` → `%2F` and space → `%20` as examples [2]. For Aaron's vault, the apostrophe should also be encoded:

```text
Aaron's Vault  ->  Aaron%27s%20Vault
```

A verified concrete example is:

```text
obsidian://open?vault=Aaron%27s%20Vault&file=Mechatronics%20Engineering.md
```

A path example is:

```text
obsidian://open?vault=Aaron%27s%20Vault&file=Mechatronics%20Course%20Content%2FExample%20Note.md
```

Generate each query value independently with percent-encoding (equivalent to Python `urllib.parse.quote(value, safe="")`). Do not encode the structural `?`, `&`, or `=` separators. Encoding the slash in the note path is important because Obsidian explicitly calls this out.

### Mobile operating-system routing

Android documents deep linking as a system capability: tapping a link can trigger an intent that Android attempts to route to an installed app whose intent filter matches the URI [3]. Android also warns that custom-scheme links are not standard web links and can be ambiguous if more than one app registers the same scheme; verified HTTPS App Links are the trusted option for domains an app controls [3].

Apple documents that tapping a custom URL can launch the app registered for that scheme and pass it the requested context [4]. Apple nevertheless strongly recommends universal links over custom URL schemes and notes that another app can register the same custom scheme; if multiple apps do so, the selected target is undefined [4].

These operating-system capabilities apply only after Calendar supplies an actual tappable link. They do not force Calendar to recognize `obsidian://` text as a link.

## Expected behavior by client

The following is a bounded assessment, not a substitute for the device test below.

| Client | What can be concluded | Remaining uncertainty |
|---|---|---|
| Calendar web | The event can store a description containing the URI [1]. A browser can hand a genuine custom-scheme hyperlink to a registered desktop app, commonly with an external-application prompt. | Google does not promise that Calendar web auto-links raw `obsidian://` text or preserves an HTML `<a href="obsidian://…">` anchor after sanitization. It may remain plain text, be stripped, or be blocked. |
| Google Calendar on Android | If Calendar exposes a tappable `obsidian://` link, Android can route it to an installed matching app [3]. | Calendar's own linkification/sanitization behavior is undocumented. Obsidian must be installed and the expected vault/note must exist locally. A chooser or failure is possible if handlers conflict or none exists. |
| Google Calendar on iPhone | If Calendar exposes a tappable custom-scheme link, iOS can launch the registered app and pass the URL [4]. | Calendar's rendering policy is undocumented. Obsidian must be installed and contain the expected vault/note. iOS may show a confirmation, and duplicate scheme registrations are not uniquely bound [4]. |

Practical verdict: **feasible as an enhancement, not dependable enough as the only link.**

## Vault and note portability

Use `vault=Aaron%27s%20Vault` only on devices where Obsidian recognizes a vault with exactly that name. The filesystem location does not need to be identical when the URI uses `vault` plus a vault-relative `file`, but the vault contents and relative note path do need to be present on that device.

The name is more human-auditable than a local vault ID and is the better first cross-device test. A vault ID may be useful only after confirming that the same identifier is valid across Aaron's installations; this should not be assumed.

Prefer the `vault` + `file` form over `path=`. An absolute Linux path such as `/home/aaron/...` cannot be portable to Android or iPhone.

Use only the non-mutating `open` action. Avoid `new`, `append`, `prepend`, `overwrite`, or links containing note content in calendar descriptions. Custom schemes are externally invokable, and both Apple and Android document ambiguity/security considerations around scheme handlers [3][4].

## Recommended HTTPS fallback

### Preferred pattern

Place a normal HTTPS link first, because HTTPS is the most consistently recognized link type across Calendar clients and always has a browser fallback. Recommended order:

1. Authoritative Canvas URL.
2. Stable HTTPS note launcher/landing page.
3. Raw Obsidian URI as a best-effort shortcut.

The best purpose-built fallback is a stable HTTPS landing URL under a domain Aaron controls. It should:

- map an opaque, allow-listed note key to a known vault-relative note path;
- show the course, note title, and Canvas URL;
- provide an explicit **Open in Obsidian** button using the encoded `obsidian://open` URI;
- explain how to find the note manually if Obsidian is unavailable;
- avoid automatically firing a custom URI on page load;
- contain no secrets, access tokens, private absolute filesystem paths, or write-capable Obsidian actions.

This does not make custom-scheme routing universal, but it guarantees that tapping the Calendar link opens a useful HTTPS page. Apple recommends universal links for trusted website-to-app routing [4], and Android recommends verified App Links for the equivalent trusted behavior [3]. A future dedicated launcher app could adopt those mechanisms; an ordinary landing page remains useful without one.

### Simpler fallbacks

- **Canvas URL:** mandatory and authoritative; useful even when Obsidian is unavailable.
- **Google Drive URL:** acceptable when it points to a safely shareable companion resource, but it does not inherently open the local Obsidian note and may create a second source of truth.
- **Obsidian Publish URL:** technically strong as HTTPS if the note is intentionally published, but unsuitable for private university notes unless privacy and access controls are explicitly reviewed.

Do not use `file://` links: they are neither portable nor reliably allowed from web/mobile Calendar clients.

## Proposed event-description template

Plain-text URLs are recommended so the Calendar API value remains auditable and every client has the same underlying data.

```text
Preparation
- <one or two grounded preparation actions>

Canvas (authoritative)
https://canvas.aut.ac.nz/<stable-course-or-item-path>

Course notes (reliable web fallback)
https://<controlled-domain>/o/<opaque-note-key>

Open directly in Obsidian (best effort; requires Obsidian and "Aaron's Vault" on this device)
obsidian://open?vault=Aaron%27s%20Vault&file=<fully-percent-encoded-vault-relative-note-path>

Source ID: Canvas <event-or-assignment-id>
```

Example deep-link line for an existing root note:

```text
obsidian://open?vault=Aaron%27s%20Vault&file=Mechatronics%20Engineering.md
```

If a future test shows the raw URI is not clickable on one or more clients, keep it for copyability only if that remains useful; otherwise omit it from production descriptions and put the **Open in Obsidian** button solely on the HTTPS landing page.

## Recommended disposable-event test procedure

This procedure is for a future explicitly approved test. It was **not** performed during this read-only investigation.

1. **Prepare a harmless target note.** Use an existing non-sensitive note or create a clearly disposable `Calendar Link Test.md` in `Aaron's Vault`. Confirm the same vault name and vault-relative path in Obsidian on desktop, Android, and iPhone.
2. **Verify the URI outside Calendar first.** On each device, enter or tap the exact encoded `obsidian://open` URI from a context known to permit links. Confirm that Obsidian opens the correct note both when already running and when cold-started. This isolates Obsidian/OS routing from Calendar rendering.
3. **Create exactly one disposable event in a test calendar.** Do this manually or only after explicit approval. Put four clearly labeled controls in its description:
   - a normal Canvas or harmless HTTPS URL;
   - the proposed HTTPS landing URL;
   - the raw `obsidian://open` URI;
   - if the Calendar editor permits it, display text linked to the same Obsidian URI.
4. **Read back without editing.** Use Calendar's event view and, if authorized, `events.get` to record the exact stored `description`. Compare whether raw text or HTML was altered. Do not infer storage from appearance alone.
5. **Test Calendar web.** Reopen the saved event in a supported browser. Record: visible text, clickable/not clickable, external-app prompt, Obsidian launch, and correct-note resolution.
6. **Test Android Google Calendar.** Sync and open the same event. Record the same observations, including any app chooser or “no app can open” result.
7. **Test iPhone Google Calendar.** Sync and open the same event. Record the same observations, including any confirmation prompt.
8. **Test failure modes.** On one device, test with Obsidian closed. If practical, temporarily use a URI with a deliberately nonexistent harmless note path to confirm the failure is understandable. Do not use write-capable actions.
9. **Retest after editing nowhere.** Reopen the event on all clients after sync to rule out a transient local rendering artifact.
10. **Clean up only with approval.** Delete the disposable event and test note only after recording results and obtaining authorization for those deletions.

Suggested result table:

| Client/version | Raw URI clickable | Labelled URI clickable | OS prompt/chooser | Correct note opens | HTTPS fallback works | Notes |
|---|---:|---:|---|---:|---:|---|
| Calendar web + browser |  |  |  |  |  |  |
| Google Calendar Android |  |  |  |  |  |  |
| Google Calendar iPhone |  |  |  |  |  |  |

### Adoption gate

- If all target clients open the correct note, include the direct URI plus HTTPS fallback.
- If only some clients do, label the direct URI “best effort” and keep HTTPS first.
- If Calendar strips or disables the custom URI everywhere, use only HTTPS in Calendar; place the Obsidian button on the landing page.
- Never remove the Canvas source URL.

## Sources

1. Google Calendar API, Events resource — `description` is a writable string that can contain HTML: https://developers.google.com/workspace/calendar/api/v3/reference/events
2. Obsidian Help, “Obsidian URI” — URI format, `open`, vault/file parameters, and required percent-encoding: https://help.obsidian.md/Extending+Obsidian/Obsidian+URI
3. Android Developers, “Create deep links” — intent routing, custom-scheme limitations, and recommendation for verified App Links: https://developer.android.com/training/app-links/create-deeplinks
4. Apple Developer Documentation, “Defining a custom URL scheme for your app” — app launching, scheme registration ambiguity/security, and recommendation for universal links: https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app

All sources were accessed on 2026-07-22. The conclusions about Google Calendar client rendering are deliberately conservative because no authoritative Google document found promises that `obsidian://` is clickable across Calendar web, Android, and iPhone, and the requested no-write constraint prevented creation of a disposable event for empirical confirmation.
