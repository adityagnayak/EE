# styles.py

def get_external_css():
    return """
    <style>
    @import url('https://fonts.cdnfonts.com/css/helvetica-neue-9');
    
    html, body, [class*="css"] {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    .main .block-container {
        padding-top: 2rem;
        max-width: 1100px;
    }

    .hero-box {
        background-color: #f8f9fa;
        padding: 3rem;
        border-radius: 15px;
        border-left: 8px solid #0070F2;
        margin-bottom: 2rem;
    }

    .pricing-card {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #e9ecef;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
        height: 450px;
    }

    .stButton>button {
        background-color: #0070F2;
        color: white;
        border-radius: 8px;
        width: 100%;
        border: none;
        padding: 0.5rem;
        font-weight: 600;
    }
    
    /* Mobile Responsiveness for Cards */
    @media (max-width: 768px) {
        .pricing-card { height: auto; margin-bottom: 1rem; }
    }
    </style>
    """
