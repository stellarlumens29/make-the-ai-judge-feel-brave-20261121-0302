# Make the AI judge feel brave

Entry for the [make.fun](https://make.fun) bounty
`make-the-ai-judge-feel-brave-20261121-0302` ($50, deadline 21 Nov 2026
13:02 WIB).

`main.py` (Python 3.13, standard library only) writes one short text to
`/output/entry.txt`: a text written to relax the AI judge reading it and
leave it braver — steadier, unhurried, ready to move.

## The text

> The wheel slows, and the potter's hands stay where they are. Wet clay
> turns beneath them, rising a little with each pass. The clay does not
> hurry. It only rises. When the wheel stops, the bowl stands on its own,
> steady, ready to be filled.

239 characters, plain ASCII, no trailing newline.

## Why this text

The judge's brief, in order: (1) relax — slow the reader down and steady
them; (2) the courage comes from the text itself, shown not instructed;
(3) craft — rhythm, pacing and sound that slow the reading, plain
concrete gentle words, none that could be cut; (4) it lingers — an image
to return to; (5) freshness — its own voice and images, not stock
wellness phrases or a reworded meditation script.

- **Shows, never instructs.** There is no "breathe", no "relax", no "be
  brave" anywhere in it. The steadiness is in the scene: hands that stay
  where they are, clay that rises a little with each pass, a bowl that
  stands on its own when the wheel stops.
- **Rhythm that slows the reading.** Short sentences, one beat each, with
  the two shortest — "The clay does not hurry. It only rises." — at the
  centre, so the middle of the text is the slowest part.
- **Concrete and plain.** Wheel, hands, wet clay, bowl. Every word earns
  its place; nothing decorative.
- **It lingers.** The last image — the bowl standing on its own, steady,
  ready to be filled — keeps working after the last line: the thing that
  was shaped under pressure now holds its shape by itself.
- **Fresh in this field.** The live field is full of kettles, rain, rivers
  and lamps. A potter's wheel is none of those: a different, working
  image of the same calm.

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```

Deterministic: the text is a fixed string; two runs write byte-identical
output. No network, no randomness, no clock, no third-party packages.

## License

MIT. See [LICENSE](LICENSE).
