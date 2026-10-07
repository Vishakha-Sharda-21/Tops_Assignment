# SESSION 2 - GPT vs BERT vs T5

## Task 1: GPT-2 Instagram caption
**File:** `task1_gpt2_caption.py`

Steps: `pip install transformers torch` -> run `python task1_gpt2_caption.py`.
The script loads GPT-2 with the `text-generation` pipeline and continues the prompt
"Sunset vibes at the beach" into a short caption (25 new tokens, temperature 0.9).
GPT-2 output is random and a bit rough, so it changes if you change the seed.

## Task 2: BERT sentiment on a Zomato review
**File:** `task2_bert_sentiment.py`

Review: *"The food was absolutely delicious and the delivery was super fast."*
I used `pipeline('sentiment-analysis')` (as per hint) and also a BERT-base-uncased model
fine-tuned on SST-2. Expected result: **POSITIVE** with a very high confidence (about 0.99).

## Task 3: T5-base paraphrase
**File:** `task3_t5_paraphrase.py`

Input given to model: `paraphrase: BookMyShow makes movie ticket booking easy and fast.`
The script uses T5-base with beam search (5 beams). Note: base T5 is not trained
specifically for paraphrasing, so the output may be very close to the original sentence.

> Run each script once on your own laptop and paste the real console output here for submission:
> - Task 1 output: ______________________
> - Task 2 output: ______________________
> - Task 3 output: ______________________

## Task 4: Comparison table - GPT vs BERT vs T5

| Model Name | Architecture Type | Typical Use Case | Example App Feature |
|------------|-------------------|------------------|---------------------|
| GPT (GPT-2/3/4) | Generator (Decoder-only) | Text generation, chatting, story/code writing | Autocomplete / smart reply in WhatsApp, Instagram caption writer |
| BERT | Encoder (Encoder-only) | Understanding text: classification, sentiment, search, question answering | Sentiment of reviews in Zomato, spam detection, Google Search understanding |
| T5 | Encoder-Decoder | Any text-to-text task: summarisation, translation, paraphrasing | Summarising news in a news feed app, paraphrase tool, translation in Google Translate |

## Task 5: Which model suits each scenario?

1. **Generating a playlist description for Spotify -> GPT.** It is a generator model, so it is best at writing fresh, creative text from a short prompt (like playlist name and mood).
2. **Classifying spam messages on WhatsApp -> BERT.** Spam detection is a text classification (understanding) task and BERT's encoder reads the whole message in both directions to understand it well.
3. **Summarising a cricket match report for an IPL app -> T5.** Summarisation is a text-to-text task (long text in, short text out), which is exactly what the encoder-decoder T5 is designed for.
