from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import os
from keras.applications.resnet50 import preprocess_input
from shutil import copyfile
from keras.preprocessing.image import ImageDataGenerator

work_dir = '.'


# test_data_dir = 'E:/pcb_image_data/data_small/test'
# 载入模型
def read_model():
    model = load_model(work_dir + '/classify.model')
    return model


# 读取多张图片
def read_img_array(img_dir):
    img = []
    for f in os.listdir(img_dir):
        image_path = os.path.join(img_dir, f)
        if os.path.isfile(image_path):
            images = image.load_img(image_path, target_size=(100, 100))
            x = image.img_to_array(images)
            x = np.expand_dims(x, axis=0)
            img.append(x)
    x = np.concatenate([x for x in img])

    # 读取模型进行预测
    model = load_model(work_dir + '/classify.model')
    y = model.predict(x)
    return y


# 单张图片读取，并预测
def read_model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(100, 100))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    # print(x)

    # 归一化
    amin, amax = x.min(), x.max()  # 求最大最小值
    x = (x - amin) / (amax - amin)

    preds = model.predict(x)
    return preds


# 测试数据集读取
def read_test(test_data_dir):
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_generator = test_datagen.flow_from_directory(
        test_data_dir,
        target_size=(100, 100),
        batch_size=64,
        class_mode='binary'
    )
    model = load_model(work_dir + '/model_weight.h5')
    score = model.evaluate_generator(test_generator, steps=1)
    print("样本准确率%s: %.2f%%" % (model.metrics_names[1], score[1] * 100))
    # y = model.evaluate_generator(test_generator, 20, max_q_size=10,workers=1, use_multiprocessing=False)
    # name_list = model.predict_generator.filenames()
    # print(name_list)
    # return y


# 迭代读取文件夹下的所有文件，对每一张图片进行预测
def read_file_all(data_dir_path, model):
    right = 0
    wrong = 0
    for f in os.listdir(data_dir_path):
        image_path = os.path.join(data_dir_path, f)
        # print(f)
        if os.path.isfile(image_path):
            preds = read_model_predict(image_path, model)
            print(preds[0][0])
            if preds[0][0] >= 0.5:
                # rdst = 'E:/pcb_image_data/data_2500/right/' + f
                # copyfile(image_path, rdst)
                right += 1
            else:
                # wdst = 'E:/pcb_image_data/data_2500/wrong/' + f
                # copyfile(image_path, wdst)
                # print(preds[0][0])
                wrong += 1
        else:
            read_file_all(image_path)
    all_num = right + wrong
    Tacc = right / all_num
    Facc = wrong / all_num
    return Tacc, Facc


if __name__ == '__main__':
    '''
    img_dir = 'E:/pcb_image_data/data_small/test'
    read_test(img_dir)  #测试集验证,批量
    '''

    '''
    #批量读取文件图片
    y = read_img_array(img_dir)
    print(y)
    #根据得出识别结果
    err = 0 
    all_n = 0
    for i in range(len(y)):
        all_n += 1
        if y[i][0] >= 0.5:
            err += 1
            print('err')
    acc = err/all_n
    print('all',all_n)
    print('acc',acc)
    '''

    img_file = 'E:/pcb_image_data/data_small/validation/False'
    model = read_model()
    tc, fc = read_file_all(img_file, model)
    print('True 识别率', tc, '\n', 'False 识别率', fc)
