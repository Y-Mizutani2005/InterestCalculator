import streamlit as st
import numpy as np
import os

def read_readme():
    """READMEファイルの内容を読み込む関数"""
    try:
        with open("README.md", "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"README.mdファイルの読み込みに失敗しました: {str(e)}"

def show_about_tab():
    """アプリについてのタブの内容を表示する関数"""
    readme_content = read_readme()
    # Markdownとして表示
    st.markdown(readme_content)
    
def main():
    st.title("外貨利息計算機")
    
    # タブの作成
    tab1, tab2 = st.tabs(["計算機", "アプリについて"])
    
    with tab1:
        # 計算機の表示
        # サイドバーでの入力欄
        st.sidebar.header("入力パラメータ")
        
        # 金額入力
        jpy_amount = st.sidebar.number_input(
            "投資する日本円 (円)",
            min_value=0.0,
            value=1000.0,
            step=100.0,
            help="変換したい日本円の金額を入力してください"
        )

        # 年間利率入力
        interest_rate = st.sidebar.number_input(
            "年利 i (%)",
            min_value=0.0,
            max_value=100.0,
            value=10.0,
            step=1.0,
            help="利率をパーセントで入力してください"
        )
        #利息が適用される年数の入力
        years = st.sidebar.number_input(
            "利息が適用される年数",
            min_value=0,
            max_value=100,
            value=1,
            step=1,
            help="年数を入力してください"
        )
        # 為替レート入力
        st.sidebar.subheader("為替レート設定")
        e1_rate = st.sidebar.number_input(
            "E1（円からドルへの換算レート）",
            min_value=0,
            value=110,
            step=10,
            help="1ドルあたりの円レート"
        )
        
        e2_rate = st.sidebar.number_input(
            "E2（ドルから円への換算レート）",
            min_value=0,
            value=110,
            step=10,
            help="1ドルあたりの円レート"
        )
        # 計算結果の表示
        st.header("計算結果")
        
        # (日本円*(1/E1))iの計算
        dollar_amount = jpy_amount * (1/e1_rate)  # 円をドルに換算
        result = (dollar_amount * (1 + interest_rate/100)** years )*e2_rate  # 利率を適用
        roundresult = np.round(result, 2)  # 小数点以下2桁に丸める
        
        # 利息額の計算（最終金額 - 元金）
        interest_amount = np.round(roundresult - jpy_amount, 2)  # 小数点以下2桁に丸める
        
        # 結果の表示
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="最終金額（円）", value=f"{roundresult:,.2f}")
        
        with col2:
            st.metric(label="利息額（円）", value=f"{interest_amount:,.2f}")
    
    with tab2:
        show_about_tab()

if __name__ == "__main__":
    main()