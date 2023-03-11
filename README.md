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

## tensorflow 導入 - conda
[MachineLearning勉強ノート](https://storikai.hatenablog.com/entry/2022/05/24/010217)
```

### 仮想環境
```
conda create --name tf2_10 python=3.10
conda activate tf2_10
```
### パッケージインストール
```
conda install numpy opencv matplotlib scikit-learn pandas jupyter
```
### TensorFlow インストール
```
conda install -c apple tensorflow-deps
```
上のコマンドはパッケージが見つからず失敗。(skip)

```
python -m pip install tensorflow-macos
python -m pip install tensorflow-metal
```

この状態で
```
python study.py

ImportError: cannot import name 'image_dataset_from_directory' from 'keras.preprocessing'
```


~~## M1/M2 Mac
[【Python】M1/M2 MacでPython環境の構築（機械学習・データ分析編）](https://namileriblog.com/python/python_library_ai/)~~
