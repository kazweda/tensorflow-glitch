# tensorflow-glitch
gdgshikokuもくもく会

## 犬猫教師データ
zip ファイルとして 
https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip 
で配布されている。

## Python環境
念のため Python-3.10.10 に切り替え。

[Can't get Tensorflow working on macOS M1 Pro Chip](https://stackoverflow.com/questions/74792286/cant-get-tensorflow-working-on-macos-m1-pro-chip)

```
python -m pip install tensorflow-macos==2.9.0
python -m pip install tensorflow-metal==0.5.0
```

```
ModuleNotFoundError: No module named 'tensorflow.python'; 'tensorflow' is not a package
```

~~## M1/M2 Mac
[【Python】M1/M2 MacでPython環境の構築（機械学習・データ分析編）](https://namileriblog.com/python/python_library_ai/)~~

https://namileriblog.com/python/python_library_ai/

## M2 / venv
[【Python】M1/M2 MacでPython環境の構築（pyenvとvenvのインストールと設定、そして使い方）](https://namileriblog.com/python/python_pyenv_venv/)

## M2 / conda
[MachineLearning勉強ノート](https://storikai.hatenablog.com/)
