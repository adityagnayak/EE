# app.py
import streamlit as st
from content import LANDING_TEXT, PRODUCT_INFO, PRICING_TIERS
from styles import get_external_css

# Page Config
st.set_page_config(page_title="EarnedEdge | Project Controls", page_icon="📈", layout="wide")

# Inject Styles
st.markdown(get_external_css(), unsafe_allow_html=True)

# Tabs Navigation
tabs = st.tabs(["🏠 Home", "🛠 Product", "💰 Pricing", "📅 Booking", "📩 Contact"])

# Tab 1: Home
with tabs[0]:
    st.markdown(f"""
        <div class="hero-box">
            <h1>{LANDING_TEXT['hero_title']}</h1>
            <p style='font-size: 1.2rem; color: #556B82;'>{LANDING_TEXT['hero_subtitle']}</p>
            <br>
            <h2 style='color: #0070F2;'>{LANDING_TEXT['hero_tagline']}</h2>
            <p>{LANDING_TEXT['hero_description']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    c1.success("**Compliance-First**")
    c2.info("**AI-Powered Insight**")
    c3.warning("**Fixed Retainer**")

# Tab 2: Product
with tabs[1]:
    st.header("The System: ControlsDesk Architecture")
    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("Process")
        for item in PRODUCT_INFO['how_it_works']:
            st.write(item)
    with col_right:
        st.subheader("Deliverables")
        for item in PRODUCT_INFO['deliverables']:
            st.write(f"✅ {item}")

# Tab 3: Pricing
with tabs[2]:
    st.header("Transparent Pricing")
    cols = st.columns(len(PRICING_TIERS))
    for i, (name, data) in enumerate(PRICING_TIERS.items()):
        with cols[i]:
            features_html = "".join([f"<p>{f}</p>" for f in data['features']])
            st.markdown(f"""
                <div class="pricing-card" style="border-top: 5px solid {data['color']};">
                    <h3 style="color: {data['color']};">{name}</h3>
                    <h2>{data['price']}<span style='font-size:0.8rem;'>/mo</span></h2>
                    <hr>
                    {features_html}
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Choose {name}", key=f"btn_{name}"):
                st.info("Directing to secure checkout/onboarding...")

# Tab 4: Booking
with tabs[3]:
    st.header("Schedule a Consultation")
    st.write("Book a 30-minute discovery call via Google Meet.")
    st.link_button("📅 Schedule Meeting", "https://calendar.google.com/calendar/appointments/schedules/")

# Tab 5: Contact
with tabs[4]:
    st.header("Contact Us")
    with st.form("contact"):
        st.text_input("Name")
        st.text_input("Email")
        st.text_area("Message")
        if st.form_submit_button("Send to EarnedEdge"):
            st.success("Message sent to Slack. Our team will contact you shortly.")

# Footer
st.markdown("---")
st.caption("© 2026 EarnedEdge. ISO 9001 Compliant Procedures. Built for West Midlands Infrastructure.")
