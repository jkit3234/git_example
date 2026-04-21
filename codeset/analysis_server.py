import os
import uvicorn
import ollama
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# 환경 변수 로드 (.env 파일이 codeset 폴더 내에 있으므로 경로 지정)
load_dotenv()

app = FastAPI(title="AI Image Analyzer Server")

# CORS 설정: 모든 출처 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyzeImage(imageFile: UploadFile = File(...)):
    """
    업로드된 이미지를 Ollama gemma3:4b 모델을 사용하여 분석합니다.
    
    Args:
        imageFile (UploadFile): 분석할 이미지 파일
        
    Returns:
        dict: 분석 결과 또는 에러 메시지
    """
    try:
        # 이미지 데이터 읽기
        imageBytes = await imageFile.read()
        
        # 환경 변수에서 모델명 가져오기 (기본값: gemma3:4b)
        targetModel = os.getenv("OLLAMA_MODEL", "gemma3:4b")
        
        # Ollama 로컬 모델 호출
        analysisResponse = ollama.chat(
            model=targetModel,
            messages=[{
                'role': 'user',
                'content': 'Describe this image in detail.',
                'images': [imageBytes]
            }]
        )
        
        return {
            "status": "success",
            "modelName": targetModel,
            "analysisResult": analysisResponse['message']['content']
        }
        
    except Exception as errorInstance:
        # 예외 발생 시 상세 로깅
        print(f"[ERROR] 이미지 분석 중 예외 발생: {str(errorInstance)}")
        raise HTTPException(
            status_code=500, 
            detail=f"이미지 분석 중 오류가 발생했습니다: {str(errorInstance)}"
        )

if __name__ == "__main__":
    # 서버 실행 설정 (환경 변수 PORT 사용, 기본값 8000)
    serverPort = int(os.getenv("PORT", 8000))
    print(f"Starting server on port {serverPort}...")
    uvicorn.run(app, host="0.0.0.0", port=serverPort)
