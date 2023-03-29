#!/usr/bin/env python
# coding: utf-8

# In[17]:


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
        
    # 이미지에 Bilateral 필터 적용
    bilateral = cv2.bilateralFilter(frame, 9, 100, 7)
    
    # 캐니 엣지 검출(흰검 반전)
    edge = 255 - cv2.Canny(frame, 80, 12)
    
    # 엣지를 컬러 이미지로 변환
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    
    #영상에 필터를 나누기
    div = cv2.divide(frame, bilateral, scale=255)
    
    #이미지와 엣지와 나눈 영상을 결합
    dst = cv2.bitwise_and(bilateral, edge) 
    
    dst = cv2.bitwise_and(dst, div)
    
    # 결과 동영상에 프레임 추가
    out.write(dst)
    
    # 결과 동영상 출력
    cv2.imshow('Cartoonized Video', dst)
    
    # 'ESC' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 객체 해제
cap.release()
out.release()
cv2.destroyAllWindows()


# In[ ]:




