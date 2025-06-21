import streamlit as st
import base64
import time
import streamlit.components.v1 as components


# Function to inject JavaScript speech synthesis
def speak_js(text):
    js_code = f"""
    <script>
        var msg = new SpeechSynthesisUtterance({text!r});
        msg.rate = 1;
        msg.pitch = 1;
        window.speechSynthesis.speak(msg);
    </script>
    """
    components.html(js_code, height=0)

# Unified response + voice
def respond_with_voice(text):
    return text



# ✅ Must be the first Streamlit command
st.set_page_config(
    page_title="Tata BlueScope Steel Chatbot",
    page_icon="logotbsl.jpg",  # Now directly in the root folder
    layout="centered"
)

# ✅ Function to set background with transparency overlay
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(255,255,255,0.45), rgba(255,255,255,0.45)),
                        url("data:image/gif;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
    """, unsafe_allow_html=True)

# ✅ Function to set sidebar background
def set_sidebar_background(image_path):
    with open(image_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        [data-testid="stSidebar"] > div:first-child {{
             background: linear-gradient(rgba(255,255,255,0.45), rgba(255,255,255,0.45)),
                        url("data:image/jpg;base64,{img_data}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
    """, unsafe_allow_html=True)

# ✅ Apply background
set_background("chatbot.gif")
set_sidebar_background("sidepanel.jpg")


# ✅ Hide Streamlit default header and footer (including the Deploy button area)
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



# --- Theme toggle with checkbox ---
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

st.sidebar.title("Settings")
st.sidebar.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode, key="dark_mode_checkbox", on_change=toggle_theme)

# --- Uniform button width style ---
button_style = """
<style>
    .stButton > button {
        width: 100% !important;
        min-width: 200px;
        text-align: center;
        padding: 0.5em 1em;
        margin-bottom: 10px;
        border-radius: 8px;
        font-weight: 500;
    }
</style>
"""

# --- CSS for themes and chat bubbles ---
light_css = """
<style>
body {
    background-color: #f4f4f9;
    color: #000;
    font-family: 'Segoe UI', sans-serif;
}
.stButton>button {
        background-color: #00adb5;
        color: black;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        transition: background-color 0.3s ease-in-out;
    }
stButton>button:hover {
        background-color: #1abc9c;
        color: black;
        font-weight: bold;
    }

.sidebar .sidebar-content {
    background-color: #d0f0f5;
}
.chatbot-container {
    max-width: 700px;
    margin: auto;
}
.user-msg {
    background:#4e4e50; 
    color:#fff; 
    padding:10px; 
    border-radius:10px; 
    margin-bottom:5px; 
    max-width:70%; 
    text-align:left;
    margin-left:auto;
    word-wrap: break-word;
}
.bot-msg {
    background: #00adb5; 
    color:#333; 
    padding:10px; 
    border-radius:10px; 
    margin-bottom:15px; 
    max-width:70%;
    text-align:left;
    word-wrap: break-word;
}
a {
    color: #0066cc;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
"""

dark_css = """
<style>
body {
    background-color: #1e1e1e;
    color: #fff;
    font-family: 'Segoe UI', sans-serif;
}
 .stButton>button {
        background-color: #2c3e50;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        transition: background-color 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #eeeeee;
        color: #111;
        font-weight: bold;
    }

.sidebar .sidebar-content {
    background-color: #2e2e2e;
}
.chatbot-container {
    max-width: 700px;
    margin: auto;
}
.user-msg {
    background:#810c51; 
    color:#fff; 
    padding:10px; 
    border-radius:10px; 
    margin-bottom:5px; 
    max-width:70%; 
    text-align: left;
    margin-left:auto;
    word-wrap: break-word;
}
.bot-msg {
    background:#2e2e2e; 
    color:#cddcfe; 
    padding:10px; 
    border-radius:10px; 
    margin-bottom:15px; 
    max-width:70%;
    text-align:left;
    word-wrap: break-word;
}
a {
    color: #4da6ff;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
"""

# Apply CSS
st.markdown(button_style + (dark_css if st.session_state.dark_mode else light_css), unsafe_allow_html=True)

