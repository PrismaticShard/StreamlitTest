import streamlit as st

# 添加一个标题
st.title('我的第一个 Streamlit 应用')

# 添加文本
st.write('这是一个简单的示例应用，用于展示 Streamlit 的基本功能。')

# 交互式组件：滑动条
x = st.slider('选择一个值')  # 让用户选择一个数值
st.write(f'您选择的值是: {x}')

# 交互式组件：按钮
if st.button('点击我'):
    st.write('按钮已被点击！')
else:
    st.write('按钮尚未被点击。')
