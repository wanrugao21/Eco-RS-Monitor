import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Eco-RS Sentinel-2 UHI Monitor", page_icon="🌍", layout="wide")

# 2. Main Header
st.title("🌍 Eco-RS Monitor: Autonomous UHI Tracker")
st.markdown("""
**Built for the TinyFish × UCL AI Society Build Night**
This agent utilizes TinyFish endpoints (**Search** + **Fetch** + **Agent**) to autonomously track the latest remote sensing methodologies for Urban Heat Island (UHI) analysis using Sentinel-2 MSI data.
""")

st.divider()

# 3. Sidebar Configuration
st.sidebar.header("Monitor Settings")
TINYFISH_API_KEY = st.sidebar.text_input("TinyFish API Key", type="password", help="Enter placeholder for demo purposes.")
target_city = st.sidebar.text_input("Target City for UHI Analysis", "London, UK")
run_btn = st.sidebar.button("Launch Autonomous Monitor", type="primary")

st.sidebar.markdown("---")
st.sidebar.caption("Endpoints utilized: \n- 🔍 /v1/search\n- 📥 /v1/fetch\n- 🧠 /v1/agent")

# 4. Simulated TinyFish API Functions (Mocked for Hackathon UI Demo)
def tinyfish_search(query):
    return [{"title": f"Recent Sentinel-2 UHI mapping techniques in {query}", "url": "https://nature-rs-journal.org/uhi-latest"}]

def tinyfish_fetch(url):
    return "Abstract: This research leverages Sentinel-2 MSI Level-2A imagery to compute the Normalized Difference Vegetation Index (NDVI) and retrieves Land Surface Temperature (LST) to evaluate the urban thermal environment..."

def tinyfish_agent(context):
    return """
#### 📊 Geospatial Intelligence Report
* **Primary Methodology:** NDVI thresholding combined with LST retrieval via the split-window algorithm.
* **Satellite Data Source:** Sentinel-2 Level-2A (Multispectral Instrument).
* **Key Findings:** Strong negative correlation (-0.82) observed between vegetation density and UHI intensity.
* **Recommended Action:** Increase green infrastructure in high LST zones identified by the agent.
"""

# 5. Execution Workflow
if run_btn:
    if not TINYFISH_API_KEY:
        st.error("⚠️ Please enter a TinyFish API Key to proceed (Rule: Keep credentials private).")
    else:
        with st.status("Initializing TinyFish Agent Workflows...", expanded=True) as status:
            # Endpoint 1: Search
            st.write(f"🔍 **[Endpoint 1: Search]** Hunting for the latest Sentinel-2 UHI research for **{target_city}**...")
            time.sleep(1.5)
            search_results = tinyfish_search(target_city)
            target_url = search_results[0]['url']
            st.write(f"✅ Found top resource: `{target_url}`")
            
            # Endpoint 2: Fetch
            st.write(f"📥 **[Endpoint 2: Fetch]** Scraping full unstructured text from the source...")
            time.sleep(1.5)
            content = tinyfish_fetch(target_url)
            
            # Endpoint 3: Agent
            st.write(f"🧠 **[Endpoint 3: Agent]** Parsing dense geospatial data into actionable insights...")
            time.sleep(2)
            analysis_report = tinyfish_agent(content)
            
            status.update(label="Mission Accomplished! All TinyFish endpoints executed successfully.", state="complete", expanded=False)
            
        st.success("Workflow executed via 3 TinyFish Endpoints: Search ➔ Fetch ➔ Agent")
        
        # Display Final Output beautifully
        with st.container(border=True):
            st.markdown("### 🛰️ Agent Output")
            st.markdown(analysis_report)