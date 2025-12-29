import streamlit as st
from utils import generate_script

# css样式背景颜色设计
st.markdown(
    """
    <style>
    /* 1. 第一个边框：包围主题和时长 */
    [data-testid="stHorizontalBlock"] {
        border: 1px solid #e6e9ef; /* 默认浅灰色边框 */
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }

    /* 2. 第二个边框：包围创意值读条 */
    .stSlider {
        border: 1px solid #e6e9ef;
        border-radius: 10px;
        padding: 20px 25px 45px 25px;
        margin-bottom: 20px;
    }

    /* 3. 亮红色开始生成按钮 */
    div.stButton > button:first-child {
        background: linear-gradient(to right, #FF4B2B, #FF416C) !important;
        border: none !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 0.6rem 2rem !important;
        transition: all 0.2s ease !important;
    }

    /* 按钮悬停效果 */
    div.stButton > button:first-child:hover {
        background: linear-gradient(to right, #FF5F43, #FF4B7D) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(255, 75, 43, 0.3) !important;
    }

    /* 隐藏页脚，保持页面干净 */
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# 正文设计
st.set_page_config(page_title="视频脚本助手", page_icon="🎬")
st.title("🎬视频脚本生成器")
st.caption("基于 AI 联想与维基百科实时搜索的创作工具")

with st.sidebar:
    st.header("🔑 密钥配置")
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    st.info("💡 提示：密钥仅用于当前运行，不会被保存。")
    st.divider()
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")


col1, col2 = st.columns([2, 1])
with col1:
    subject = st.text_input("请输入视频主题：", placeholder="例如：梁祝-永恒之爱")
with col2:
    video_length = st.number_input("请输入视频时长（分钟）：", min_value =0.0, max_value = 10.0, step = 0.5, help = "请输入0到10之间的数字")


creativity = st.slider("🧠请选择视频脚本的的创造力（数字越小越严谨，数字越大越多样）：", min_value=0.0, max_value=1.0, value=0.6, step=0.1)

submission = st.button("🚀 开始生成脚本", use_container_width=True)

if submission and not openai_api_key:
    st.info("请在侧边栏输入OpenAI API密钥！")
    st.stop()
if submission and not subject:
    st.info("请输入视频主题！")
    st.stop()
if submission and not video_length >= 0.1:
    st.info("视频时长不能为0！")
    st.stop()
if submission:
    with st.spinner("🤖 正在撰写脚本，请稍候..."):
        title, script, search_results = generate_script(subject, video_length, creativity, openai_api_key)
    st.balloons()
    st.success("✨ 视频脚本已就绪！")
    st.divider()

    st.subheader("💡视频标题：")
    st.markdown(f"##### {title}")
    st.subheader("📝脚本正文（支持复制）")
    st.text_area(label="", value=script, height=400)
    with st.expander("🔍查看维基百科搜索结果（仅供参考）："):
        st.write(search_results)

#页脚
st.markdown("---")
st.markdown("<center style='color: #888888;'>Powered by LangChain & Streamlit</center>", unsafe_allow_html=True)