# 1. CUDA 설치 및 적용
    # CUDA 버전에 맞는 torch 설치
        # pip install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio==0.10.2 --extra-index-url https://download.pytorch.org/whl/cu113
    # CUDA 확인
        # import torch
        # print(torch.__version__)
        # print(torch.version.cuda)
        # print(torch.cuda.is_available())

# 2. CUDA 버전에 맞는 TensorRT 설치
    # https://developer.nvidia.com/nvidia-tensorrt-8x-download

# 3. TensorRT 라이브러리 다운로드 
    # 다운 받은 TensorRT 폴더 안에 python 경로로 이동
    # (py_cuda) C:\Users\Administrator\Downloads\TensorRT-8.6.1.6.Windows10.x86_64.cuda-11.8\TensorRT-8.6.1.6\python>
    # 위 경로에서 설치 진행
    # pip install tensorrt-8.6.1-cp39-none-win_amd64.whl tensorrt_dispatch-8.6.1-cp39-none-win_amd64.whl tensorrt_lean-8.6.1-cp39-none-win_amd64.whl

# 4. TensorRT 환경 변수 추가
    # 환경 변수 편집:
        # **"새로 만들기"**를 클릭하고, TensorRT 폴더 안의 bin 폴더의 전체 경로를 추가합니다.
        # 예시: C:\Users\Administrator\Downloads\TensorRT-8.6.1.6.Windows10.x86_64.cuda-11.8\TensorRT-8.6.1.6\bin
        # **"새로 만들기"**를 다시 클릭하고, TensorRT 폴더 안의 lib 폴더의 전체 경로를 추가합니다.
        # 예시: C:\Users\Administrator\Downloads\TensorRT-8.6.1.6.Windows10.x86_64.cuda-11.8\TensorRT-8.6.1.6\lib
    # VSCODE 재부팅

# 5. Export TensorRT

# 6. Numpy ERROR
    # pip uninstall numpy
    # pip install numpy==1.26.4
    
# 7. Let's predict

'''
여러 개의 연산(코드 두 줄)을 하나의 연산(코드 한 줄)으로 합쳐서 효율을 높인다는 개념과 같습니다.

레이어 융합은 Convolution, Bias, ReLU처럼 GPU에서 각각 실행되어야 할 연산들을 하나로 묶어, GPU가 여러 작업을 왔다 갔다 하는 비효율적인 과정을 없애는 것입니다. 이는 마치 여러 줄의 코드를 하나의 함수로 묶어 호출하는 것과 비슷합니다.

<Pytorch>
output_conv = conv(input)  # GPU에서 연산 1
output_bias = output_conv + bias # GPU에서 연산 2
output_relu = relu(output_bias) # GPU에서 연산 3

to

<TensorRT>
output_fused = fused_conv_bias_relu(input, bias) # GPU에서 한 번에 연산
'''

# model = YOLO("yolo11n.pt")
# 지난 10초 동안의 평균 FPS: 23.79
# 지난 10초 동안의 평균 FPS: 31.71
# 지난 10초 동안의 평균 FPS: 32.24
# 지난 10초 동안의 평균 FPS: 31.63
# 지난 10초 동안의 평균 FPS: 31.77

# model = YOLO("yolo11n.engine")
# 지난 10초 동안의 평균 FPS: 31.65
# 지난 10초 동안의 평균 FPS: 39.42
# 지난 10초 동안의 평균 FPS: 39.99
# 지난 10초 동안의 평균 FPS: 39.52
# 지난 10초 동안의 평균 FPS: 39.98

# model = YOLO("yolo11n_int.engine")
# 지난 10초 동안의 평균 FPS: 27.39
# 지난 10초 동안의 평균 FPS: 54.07
# 지난 10초 동안의 평균 FPS: 59.58
# 지난 10초 동안의 평균 FPS: 38.25
# 지난 10초 동안의 평균 FPS: 34.16

# model = YOLO("yolo11l.engine")
# 지난 10초 동안의 평균 FPS: 11.24
# 지난 10초 동안의 평균 FPS: 16.28
# 지난 10초 동안의 평균 FPS: 15.59
# 지난 10초 동안의 평균 FPS: 15.76
# 지난 10초 동안의 평균 FPS: 15.86