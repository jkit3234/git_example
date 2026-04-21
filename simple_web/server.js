const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

/**
 * Express 서버 설정을 초기화하고 정적 파일을 제공합니다.
 */
function startServer() {
    try {
        // public 폴더를 정적 파일 루트로 설정
        app.use(express.static(path.join(__dirname, 'public')));

        app.listen(port, () => {
            console.log(`[INFO] Web UI server is running at http://localhost:${port}`);
        });
    } catch (errorInstance) {
        console.error(`[ERROR] Server failed to start: ${errorInstance.message}`);
    }
}

startServer();
