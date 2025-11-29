"""Phoenix AI Buddy chat interface with custom logo."""
import streamlit as st
from datetime import datetime
import os

from src.core.session_manager import SessionManager
from src.core.observability import ObservabilityManager
from src.core.orchestrator import OrchestratorAgent
from src.agents import (
    ConceptExplainerAgent, CodeReviewerAgent, DebuggingAgent,
    PracticeGeneratorAgent, CodeGeneratorAgent, GeneralChatAgent
)


def initialize_system():
    """Initialize the system."""
    session_mgr = SessionManager()
    session_mgr.create_session("user", "beginner")
    observ = ObservabilityManager()
    orchestrator = OrchestratorAgent(session_mgr, observ)
    
    orchestrator.register_agent("ConceptExplainer", ConceptExplainerAgent())
    orchestrator.register_agent("CodeReviewer", CodeReviewerAgent())
    orchestrator.register_agent("DebuggingAgent", DebuggingAgent())
    orchestrator.register_agent("PracticeGenerator", PracticeGeneratorAgent())
    orchestrator.register_agent("CodeGenerator", CodeGeneratorAgent())
    orchestrator.register_agent("GeneralChatAgent", GeneralChatAgent())

    return session_mgr, observ, orchestrator


def setup_page_config():
    """Configure the page with Phoenix AI Buddy branding."""
    # Your logo path
    logo_path = "src/assets/icon1.png"
    
    try:
        if os.path.exists(logo_path):
            st.set_page_config(
                page_title="Phoenix AI Buddy",
                page_icon=logo_path,
                layout="centered",
                initial_sidebar_state="collapsed"
            )
        else:
            st.set_page_config(
                page_title="Phoenix AI Buddy",
                page_icon="🐦‍🔥",
                layout="centered",
                initial_sidebar_state="collapsed"
            )
    except Exception as e:
        st.set_page_config(
            page_title="Phoenix AI Buddy",
            page_icon="🐦‍🔥",
            layout="centered",
            initial_sidebar_state="collapsed"
        )
    
    # CSS with optimized spacing and flexible chat width
    st.markdown("""
    <style>
    .main {
        padding: 0 !important;
        background-color: #000000 !important;
    }
    
    .stApp {
        background-color: #000000 !important;
    }
    
    .header-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: black;
        padding: 0px 20px 0px 50px;
        border-bottom: 2px solid gold;
        z-index: 9999 !important;
        height: 1px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    
    .header-content {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        width: 100%;
        gap: 2px;
    }
    
    .logo-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 65px;
        margin-left:100px;
    }
    
    .title-wrapper {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        height: 65px;
        margin-left: 2px;
    }
    
    .logo-title {
        font-size: 1.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FF6B35 0%, #FF8E53 20%, #F7931E 40%, #FFB74D 60%, #FFD54F 80%, #FFF176 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
        text-shadow: 0 0 20px rgba(255, 107, 53, 0.5);
        line-height: 1;
        margin: 0;
        padding: 0;
        position:relative;
        top:-70px;
        left:80px;
        
    }
    
    .logo-subtitle {
        font-size: 0.65rem;
        color: #FFB74D;
        font-weight: 500;
        letter-spacing: 0.5px;
        text-shadow: 0 0 10px rgba(255, 183, 77, 0.3);
        line-height: 1.1;
        margin-top: 2px;
        margin-bottom: 0;
        padding: 0;
        position:relative;
        top:-70px;
        left:80px;
    }
    
    .user-message {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        color: #ffffff;
        padding: 10px 14px;
        border-radius: 16px 16px 4px 16px;
        margin: 4px 0;
        max-width: fit-content;
        margin-left: auto;
        margin-right: 10px;
        margin-bottom:8px;
        border: 1px solid #333333;
        box-shadow: 0 3px 12px rgba(255, 107, 53, 0.2);
        word-wrap: break-word;
    }
    
    .assistant-message {
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
        color: #ffffff;
        padding: 10px 14px;
        border-radius: 16px 16px 16px 4px;
        margin: 4px 0;
        max-width: 900px;
        margin-right: auto;
        margin-left: 10px;
        margin-bottom:20px;
        border: 1px solid #444444;
        box-shadow: 0 3px 12px rgba(255, 183, 77, 0.15);
        word-wrap: break-word;
    }
    
    .thinking-message {
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
        color: #ffffff;
        padding: 10px 14px;
        border-radius: 16px 16px 16px 4px;
        margin: 4px 0;
        max-width: fit-content;
        margin-right: auto;
        margin-left: 10px;
        margin-bottom:20px;
        border: 1px solid #444444;
        box-shadow: 0 3px 12px rgba(255, 183, 77, 0.15);
        word-wrap: break-word;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Position spinner on the left */
    [data-testid="stSpinner"] {
        margin-left: 10px !important;
        margin-right: auto !important;
        justify-content: flex-start !important;
    }
    
    .stSpinner > div {
        margin-left: 0 !important;
    }
    
    .stChatInput {
        position: fixed;
        bottom: 5px;
        left: 50%;
        transform: translateX(-50%);
        width: 96%;
        max-width: 800px;
        background: #1a1a1a;
        border-radius: 18px;
        padding: 8px;
        box-shadow: 0 3px 15px rgba(255, 107, 53, 0.25);
        border: 2px solid #333333;
    }
    
    .stChatInput input {
        border: none !important;
        box-shadow: none !important;
        font-size: 0.95rem !important;
        background: #1a1a1a !important;
        color: #ffffff !important;
    }
    
    .stChatInput input:focus {
        border: none !important;
        box-shadow: none !important;
    }
    
    .stChatInput input::placeholder {
        color: #888888 !important;
    }
    
    #root > div:nth-child(1) > div > div > div > div > section > div {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        background-color: #000000 !important;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #000000 !important;
    }
    
    /* Hide everything except chat and header */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Remove unnecessary containers and spacing */
    .stApp > header {
        display: none !important;
    }
    
    div[data-testid="stHeader"] {
        display: none !important;
    }
    
    .main .block-container {
        padding-top: 0 !important;
        padding-bottom: 25px !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        z-index: 1 !important;
    }
    
    /* Remove any default Streamlit spacing above content */
    .element-container {
        margin-top: 0 !important;
        padding-top: 0 !important;
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
    }
    
    /* Move spacing to input box area - increase height up to input box */
    div[data-testid="stChatInputContainer"] {
        margin-top: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        margin-bottom: 0 !important;
        height: auto !important;
    }
    
    /* Remove all containers above header/logo */
    .header-container {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    .header-container::before,
    .header-container::after {
        display: none !important;
    }
    
    /* Ensure header is above all containers */
    .header-container,
    .header-content,
    .logo-wrapper,
    .title-wrapper {
        z-index: 9999 !important;
        position: relative;
    }
    
    /* Remove any parent containers wrapping the header and ensure they don't cover it */
    .main > div:first-child,
    section[data-testid="stMain"] > div:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 25px !important;
        z-index: 1 !important;
    }
    
    /* Ensure Streamlit containers don't cover the header */
    .block-container,
    div[data-testid="stVerticalBlock"],
    div[data-testid="stHorizontalBlock"] {
        z-index: 1 !important;
    }
    
    /* Remove containers above input box */
    .stChatInput {
        margin-top: 0 !important;
        z-index: 9998 !important;
    }
    
    .stChatInput::before,
    .stChatInput::after {
        display: none !important;
    }
    
    /* Move spacing to wrapper divs around chat input - match input box height */
    div:has(> .stChatInput),
    div:has([data-testid="stChatInput"]) {
        margin-top: 0 !important;
        padding-top: 0 !important;
        margin-bottom: 0 !important;
        padding-bottom: 25px !important;
    }
    
    /* Remove spacing from all Streamlit containers */
    [class*="st"] {
        margin-top: 0 !important;
    }
    
    /* Specifically target containers that might wrap header */
    .main > div > div:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 15px !important;
        z-index: 1 !important;
    }
    
    /* Remove any spacing containers - move spacing to input box area */
    .stApp > div > div:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 15px !important;
        z-index: 1 !important;
    }
    
    /* Remove Streamlit container wrappers */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    
    div[data-testid="stVerticalBlock"] {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    div[data-testid="stHorizontalBlock"] {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Remove wrapper divs around content */
    .main > div {
        padding: 0 !important;
    }
    
    section[data-testid="stMain"] > div {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Remove any column wrappers */
    [data-testid="column"] {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 5px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1a1a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #FF6B35;
        border-radius: 2px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #FF8E53;
    }
    
    /* Flexible message containers */
    .message-container {
        display: flex;
        width: 60%;
        justify-content: center;
        margin: 0 auto;
    }
    
    /* Add padding to content area for fixed header and input */
    section[data-testid="stMain"] {
        padding-top: 65px !important;
        padding-bottom: 55px !important;
        z-index: 1 !important;
    }
    </style>
    """, unsafe_allow_html=True)


