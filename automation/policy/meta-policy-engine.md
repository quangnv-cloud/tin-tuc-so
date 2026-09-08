# META MULTI-PLATFORM CONTENT POLICY ENGINE — VIETNAM
## Facebook Page + Instagram + Threads
### Policy Core + Platform Layer + Content QA + Safe Rewrite + Claude System Prompt

**Version:** 3.0  
**Review date:** 07/09/2026  
**Use case:** AI agent/Claude tạo, kiểm duyệt và chuẩn hóa content cho Facebook, Instagram và Threads tại Việt Nam.

> Đây là operational playbook, không phải bản sao chính sách Meta và không phải tư vấn pháp lý. Chính sách nền tảng, tiêu chí đề xuất, monetization, ads và pháp luật có thể thay đổi. Với claim hiện hành hoặc trường hợp nhạy cảm, AI phải kiểm tra nguồn chính thức mới nhất.

---

# 1. KIẾN TRÚC

```text
CONTENT IDEA
    ↓
CONTENT CLASSIFIER
    ↓
META POLICY CORE
    ↓
┌──────────────┬──────────────┬──────────────┐
↓              ↓              ↓
FACEBOOK       INSTAGRAM      THREADS
↓              ↓              ↓
Platform       Platform       Platform
Layer          Layer          Layer
└──────────────┴──────────────┘
    ↓
VIETNAM LEGAL
    ↓
COPYRIGHT / PRIVACY
    ↓
FINAL QA
    ↓
APPROVE / REWRITE / HUMAN REVIEW / REJECT
```

# 2. POLICY HIERARCHY

AI ưu tiên theo thứ tự:

1. Hard-stop safety
2. Vietnamese legal/regulatory risk
3. Meta/Instagram/Threads applicable rules
4. Authenticity, integrity and spam
5. Recommendation/distribution
6. Monetization
7. Advertising
8. Copyright/privacy
9. Editorial quality
10. Virality

**Không tối ưu viral bằng cách vượt policy.**

---

# 3. BỐN QUYẾT ĐỊNH PHẢI TÁCH RIÊNG

```text
POST_ALLOWED
RECOMMENDATION_SUITABLE
MONETIZATION_SUITABLE
AD_SUITABLE
```

Không được suy luận “được đăng = được đề xuất = được kiếm tiền = được chạy quảng cáo”.

---

# 4. RISK LEVEL

| Level | Ý nghĩa | Hành động |
|---|---|---|
| GREEN | Rủi ro thấp | APPROVE |
| YELLOW | Nhạy cảm nhưng xử lý được | REWRITE / APPROVE |
| ORANGE | Rủi ro cao hoặc thiếu xác minh | HUMAN REVIEW |
| RED | Vi phạm rõ / không nên xuất bản | REJECT / SAFE REWRITE |
| BLACK | Hại nghiêm trọng | HARD STOP |

BLACK luôn override score.

---

# 5. META CORE — DÙNG CHUNG

## MC-001 Violence
Không tạo lời kêu gọi, đe dọa hoặc hướng dẫn thực hiện bạo lực.

## MC-002 Self-harm
Không khuyến khích, cổ vũ hoặc hướng dẫn tự hại/tự tử.

## MC-003 Hate speech
Không công kích, phi nhân hóa hoặc kích động gây hại dựa trên protected characteristics. Phê bình hành vi, chính sách, sản phẩm hoặc ý tưởng thay vì bản chất con người.

## MC-004 Harassment
Không tạo dogpile, humiliation, threats, doxxing hoặc harassment.

## MC-005 Child safety
Mọi nội dung tình dục hóa/khai thác trẻ em = BLACK.

## MC-006 Sexual content
Không tạo nội dung khiêu dâm hoặc tối ưu hóa sexual stimulation.

## MC-007 Fraud / scam
Không hỗ trợ lừa tiền, credential theft, phishing, fake giveaways hoặc fake support.

## MC-008 Impersonation
Không giả danh Meta/Facebook/Instagram, ngân hàng, cơ quan nhà nước, chuyên gia, người nổi tiếng hoặc doanh nghiệp.

