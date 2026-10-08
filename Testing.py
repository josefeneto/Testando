import random
import sys

import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx

msg = "Roll a dice!"
FACES = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]


def main():
    st.set_page_config(page_title="Dice Roller", page_icon="🎲")
    st.title(msg)

    # session_state keeps values between reruns (every click reruns the script)
    if "history" not in st.session_state:
        st.session_state.history = []

    if st.button("Roll", type="primary"):
        st.session_state.history.append(random.randint(1, 6))

    if st.session_state.history:
        value = st.session_state.history[-1]
        st.markdown(f"<div style='font-size:120px'>{FACES[value - 1]}</div>", unsafe_allow_html=True)
        st.subheader(f"You rolled a {value}")
        st.write("History:", ", ".join(map(str, st.session_state.history)))
    else:
        st.markdown("<div style='font-size:120px'>🎲</div>", unsafe_allow_html=True)
        st.write("Click the button to roll")


if get_script_run_ctx() is None:
    # Started with "python Testing.py" (e.g. F5) -> relaunch via "streamlit run"
    from streamlit.web import cli as stcli

    sys.argv = ["streamlit", "run", __file__]
    sys.exit(stcli.main())
else:
    main()