if "show_about" not in st.session_state:
    st.session_state.show_about = False
if "show_headquarters" not in st.session_state:
    st.session_state.show_headquarters = False
if "show_manufacturers" not in st.session_state:
    st.session_state.show_manufacturers = False
if "show_products" not in st.session_state:
    st.session_state.show_products = False

# Sidebar navigation buttons
st.sidebar.title("Tata BlueScope Steel Info")
if st.sidebar.button("🏢 About TBSL"):
    st.session_state.show_about = not st.session_state.show_about
    if st.session_state.show_about:
        st.sidebar.info(
        "🏗 Tata BlueScope Steel is a joint venture between Tata Steel (India) and BlueScope Steel (Australia), established in 2005.\n\n"
        "📍 Headquartered in Pune, it specializes in coated steel products and pre-engineered building solutions.\n\n"
        "🏭 Manufacturing Facilities:\n"
        "- Pune\n"
        "- Bhiwadi\n"
        "- Sriperumbudur\n\n"
        "🏘 Sectors Served:\n"
        "- Residential\n"
        "- Commercial\n"
        "- Industrial\n\n"
        "🌱 Committed to:\n"
        "- Sustainability\n"
        "- Innovation in steel solutions\n\n"
        "🏷 Major Brands:\n"
        "- ZINCALUME®\n"
        "- COLORBOND®\n"
        "- LYSAGHT®\n"
        "- DURASHINE®\n"
        "- BUTLER®\n\n"
        "🌐 Operational Region:\n"
        "- India\n"
        "- SAARC region\n\n"
        "🏢 Additional Manufacturing Units:\n"
        "- Jamshedpur\n"
        "- Pune\n"
        "- Chennai (Sriperumbudur)\n"
        "- Bhiwadi\n\n"
        "Tata BlueScope Steel is recognized for innovation, sustainability, and delivering high-quality steel solutions."
    )
if st.sidebar.button("📍 Headquarters"):
    st.session_state.show_headquarters = not st.session_state.show_headquarters
if st.session_state.show_headquarters:
    st.sidebar.info("🏢 Tata BlueScope Steel is headquartered in Pune, Maharashtra, India.")
if st.sidebar.button("🏭 Manufacturers"):
    st.session_state.show_manufacturers = not st.session_state.show_manufacturers
if st.session_state.show_manufacturers:
    st.sidebar.info("🏗 Tata BlueScope Steel operates state-of-the-art facilities across India including Pune, Bhiwadi, and Sriperumbudur.")
if st.sidebar.button("🛠 Main Products"):
    st.session_state.show_products = not st.session_state.show_products
if st.session_state.show_products:
    st.sidebar.markdown("""
        <div style="
        background-color: #d4e1ec;
        border: 1px solid #c3e6cb;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 14px;
        color: #164976;
        font-weight: 500;
    ">
    🔹 DURASHINE® Sheets<br>
    🔹 LYSAGHT® Building Solutions<br>
    🔹 ZINCALUME® Steel<br>
    🔹 COLORBOND® Steel<br>
    🔹 Pre-engineered Building Systems
    """, unsafe_allow_html=True)
if "show_sidebar_map" not in st.session_state:
    st.session_state.show_sidebar_map = False
if st.sidebar.button("🗺 Map"):
     st.session_state.show_sidebar_map = not st.session_state.show_sidebar_map
# Show map inside sidebar if triggered
if st.session_state.show_sidebar_map:
    with st.sidebar:
        st.markdown("###  🗺️  Jamshedpur Plant")
        components.iframe(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3672.488394494652!2d86.2332973!3d22.8134767!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39f5e28a5ce096f5%3A0x8afcdff3cf6a23a6!2sTata%20BlueScope%20Steel%20Pvt.%20Ltd.!5e0!3m2!1sen!2sin!4v1718619123456!5m2!1sen!2sin",
            width=270,
            height=200,
            scrolling=False
        )

if st.sidebar.button("❓ Ask Query"):
    st.session_state.show_input = True