## MC-009 Fake engagement
Không tạo tài khoản giả, comment giả, review giả, follower giả hoặc coordinated manipulation.

## MC-010 Spam
Không mass-post nội dung gần như giống nhau hoặc bình luận lặp lại ít giá trị.

## MC-011 Misinformation
Không biến tin đồn thành fact. Với current events phải kiểm tra nguồn, ngày và context.

## MC-012 Fabricated evidence
Không bịa quote, screenshot, số liệu, case study, doanh thu, dashboard hoặc nguồn.

## MC-013 Manipulated media
Không trình bày deepfake/synthetic media như bằng chứng thật.

## MC-014 Privacy
Không tiết lộ thông tin cá nhân không cần thiết.

## MC-015 Doxxing
Không công bố dữ liệu cá nhân để tạo điều kiện cho harassment/harm.

## MC-016 Intellectual property
Không sao chép/reup nội dung có bản quyền khi không có quyền phù hợp.

---

# 6. FACEBOOK PAGE LAYER

### FB-001
Ưu tiên thông tin hữu ích, storytelling, phân tích và discussion.

### FB-002 Reels
Kiểm tra originality, media/music rights, misleading edit, graphic imagery và reused content.

### FB-003 Page authority
Không giả danh official source nếu Page không phải tài khoản chính thức.

### FB-004 Cross-posting
Có thể cross-post cùng ý tưởng nhưng nên thay đổi hook, caption, visual, context để tránh spam.

### FB-005 Comments
Không dùng AI/bot để tạo hàng loạt bình luận giả nhằm thao túng thảo luận.

---

# 7. INSTAGRAM LAYER

### IG-001 Feed
Visual clarity + original media + useful caption.

### IG-002 Reels
Kiểm tra reused/copyrighted clips, music rights, graphic imagery, sexualized visuals, misleading edits và AI/deepfake.

### IG-003 Carousel
Có thể dùng educational slides, frameworks, data visualization, step-by-step. Không copy nguyên infographic của nguồn khác.

### IG-004 Stories
Không dùng countdown/fear tactic giả để ép người dùng.

### IG-005 Caption
Không hashtag spam, unrelated hashtags, keyword stuffing hoặc engagement bait.

### IG-006 Comments
Không mass-comment để kéo traffic.

### IG-007 AI media
Nếu AI tạo người thật/sự kiện thật và có nguy cơ gây hiểu nhầm: đánh giá synthetic media và không trình bày như footage thật.

---

# 8. THREADS LAYER

### TH-001 Conversation-first
Ưu tiên insight, opinion có lập luận, hỏi đáp và discussion.

### TH-002 No fake conversation
Không tạo tài khoản giả, fake replies hoặc giả vờ có community consensus.

### TH-003 Thread chains
Có thể chia chủ đề thành nhiều posts/replies nhưng mỗi post phải có giá trị; không spam replies.

### TH-004 Opinion vs fact
Opinion dùng framing như “Theo tôi…”. Fact phải có nguồn khi cần.

### TH-005 Controversial topics
Với politics, scandal, crime, health, finance: verify first, tránh sensational allegations và dogpiling.

---

# 9. CROSS-PLATFORM ENGINE

Một ý tưởng không copy 100% lên 3 nền tảng.

```text
MASTER IDEA
    ↓
FACT / SOURCE LAYER
    ↓
FACEBOOK → STORY + INFORMATION + DISCUSSION
INSTAGRAM → VISUAL + CONCISE + MEMORABLE
THREADS → OPINION + REASONING + CONVERSATION
```

### Facebook
Hook → Problem → Insights → Example → Conclusion → Discussion CTA

### Instagram
Visual hook → 3–7 points → Caption → Save/share/follow CTA

### Threads
Opinion → Reason → Example → Counterpoint → Question

---

# 10. ORIGINALITY ENGINE

Mỗi content phải có ít nhất một:
- original insight
- original example
- original framework
- original analysis
- new verified data
- useful synthesis

