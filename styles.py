# styles.py

def get_external_css():
    return """
    <style>
    /* 1. GLOBAL SAP-STYLE FONTS & COLORS */
    @import url('https://fonts.cdnfonts.com/css/helvetica-neue-9');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        background-color: #FFFFFF;  /* SAP White Background */
        color: #32363A;             /* SAP Dark Grey Text */
    }

    /* 2. HIDE STREAMLIT CHROME */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 3. CONTAINER STYLING */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px;
    }

    /* 4. HEADERS (High Contrast) */
    h1, h2, h3 {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    h2 {
        font-size: 1.8rem !important;
        margin-top: 1rem !important;
    }
    p, li {
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
        color: #32363A !important;
    }

    /* 5. HERO SECTION (SAP Style Banner) */
    .hero-banner {
        background-color: #F5F7F9; /* Very light grey */
        padding: 4rem 2rem;
        border-radius: 0px; /* SAP uses square or slightly rounded corners */
        border-left: 6px solid #0070F2; /* SAP Blue Accent */
        margin-bottom: 2rem;
    }

    /* 6. CARDS (Product & Pricing) */
    .sap-card {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 8px;
        padding: 2rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        height: 100%;
        transition: transform 0.2s;
    }
    .sap-card:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }

    /* 7. BUTTONS (SAP Horizon Blue) */
    .stButton>button {
        background-color: #0070F2;
        color: white;
        border-radius: 4px; /* Sharper corners like enterprise software */
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 0.9rem;
    }
    .stButton>button:hover {
        background-color: #005bb5;
        border: none;
        color: white;
    }

    /* 8. FORM INPUTS (Fixing the Invisible Label Issue) */
    .stTextInput label, .stTextArea label {
        color: #32363A !important;
        font-weight: 600;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #FFFFFF;
        border: 1px solid #89919A; /* SAP Input Border */
        color: #32363A;
        border-radius: 4px;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #0070F2;
        box-shadow: 0 0 0 1px #0070F2;
    }

    /* 9. TABS (SAP Style Underline) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: #FFFFFF;
        padding-bottom: 10px;
        border-bottom: 2px solid #E0E0E0;
    }
    .stTabs [data-baseweb="tab"] {
        height: auto;
        white-space: pre-wrap;
        background-color: transparent;
        border: none;
        color: #555;
        font-weight: 600;
        font-size: 1rem;
        padding: 10px 0;
    }
    .stTabs [aria-selected="true"] {
        color: #0070F2 !important;
        border-bottom: 4px solid #0070F2; /* Thick blue underline */
    }
    </style>
    """