def render_header_with_logo():
    """Render header positioned at the very top with perfectly aligned logo and title."""
    logo_path = "src/assets/icon1.png"
    
    # Fixed header at the very top with perfect alignment
    st.markdown("""
    <div class="header-container">
        <div class="header-content">
            <div class="logo-wrapper">
    """, unsafe_allow_html=True)
    
    # Logo column
    try:
        if os.path.exists(logo_path):
            st.image(logo_path, width=70)
        else:
            st.markdown('<div style="font-size: 2rem;">🐦‍🔥</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown('<div style="font-size: 2rem;">🐦‍🔥</div>', unsafe_allow_html=True)
    
    st.markdown("""
            </div>
            <div class="title-wrapper">
                <div class="logo-title">Phoenix AI Buddy</div>
                <div class="logo-subtitle">Your Intelligent Learning Companion</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def run_streamlit_app():
    """Run the Phoenix AI Buddy chat app."""
    setup_page_config()
    
    # Initialize system
    if "system_initialized" not in st.session_state:
        st.session_state.session_mgr, st.session_state.observ, st.session_state.orchestrator = initialize_system()
        st.session_state.system_initialized = True
    
    # Render header with logo - this will be fixed at the very top
    render_header_with_logo()
    
    # Chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display messages with flexible width
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="message-container user-container">
                <div class="user-message">
                    {message["content"]}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="message-container assistant-container">
                <div class="assistant-message">
                    {message["content"]}
            
            """, unsafe_allow_html=True)
    
    # Chat input - positioned very high with flexible width
    user_input = st.chat_input("Ask your AI Buddy...")
    
    if user_input:
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now().isoformat()
        })
        
        # Show thinking indicator on the left
        st.markdown("""
        <div class="message-container assistant-container">
            <div class="thinking-message">
                🔥 Thinking...
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Process with orchestrator
        result = st.session_state.orchestrator.process_query(user_input, "")
        final_response = result.get("final_response", "No response generated.")
        
        # Add assistant response
        st.session_state.messages.append({
            "role": "assistant", 
            "content": final_response,
            "timestamp": datetime.now().isoformat()
        })
        
        # Use st.rerun() instead of st.experimental_rerun()
        st.rerun()


if __name__ == "__main__":
    run_streamlit_app()