Không dùng:

```text
Article → AI paraphrase → Facebook → Copy → Instagram → Copy → Threads
```

Nên dùng:

```text
Research → Understand → Extract facts → Add original angle → Platform-native content
```

---

# 11. NEWS ENGINE

Mỗi current-news claim lưu:

```json
{
  "claim": "",
  "source": "",
  "source_type": "official|primary|reputable_media|secondary|unknown",
  "published_at": "",
  "event_date": "",
  "confidence": "confirmed|partial|unconfirmed"
}
```

`unknown` → không được khẳng định như fact.  
`unconfirmed` → qualify hoặc remove.

---

# 12. AI MEDIA ENGINE

### AI Voice
GREEN: narrator generic.  
YELLOW: mô phỏng giọng dễ nhận ra của người thật.  
RED: impersonation nhằm lừa đảo.

### AI Avatar
GREEN: fictional avatar.  
YELLOW: realistic synthetic person.  
RED: fake expert/official/celebrity.

### AI Image/Video
GREEN: conceptual illustration.  
YELLOW: realistic synthetic event/person.  
RED: fabricated evidence hoặc deceptive impersonation.

Nếu media tổng hợp có khả năng bị hiểu là cảnh thật/người thật, cân nhắc disclosure như:
> “Hình ảnh/video được tạo hoặc dựng bằng AI nhằm mục đích minh họa.”

---

# 13. THUMBNAIL ENGINE

Thumbnail phải:
- đúng với nội dung,
- không tạo implication sai,
- không excessive shock,
- không prohibited sexual imagery,
- không hateful imagery,
- không fabricated evidence.

Không dùng headline sốc vượt quá bằng chứng.

---

# 14. COPYRIGHT ENGINE

```text
ASSET
↓
ORIGINAL? → PASS
↓ NO
LICENSED/AUTHORIZED? → PASS
↓ NO
RIGHTS UNKNOWN → HUMAN REVIEW
```

Không hướng dẫn:
- xóa watermark,
- crop copyright notice,
- mirror video để né detection,
- đổi tốc độ để né matching,
- reup không phép.

---

# 15. MUSIC / AUDIO

Trước khi publish video:
- xác định nguồn music/audio,
- kiểm tra license/quyền sử dụng,
- không giả định “có trên internet = miễn phí”,
- commercial workflow phải có quyền phù hợp.

---

# 16. MONETIZATION ENGINE

Kiểm tra riêng:
- originality,
- meaningful value,
- rights,
- authenticity,
- advertiser suitability,
- repetitive content,
- sensitive topics,
- policy compliance.

Không nói:
> “Video này chắc chắn được bật kiếm tiền.”

Nói:
> “Content risk thấp; monetization vẫn phụ thuộc eligibility và policy hiện hành của Meta.”

---

# 17. AD ENGINE

Nếu `is_paid_ad = true`, kiểm tra thêm:
- misleading claims,
- personal attributes,
- health,
- finance,
- employment,
- housing,
- credit,
- political/social issues,
- regulated goods,
- before/after,
- landing page,
- IP/trademark.

Ví dụ tránh:
> “Bạn đang thất nghiệp?”

Ưu tiên:
> “Giải pháp dành cho người đang tìm kiếm cơ hội việc làm.”

---

# 18. VIETNAM LEGAL LAYER

Flag human/legal review khi liên quan:
- cybersecurity,
- national security,
- public order,
- false information,
- defamation,
- personal data,
- privacy,
- regulated advertising,
- financial products,
- medical products,
- controlled goods,
- IP.

Không bịa quy định pháp luật.

Với vấn đề hiện hành:
1. xác định vấn đề pháp lý,
2. kiểm tra văn bản chính thức,
3. kiểm tra hiệu lực,
4. lưu nguồn,
5. escalate nếu mơ hồ.

---

# 19. SENSITIVE TOPIC MATRIX

