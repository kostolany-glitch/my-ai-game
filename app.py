import streamlit as st

# --- 1. 初始化遊戲狀態 ---
# 檢查 session_state 中是否有 'page'，若無則設定為 'start'
if 'page' not in st.session_state:
    st.session_state.page = 'start'

# --- 2. 定義遊戲內容 ---
# 這裡我們將文字、選項與結局路徑封裝起來
game_content = {
    'start': {
        'text': "一台失控的電車正全速衝向軌道上的五個人。你站在轉轍器旁，只要拉下拉桿，電車就會轉向另一條只有一個人的軌道。你會怎麼做？",
        'image_url': "https://images.unsplash.com/photo-1515091943-9d5c0ad475af?q=80&w=1000", # 範例圖，稍後可換成 AI 生成圖
        'choices': [
            {"label": "拉下拉桿 (犧牲 1 人，救下 5 人)", "next": "result_a"},
            {"label": "不採取行動 (眼睜睜看著 5 人犧牲)", "next": "result_b"}
        ]
    },
    'result_a': {
        'text': "### 結局 A：功利主義者的抉擇\n\n你選擇了拉下拉桿。雖然你救了五個人，但你必須終身背負著「親手殺死一個無辜者」的道德重擔。",
        'image_url': "https://images.unsplash.com/photo-1454496406107-dc34337da8d6?q=80&w=1000",
        'is_end': True
    },
    'result_b': {
        'text': "### 結局 B：義務論者的堅持\n\n你選擇不介入。雖然五個人因此喪命，但你認為自己不該扮演上帝決定誰生誰死。這種沉默的旁觀，是否也是一種共犯？",
        'image_url': "https://images.unsplash.com/photo-1476124369491-e7addf5db371?q=80&w=1000",
        'is_end': True
    }
}

# --- 3. 渲染介面 ---
st.title("⚖️ 電車難題：道德實驗室")

# 獲取當前頁面資料
current_data = game_content[st.session_state.page]

# 顯示圖片與故事文字
st.image(current_data['image_url'], use_container_width=True)
st.write(current_data['text'])

# 顯示按鈕邏輯
if 'is_end' in current_data:
    if st.button("重新開始"):
        st.session_state.page = 'start'
        st.rerun()
else:
    # 橫向排列按鈕
    cols = st.columns(len(current_data['choices']))
    for idx, choice in enumerate(current_data['choices']):
        if cols[idx].button(choice['label'], use_container_width=True):
            st.session_state.page = choice['next']
            st.rerun()