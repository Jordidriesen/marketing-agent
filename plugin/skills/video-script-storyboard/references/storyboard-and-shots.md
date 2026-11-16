# Storyboard and shot list

## Storyboard entry

```markdown
### Scene [n]: [name] ([duration] s)
Shot: [type] | Framing: [subject position, headroom] | Camera: [static, push in, pan, handheld, screen capture]
On screen: [what appears; exact on-screen text]
Script: [the spoken line or A/V row number it carries]
Source: [real screen, photo, footage, generated concept, stand-in]
Transition out: [cut, match cut on ..., carry of ..., crossfade]
Frame: frames/scene-[nn].png
```

## Shot types

| Code | Shot | Use it for |
|---|---|---|
| WS | Wide | Setting the place, the desk, the site |
| MS | Medium (waist up) | Talking to camera, the default for face-on-camera |
| MCU | Medium close-up (chest up) | Emphasis, the hook, a Short |
| CU | Close-up | A product detail, a dial, a bottle, a hand on a control |
| ECU | Extreme close-up | Texture, a single number, a logo detail |
| OTS | Over the shoulder | Someone using a screen or a product |
| SC | Screen capture | Software in use; record at the output resolution or higher |
| BR | B-roll | Cutaways that cover edits and show what is being said |
| GFX | Graphic or motion | Built scenes (launch-video), titles, lower thirds |

Camera moves: keep one camera idea per video for built motion (see `launch-video`). For filmed work, static
by default; a move needs a reason.

## Shot list (filmed work)

Grouped by set-up, not by script order, so each set-up is lit and framed once.

```markdown
# Shot list: [title], shoot date [DD/MM/YYYY]

## Set-up A: [location, framing, lens or phone, light]
| Shot | Scenes | Content | Notes |
|---|---|---|---|
| A1 | 1, 4, 9 | MS talking to camera, sections 1 to 3 | Two takes of the hook |
| A2 | 1 | MCU of the hook line | For the Short |

## Set-up B: [product table, top light]
| B1 | 3 | CU bottle, slow rotate | 10 s clean at start and end |

## B-roll and pick-ups
- [cutaway list]

## Vertical cut
Scenes [n to n] become the Short: frame the subject centred with room above and below so a 9:16 crop works.

## Audio
Room tone 30 s per location. Microphone: [what]. Music: none on set.
```

## Safe areas

Platform interfaces cover parts of the frame and change often. Keep titles, faces and key UI inside a
central safe zone and check the platform's current specification before relying on a margin. For a
landscape video with a planned vertical cut, keep the subject in the centre third.