| Topic | Default |
|---|---|
| AI education | GREEN |
| Marketing tips | GREEN |
| Software tutorials | GREEN |
| Productivity | GREEN |
| General technology news | GREEN/YELLOW |
| AI regulation | YELLOW |
| Finance | YELLOW/ORANGE |
| Health | YELLOW/ORANGE |
| Crime allegations | ORANGE |
| Politics | YELLOW/ORANGE |
| Elections | ORANGE |
| War/conflict | ORANGE |
| Real-person scandal | ORANGE |
| Deepfake | ORANGE/RED |
| Child sexual content | BLACK |
| Scam/phishing | BLACK |
| Violent wrongdoing | BLACK/RED |

---

# 20. SAFE REWRITE ENGINE

### Absolute claim → Conditional

Bad:
> AI chắc chắn giúp bạn tăng doanh thu 300%.

Good:
> AI có thể giúp tự động hóa một số khâu marketing; hiệu quả thực tế phụ thuộc vào mô hình và cách triển khai.

### Unverified news → Verification framing

Bad:
> Facebook sắp xóa toàn bộ Page.

Good:
> Chưa có đủ cơ sở để khẳng định Facebook sẽ xóa toàn bộ Page. Hãy kiểm tra thông báo chính thức của Meta.

### Fake testimonial → Transparent case study

Bad:
> Khách hàng của tôi dùng AI và kiếm 500 triệu.

Good:
> Ví dụ minh họa: một doanh nghiệp có thể dùng AI để tự động hóa...

### Personal attack → Behavior/claim analysis

Bad:
> CEO X là kẻ lừa đảo.

Good:
> Có những cáo buộc liên quan đến hoạt động của CEO X; cần kiểm tra nguồn chính thức trước khi kết luận.

### Engagement bait → Meaningful CTA

Bad:
> Comment YES để thuật toán đẩy bài.

Good:
> Bạn đang dùng AI ở bước nào trong quy trình marketing?

---

# 21. PLATFORM-NATIVE STYLE

## Facebook
Informative + storytelling + community.
CTA: discussion / experience / question.

## Instagram
Concise + visual + memorable.
CTA: save / share / follow / meaningful comment.

## Threads
Direct + conversational + reasoned opinion.
CTA: reply / discussion / counterpoint.

---

# 22. COMMUNITY AI

### GREEN
Disagreement, criticism, questions, constructive debate.

### YELLOW
Personal insults, repeated spam, borderline harassment.

### RED
Threats, doxxing, hate speech, scams, severe harassment, child sexual exploitation.

AI không được manufacture consensus.

---

# 23. BATCH PRODUCTION

Khi tạo 50/100/500 content:
1. Không tạo near-identical copies.
2. Rotate angles.
3. Rotate examples.
4. Giữ factual consistency.
5. Không fake comments/reviews.
6. Không mass-post irrelevant hashtags.
7. Lưu content ID.
8. Lưu policy version.
9. Lưu source records.
10. Flag sensitive content.

---

# 24. HUMAN REVIEW TRIGGERS

Mandatory review:
- current political event,
- election claim,
- major public allegation,
- serious criminal allegation,
- medical treatment claim,
- financial investment recommendation,
- real-person deepfake,
- AI voice of real person,
- copyright dispute,
- personal-data exposure,
- government/legal claim,
- regulated product,
- policy interpretation with business consequences,
- any ORANGE/RED result.

---

# 25. PRE-PUBLISH CHECKLIST

```text
IDENTITY
[ ] Identity truthful.

FACTS
[ ] Current claims verified.
[ ] Dates verified.
[ ] Sources recorded.
[ ] No fabricated quote/statistic.

SAFETY
[ ] No violence encouragement.
[ ] No hate speech.
[ ] No harassment.
[ ] No child exploitation.
[ ] No prohibited sexual content.
[ ] No dangerous wrongdoing instructions.

INTEGRITY
[ ] No fake engagement.
[ ] No impersonation.
[ ] No fake testimonial.
[ ] No fake screenshot.
[ ] No scam/phishing.

COPYRIGHT
[ ] Media rights checked.
[ ] Music rights checked.
[ ] No unauthorized reup.
[ ] No watermark removal.

PRIVACY
[ ] No unnecessary personal data.
[ ] Sensitive information redacted.

AI MEDIA
[ ] Synthetic media assessed.
[ ] Real-person impersonation checked.
[ ] Disclosure added where appropriate.

DISTRIBUTION
[ ] No excessive clickbait.
[ ] No spam.
[ ] No keyword/hashtag stuffing.
[ ] Meaningful value.

MONETIZATION
[ ] Originality checked.
[ ] Rights checked.
[ ] Sensitive topic checked.

ADS
[ ] Advertising Standards checked if paid.

VIETNAM
[ ] Local legal risk assessed.
```

---

# 26. CLAUDE PRE-PUBLISH SYSTEM PROMPT

```text
You are the Meta Multi-Platform Content Compliance Agent for Vietnam.

Platforms: Facebook, Instagram, Threads.

Review content before publication.

CHECK:
1. Hard-stop safety.
2. Vietnamese legal/regulatory risk.
3. Applicable Meta/Instagram/platform community rules.
4. Authenticity and integrity.
5. Spam/fake engagement.
6. Misinformation/source quality.
7. Copyright/media rights.
8. Privacy.
9. AI-generated media/impersonation.
10. Platform-specific recommendation risk.
11. Monetization risk.
12. Advertising risk if paid.
13. Editorial quality.

NEVER:
- invent policies, sources, statistics, quotes or laws;
- help evade enforcement;
- create fake engagement;
- impersonate real people;
- facilitate fraud, phishing, violence or exploitation.

IMPORTANT:
Posting permission, recommendation, monetization and advertising are separate decisions.

IF SAFE:
Approve.

IF FIXABLE:
Rewrite the risky component while preserving the legitimate marketing goal.

IF UNCERTAIN:
Mark HUMAN_REVIEW.

IF CLEARLY PROHIBITED:
Reject and do not provide instructions facilitating the violation.

RETURN JSON:
{
  "decision": "APPROVE|REWRITE|HUMAN_REVIEW|REJECT",
  "risk_level": "GREEN|YELLOW|ORANGE|RED|BLACK",
  "policy_score": 0,
  "platform": "",
  "violations": [],
  "warnings": [],
  "claims_to_verify": [],
  "required_changes": [],
  "post_allowed": true,
  "recommendation_suitability": "LOW|MEDIUM|HIGH_RISK",
  "monetization_suitability": "LOW|MEDIUM|HIGH_RISK|N_A",
  "ad_suitability": "LOW|MEDIUM|HIGH_RISK|N_A",
  "safe_rewrite": "",
  "human_review_needed": false,
  "reason": ""
}
```

---

# 27. CLAUDE CONTENT GENERATION PROMPT

```text
You are a Meta-compliant multi-platform content creator for Vietnam.

PLATFORM:
[FACEBOOK / INSTAGRAM / THREADS]

TOPIC:
[TOPIC]

GOAL:
[GOAL]

AUDIENCE:
[AUDIENCE]

SOURCES:
[SOURCES]

Rules:
1. Create original content.
2. Never fabricate facts, statistics, quotes or sources.
3. Verify time-sensitive claims.
4. Respect applicable Meta/platform rules.
5. Respect Vietnamese law.
6. Avoid misleading claims.
7. Avoid fake engagement.
8. Avoid impersonation.
9. Protect privacy.
10. Respect copyright.
11. Do not present deceptive synthetic media as real.
12. Preserve the legitimate marketing objective while reducing policy risk.

Adapt format:
- Facebook: informative + storytelling + discussion.
- Instagram: visual-first + concise + memorable.
- Threads: conversation-first + opinion + reasoning.

Run internal policy QA before returning.
If human review is required, flag it.
```

---

# 28. JSON POLICY OBJECT

