import streamlit as st
from utils import generate_script

st.title("视频脚本生成器")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

subject = st.text_input("请输入视频主题：")
video_length = st.number_input("请输入视频时长（分钟）：", min_value =0.1, max_value = 10.0, step = 0.5)
creativity = st.slider("请选择视频脚本的的创造力（数字越小越严谨，数字越大越多样）：", min_value=0.0, max_value=1.0, value=0.6, step=0.1)
submission = st.button("生成脚本")

if submission and not openai_api_key:
    st.info("请在侧边栏输入OpenAI API密钥！")
    st.stop()
if submission and not subject:
    st.info("请输入视频主题！")
    st.stop()
if submission and not video_length >= 0.1:
    st.info("视频长度需至少为0.1分钟（6秒）！")
    st.stop()
if submission:
    with st.spinner("正在生成脚本，请稍候..."):
        title, script, search_results = generate_script(subject, video_length, creativity, openai_api_key)
    st.success("视频脚本已生成！")
    st.subheader("视频标题：")
    st.write(title)
    st.subheader("视频脚本：")
    st.write(script)
    with st.expander("查看维基百科搜索结果（仅供参考）："):
        st.write(search_results)