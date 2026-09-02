import streamlit as st
import time

st.set_page_config(
    page_title="Personal Assistant",
    page_icon="🤖"
)

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []


def detect_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["booking", "bookings", "ticket", "tickets"]):
        return "show_bookings"

    if any(word in text for word in ["play", "song", "music"]):
        return "play_music"

    if any(word in text for word in ["weather", "temperature", "forecast"]):
        return "get_weather"

    return "unknown"


def select_tool(intent):
    tools = {
        "show_bookings": "BookMyShowAPI",
        "play_music": "SpotifyAPI",
        "get_weather": "OpenMeteoAPI",
        "unknown": "GeneralAssistant"
    }

    return tools[intent]


def generate_response(intent):
    responses = {
        "show_bookings": "You have 2 upcoming movie bookings.",
        "play_music": "Playing your requested music.",
        "get_weather": "The current weather information is being fetched.",
        "unknown": "I can help with bookings, music, and weather."
    }

    return responses[intent]


st.title("🤖 Personal Assistant Agent")
st.write("Ask me about movie bookings, music, or weather.")

user_input = st.chat_input("Enter your request...")

if user_input:
    intent = detect_intent(user_input)
    tool = select_tool(intent)

    with st.spinner("Gathering information..."):
        time.sleep(1)

    with st.spinner(f"Executing {tool}..."):
        time.sleep(1)
        response = generate_response(intent)

    st.session_state.conversation_history.append(
        {
            "user": user_input,
            "assistant": response
        }
    )

    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)

st.subheader("Recent Conversation")

history = st.session_state.conversation_history[-3:]

if history:
    for exchange in history:
        st.chat_message("user").write(exchange["user"])
        st.chat_message("assistant").write(exchange["assistant"])
else:
    st.info("No conversation history yet.")