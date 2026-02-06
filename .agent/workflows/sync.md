---
description: 맥과 윈도우 간 작업을 동기화하기 위한 깃 워크플로우
---

## 🚀 기기 전환 동기화 방법

맥북과 윈도우를 오가며 작업할 때 발생할 수 있는 충돌을 방지하고 최신 상태를 유지하는 방법입니다.

### 1. 작업 시작 시 (가져오기)
새로운 기기에서 작업을 시작하기 전에 아래 명령어를 실행하여 깃허브의 최신 버전을 로컬로 가져옵니다.

// turbo
```bash
git pull origin main
```

### 2. 작업 종료 시 (보내기)
다른 기기로 옮기기 전에 현재 변경사항을 모두 저장하고 깃허브로 올립니다.

// turbo
```bash
git add . && git commit -m "wip: sync before switching OS" && git push origin main
```

> [!TIP]
> **Antigravity에게 부탁하기**
> 직접 명령어를 치기 번거로우시면 저에게 **"지금 작업 맥북으로 옮길 거야"** 또는 **"윈도우에서 작업한 거 가져와줘"**라고 말씀해 주세요. 제가 위 과정을 자동으로 처리해 드립니다.

### 3. OS 간 줄바꿈 설정 (최초 1회)
파일 형식이 깨지지 않도록 각 OS의 터미널에서 한 번만 실행해 주세요.

*   **맥북:** `git config --global core.autocrlf input`
*   **윈도우:** `git config --global core.autocrlf true`
