# SESSION 6 - Real Projects & Use Cases

## Files
| Task | File |
|------|------|
| 1 PDF Chatbot | `task1_pdf_chatbot.py` |
| 2 Customer Support Bot | `task2_support_bot.py` |
| 3 AI Content Generator | `task3_content_generator.py` |
| 5 Improved Content Generator | `task5_content_generator_improved.py` |

## Task 1: PDF Chatbot (PyPDF2 + Streamlit)
Setup: `pip install streamlit PyPDF2` -> `streamlit run task1_pdf_chatbot.py`.
The user uploads a PDF (timetable / IRCTC ticket). `PdfReader` reads each page, `extract_text()` collects the text,
and it is shown in a text area in the browser. I also added a small keyword search box (e.g., search "Monday" or "PNR").
Tested: text extraction works on a sample PDF. Scanned (image-only) PDFs will show a warning because they contain no text.

## Task 2: Customer Support Chatbot (if-else logic)
Run: `python task2_support_bot.py`. The function `get_reply()` checks keywords in the input:
- "order status / track / where is my order" -> order status reply
- "refund / money back / wrong item" -> refund reply
- "delay / late / taking too long" -> delivery delay reply
- anything else -> asks the user to type one of the three options

Sample run (tested):
```
You: Where is my order?
Bot: Your order is being prepared by the restaurant and will be picked up soon. ...
You: I want a refund
Bot: Sorry for the trouble! Your refund request has been noted. ...
You: my food is very late
Bot: We are sorry your order is late. ...
You: pizza
Bot: Sorry, I did not understand that. Please type one of these: ...
```

## Task 3: AI Content Generator function
File `task3_content_generator.py` has `generate_blog(topic)` which sends the topic to the GPT API with `max_tokens=100`.
Example input: `Best Cafes in Ahmedabad`.
The hint's `openai.Completion.create()` is the old method (removed in openai 1.0+), so I used the new
`client.chat.completions.create()` and kept the old version in comments. An API key is required to run it.

## Task 4: 3 ways companies in India use LLMs
1. **IRCTC (AskDISHA chatbot, built with CoRover's BharatGPT)** - answers passenger queries about tickets, PNR and refunds in many languages, reducing the load on call centres.
2. **Ola Krutrim** - Ola built its own Indian-language AI assistant/model so users can chat in Indian languages, creating a local alternative to foreign AI products.
3. **Sarvam AI (Indic LLMs)** - builds models for Indian languages, so banks, government and startups can serve customers in Hindi, Gujarati, Tamil etc., reaching users who do not use English.

(Other common uses: Zomato/Swiggy AI assistants for food discovery and customer support, Jio's Haptik for customer-service bots.)

## Task 5: Improving the AI Content Generator
**Question asked to the AI tool:** "How can I make my GPT-based content generator more engaging for users?"

**Main suggestions received:**
1. Give the model a role, audience and tone (e.g., "popular lifestyle blogger writing for college students").
2. Ask for a catchy title, an engaging first line and a call-to-action.
3. Let the user choose the tone (fun, professional, trendy).
4. Add emojis/hashtags and increase output length slightly so the post is not cut off.

**Suggestion implemented:** (1)+(2)+(3) - a tone selection and a structured prompt (title + hook + CTA), with `max_tokens`
raised from 100 to 150. See `task5_content_generator_improved.py`.

```python
prompt = (
    f"You are a popular Indian lifestyle blogger. Write a short blog post about '{topic}' "
    f"in a {tone} tone for college students. "
    "Start with a catchy title, then an engaging opening line, "
    "and end with a one-line call-to-action. Use 1-2 emojis."
)
```
