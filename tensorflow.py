import tensorflow as tf
import os
# from tensorflow import keras
from keras.applications.mobilenet import MobileNet
from keras.layers import Input, Dense, GlobalAveragePooling2D
# from tensorflow.keras import optimizers
from keras.models import Sequential
from keras.preprocessing import image_dataset_from_directory


IMAGE_SIZE = 224


def get_data():
    # 画像ファイル含むデータセットダウンロード
    train_dir = os.path.dirname(
        "cats_and_dogs_filtered/validation/")

    BATCH_SIZE = 32
    IMG_SIZE = (IMAGE_SIZE, IMAGE_SIZE)

    # 訓練データセット作成
    train_dataset = image_dataset_from_directory(
        train_dir, shuffle=True, batch_size=BATCH_SIZE, image_size=IMG_SIZE)

    return train_dataset


def create_model():
    # Lambdaを使わずにMobaileNetのpreprocess_inputを再現することが
    # Sequential APIでは難しそうなので、自前で関数を作ってnetworkの外に切り出す

    # Sequential APIでモデルを定義する
    model = Sequential()
    base_model = MobileNet(
        input_shape=[IMAGE_SIZE, IMAGE_SIZE, 3],
        include_top=False, weights='imagenet')
    base_model.trainable = False

    # conv_dw_11以降のLaylerを学習対象にする
    for layer in base_model.layers[67:]:
        layer.trainable = True

    model.add(base_model)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(1, activation='sigmoid'))

    base_learning_rate = 0.0001

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate),
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    # モデルのアーキテクチャを出力
    model.summary()
    return model


model = create_model()

epochs = 10

train_dataset = get_data()

# model.load_weights('model')

history = model.fit(train_dataset,
                    epochs=epochs)

model.save_weights('model')