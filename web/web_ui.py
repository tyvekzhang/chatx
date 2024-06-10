import os
import time

import requests
import streamlit as st

st.set_page_config(
    "chatx",
    os.path.join("../doc/img", "chatx.ico"),
    initial_sidebar_state="expanded",
)

st.title("Chatx")
headers = {"Content-Type": "application/json"}

st.markdown("你好, 欢迎来到AI的世界! &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower:")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("请问有什么能帮助您的?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        data = {
          "question": f"{prompt}",
          "collection_name": "wujilab",
          "chat_history": [],
          "limit": 0,
          "stream": False,
          "strict_model": False
        }
        endpoint_url = "http://121.199.73.10:8888/api/v1/chat"
        response = requests.post(
            endpoint_url,
            headers=headers,
            json=data,
            timeout=(10, 300),
            stream=False,
        )
        response_json = response.json()
        result = response_json["data"]

        def response_generator():
            for word in result.split():
                yield word + " "
                time.sleep(0.3)
        response = st.write_stream(response_generator())
    st.session_state.messages.append({"role": "assistant", "content": response})

