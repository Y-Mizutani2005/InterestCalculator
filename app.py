import streamlit as st
import numpy as np

def main():
    st.title("外貨利息計算機")
    
    # サイドバーでの入力欄
    st.sidebar.header("入力パラメータ")
    
    # 金額入力
    jpy_amount = st.sidebar.number_input(
        "日本円金額",
        min_value=0.0,
        value=1000.0,
        step=100.0,
        help="変換したい日本円の金額を入力してください"
    )

        # 利率入力
    interest_rate = st.sidebar.number_input(
        "利率 i (%)",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=1.0,
        help="利率をパーセントで入力してください"
    )
    
    # 為替レート入力
    st.sidebar.subheader("為替レート設定")
    e1_rate = st.sidebar.number_input(
        "E1（円からドルへの換算レート）",
        min_value=0.0,
        value=110.0,
        step=10.0,
        help="1ドルあたりの円レート"
    )
    
    e2_rate = st.sidebar.number_input(
        "E2（ドルから円への換算レート）",
        min_value=0.0,
        value=110.0,
        step=10.0,
        help="1ドルあたりの円レート"
    )
    

    
    # 計算結果の表示
    st.header("計算結果")
    
    # (日本円*(1/E1))iの計算
    dollar_amount = jpy_amount * (1/e1_rate)  # 円をドルに換算
    result = (dollar_amount * (1 + interest_rate/100))*e2_rate  # 利率を適用
    roundresult = np.round(result, 2)  # 小数点以下2桁に丸める
    st.success(roundresult)

if __name__ == "__main__":
    main()
