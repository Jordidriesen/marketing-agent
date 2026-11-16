# ffmpeg recipes

Flags change between ffmpeg builds: check `ffmpeg -h filter=<name>` when a filter complains. Write to a
temporary `.mp4` name and rename on exit code 0.

## Cutting

Fast trim without re-encoding (cuts land on the nearest keyframe, so the start can drift slightly):

```bash
ffmpeg -ss 00:01:12 -to 00:01:58 -i input.mp4 -c copy clip.mp4
```

Frame-accurate trim (re-encodes):

```bash
ffmpeg -ss 00:01:12 -to 00:01:58 -i input.mp4 -c:v libx264 -crf 18 -preset veryfast -c:a aac -b:a 192k clip.mp4
```

Join clips with identical settings: write `list.txt` (`file 'a.mp4'` per line) and run
`ffmpeg -f concat -safe 0 -i list.txt -c copy joined.mp4`.

## Loudness

Two-pass loudness normalisation. A common streaming target is about -14 LUFS integrated with a true peak
at or below -1 dBTP; check the platform's current guidance, and use the user's target when given.

```bash
# pass 1: measure
ffmpeg -i input.mp4 -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2> loud.txt
# pass 2: apply the measured values from loud.txt
ffmpeg -i input.mp4 -af loudnorm=I=-14:TP=-1:LRA=11:measured_I=<i>:measured_TP=<tp>:measured_LRA=<lra>:measured_thresh=<thresh>:offset=<offset>:linear=true -c:v copy -c:a aac -b:a 192k out.mp4
```

Light clean-up for a voice recorded in a room: `highpass=f=80` before `loudnorm`. Do not stack noise
reduction filters without listening to the result; say that you could not listen.

## Reframing

Centre crop from 16:9 to 9:16:

```bash
ffmpeg -i input.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" -c:v libx264 -crf 20 -preset veryfast -c:a copy out-9x16.mp4
```

Subject off centre: replace the crop x offset, for example `crop=ih*9/16:ih:x=iw*0.55-ih*9/32`. Extract a
frame every few seconds from the result and check the subject stays in frame; split the clip and use
different offsets per section when the subject moves.

Square: `crop=ih:ih,scale=1080:1080`. Keeping the full landscape frame inside a vertical video (letterbox
on a blurred copy):

```bash
ffmpeg -i input.mp4 -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20[bg];[0:v]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" -c:v libx264 -crf 20 -preset veryfast -c:a copy out.mp4
```

## Exports

General web and social delivery: H.264, `-pix_fmt yuv420p`, AAC audio, `-movflags +faststart`, 30 fps
unless the source differs. Check each platform's current limits (length, file size, aspect ratios) before
exporting; they change.

```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart out.mp4
```

Smaller file for an upload cap: raise `-crf` in steps of 2 and check the result looks acceptable.

## Poster frame

Pick a settled frame (no blink, no motion blur, text fully in), extract it, and look at it:

```bash
ffmpeg -ss 00:00:03.2 -i input.mp4 -frames:v 1 -q:v 2 poster.jpg
```

For a YouTube thumbnail, the frame is source material only: the thumbnail itself comes from
`youtube-packaging` or `creative-brief` with `canva-workflow`.
