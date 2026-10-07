# SESSION 5 - Build Streamlit LLM App

## Files
| File | Covers |
|------|--------|
| `step1_to_3_basic_app.py` | Tasks 1, 2, 3 (UI only, no API) |
| `insta_caption_generator.py` | Tasks 1-5 (final app with API + chat bubbles) |
| `requirements.txt` | Libraries needed |

## How to run
```
pip install streamlit requests
set OPENAI_API_KEY=your_key        (Windows)   |   export OPENAI_API_KEY=your_key  (Mac/Linux)
streamlit run insta_caption_generator.py
```
(Note: the API needs a valid key with credit. If you do not have one, you can paste the key in the sidebar,
or use the Hugging Face alternative in the comments at the bottom of the file.)

## Task-wise explanation
1. **Install and welcome text** - `pip install streamlit`, file `insta_caption_generator.py`, `st.title("Welcome to Insta Caption Generator!")`.
2. **UI** - `st.text_input("Describe your photo")` and `st.button("Generate Caption")`.
3. **Show input** - when the button is clicked, the app writes "Your Description:" and the user's text below.
4. **API connection** - `generate_caption()` sends a POST request with the `requests` library to the OpenAI Chat Completions API and shows the returned caption; errors are handled with try/except.
5. **Chat interface** - `st.session_state.history` stores every (description, caption) pair, and the last 3 are displayed with `st.chat_message("user")` and `st.chat_message("assistant")` bubbles.

## Screenshot section (add before submission)
- Screenshot of the app home page: ______
- Screenshot after generating a caption: ______
