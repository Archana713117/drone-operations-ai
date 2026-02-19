
import streamlit as st
from sheets import load_sheet
from operations import find_available_pilots
from agent import extract_search_details
from assignments import suggest_assignment
from reassign import urgent_reassignment

st.set_page_config(
    page_title="Drone Operations AI",
    page_icon="🚁",
    layout="wide"
)

st.markdown("""
# 🚁 Drone Operations Coordinator AI
### Intelligent mission planning & fleet management
""")


st.write("Ask me to find pilots, assign missions, or check availability.")

# ===== Sidebar Status Panel =====
with st.sidebar:
    st.header("📊 Fleet Status")

    pilots = load_sheet("pilot_roster")
    drones = load_sheet("drone_fleet")

    available_pilots = len(pilots[pilots["status"] == "Available"])
    available_drones = len(drones[drones["status"] == "Available"])
    maintenance_drones = len(drones[drones["status"] == "maintenance"])

    st.metric("Available Pilots", available_pilots)
    st.metric("Available Drones", available_drones)
    st.metric("Drones in Maintenance", maintenance_drones)

    st.divider()

    st.subheader("💡 Try commands")
    st.caption("find mapping pilot in bangalore")
    st.caption("assign mapping mission in bangalore")
    st.caption("urgent replace mission in bangalore")


# chat input
user_message = st.chat_input("Type your request...")

if user_message:

    st.chat_message("user").write(user_message)

    msg = user_message.lower()

    if "urgent" in msg:
        _, location = extract_search_details(user_message)
        reply = urgent_reassignment(location)
        with st.chat_message("assistant"):
            st.error(reply)



    # assignment request
    elif "assign" in msg:
        skill, location = extract_search_details(user_message)
        reply = suggest_assignment(skill, location)
        with st.chat_message("assistant"):
            if "⚠" in reply:
                st.warning(reply)
            else:
                st.success(reply)


    else:
        skill, location = extract_search_details(user_message)

        if skill and location:
            pilots = load_sheet("pilot_roster")
            result = find_available_pilots(pilots, skill, location)

            if result.empty:
                 with st.chat_message("assistant"):
                    st.warning("❌ No available pilot found")
            else:
                with st.chat_message("assistant"):
                    st.info(f"Available pilots for {skill} in {location}")
                    st.dataframe(result, use_container_width=True)
        else:
            with st.chat_message("assistant"):
                st.info("Try: find mapping pilot in bangalore")


