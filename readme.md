# 카카오톡 오픈 채팅방 통계

iOS로부터 export된 대화내용을 가지고 이런 저런 통계를 내줍니다.
오픈채팅방을 타겟으로 사람들간의 인터랙션 같은 것들이 궁금해서 제작

## 선행 작업

### merge.py
iOS에서 대화내용을 내보내기 하면, 여러개의 txt파일이 포함된 압축파일을 메일로 보내게 되는데, 이 텍스트 파일들을 `./src`에 넣고 실행하면 `combined.txt`로 합쳐줍니다.

### 2csv.py
`combined.txt`로부터 일자, 시간, 사람, 메시지를 파싱해서, `conversation.csv`를 생성합니다. 이 `conversation.csv`를 가지고 아래 기능들을 수행합니다.

---
### race.py

`bar_chart_race` 패키지를 사용해서 Bar chart race를 그려줍니다.

사용하기 전에 먼저 
- `pip install bar_chart_race` 를 통해 패키지를 설치합니다.<br>`matplotlib`, `pandas`, `numpy` 등의 의존하는 패키지들이 함께 설치됩니다.
- [ffmpeg](https://www.ffmpeg.org/download.html)이 설치되어서 시스템의 path에 포함되어 있어야 하고
- `D2Coding Ligature` 폰트를 설치해야 합니다. (딴걸로 변경 가능)

#### 인풋
- `conversation.csv`
- title 변수에 영상에 첨부할 제목을 입력합니다.

#### 아웃풋
- `race.mp4`
- `dailyTMI.csv`

<iframe width="560" height="315" src="https://www.youtube.com/embed/emSiK0Q_f6I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---
### rank.py
그냥 단순히 전체기간의 대화량 순위를 카운트해서 정렬해줍니다.

#### 인풋
- `conversation.csv`
#### 아웃풋
- `result.csv`
---
### talk2.py

여러명이 있는 단톡방에서 어떤 사람이 메시지를 보냈을 때, 그 직전 메시지의 주인을 찾으면 이 사람이 누구의 말에 응답했는지를 알 수 있습니다. 뭐 항상 그런 건 아니겠지만 어느정도 경향성을 찾을 수 있다고 생각. 따라서 전체 대화내용에서 주어진 사람의 모든 메시지의 직전 메시지의 주인이 나타난 숫자를 카운트하고, 내림차순 정렬합니다.

#### 인풋
- `conversation.csv`
- who 변수에 타겟 사용자명을 적어줍니다 ..

#### 아웃풋
- `result.csv`