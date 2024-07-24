import streamlit as st
st.set_page_config(page_icon="🕷️")
st.title("manoj naik",anchor=False)
st.subheader("Gen AI developer|photography|content creater")
with st.container(border=2):
    st.warning("I am a stundet............")
    st.info("Iam a photographer")
col1, col2, col3=st.columns(3)
with col1:
    with st.expander(label="know me more",expanded=False):
            st.info("hii........")
    with col2:
        st.image("manoj.jpg")
    with col3:
        with st.expander(label="know me ",expanded=False):
            st.warning("hello........")