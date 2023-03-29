#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2

# 동영상 파일 경로
video_path = 'C:/Users/이대훈/JokerStair.mp4'

# 동영상을 읽어오기 위한 객체 생성
cap = cv2.VideoCapture(video_path)

# 동영상 프레임 사이즈 가져오기
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 동영상 프레임 속도 가져오기
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 동영상 저장을 위한 객체 생성
out = cv2.VideoWriter('cartoonized.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# 동영상이 끝날 때까지 반복
while cap.isOpened():
    # 현재 프레임 가져오기
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 현재 프레임을 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 가우시안 블러 필터 적용 (메디안 필터)
    gray = cv2.medianBlur(gray, 5)

    # 캐니 엣지 검출
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # 적응형 이진화
    thresh = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)

    # 컬러 반전
    thresh = cv2.bitwise_not(thresh)

    # 컬러 이미지로 변환
    color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

    # Bilateral 필터 적용
    bilateral = cv2.bilateralFilter(color, 9, 75, 75)

    # 결과 동영상에 프레임 추가
    out.write(bilateral)
    
    # 결과 동영상 출력
    cv2.imshow('Cartoonized Video', bilateral)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 객체 해제
cap.release()
out.release()
cv2.destroyAllWindows()


# In[ ]:




