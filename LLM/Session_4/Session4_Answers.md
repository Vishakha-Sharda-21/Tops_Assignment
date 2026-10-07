# SESSION 4 - Prompt Engineering Basics

## Task 1: Prompt for an Instagram bio

**Prompt:**

```
Act as a creative social media writer. Write 3 catchy Instagram bio options for a
college student who loves cricket and music. Each bio should be under 150
characters, have a fun and confident tone, include 2-3 relevant emojis, and
end with a short call-to-action or punchline. Keep it in simple English.
```

**Why this prompt will give a good result:**
- It gives the model a **role** ("creative social media writer"), so the style matches.
- It clearly states the **audience/subject** (college student, loves cricket and music).
- It sets **constraints** (3 options, under 150 characters, emojis, tone), so the output is short and usable.
- It specifies the **format** (punchline at the end), so the result is not generic.

---

## Task 2: Improving the vague prompt "Suggest some food."

**Improved prompt:**

```
Suggest 7 vegetarian dinner ideas for a college student staying in a hostel in
Ahmedabad. The meals should be Gujarati or North Indian, budget-friendly
(under Rs 100 per meal), simple to order or make with minimal equipment (like
an electric kettle or induction), and reasonably healthy. For each idea, give the
dish name and one line on why it suits a hostel student.
```

**What changed:** I added the cuisine (Gujarati/North Indian), meal type (dinner), diet (vegetarian), location (Ahmedabad), budget, user type (hostel student), quantity (7) and output format (name + one line).

---

## Task 3: Zero-shot prompt - trending IPL topic

**Prompt used (zero-shot, no examples):**

```
Summarize the latest trending topic on IPL in 3 sentences.
```

**Output (based on news at the time of writing - October 2026):**

> The biggest IPL talk right now is the IPL 2027 auction, which will be a mini-auction, meaning teams will mostly keep their current squads and only fill specific gaps. The BCCI has confirmed that the auction will be held in Goa in December, bringing it back to India after three years of overseas auctions in Dubai, Jeddah and Abu Dhabi. Franchises have already started making player movements and personnel changes, so fans are speculating about who will be retained, released or traded before the auction.

*(Since LLMs change their answers daily, run this prompt once yourself in ChatGPT with web search ON and paste your own output here if your instructor needs a screenshot.)*

---

## Task 4: Few-shot prompt for funny Flipkart reviews

**Prompt:**

```
Write short, funny one-line reviews for Flipkart products.

Product: Steel Water Bottle
Review: Keeps water cold for 24 hours, but my excuses for not drinking it stay warm forever.

Product: Wireless Mouse
Review: Finally a mouse with no tail - now only my cursor runs away from me.

Product: Bluetooth Speaker
Review:
```

**Expected output (sample):**

> Review: Small speaker, big bass - my neighbours now know my playlist better than I do.

**Why it works:** The two examples teach the model the format (Product -> Review), the length (one line) and the humour style, so it copies the pattern for the new product.

---

## Task 5: 3 common prompt mistakes and better prompts

### Mistake 1: Being vague / no context
- **Bad prompt:** `Write about cricket.`
- **Better prompt:** `Write a 100-word beginner-friendly paragraph explaining how a T20 cricket match works, for a school student who has never watched cricket.`
- **Best practice used:** Give clear context, audience, topic and length.

### Mistake 2: Asking too many things at once / no structure
- **Bad prompt:** `Tell me about AI and also machine learning and give me notes and a quiz and a project idea.`
- **Better prompt:**
  ```
  Step 1: Explain the difference between AI and machine learning in 5 simple points.
  Step 2: Then give me 3 MCQs to test my understanding.
  ```
- **Best practice used:** Break a big task into small steps and give a clear order.

### Mistake 3: Not specifying the format or tone of the output
- **Bad prompt:** `Write an email to my professor.`
- **Better prompt:** `Write a polite and formal email (under 100 words) to my professor asking for a 2-day extension on my assignment submission because I was ill. Include a subject line.`
- **Best practice used:** Specify the format, tone, length and the key details to include.

(Bonus tips: use a role like "Act as...", give examples (few-shot) and refine the prompt step by step if the first answer is not perfect.)
