import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="停車場併排登記系統", page_icon="🚗")

st.title("🚗 停車場併排登記系統")
st.write("為了方便鄰居進出，併排停車請務必登記資訊。")

# 建立車位選單（B1 20格, B2 10格）
b1_slots = [f"B1-{i:02d}" for i in range(1, 21)]
b2_slots = [f"B2-{i:02d}" for i in range(1, 11)]
all_slots = b1_slots + b2_slots

# 建立填寫表單
with st.form("parking_form"):
    car_id = st.text_input("1. 車牌號碼", placeholder="例如：ABC-1234")
    phone = st.text_input("2. 聯絡電話", placeholder="例如：0912-345-678")
    target_slot = st.selectbox("3. 您擋住的車位編號", options=all_slots)
    
    # 提交按鈕
    submit_button = st.form_submit_button("提交登記")

# 按下按鈕後的反應
if submit_button:
    if car_id and phone:
        st.success(f"登記成功！車牌 {car_id} 已記錄。管理員已收到通知。")
        st.balloons() # 噴出慶祝氣球
    else:
        st.error("請填寫完整的車牌與電話資訊！")

