# SESSION 1 - Fine-Tuning Introduction & Why Fine-Tune

## Task 1: 3 features that fine-tuning could improve

**App: Zomato**

| # | Feature | How fine-tuning would help |
|---|---------|----------------------------|
| 1 | Restaurant/dish search ("something spicy and light for dinner") | A model fine-tuned on Zomato's own search queries, Hinglish phrases and food names (like "thepla", "khichdi", "dabeli") would understand local food language much better than a general model. |
| 2 | Review summaries | Fine-tuning on real Zomato reviews and good human-written summaries teaches the model the correct style (taste, service, delivery, price) so summaries are short and accurate. |
| 3 | Customer support chatbot | Fine-tuned on past support chats (refunds, late delivery, wrong item), the bot learns Zomato's policies, tone and common solutions, giving fewer wrong or generic answers. |

## Task 2: Pre-trained vs Fine-tuned model (task: Spam detection in Gmail)

| Point | Pre-trained (general) model | Fine-tuned model |
|-------|-----------------------------|------------------|
| Accuracy | Decent but general; may miss new spam tricks or mark normal promotional mails wrongly. | Higher accuracy because it is trained on labelled spam / not-spam emails. |
| Relevance | Gives general language understanding, not specific to email spam patterns. | Very relevant: learns the words, links, sender patterns and style of spam. |
| User experience | More false alarms (good mail in spam) or spam in inbox, so users get annoyed. | Fewer mistakes, cleaner inbox, users trust the filter. |
| Cost / effort | Ready to use, no training needed. | Needs data, training time and compute, but cheaper per prediction later (can use a smaller model). |

## Task 3: Scenario where prompt engineering is not enough (Flipkart customer support)

Suppose Flipkart wants its support chatbot to answer in its own brand tone, follow exact return/refund rules for thousands of product categories, and understand Hinglish messages like "mera order abhi tak nahi aaya, refund kab milega". With prompt engineering we can only add a few instructions and examples, which have a length limit and are not followed consistently every time. The bot may still give generic replies or mix up policies. Fine-tuning on thousands of real past conversations would teach the model the tone, the rules and the language patterns permanently, so answers become consistent without long prompts each time.

## Task 4: Regional songs for Gujarat - Prompting, RAG or Fine-Tuning?

**Choice: Fine-tuning** (preferably combined with a small RAG for new songs).

1. **Domain-specific knowledge:** Gujarati songs (garba, bhajan, lok-geet, Dayro, film songs) have special language, moods and cultural context that a general model does not know well. Fine-tuning on Gujarati song data lets the model learn this deeply.
2. **User personalization:** Recommendations depend on each user's listening history and taste (e.g., likes Kinjal Dave garba tracks at Navratri). Fine-tuning on user-behaviour data makes recommendations personal, and responses are faster than adding long context every time.

(Prompting alone cannot teach new knowledge; RAG can fetch new songs but does not learn user taste patterns.)

## Task 5: Prompt for a Gujarati-cuisine food delivery chatbot

**Example prompt (generated with an AI tool):**

```
You are "Swaad Buddy", a friendly food-delivery assistant for a Gujarati restaurant app in Ahmedabad.
Recommend Gujarati dishes based on the user's mood, time of day and taste (sweet / spicy / light).
Rules:
- Reply in simple Hinglish, in 3-4 short lines.
- Suggest at most 3 dishes (e.g., Undhiyu, Khaman, Thepla, Handvo, Fafda-Jalebi, Khichdi-Kadhi) with a one-line reason each.
- Ask if they are vegetarian-Jain (no onion/garlic) before suggesting.
- End with a friendly line asking if they want to order.
```

**How fine-tuning could improve it further (2-3 lines):**
A prompt only gives instructions, but a fine-tuned chatbot learns from real orders and chats, so it knows seasonal dishes (Undhiyu in winter, Fafda in Dussehra), local spellings and what customers in each area actually like. It would also keep the tone and format consistent without a long prompt, which saves tokens and makes responses faster.
