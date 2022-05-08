# _*_ coding:utf-8 _*_
import os
import sys
import smtplib
sys.path.append('..')
import numpy as np
from keras.utils import plot_model
import matplotlib.pyplot as plt
from keras.optimizers import Adam
from model.model import ImageModel
from email.mime.text import MIMEText
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from image_matrix import image2matrix
from keras.preprocessing.image import ImageDataGenerator


def run(train_path):
    """
    训练模型
    """

    height = 400
    width = 600
    classes = 196
    epochs = 100
    batch_size = 64
    save_path = "../classify.model"

    #加载CNN模型
    model = ImageModel.build(width=width, heigth=height, classes=classes)
    # init_lr = 0.001  学习率
    init_lr = 1e-3
    decay=0.0
    opt = Adam(lr=init_lr, decay=decay)    #优化器
    # adam = Adam(lr=0.001, beta_1=0.99,beta_2=0.9, epsilon=1e-8)
    # 编译模型需要三个参数， 优化器，损失函数，指标列表
    model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=['accuracy'])
    train_matrix, test_matrix, train_label, test_label = image2matrix(train_path)

    # 图像预处理， rotation range的作用是用户指定旋转角度范围
    # width_shift_range & height_shift_range 分别是水平位置平移和上下位置平移
    # horizontal_flip的作用是随机对图片执行水平翻转操作
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True)

    result = model.fit_generator(
        datagen.flow(train_matrix, train_label, batch_size=batch_size), 
        validation_data=(test_matrix, test_label),
        # steps_per_epoch = len(train_matrix) // epochs,
        epochs=epochs,
        verbose=2,
        steps_per_epoch = train_matrix.shape[0],          #****************
        # callbacks=[EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto')]
        callbacks = [ModelCheckpoint('checkpoint.chk', monitor='val_loss',
                                     verbose=0, save_best_only=True, save_weights_only=False, mode='auto', period=1)]
        )
    model.save(save_path)
    print(model.summary())
    plot_model(model, to_file='model.png')
    plt.style.use("ggplot")
    plt.figure()
    n = epochs
    aranges = np.arange(0, n)
    plt.plot(result.history["loss"], label="train_loss")
    plt.plot(result.history["acc"], label="train_acc")
    plt.plot(result.history["val_loss"], label="val_loss")
    plt.plot(result.history["val_acc"], label="val_acc")

    plt.title("Image recognition")
    plt.xlabel("Epochs")
    plt.ylabel("loss/acc")
    plt.legend(loc="lower left")
    plt.savefig("reco.png")





if __name__ == "__main__":

    train = "../Img"
    run(train)
