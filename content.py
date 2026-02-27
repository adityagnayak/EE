# content.py

LANDING_TEXT = {
    "hero_title": "EarnedEdge",
    "hero_subtitle": "Fractional Project Controls & EVM for UK Engineering SMEs",
    "hero_tagline": "Tier 1 Reporting. SME Budget.",
    "hero_description": """Bridge the gap between chaotic spreadsheets and expensive day-rate consultants. 
    Automated, audit-ready project governance for high-growth contractors winning public-sector and Tier 1 subcontracts.""",
}

PRODUCT_INFO = {
    "how_it_works": [
        "**Data Export:** Send us monthly CSV/Excel data from your ERP or PM tool.",
        "**Processing:** Our engine runs EVM calculations (CPI, SPI, EAC, VAC).",
        "**Narrative:** Claude generates deep-dive commentary on variances.",
        "**Review:** A human analyst signs off the final board-ready pack."
    ],
    "deliverables": [
        "WBS Structure Setup & Governance",
        "S-Curve Progress Tracking",
        "Forecast-to-Complete (ETC/EAC)",
        "Board-Level Financial Status Packs"
    ]
}

PRICING_TIERS = {
    "Foundation": {
        "price": "£1,800",
        "features": ["WBS Setup", "Monthly EVM Reports", "Basic Variance Analysis", "Email Support"],
        "color": "#0070F2" # SAP Horizon Blue
    },
    "Performance": {
        "price": "£2,600",
        "features": ["Everything in Foundation", "Forecast-to-Complete", "Board-Level Status Packs", "Monthly Strategy Call"],
        "color": "#107E3E" # SAP Positive Green
    },
    "Strategic": {
        "price": "£3,500",
        "features": ["Everything in Performance", "Multi-Currency (FX)", "Custom API Connectors", "24h Support SLA"],
        "color": "#F0AB00" # SAP Critical/Gold
    }
}
