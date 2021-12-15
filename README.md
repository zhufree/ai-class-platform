# AI-TEACH 人工智能辅助教学平台
图形化人工智能流程演示应用，使用百度API及Pyside6开发。

## 人脸识别
已支持**人脸检测**，**人脸注册**，**人脸1：N搜索**，**人脸M：N搜索**，**人脸对比**。

支持直接调用摄像头拍照。

## 语音识别
支持**语音转文字**，**文字转语音**。

使用麦克风录音。

## 使用说明
### 针对用户的说明
dist文件夹下的`ai-teach.exe`文件可直接运行

### 针对开发者的说明
#### 依赖库安装
```python
pip install -r requirements.txt
pip install opencv-python
```
pyAudio需要[单独下载.whl文件](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)安装
#### 运行主程序
运行`python ai-teach.py`启动图形化界面
#### 打包可执行文件
可以安装`pyinstaller`并使用`pyinstaller -F -w ai-teach.py`打包为exe文件，要将`ai-teach.ui`文件放在和exe文件同级文件夹下才能顺利启动。