# Header
st.title("Tata BlueScope Steel Chatbot")
st.markdown("### 👋 Hello! How can I help you?")
st.markdown("##### 💬 Inspiring Possibilities.")
st.markdown("""
<div style="font-family: cursive; font-size: 15px;">
    We create and inspire smart solutions in steel, to strengthen our communities for the future.
</div>
""", unsafe_allow_html=True)

# Session states
if "show_input" not in st.session_state:
    st.session_state.show_input = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "is_typing" not in st.session_state:
    st.session_state.is_typing = False
if "feedback" not in st.session_state:
    st.session_state.feedback = {}
if "feedback_given" not in st.session_state:
    st.session_state.feedback_given = {}
if "video_display" not in st.session_state:
    st.session_state.video_display = False


# Chatbot container
chat_container = st.container()

# Input area
if st.session_state.show_input:
    with st.form(key="user_input_form_1", clear_on_submit=True):
        user_query = st.text_area("Please enter your query below:", max_chars=300, height=80, key="query_input")
        submit_button = st.form_submit_button(label="Send")
        

    if submit_button and user_query.strip():
        st.session_state.is_typing = True
        with st.spinner("Bot is typing..."):
            time.sleep(1)

        query = user_query.lower().strip()


        # Response Mapping (same as your original code)
        if "tata bluescope" in query or "about tata bluescope" in query or "about" in query or "about tbsl" in query or "tbsl" in query or "tata bluescope steel" in query: 
            response = respond_with_voice ("Tata BlueScope Steel is a joint venture between Tata Steel and BlueScope Steel, established in 2005 for coated steel and roofing solutions.")
        elif "projects" in query:
            response = respond_with_voice ("Tata BlueScope Steel supports commercial, industrial, and residential steel projects.")
        elif "locations" in query or "branches" in query or "offices" in query or "where are" in query or "location" in query: 
            response = respond_with_voice (
        "Tata BlueScope Steel Locations:\n\n"
        "Corporate Headquarters:\n"
        "The Metropolitan, Final Plot No. 27,\n"
        "Survey No. 21, Wakdewadi, Shivaji Nagar,\n"
        "Pune - 411005, Maharashtra, India.\n\n"
        "Manufacturing Plants:\n"
        "1. Jamshedpur, Jharkhand\n"
        "2. Sriperumbudur, Tamil Nadu\n"
        "3. Bhiwadi, Rajasthan\n"
        "4. Pune, Maharashtra\n\n"
        "Regional Offices:\n"
        "- North Zone: Delhi, Lucknow\n"
        "- West Zone: Mumbai, Ahmedabad\n"
        "- South Zone: Bengaluru, Hyderabad, Chennai\n"
        "- East Zone: Kolkata, Bhubaneswar"
    )
        elif "departments" in query:
            response =respond_with_voice ( "Tata BlueScope Steel has key departments like Procurement, Utilities, Finance, HR, PPC, Supply Chain, Production, Quality, and Customer Service.")
        elif "headquarter" in query or "headquarters" in query or "location" in query or "where is" in query:
            response = respond_with_voice ("The headquarters of Tata BlueScope Steel is located in Pune, Maharashtra, India.")
        elif "products" in query or "key products" in query or "main products" in query or "product" in query:
            response = respond_with_voice (
        "Tata BlueScope Steel Products:\n\n"
        "*1. Color Coated Steel:*\n"
        "   - COLORBOND® Steel\n"
        "   - DURASHINE® Sheets\n\n"
        "*2. Zinc-Aluminium Coated Steel:*\n"
        "   - ZINCALUME® Steel\n\n"
        "*3. Pre-Engineered Buildings (PEBs):*\n"
        "   - Butler® Building Systems\n"
        "   - EZYBUILD® Solutions\n\n"
        "*4. Structural Decking and Roofing Solutions:*\n"
        "   - LYSAGHT® Roofing and Walling Sheets\n"
        "   - LYSAGHT® SmartDeck™ Decking System\n\n"
        "Serving sectors like industrial, infrastructure, residential, and commercial."
    )
        elif "industries served" in query or "sectors served" in query or "industries" in query or "sectors" in query:
            response = respond_with_voice (" The company serves construction, infrastructure, industrial, and automotive sectors.")
        elif "colorbond" in query:
            response = respond_with_voice (" COLORBOND® steel is premium pre-painted steel used for roofing and wall cladding.")
        elif "lysaght" in query:
            response = respond_with_voice (" LYSAGHT® offers innovative steel building components and solutions.")
        elif "zincalume" in query:
            response = respond_with_voice("ZINCALUME® steel is known for its corrosion resistance and durability.")
        elif "sustainability" in query:
            response = respond_with_voice("Tata BlueScope focuses on eco-friendly manufacturing, energy efficiency, and recyclable steel products.")
        elif "iso" in query or "certification" in query:
            response = respond_with_voice("Tata BlueScope Steel is ISO 9001, ISO 14001, and OHSAS 18001 certified.")
        elif "vision" in query:
            response = respond_with_voice("Vision: To be the most admired steel building solutions company.")
        elif "mission" in query or "scope" in query or "goal" in query:
            response = respond_with_voice("Mission: Deliver superior value through innovation, quality, and sustainability.")
        elif "employees" in query or "team" in query:
            response = respond_with_voice("Tata BlueScope Steel values teamwork, safety, and innovation across its workforce.")
        elif "careers" in query or "job" in query:
            response = respond_with_voice("Visit the Careers section on their official website for openings.")
        elif "contact" in query or "email" in query or "phone" in query:
            response = respond_with_voice("Contact Details: Email: contact@tatabluescopesteel.com, <br> Phone: +91-20-6621 8000.")
        elif "tagline" in query or "slogan" in query or "motto" in query:
            response = respond_with_voice("Tagline: We create and inspire smart solutions in steel, to strengthen our communities for the future.")
        elif "latest update" in query:
            response = "For latest updates visit Official Site: <a href='https://tatabluescopesteel.com' target='_blank'>official site</a>"
        elif "peb" in query or "pre engineered buildings" in query:
            response = respond_with_voice (" The PEB division delivers customized steel building solutions for industrial and commercial needs.")
        elif "why join" in query or "why work" in query:
            response = respond_with_voice(" Tata BlueScope offers professional growth, innovation, and a trusted brand legacy.")
        elif "tata role" in query or "tata group" in query:
            response = respond_with_voice(" Tata Steel brings its legacy in infrastructure and materials to this strategic joint venture.")
        elif "unique" in query or "different" in query:
            response = respond_with_voice(" The blend of global technology with Tata’s trust and sustainable building focus makes it stand out.")
        elif "skills needed" in query or "skills required" in query or "skills" in query:
            response = respond_with_voice(" Required skills include engineering knowledge, communication, problem-solving, experience and teamwork.")
        elif "innovation" in query or "innovations" in query:
            response = respond_with_voice(" Tata BlueScope fosters innovation through R&D, advanced processes, and collaborative efforts.")
        elif "ceo" in query or "md" in query:
            response = respond_with_voice(" As of now, the Managing Director is Anoop Kr Trivedi. Please check official site for updates.")
        elif "values" in query:
            response = respond_with_voice(" Core values include Integrity, Responsibility, Excellence, Pioneering, and Unity.")
        elif "csr" in query or "corporate social responsibility" in query or "community" in query:
            response = respond_with_voice(" Tata BlueScope invests in education, health, environment, and community upliftment around its plants.")
        elif "established" in query or "founded" in query or "year" in query or "establishment" in query:
            response = respond_with_voice(" Tata BlueScope Steel was established in 2005 as a joint venture between Tata Steel and BlueScope Steel.")
        elif "management" in query or "leadership" in query:
            response = respond_with_voice(" Tata BlueScope Steel is led by a team of experienced leaders focused on innovation, sustainability, and operational excellence.")
        elif "partnership" in query or "joint venture" in query:
            response = respond_with_voice(" Tata BlueScope Steel is a joint venture between Tata Steel (India) and BlueScope Steel (Australia), formed in 2005.")
        elif "manufacturing" in query or "plants" in query:
            response = respond_with_voice(" TBSL has advanced manufacturing plants in Jamshedpur, Pune, Bhiwadi, and Sriperumbudur with state-of-the-art technology.")
        elif "clientele" in query or "clients" in query:
            response = respond_with_voice(" Tata BlueScope serves clients across construction, automotive, infrastructure, and residential sectors.")
        elif "environment" in query or "green" in query:
            response = respond_with_voice(" Tata BlueScope promotes green building practices and produces recyclable steel for sustainable development.")
        elif "recognition" in query or "awards" in query:
            response = respond_with_voice("Tata BlueScope has received several recognitions for quality, sustainability, and employee engagement.")
        elif "training" in query or "learning" in query:
            response = respond_with_voice(" TBSL provides continuous training programs for employee skill development and leadership growth.")
        elif "safety" in query or "workplace safety" in query:
            response = respond_with_voice(" Safety is a core value at TBSL, with strong policies and a culture of zero harm.")
        elif "support" in query or "after-sales" in query:
            response = respond_with_voice(" TBSL ensures strong after-sales support, technical assistance, and customer engagement.")
        elif "export" in query or "global" in query:
            response = respond_with_voice(" Tata BlueScope exports steel solutions to various countries, maintaining international standards and partnerships.")
        elif "listed" in query or "stock" in query:
            response = respond_with_voice(" Tata BlueScope Steel is a privately held company and not listed on stock exchanges.")
        elif "video" in query or "informational video" in query or "watch video" in query:
            response = " Here is the informational video you requested."
            st.session_state.video_display = True  # Show video
        else:
           response = "You can visit the <a href='https://tatabluescopesteel.com' target='_blank'>official site</a> for more details."

        # ✅ Append only when user_query is valid
        st.session_state.chat_history.append((user_query, response))
        st.session_state.is_typing = False


