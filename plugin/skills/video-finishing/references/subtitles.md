# Subtitles

## Getting a transcript, in order of preference

1. A transcript or caption file the user supplies (YouTube Studio lets the owner download captions).
2. Local speech recognition in the workspace or on the user's computer: `pip install faster-whisper`
   (or `openai-whisper`), run on an extracted audio track. Nothing leaves the machine. Say which model ran;
   small models make more errors on brand names and Dutch.
3. A hosted transcription service only with a yes for that specific service.

Extract audio for recognition: `ffmpeg -i input.mp4 -vn -ac 1 -ar 16000 audio.wav`.

## Cleaning the transcript

- Fix clear recognition errors, especially brand names, product names and locked terms from the brand kit.
- Keep the speaker's wording. Remove filler ("uh", "um") only when it carries no meaning.
- Mark anything you could not make out as `[inaudible]` and list it in the notes.

## SRT rules

- At most two lines per cue, about 42 characters per line.
- A cue stays on screen at least about 1 second and at most about 7 seconds.
- Break lines at natural phrase boundaries, never between an article and its noun.
- Timing follows the speech; no cue starts before the words are said.

## Burnt-in captions

Style from the brand kit: the body or display font, the text colour, and a background box or outline for
contrast. Captions sit inside the safe area: for 9:16, in the lower middle, clear of the bottom interface
overlay; check the platform's current overlay before relying on a margin.

```bash
ffmpeg -i input.mp4 -vf "subtitles=input.srt:force_style='FontName=<brand font>,FontSize=18,PrimaryColour=&H00FFFFFF,BackColour=&H99000000,BorderStyle=4,Outline=0,MarginV=60'" -c:v libx264 -crf 20 -preset veryfast -c:a copy out.mp4
```

Font names must be installed where ffmpeg runs; use `fontsdir=` to point at the brand font files. In ASS
colour codes the order is `&HAABBGGRR`. Look at frames from the result before delivering.

## Languages

For other languages, translate the cleaned SRT with `content-translate`, keeping every timestamp; then
recheck line lengths, since translated lines often run longer and need re-breaking or splitting.
