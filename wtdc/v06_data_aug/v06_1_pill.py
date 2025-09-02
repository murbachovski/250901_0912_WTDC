from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = Image.open("v06_data_aug/data_aug.jpg")

# 2. 이미지 조정(회전)
img_rotated = img.rotate(90)
############################ + 3가지 데이터 증강 진행해서 이미지 시각화!!

# 2-1. 이미지 조정(밝기)
enhancer = ImageEnhance.Brightness(img)
img_brightness = enhancer.enhance(0.5)

# 3. 결과 시각화
fig, ax = plt.subplots(2, 3, figsize=(20, 10))

# 3-1. 원본 이미지 시각화
ax[0,0].imshow(img)
ax[0,0].axis('on')
ax[0,0].set_title('Original')

# 3-2. 회전 이미지 시각화
ax[0,1].imshow(img_rotated)
ax[0,1].axis('off')
ax[0,1].set_title('Rotated')

# 3-3. 밝기 이미지 시각화
ax[0,2].imshow(img_brightness)
ax[0,2].axis('off')
ax[0,2].set_title('Brightness')

# plt.show()

# 4. 결과 이미지 저장
img_rotated.save("./img_rotated.jpg")
print("이미지 저장이 잘 됐습니다.")