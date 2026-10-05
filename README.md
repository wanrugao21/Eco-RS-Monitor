# 🌍 Eco-RS Monitor: Autonomous UHI Tracker

**Built for the TinyFish × UCL AI Society Build Night**

## 🚀 Project Overview
Eco-RS Monitor is an autonomous scientific intelligence agent designed for environmental scientists and urban planners. It solves a highly technical pain point: automatically tracking and synthesizing the latest remote sensing methodologies applied to Urban Heat Island (UHI) analysis using satellite imagery.

## 🛠️ How TinyFish is Used (Hitting the 200 pts Tier)
This web app successfully integrates **3 TinyFish Endpoints** to create a seamless, end-to-end data pipeline:

1. **🔍 Search Endpoint (`/v1/search`):** Hunts the live web for the most recent open-access academic papers regarding Sentinel-2 MSI data and UHI analysis for a specific target city (e.g., London).
2. **📥 Fetch Endpoint (`/v1/fetch`):** Scrapes the full unstructured abstract and text from the top research result.
3. **🧠 Agent Endpoint (`/v1/agent`):** Acts as a geospatial expert, parsing the dense text to extract specific methodologies (e.g., NDVI thresholds, LST split-window algorithms) and outputs a clean, actionable `Geospatial Intelligence Report`.
