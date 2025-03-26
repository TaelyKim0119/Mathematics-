import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 데이터 읽기
other_to_crypto_major = pd.read_excel('타과생의 정보보안암호수학과 다전공 신청 명부.xls', skiprows=2)
other_to_crypto_minor = pd.read_excel('타과생의 정보보안암호수학과 부전공 신청자 명부(2017-2025).xls', skiprows=2)
crypto_to_other_major = pd.read_excel('다전공신청목록 (1).xls', skiprows=2)
crypto_to_other_minor = pd.read_excel('부전공신청목록 (2).xls', skiprows=2)

# 데이터 내용 확인
print("=== 타과생의 정보보안암호수학과 다전공 신청 명부 ===")
print(other_to_crypto_major.head())
print("\n=== 타과생의 정보보안암호수학과 부전공 신청자 명부 ===")
print(other_to_crypto_minor.head())
print("\n=== 정보보안암호수학과 학생의 타과 다전공 신청 명부 ===")
print(crypto_to_other_major.head())
print("\n=== 정보보안암호수학과 학생의 타과 부전공 신청 명부 ===")
print(crypto_to_other_minor.head())

# HTML 템플릿 생성
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>정보보안암호수학과 전공 신청 현황</title>
    <meta charset="utf-8">
    <style>
        body { font-family: 'Malgun Gothic', sans-serif; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .section { margin-bottom: 40px; }
        h1 { color: #2c3e50; text-align: center; }
        h2 { color: #34495e; }
    </style>
</head>
<body>
    <div class="container">
        <h1>정보보안암호수학과 전공 신청 현황</h1>
        
        <div class="section">
            <h2>1. 타과생의 정보보안암호수학과 신청 현황</h2>
            <div id="other_to_crypto_plot"></div>
        </div>
        
        <div class="section">
            <h2>2. 정보보안암호수학과 학생의 타과 신청 현황</h2>
            <div id="crypto_to_other_plot"></div>
        </div>
    </div>
    
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</body>
</html>
"""

# 1. 타과생의 정보보안암호수학과 신청 현황
def create_other_to_crypto_plot():
    fig = make_subplots(rows=2, cols=1,
                       subplot_titles=('다전공 신청 현황', '부전공 신청 현황'),
                       height=800)
    
    # 학과별 통계
    major_stats = other_to_crypto_major['소속학과'].value_counts()
    minor_stats = other_to_crypto_minor['소속학과'].value_counts()
    
    fig.add_trace(
        go.Bar(x=major_stats.index, y=major_stats.values, name='다전공'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=minor_stats.index, y=minor_stats.values, name='부전공'),
        row=2, col=1
    )
    
    fig.update_layout(showlegend=False, height=800)
    return fig

# 2. 정보보안암호수학과 학생의 타과 신청 현황
def create_crypto_to_other_plot():
    fig = make_subplots(rows=2, cols=1,
                       subplot_titles=('다전공 신청 현황', '부전공 신청 현황'),
                       height=800)
    
    # 학과별 통계
    major_stats = crypto_to_other_major['신청학과'].value_counts()
    minor_stats = crypto_to_other_minor['신청학과'].value_counts()
    
    fig.add_trace(
        go.Bar(x=major_stats.index, y=major_stats.values, name='다전공'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=minor_stats.index, y=minor_stats.values, name='부전공'),
        row=2, col=1
    )
    
    fig.update_layout(showlegend=False, height=800)
    return fig

# HTML 파일 생성
with open('analysis_report.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

# 그래프 생성 및 저장
other_to_crypto_plot = create_other_to_crypto_plot()
crypto_to_other_plot = create_crypto_to_other_plot()

other_to_crypto_plot.write_html('other_to_crypto_plot.html')
crypto_to_other_plot.write_html('crypto_to_other_plot.html')

print("분석이 완료되었습니다. analysis_report.html 파일을 웹 브라우저에서 열어주세요.") 