# Display chat history 
with chat_container:
    st.markdown("### 🧾 Queries")

    # Initialize feedback state
    if "feedback_given" not in st.session_state:
        st.session_state.feedback_given = {}

    for i, (q, r) in enumerate(st.session_state.chat_history, 1):
        speaker_id = f"speaker_{i}"
        safe_response = r.replace('"', '\\"').replace('\n', '\\n')

        # Show query and response
        st.markdown(f"""
            <div class="user-msg">🧑‍💻: {q}</div>
            <div class="bot-msg" style="position: relative; color: white; padding: 14px 18px; border-radius: 12px; margin: 8px 0; max-width: 700px;">
                🤖: {r}
                <span id="{speaker_id}" 
                      style="position: absolute; bottom: 8px; right: 14px; cursor: pointer;" 
                      title="Click to listen">🔊</span>
            </div>
        """, unsafe_allow_html=True)


        # Inject JavaScript for speech synthesis
        components.html(f"""
            <script>
                const btn = window.parent.document.getElementById("{speaker_id}");
                if (btn) {{
                    btn.onclick = function() {{
                        var msg = new SpeechSynthesisUtterance("{safe_response}");
                        msg.rate = 1;
                        msg.pitch = 1;
                        window.speechSynthesis.speak(msg);
                    }};
                }}
            </script>
        """, height=0)

        if "show_input" not in st.session_state:
            st.session_state.show_input = False
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        if "is_typing" not in st.session_state:
            st.session_state.is_typing = False
        if "feedback" not in st.session_state:
            st.session_state.feedback = {}

    
        # ✅ Show video *below its respective query*
        if "informational video" in r.lower():
            st.markdown("#### 🎥 Informational Video")
            try:
                with open("video.mp4", "rb") as video_file:
                    video_bytes = video_file.read()
                    st.video(video_bytes)
            except FileNotFoundError:
                st.warning("⚠️ Video file not found.")

# ✅ Add this to fix the feedback error
if "feedback" not in st.session_state:
    st.session_state.feedback = {}


# Auto-scroll (best-effort)
st.markdown("""
    <script>
    const chatContainer = window.parent.document.querySelector('.stContainer');
    if(chatContainer){
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
    </script>
""", unsafe_allow_html=True)