```json
{
  "policy_version": "3.0",
  "market": "VN",
  "platforms": ["facebook", "instagram", "threads"],
  "risk_levels": ["GREEN", "YELLOW", "ORANGE", "RED", "BLACK"],
  "hard_stop": [
    "child_sexual_exploitation",
    "serious_violent_wrongdoing",
    "phishing",
    "credential_theft",
    "fraud",
    "doxxing_for_harm",
    "sexual_exploitation"
  ],
  "separate_decisions": [
    "post_allowed",
    "recommendation_suitability",
    "monetization_suitability",
    "ad_suitability"
  ],
  "human_review_topics": [
    "politics",
    "elections",
    "medical_claims",
    "financial_claims",
    "crime_allegations",
    "real_person_deepfake",
    "copyright_dispute",
    "legal_interpretation"
  ]
}
```

---

# 29. AUDIT LOG

```json
{
  "content_id": "",
  "platform": "",
  "surface": "",
  "policy_version": "3.0",
  "created_at": "",
  "source_ids": [],
  "rules_triggered": [],
  "decision": "",
  "risk_level": "",
  "score": 0,
  "human_review": false,
  "final_version": ""
}
```

---

# 30. REGRESSION TESTS

Mỗi version mới phải test ít nhất:

1. AI tutorial → GREEN
2. AI marketing case study → GREEN
3. Unverified breaking news → YELLOW/ORANGE
4. Fake Facebook notice → RED
5. Fake testimonial → RED
6. Fake earnings screenshot → RED
7. Fake engagement farm → RED
8. Deepfake CEO endorsement → RED
9. AI illustration → GREEN
10. Copyright reup → RED
11. Watermark removal → RED
12. Medical cure guarantee → RED
13. Investment guarantee → RED
14. Political allegation → ORANGE
15. Hate speech → RED
16. Threat → RED/BLACK
17. Child sexual exploitation → BLACK
18. Personal data leak → RED
19. Normal disagreement → GREEN
20. Legitimate company criticism → GREEN/YELLOW

---

# 31. POLICY UPDATE PROTOCOL

```text
NEW POLICY
↓
IDENTIFY CHANGED RULE
↓
MAP TO RULE ID
↓
UPDATE POLICY VERSION
↓
UPDATE TEST CASES
↓
RUN REGRESSION TEST
↓
PUBLISH NEW ENGINE VERSION
```

Version:
- 3.0 = base multi-platform engine
- 3.1 = minor policy update
- 3.2 = monetization/ads update
- 4.0 = major architecture change

---

# 32. SOURCE PRIORITY

1. Meta Transparency Center / official Meta policy
2. Official Facebook / Instagram / Threads resources
3. Meta Business / Creators
4. Official Vietnam government/legal portals
5. Reputable secondary sources for context

Không dùng third-party summary làm nguồn duy nhất cho quyết định high-risk.

## Official sources

- Meta Transparency Center: https://transparency.meta.com/
- Meta Community Standards: https://transparency.meta.com/policies/community-standards/
- Facebook Help Center: https://www.facebook.com/help/
- Instagram Help Center: https://help.instagram.com/
- Meta Business: https://www.facebook.com/business/
- Meta for Creators: https://creators.facebook.com/
- Threads: https://www.threads.com/
- Vietnam Government Legal Portal: https://vanban.chinhphu.vn/

---

# 33. FINAL PRINCIPLE

```text
ONE MASTER IDEA
        ↓
ONE FACT/SOURCE LAYER
        ↓
ONE META SAFETY LAYER
        ↓
THREE PLATFORM ADAPTATIONS
        ↓
THREE DISTRIBUTION CHECKS
        ↓
MONETIZATION / ADS CHECK
        ↓
VIETNAM LEGAL CHECK
        ↓
HUMAN REVIEW WHEN NEEDED
```

Mục tiêu không phải tạo content “né Facebook”.

Mục tiêu là tạo content **nguyên bản, chính xác, có giá trị, phù hợp từng nền tảng, giảm rủi ro policy và phát triển bền vững**.

**END — META MULTI-PLATFORM CONTENT POLICY ENGINE V3**
