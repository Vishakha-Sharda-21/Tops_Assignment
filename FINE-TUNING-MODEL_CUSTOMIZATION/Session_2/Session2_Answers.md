# SESSION 2 - Prompt vs RAG vs Fine-Tuning

## Task 1: Instagram bio prompt (and result)

**Prompt:**
```
Act as a creative social media writer. Write 3 catchy Instagram bios for a college student.
Each bio: under 120 characters, fun and confident tone, 2 emojis, one punchline at the end.
Interests: cricket, music, late-night chai.
```

**Result (sample output - replace with your own run):**
```
1. Cover drives by day, playlists by night 🏏🎧 Chai is my power-play.
2. Bat in one hand, headphones in the other 🎶🏏 Living every over like a last-ball six.
3. Student by degree, cricketer by heart ☕🏏 Plot twist: my playlist is better than my timetable.
```
(Paste the actual output from your own ChatGPT run if your instructor needs a screenshot.)

## Task 2: RAG simulation for IPL stats
**Files:** `task2_rag_ipl.py` and the data file `ipl_stats.txt` (keep both in the same folder).

Run: `python task2_rag_ipl.py`, then ask e.g. "Who has scored the most runs in IPL?"

How it works:
1. **Retrieve** - the question is cleaned into keywords (stop words removed) and each line of `ipl_stats.txt` is scored by matching keywords; best lines are kept.
2. **Augment** - question + retrieved lines are combined into one prompt.
3. **Generate** - prints a combined answer (a real RAG would send this prompt to an LLM).

Tested sample run:
```
Ask a question about IPL: Who has scored the most runs in IPL?
[1] Retrieved lines:
   * Virat Kohli is the all-time leading run-scorer in IPL history with over 8000 runs.
[3] Final answer:
Based on the stats file: Virat Kohli is the all-time leading run-scorer in IPL history with over 8000 runs.
```
(The stats file is a small sample dataset I prepared, current up to IPL 2025; edit it if you want more data.)

## Task 3: Best approach in real apps

| Approach | Scenario (app) | Reasoning |
|----------|----------------|-----------|
| Prompt engineering | **Zomato** - writing a friendly notification like "Your biryani is on the way!" | The task is simple and general. A good prompt with tone, length and an example is enough; no extra data or training needed. |
| RAG | **Flipkart** - answering "What is the return policy for this phone?" | Policies and product details change often and live in documents. RAG fetches the latest policy at question time, so no retraining is needed and answers stay up to date. |
| Fine-tuning | **Paytm** - classifying/handling customer complaints in Hinglish with Paytm's specific style and categories | It needs consistent behaviour, special vocabulary and a fixed output format learned from thousands of past tickets, which prompts or documents alone cannot teach reliably. |

## Task 4: Comparison table

| Criteria | Prompt Engineering | RAG | Fine-Tuning |
|----------|--------------------|-----|-------------|
| Setup cost | Very low (just write prompts) | Medium (vector DB / search, embeddings, document pipeline) | High (data collection, labelling, GPU compute) |
| Time to deploy | Minutes to hours | Days to a couple of weeks | Weeks (data prep + training + testing) |
| Maintenance effort | Low - edit the prompt | Medium - keep documents updated and re-index | High - retrain when data or needs change, track model versions |
| Ideal use cases | Quick prototypes, general tasks, tone/format control | Question answering on private or frequently changing data (policies, manuals, FAQs) | Fixed domain/style, specialised language, consistent output format, high-volume tasks |

## Task 5: Choosing an approach for a BookMyShow-style movie recommendation chatbot

**Advice from the AI tool (summary):** Start with prompt engineering to prototype the chatbot quickly. Use RAG because movie listings, show timings, theatres and reviews change daily and must come from live data. Consider fine-tuning only later, if you have a lot of user-behaviour data and want deeper personalization or a fixed brand tone.

**My final decision:** I would use **RAG (with good prompt engineering)**. Show timings, new releases and seat availability change every day, so the bot must read the latest data instead of memorised knowledge; RAG does this without retraining and is faster and cheaper to build. I would add fine-tuning later only after collecting enough user data.
