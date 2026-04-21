# AI 이미지 분석기 (AI Image Analyzer)

로컬 AI 모델(Ollama)과 OCR 기술을 결합하여 업로드된 이미지를 지능적으로 분석하는 풀스택 애플리케이션입니다.

## 🚀 주요 기능

- **이미지 텍스트 추출 (OCR)**: EasyOCR을 사용하여 이미지 내의 한국어 및 영어 텍스트를 정밀하게 추출합니다.
- **AI 이미지 분석**: Ollama(gemma3:4b) 모델을 통해 추출된 텍스트와 이미지 데이터를 종합적으로 분석하여 상세한 설명을 제공합니다.
- **다크 모드 웹 UI**: 사용자 친화적인 다크 테마 인터페이스로 이미지 업로드 및 분석 결과를 실시간으로 확인할 수 있습니다.
- **로컬 실행**: 데이터 보안을 위해 모든 분석은 로컬 환경에서 수행됩니다.

## 🛠 사용 기술

- **AI/LLM**: Ollama (gemma3:4b)
- **OCR**: EasyOCR
- **Backend**: FastAPI (Python 3.12.10)
- **Frontend**: Node.js (Express), Vanilla JS, CSS
- **Dev Tool**: Gemini CLI

## 📋 사전 준비 사항

1. **Ollama 설치 및 모델 다운로드**
   - [Ollama](https://ollama.com/)를 설치합니다.
   - 터미널에서 모델을 다운로드합니다: `ollama run gemma3:4b`

2. **Python 환경 설정**
   - `codeset/requirements.txt`에 명시된 라이브러리를 설치합니다.
   ```bash
   pip install -r codeset/requirements.txt
   ```

3. **Node.js 환경 설정**
   - `simple_web` 폴더에서 패키지를 설치합니다.
   ```bash
   cd simple_web
   npm install
   ```

## 🏃 실행 방법

이 프로젝트는 백엔드 서버와 프론트엔드 웹 서버를 각각 실행해야 합니다.

### 1. 백엔드 서버 (FastAPI) 실행
```bash
python codeset/analysis_server.py
```
- 서버는 기본적으로 `http://localhost:8000`에서 실행됩니다.

### 2. 웹 UI 서버 (Node.js) 실행
```bash
node simple_web/server.js
```
- 브라우저에서 `http://localhost:3000`에 접속하여 서비스를 이용할 수 있습니다.

## ⚙️ 환경 설정 (.env)

`codeset/.env` 파일을 통해 설정을 변경할 수 있습니다.
- `OLLAMA_MODEL`: 사용할 Ollama 모델명 (기본값: gemma3:4b)
- `PORT`: 백엔드 서버 포트 (기본값: 8000)

## 📝 개발 규칙

- **언어**: 모든 코드 주석 및 문서는 한국어를 원칙으로 합니다.
- **스타일**: 변수명은 `camelCase`를 사용하며, 모든 함수에 `docstring`을 작성합니다.
- **안정성**: `try-except` 구문을 통한 예외 처리를 엄격히 준수합니다.
