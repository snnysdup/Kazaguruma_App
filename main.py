import streamlit as st
import numpy as np
import pandas as pd
import datetime
# import plotly.graph_objects as go

# タイトル
st.title('KAZAGURUMA（画像入れたい）')
import streamlit as st
import datetime

# `plotly` のインポートを試みる
try:
    import plotly.graph_objects as go
    plotly_available = True
except ImportError:
    plotly_available = False
    st.warning("⚠️ `plotly` がインストールされていません。以下のコマンドでインストールしてください。\n\n```sh\npip install plotly\n```")

# タイトル
st.title("学習レベル記録アプリ（仮）")

# 6 つの分野
categories = ["Python", "生成AI", "BIツール", "自動化ツール", "デジタルマーケティング", "データ分析"]

# session_state に履歴がない場合は初期化
if "history" not in st.session_state:
    st.session_state.history = []

# 学習レベル入力フォーム
st.subheader("🔹 各分野のレベルを選択してください（1: 初心者 〜 5: マスター）")

with st.form("level_form"):
    levels = {category: st.slider(category, 1, 5, 3) for category in categories}
    submitted = st.form_submit_button("記録する")

    if submitted:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.history.append({"levels": levels.copy(), "time": timestamp})
        st.success("✅ 学習レベルを記録しました！")

# レーダーチャートを描画する関数
def draw_radar_chart(levels):
    if not plotly_available:
        return  # `plotly` がない場合はスキップ

    values = list(levels.values()) + [list(levels.values())[0]]  # 最後に最初の値を追加して閉じる
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories + [categories[0]],
        fill='toself',
        name='学習レベル'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[1, 5]
            )
        ),
        showlegend=False
    )
    
    st.plotly_chart(fig)

# 過去の記録を表示
st.subheader("📜 学習履歴とレーダーチャート")

if st.session_state.history:
    # 最新のデータでレーダーチャートを描画
    latest_record = st.session_state.history[-1]
    draw_radar_chart(latest_record["levels"])

    st.write("### 🕒 過去の記録→もっといい感じに見せたい")
    for record in reversed(st.session_state.history):
        st.write(f"📅 {record['time']}")
        st.write(", ".join([f"{k}: {v}" for k, v in record["levels"].items()]))
else:
    st.info("まだ記録がありません。")




df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
}) # データフレームの作成

st.write(df)  # データフレームの表示
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100) # データフレームの表示（スタイル付き）

#公式ドキュメントを見に行くと、いろんな表示形式があるので確認する（display data）

st.table(df.style.highlight_max(axis=0)) # データフレームの表示（スタイル付き）

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

st.write('DataFrame') # テキストの表示

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)   # データフレームの作成

st.line_chart(df) # 折れ線グラフの表示
st.area_chart(df) # エリアグラフの表示

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df) # 地図の表示

# st.write('Display Image') #画像の表示

# img = Image.open('pic/img031.jpg') # 画像の読み込み
# st.image(img, caption='sample', use_column_width=True) # 画像の表示


st.write('Interactive Widgets') # ウィジェットの表示

text = st.sidebar.text_input('強化したい・学びたい内容を入力してください') # テキスト入力
'あなたの趣味は', text, 'です。' # テキスト表示

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50) # スライダー
'コンディション：', condition # テキスト表示


# import streamlit as st # フロントエンドを扱うstreamlitの機能をインポート
import time # 時間を扱う機能をインポート

st.title("streamlitの基礎") # タイトルが出力される
st.write("hello world") # hello worldが出力される

# レイアウトとして２列を定義
col1, col2 = st.columns(2)

# 1列目をwithで囲む
with col1:
    st.write("列1がここに表示されます")

# 2列目をwithで囲む
with col2:
    st.write("列2がここに表示されます")



st.sidebar.write("hello world") #.sidebar付けるとサイトバーに出力されます。
st.text_input("ここに文字が入力できます。") # テキストを入力できます。

slider_text = st.slider("スライダーで数字を決定できます。",0,100,5) # (最小、最大値、デフォルト値)の順で設定されます。
"スライダーの数字:",slider_text

st.button("ボタン") # ボタンが設置されます。

x = st.empty() # 文字が出力される場所をあらかじめ確保します。その場所をxとしています。
bar = st.progress(0) # 進捗0のプログレスバーを出力します。

# iに0から99まで代入しながら実行されます
for i in range(100):
    time.sleep(0.1) # 0.1秒待機します。
    x.text(i) # 確保した場所xに代入されたiの値を代入します。
    bar.progress(i) # 進捗iに変更します。
    i += 1 # iに1足し算して代入します。

# 選択肢を配列で指定して選択肢を出力します。
st.selectbox("選んでください。",["選択肢1","選択肢2","選択肢3"])



# ダウンロードする文字を定義し、output_textに代入します。
output_text = "この文字がダウンロードされます"

 # 代入された文字をダウンロードするボタンを設置。オプションは内容をdataに指定、ファイル名をfile_nameに指定、ファイルタイプをmimeに指定
st.download_button(label='記事内容 Download', 
                   data=output_text, 
                   file_name='out_put.txt',
                   mime='text/plain',
                   )


# ファイルアップローダーを設置します。typeでアップロードできるファイルの種類を指定できます。
file_upload = st.file_uploader("ここに音声認識したファイルをアップロードしてください。",type=["png","jpg"])

# ファイルがアップロードされた時にその画像を表示します。
if (file_upload !=None):
    st.image(file_upload)# 画像を表示します。



import numpy as np # 数列を扱う機能をインポート
import pandas as pd # データフレームを扱う機能をインポート

# 乱数の配列を作るメソッドを作ります。引数r,cとし、それぞれおのデフォルト値を10と5に設定します。
def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.randn(r, c),
        columns=('col %d' % i for i in range(c)))# 乱数10の５個の数列を作ります。カラムの設定は0-4の名前を付けます。
    return df # 作ったデータフレームを返します。

dataframe = rand_df(r=10,c=3) # rに10、cに3を代入したrand_dfメソッドを処理します。

# 表の描画します。
st.dataframe(dataframe.head(n=3))
# データフレームのチャートの描画します。
st.line_chart(dataframe)
