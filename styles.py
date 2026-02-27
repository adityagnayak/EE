def get_external_css():
    return """
    <style>
    /* 1. GLOBAL FONTS & COLORS */
    @import url('https://fonts.cdnfonts.com/css/helvetica-neue-9');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        background-color: #E6F3FF;  /* Sky Blue Background */
        color: #000000;             /* Black Text */
    }

    /* 2. HIDE STREAMLIT DEFAULT ELEMENTS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 3. CONTAINER STYLING */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1100px;
    }

    /* 4. HERO SECTION */
    .hero-box {
        background-color: #FFFFFF; /* White box for contrast against blue */
        padding: 3rem;
        border-radius: 15px;
        border-left: 8px solid #0070F2; /* SAP Blue Accent */
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .hero-box h1, .hero-box h2, .hero-box p {
        color: #000000 !important; /* Force black text inside hero */
    }

    /* 5. PRICING CARDS */
    .pricing-card {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #e9ecef;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
        height: 100%;
        color: #000000;
    }

    /* 6. BUTTONS */
    .stButton>button {
        background-color: #0070F2;
        color: white;
        border-radius: 8px;
        width: 100%;
        border: none;
        padding: 0.6rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #005bb5;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    /* 7. FORM INPUTS */
    /* Ensure text inside input boxes is visible */
    input, textarea {
        color: #000000 !important;
        background-color: #FFFFFF !important;
    }

    /* 8. TABS */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: #FFFFFF;
        padding: 10px 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px;
        color: #000000;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        color: #0070F2 !important;
        border-bottom: 3px solid #0070F2;
    }

    /* 9. MOBILE RESPONSIVENESS */
    @media (max-width: 768px) {
        .pricing-card { 
            height: auto !important; 
            margin-bottom: 1.5rem;
        }
        .hero-box {
            padding: 1.5rem;
        }
    }
    </style>
    """
