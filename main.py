import streamlit as st
from PIL import Image, ImageDraw

from core.pdf_parser import extract_pdf_layout
from core.text_merger import merge_words
from core.direction_math import centroid, angle_from_center, angle_to_direction
from utils.csv_exporter import export_to_csv
from agents.component_cleaner import ComponentCleaner

st.set_page_config(layout="wide")
st.title("🧭 Vaastu AI – Geometry-Based Plan Analyzer")

cleaner = ComponentCleaner()

uploaded = st.file_uploader("Upload Architectural PDF", type=["pdf"])

if uploaded:
    with open("data/temp_plan.pdf", "wb") as f:
        f.write(uploaded.read())

    pages = extract_pdf_layout("data/temp_plan.pdf")
    rows = []

    for page_data in pages:
        st.subheader(f"Page {page_data['page']}")

        words = page_data["words"]
        blocks = merge_words(words)

        page_cx = page_data["width"] / 2
        page_cy = page_data["height"] / 2

        for b in blocks:
            cx, cy = centroid(b)
            angle = angle_from_center(cx, cy, page_cx, page_cy)
            direction = angle_to_direction(angle)

            rows.append({
                "page_number": page_data["page"],
                "component": b["text"],
                "direction": direction
            })

    
    with st.spinner("Component Cleaning in progress..."):
        for r in rows:
            r["component"] = cleaner.clean(r["component"])

    csv, df = export_to_csv(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.download_button("⬇ Download Vaastu CSV", csv, "vaastu_analysis.csv")
    st.success("Analysis complete!")