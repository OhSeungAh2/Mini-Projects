# [PDF 읽어오기]
# 실행: python 01_load_pdf.py

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

# 경로 설정
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

pdf_path = DATA_DIR / "[삼성전자]반기보고서(2024.08.14).pdf"


# 파일 존재하는지 확인
if not pdf_path.exists():
    raise FileNotFoundError(f"PDF 파일을 찾을 수 없습니다: {pdf_path}")
print(f"선택한 PDF 파일: {pdf_path.name}")


# 본격) PDF 불러오기
loader = PyPDFLoader(str(pdf_path))
pdf_pages = loader.load()
print("불러온 페이지 수:", len(pdf_pages))


# 첫 번째 페이지 메타데이터 확인하기
print("\n[첫 페이지 메타데이터]")
print(pdf_pages[0].metadata)


# 텍스트가 있는 첫번째 페이지 확인하기
for i, page in enumerate(pdf_pages):
    if page.page_content.strip():
        print(f"\n[PDF {i+1}페이지 텍스트]")
        print(page.page_content[:1000])
        break

# 재무 관련 키워드가 추출되었는지 확인하기
keywords = ["재무상태표", "손익계산서", "매출액", "영업이익"]

print("\n[재무 관련 키워드 확인]")
for keyword in keywords:
    found_pages = [
        i + 1
        for i, page in enumerate(pdf_pages)
        if keyword in page.page_content
    ]
    print(f"{keyword}: {len(found_pages)}페이지에서 발견")
    print(f"  앞부분 페이지: {found_pages[:5]}")

