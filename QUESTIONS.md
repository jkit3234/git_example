# 질문 기록

## 2026-04-21

1. .venv 삭제 방법 (PowerShell에서 rm -rf 안됨)
   → Remove-Item -Recurse -Force .venv 사용

2. Python 경로 문제 (포맷 후 이전 경로 참조)
   → 새 .venv 생성으로 해결

3. 8000번 포트 충돌
   → taskkill /PID [번호] /F 로 해결

4. node_modules gitignore 누락
   → git rm -r --cached 로 해결