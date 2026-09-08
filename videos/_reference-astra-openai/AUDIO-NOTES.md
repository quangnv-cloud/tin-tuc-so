# Ghi chú audio — tuyến "Công Nghệ Số"

## Nhạc nền (phản hồi người dùng 2026-09-07: bản đầu "quá nhiều nhịp, lớn, lấn giọng")
Dùng prompt AMBIENT NHẸ, không dùng prompt "driving/fast-paced" như tuyến kinh doanh:

    python lyria-recipe.py --output track-raw.wav --duration <TOTAL+đệm> --density 0.25 --brightness 0.4 \
      --prompt "soft ambient underscore for a news explainer, calm, minimal, sparse, gentle warm synth pad, very subtle, low-key, almost no percussion, atmospheric, understated, instrumental only, quiet background bed" \
      --negative-prompt "vocals, lyrics, singing, choir, rap, spoken word, humming, drums, heavy beat, aggressive percussion, busy rhythm, loud, driving, energetic, buildup, drop"

- `data-volume` trên `#el-bgm` = **0.30** (không phải 0.5).
- carve: `--strength 0.4` (floor ~ -9.6 dB) để nhạc lùi hẳn khi có giọng.
- fade-in 1.5s đầu + fade-out 3s cuối.
