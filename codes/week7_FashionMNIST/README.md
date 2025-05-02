# 컴퓨터비전 스터디 기록 📚  

## 7주차 - Fashion MNIST 이미지 분류 실습

✅ **학습 목표**  
- Fashion MNIST 데이터셋 구조 및 라벨 클래스 이해, 기존 MNIST와의 차이 인식  
- 다양한 CNN 기반 모델 구조 설계 및 성능 비교  
- Dropout, BatchNorm 등 정규화 기법의 효과 분석  
- 학습 곡선 시각화를 통한 오버피팅 여부 확인 및 일반화 성능 비교  

1️⃣ **Fashion MNIST란?**
- Zalando에서 제공한 의류 이미지 데이터셋 (총 70,000장)  
- 흑백 이미지, 크기 28×28, 클래스 수 10개 (T-shirt, Trouser, Pullover, Dress 등)  
- MNIST보다 시각적 난이도가 높고 실제 이미지 분류 문제에 더 가까움  