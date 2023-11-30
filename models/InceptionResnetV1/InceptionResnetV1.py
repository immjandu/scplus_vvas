# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class InceptionResnetV1(torch.nn.Module):
    def __init__(self):
        super(InceptionResnetV1, self).__init__()
        self.module_0 = py_nndct.nn.Module('const') #InceptionResnetV1::24952
        self.module_1 = py_nndct.nn.Module('const') #InceptionResnetV1::24954
        self.module_2 = py_nndct.nn.Module('const') #InceptionResnetV1::24956
        self.module_3 = py_nndct.nn.Module('const') #InceptionResnetV1::24958
        self.module_4 = py_nndct.nn.Module('const') #InceptionResnetV1::24960
        self.module_5 = py_nndct.nn.Module('const') #InceptionResnetV1::24962
        self.module_6 = py_nndct.nn.Module('const') #InceptionResnetV1::24964
        self.module_7 = py_nndct.nn.Module('const') #InceptionResnetV1::24966
        self.module_8 = py_nndct.nn.Module('const') #InceptionResnetV1::24968
        self.module_9 = py_nndct.nn.Module('const') #InceptionResnetV1::24970
        self.module_10 = py_nndct.nn.Module('const') #InceptionResnetV1::24972
        self.module_11 = py_nndct.nn.Module('const') #InceptionResnetV1::24974
        self.module_12 = py_nndct.nn.Module('const') #InceptionResnetV1::24976
        self.module_13 = py_nndct.nn.Module('const') #InceptionResnetV1::24978
        self.module_14 = py_nndct.nn.Module('const') #InceptionResnetV1::24980
        self.module_15 = py_nndct.nn.Module('const') #InceptionResnetV1::24982
        self.module_16 = py_nndct.nn.Module('const') #InceptionResnetV1::24984
        self.module_17 = py_nndct.nn.Module('const') #InceptionResnetV1::24986
        self.module_18 = py_nndct.nn.Module('const') #InceptionResnetV1::24988
        self.module_19 = py_nndct.nn.Module('const') #InceptionResnetV1::24990
        self.module_20 = py_nndct.nn.Module('const') #InceptionResnetV1::24992
        self.module_21 = py_nndct.nn.Input() #InceptionResnetV1::input_0
        self.module_22 = py_nndct.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_1a]/Conv2d[conv]/input.3
        self.module_23 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_1a]/ReLU[relu]/input.7
        self.module_24 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_2a]/Conv2d[conv]/input.9
        self.module_25 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_2a]/ReLU[relu]/input.13
        self.module_26 = py_nndct.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_2b]/Conv2d[conv]/input.15
        self.module_27 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_2b]/ReLU[relu]/20946
        self.module_28 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #InceptionResnetV1::InceptionResnetV1/MaxPool2d[maxpool_3a]/input.19
        self.module_29 = py_nndct.nn.Conv2d(in_channels=64, out_channels=80, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_3b]/Conv2d[conv]/input.21
        self.module_30 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_3b]/ReLU[relu]/input.25
        self.module_31 = py_nndct.nn.Conv2d(in_channels=80, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_4a]/Conv2d[conv]/input.27
        self.module_32 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_4a]/ReLU[relu]/input.31
        self.module_33 = py_nndct.nn.Conv2d(in_channels=192, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_4b]/Conv2d[conv]/input.33
        self.module_34 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/BasicConv2d[conv2d_4b]/ReLU[relu]/input.37
        self.module_35 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/BasicConv2d[branch0]/Conv2d[conv]/input.39
        self.module_36 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/BasicConv2d[branch0]/ReLU[relu]/21064
        self.module_37 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.43
        self.module_38 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.47
        self.module_39 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.49
        self.module_40 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/21116
        self.module_41 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch2]/BasicConv2d[0]/Conv2d[conv]/input.53
        self.module_42 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch2]/BasicConv2d[0]/ReLU[relu]/input.57
        self.module_43 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch2]/BasicConv2d[1]/Conv2d[conv]/input.59
        self.module_44 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch2]/BasicConv2d[1]/ReLU[relu]/input.63
        self.module_45 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch2]/BasicConv2d[2]/Conv2d[conv]/input.65
        self.module_46 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Sequential[branch2]/BasicConv2d[2]/ReLU[relu]/21194
        self.module_47 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/input.69
        self.module_48 = py_nndct.nn.Conv2d(in_channels=96, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/Conv2d[conv2d]/21216
        self.module_49 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24953
        self.module_50 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/input.71
        self.module_51 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[0]/ReLU[relu]/input.73
        self.module_52 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/BasicConv2d[branch0]/Conv2d[conv]/input.75
        self.module_53 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/BasicConv2d[branch0]/ReLU[relu]/21247
        self.module_54 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.79
        self.module_55 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.83
        self.module_56 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.85
        self.module_57 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/21299
        self.module_58 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch2]/BasicConv2d[0]/Conv2d[conv]/input.89
        self.module_59 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch2]/BasicConv2d[0]/ReLU[relu]/input.93
        self.module_60 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch2]/BasicConv2d[1]/Conv2d[conv]/input.95
        self.module_61 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch2]/BasicConv2d[1]/ReLU[relu]/input.99
        self.module_62 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch2]/BasicConv2d[2]/Conv2d[conv]/input.101
        self.module_63 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Sequential[branch2]/BasicConv2d[2]/ReLU[relu]/21377
        self.module_64 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/input.105
        self.module_65 = py_nndct.nn.Conv2d(in_channels=96, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/Conv2d[conv2d]/21399
        self.module_66 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24955
        self.module_67 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/input.107
        self.module_68 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[1]/ReLU[relu]/input.109
        self.module_69 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/BasicConv2d[branch0]/Conv2d[conv]/input.111
        self.module_70 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/BasicConv2d[branch0]/ReLU[relu]/21430
        self.module_71 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.115
        self.module_72 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.119
        self.module_73 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.121
        self.module_74 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/21482
        self.module_75 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch2]/BasicConv2d[0]/Conv2d[conv]/input.125
        self.module_76 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch2]/BasicConv2d[0]/ReLU[relu]/input.129
        self.module_77 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch2]/BasicConv2d[1]/Conv2d[conv]/input.131
        self.module_78 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch2]/BasicConv2d[1]/ReLU[relu]/input.135
        self.module_79 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch2]/BasicConv2d[2]/Conv2d[conv]/input.137
        self.module_80 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Sequential[branch2]/BasicConv2d[2]/ReLU[relu]/21560
        self.module_81 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/input.141
        self.module_82 = py_nndct.nn.Conv2d(in_channels=96, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/Conv2d[conv2d]/21582
        self.module_83 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24957
        self.module_84 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/input.143
        self.module_85 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[2]/ReLU[relu]/input.145
        self.module_86 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/BasicConv2d[branch0]/Conv2d[conv]/input.147
        self.module_87 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/BasicConv2d[branch0]/ReLU[relu]/21613
        self.module_88 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.151
        self.module_89 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.155
        self.module_90 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.157
        self.module_91 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/21665
        self.module_92 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch2]/BasicConv2d[0]/Conv2d[conv]/input.161
        self.module_93 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch2]/BasicConv2d[0]/ReLU[relu]/input.165
        self.module_94 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch2]/BasicConv2d[1]/Conv2d[conv]/input.167
        self.module_95 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch2]/BasicConv2d[1]/ReLU[relu]/input.171
        self.module_96 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch2]/BasicConv2d[2]/Conv2d[conv]/input.173
        self.module_97 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Sequential[branch2]/BasicConv2d[2]/ReLU[relu]/21743
        self.module_98 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/input.177
        self.module_99 = py_nndct.nn.Conv2d(in_channels=96, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/Conv2d[conv2d]/21765
        self.module_100 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24959
        self.module_101 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/input.179
        self.module_102 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[3]/ReLU[relu]/input.181
        self.module_103 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/BasicConv2d[branch0]/Conv2d[conv]/input.183
        self.module_104 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/BasicConv2d[branch0]/ReLU[relu]/21796
        self.module_105 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.187
        self.module_106 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.191
        self.module_107 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.193
        self.module_108 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/21848
        self.module_109 = py_nndct.nn.Conv2d(in_channels=256, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch2]/BasicConv2d[0]/Conv2d[conv]/input.197
        self.module_110 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch2]/BasicConv2d[0]/ReLU[relu]/input.201
        self.module_111 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch2]/BasicConv2d[1]/Conv2d[conv]/input.203
        self.module_112 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch2]/BasicConv2d[1]/ReLU[relu]/input.207
        self.module_113 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch2]/BasicConv2d[2]/Conv2d[conv]/input.209
        self.module_114 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Sequential[branch2]/BasicConv2d[2]/ReLU[relu]/21926
        self.module_115 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/input.213
        self.module_116 = py_nndct.nn.Conv2d(in_channels=96, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/Conv2d[conv2d]/21948
        self.module_117 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24961
        self.module_118 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/input.215
        self.module_119 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_1]/Block35[4]/ReLU[relu]/input.217
        self.module_120 = py_nndct.nn.Conv2d(in_channels=256, out_channels=384, kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/BasicConv2d[branch0]/Conv2d[conv]/input.219
        self.module_121 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/BasicConv2d[branch0]/ReLU[relu]/21979
        self.module_122 = py_nndct.nn.Conv2d(in_channels=256, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.223
        self.module_123 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.227
        self.module_124 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.229
        self.module_125 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.233
        self.module_126 = py_nndct.nn.Conv2d(in_channels=192, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.235
        self.module_127 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/22057
        self.module_128 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/MaxPool2d[branch2]/22071
        self.module_129 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Mixed_6a[mixed_6a]/input.239
        self.module_130 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/BasicConv2d[branch0]/Conv2d[conv]/input.241
        self.module_131 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/BasicConv2d[branch0]/ReLU[relu]/22100
        self.module_132 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.245
        self.module_133 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.249
        self.module_134 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.251
        self.module_135 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.255
        self.module_136 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.257
        self.module_137 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/22178
        self.module_138 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/input.261
        self.module_139 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/Conv2d[conv2d]/22200
        self.module_140 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24963
        self.module_141 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/input.263
        self.module_142 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[0]/ReLU[relu]/input.265
        self.module_143 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/BasicConv2d[branch0]/Conv2d[conv]/input.267
        self.module_144 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/BasicConv2d[branch0]/ReLU[relu]/22231
        self.module_145 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.271
        self.module_146 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.275
        self.module_147 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.277
        self.module_148 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.281
        self.module_149 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.283
        self.module_150 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/22309
        self.module_151 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/input.287
        self.module_152 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/Conv2d[conv2d]/22331
        self.module_153 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24965
        self.module_154 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/input.289
        self.module_155 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[1]/ReLU[relu]/input.291
        self.module_156 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/BasicConv2d[branch0]/Conv2d[conv]/input.293
        self.module_157 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/BasicConv2d[branch0]/ReLU[relu]/22362
        self.module_158 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.297
        self.module_159 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.301
        self.module_160 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.303
        self.module_161 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.307
        self.module_162 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.309
        self.module_163 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/22440
        self.module_164 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/input.313
        self.module_165 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/Conv2d[conv2d]/22462
        self.module_166 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24967
        self.module_167 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/input.315
        self.module_168 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[2]/ReLU[relu]/input.317
        self.module_169 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/BasicConv2d[branch0]/Conv2d[conv]/input.319
        self.module_170 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/BasicConv2d[branch0]/ReLU[relu]/22493
        self.module_171 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.323
        self.module_172 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.327
        self.module_173 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.329
        self.module_174 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.333
        self.module_175 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.335
        self.module_176 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/22571
        self.module_177 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/input.339
        self.module_178 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/Conv2d[conv2d]/22593
        self.module_179 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24969
        self.module_180 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/input.341
        self.module_181 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[3]/ReLU[relu]/input.343
        self.module_182 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/BasicConv2d[branch0]/Conv2d[conv]/input.345
        self.module_183 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/BasicConv2d[branch0]/ReLU[relu]/22624
        self.module_184 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.349
        self.module_185 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.353
        self.module_186 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.355
        self.module_187 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.359
        self.module_188 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.361
        self.module_189 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/22702
        self.module_190 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/input.365
        self.module_191 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/Conv2d[conv2d]/22724
        self.module_192 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24971
        self.module_193 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/input.367
        self.module_194 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[4]/ReLU[relu]/input.369
        self.module_195 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/BasicConv2d[branch0]/Conv2d[conv]/input.371
        self.module_196 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/BasicConv2d[branch0]/ReLU[relu]/22755
        self.module_197 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.375
        self.module_198 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.379
        self.module_199 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.381
        self.module_200 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.385
        self.module_201 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.387
        self.module_202 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/22833
        self.module_203 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/input.391
        self.module_204 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/Conv2d[conv2d]/22855
        self.module_205 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24973
        self.module_206 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/input.393
        self.module_207 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[5]/ReLU[relu]/input.395
        self.module_208 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/BasicConv2d[branch0]/Conv2d[conv]/input.397
        self.module_209 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/BasicConv2d[branch0]/ReLU[relu]/22886
        self.module_210 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.401
        self.module_211 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.405
        self.module_212 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.407
        self.module_213 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.411
        self.module_214 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.413
        self.module_215 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/22964
        self.module_216 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/input.417
        self.module_217 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/Conv2d[conv2d]/22986
        self.module_218 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24975
        self.module_219 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/input.419
        self.module_220 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[6]/ReLU[relu]/input.421
        self.module_221 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/BasicConv2d[branch0]/Conv2d[conv]/input.423
        self.module_222 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/BasicConv2d[branch0]/ReLU[relu]/23017
        self.module_223 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.427
        self.module_224 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.431
        self.module_225 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.433
        self.module_226 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.437
        self.module_227 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.439
        self.module_228 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/23095
        self.module_229 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/input.443
        self.module_230 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/Conv2d[conv2d]/23117
        self.module_231 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24977
        self.module_232 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/input.445
        self.module_233 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[7]/ReLU[relu]/input.447
        self.module_234 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/BasicConv2d[branch0]/Conv2d[conv]/input.449
        self.module_235 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/BasicConv2d[branch0]/ReLU[relu]/23148
        self.module_236 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.453
        self.module_237 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.457
        self.module_238 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.459
        self.module_239 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.463
        self.module_240 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.465
        self.module_241 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/23226
        self.module_242 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/input.469
        self.module_243 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/Conv2d[conv2d]/23248
        self.module_244 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24979
        self.module_245 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/input.471
        self.module_246 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[8]/ReLU[relu]/input.473
        self.module_247 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/BasicConv2d[branch0]/Conv2d[conv]/input.475
        self.module_248 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/BasicConv2d[branch0]/ReLU[relu]/23279
        self.module_249 = py_nndct.nn.Conv2d(in_channels=896, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.479
        self.module_250 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.483
        self.module_251 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 7], stride=[1, 1], padding=[0, 3], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.485
        self.module_252 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.489
        self.module_253 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[7, 1], stride=[1, 1], padding=[3, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.491
        self.module_254 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/23357
        self.module_255 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/input.495
        self.module_256 = py_nndct.nn.Conv2d(in_channels=256, out_channels=896, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/Conv2d[conv2d]/23379
        self.module_257 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24981
        self.module_258 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/input.497
        self.module_259 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_2]/Block17[9]/ReLU[relu]/input.499
        self.module_260 = py_nndct.nn.Conv2d(in_channels=896, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch0]/BasicConv2d[0]/Conv2d[conv]/input.501
        self.module_261 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch0]/BasicConv2d[0]/ReLU[relu]/input.505
        self.module_262 = py_nndct.nn.Conv2d(in_channels=256, out_channels=384, kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch0]/BasicConv2d[1]/Conv2d[conv]/input.507
        self.module_263 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch0]/BasicConv2d[1]/ReLU[relu]/23436
        self.module_264 = py_nndct.nn.Conv2d(in_channels=896, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.511
        self.module_265 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.515
        self.module_266 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.517
        self.module_267 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/23488
        self.module_268 = py_nndct.nn.Conv2d(in_channels=896, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch2]/BasicConv2d[0]/Conv2d[conv]/input.521
        self.module_269 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch2]/BasicConv2d[0]/ReLU[relu]/input.525
        self.module_270 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch2]/BasicConv2d[1]/Conv2d[conv]/input.527
        self.module_271 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch2]/BasicConv2d[1]/ReLU[relu]/input.531
        self.module_272 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch2]/BasicConv2d[2]/Conv2d[conv]/input.533
        self.module_273 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/Sequential[branch2]/BasicConv2d[2]/ReLU[relu]/23566
        self.module_274 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[2, 2], padding=[0, 0], dilation=[1, 1], ceil_mode=False) #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/MaxPool2d[branch3]/23580
        self.module_275 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Mixed_7a[mixed_7a]/input.537
        self.module_276 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/BasicConv2d[branch0]/Conv2d[conv]/input.539
        self.module_277 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/BasicConv2d[branch0]/ReLU[relu]/23609
        self.module_278 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.543
        self.module_279 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.547
        self.module_280 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 3], stride=[1, 1], padding=[0, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.549
        self.module_281 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.553
        self.module_282 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 1], stride=[1, 1], padding=[1, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.555
        self.module_283 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/23687
        self.module_284 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/input.559
        self.module_285 = py_nndct.nn.Conv2d(in_channels=384, out_channels=1792, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/Conv2d[conv2d]/23709
        self.module_286 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24983
        self.module_287 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/input.561
        self.module_288 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[0]/ReLU[relu]/input.563
        self.module_289 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/BasicConv2d[branch0]/Conv2d[conv]/input.565
        self.module_290 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/BasicConv2d[branch0]/ReLU[relu]/23740
        self.module_291 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.569
        self.module_292 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.573
        self.module_293 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 3], stride=[1, 1], padding=[0, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.575
        self.module_294 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.579
        self.module_295 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 1], stride=[1, 1], padding=[1, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.581
        self.module_296 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/23818
        self.module_297 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/input.585
        self.module_298 = py_nndct.nn.Conv2d(in_channels=384, out_channels=1792, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/Conv2d[conv2d]/23840
        self.module_299 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24985
        self.module_300 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/input.587
        self.module_301 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[1]/ReLU[relu]/input.589
        self.module_302 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/BasicConv2d[branch0]/Conv2d[conv]/input.591
        self.module_303 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/BasicConv2d[branch0]/ReLU[relu]/23871
        self.module_304 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.595
        self.module_305 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.599
        self.module_306 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 3], stride=[1, 1], padding=[0, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.601
        self.module_307 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.605
        self.module_308 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 1], stride=[1, 1], padding=[1, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.607
        self.module_309 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/23949
        self.module_310 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/input.611
        self.module_311 = py_nndct.nn.Conv2d(in_channels=384, out_channels=1792, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/Conv2d[conv2d]/23971
        self.module_312 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24987
        self.module_313 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/input.613
        self.module_314 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[2]/ReLU[relu]/input.615
        self.module_315 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/BasicConv2d[branch0]/Conv2d[conv]/input.617
        self.module_316 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/BasicConv2d[branch0]/ReLU[relu]/24002
        self.module_317 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.621
        self.module_318 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.625
        self.module_319 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 3], stride=[1, 1], padding=[0, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.627
        self.module_320 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.631
        self.module_321 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 1], stride=[1, 1], padding=[1, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.633
        self.module_322 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/24080
        self.module_323 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/input.637
        self.module_324 = py_nndct.nn.Conv2d(in_channels=384, out_channels=1792, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/Conv2d[conv2d]/24102
        self.module_325 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24989
        self.module_326 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/input.639
        self.module_327 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[3]/ReLU[relu]/input.641
        self.module_328 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/BasicConv2d[branch0]/Conv2d[conv]/input.643
        self.module_329 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/BasicConv2d[branch0]/ReLU[relu]/24133
        self.module_330 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.647
        self.module_331 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.651
        self.module_332 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 3], stride=[1, 1], padding=[0, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.653
        self.module_333 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.657
        self.module_334 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 1], stride=[1, 1], padding=[1, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.659
        self.module_335 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/24211
        self.module_336 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/input.663
        self.module_337 = py_nndct.nn.Conv2d(in_channels=384, out_channels=1792, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/Conv2d[conv2d]/24233
        self.module_338 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24991
        self.module_339 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/input.665
        self.module_340 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Sequential[repeat_3]/Block8[4]/ReLU[relu]/input.667
        self.module_341 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Block8[block8]/BasicConv2d[branch0]/Conv2d[conv]/input.669
        self.module_342 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Block8[block8]/BasicConv2d[branch0]/ReLU[relu]/24264
        self.module_343 = py_nndct.nn.Conv2d(in_channels=1792, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Block8[block8]/Sequential[branch1]/BasicConv2d[0]/Conv2d[conv]/input.673
        self.module_344 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Block8[block8]/Sequential[branch1]/BasicConv2d[0]/ReLU[relu]/input.677
        self.module_345 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[1, 3], stride=[1, 1], padding=[0, 1], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Block8[block8]/Sequential[branch1]/BasicConv2d[1]/Conv2d[conv]/input.679
        self.module_346 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Block8[block8]/Sequential[branch1]/BasicConv2d[1]/ReLU[relu]/input.683
        self.module_347 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 1], stride=[1, 1], padding=[1, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Block8[block8]/Sequential[branch1]/BasicConv2d[2]/Conv2d[conv]/input.685
        self.module_348 = py_nndct.nn.ReLU(inplace=False) #InceptionResnetV1::InceptionResnetV1/Block8[block8]/Sequential[branch1]/BasicConv2d[2]/ReLU[relu]/24342
        self.module_349 = py_nndct.nn.Cat() #InceptionResnetV1::InceptionResnetV1/Block8[block8]/input.689
        self.module_350 = py_nndct.nn.Conv2d(in_channels=384, out_channels=1792, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #InceptionResnetV1::InceptionResnetV1/Block8[block8]/Conv2d[conv2d]/24364
        self.module_351 = py_nndct.nn.Module('elemwise_mul') #InceptionResnetV1::24993
        self.module_352 = py_nndct.nn.Add() #InceptionResnetV1::InceptionResnetV1/Block8[block8]/input.691
        self.module_353 = py_nndct.nn.AdaptiveAvgPool2d(output_size=1) #InceptionResnetV1::InceptionResnetV1/AdaptiveAvgPool2d[avgpool_1a]/input.693
        self.module_354 = py_nndct.nn.Module('shape') #InceptionResnetV1::InceptionResnetV1/24389
        self.module_355 = py_nndct.nn.Module('reshape') #InceptionResnetV1::InceptionResnetV1/input.695
        self.module_356 = py_nndct.nn.Linear(in_features=1792, out_features=512, bias=False) #InceptionResnetV1::InceptionResnetV1/Linear[last_linear]/input
        self.module_357 = py_nndct.nn.BatchNorm(num_features=512, eps=0.0, momentum=0.1) #InceptionResnetV1::InceptionResnetV1/BatchNorm1d[last_bn]/24410

    def forward(self, *args):
        output_module_0 = self.module_0(data=0.17000000178813934, dtype=torch.float, device='cpu')
        output_module_1 = self.module_1(data=0.17000000178813934, dtype=torch.float, device='cpu')
        output_module_2 = self.module_2(data=0.17000000178813934, dtype=torch.float, device='cpu')
        output_module_3 = self.module_3(data=0.17000000178813934, dtype=torch.float, device='cpu')
        output_module_4 = self.module_4(data=0.17000000178813934, dtype=torch.float, device='cpu')
        output_module_5 = self.module_5(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_6 = self.module_6(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_7 = self.module_7(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_8 = self.module_8(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_9 = self.module_9(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_10 = self.module_10(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_11 = self.module_11(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_12 = self.module_12(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_13 = self.module_13(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_14 = self.module_14(data=0.10000000149011612, dtype=torch.float, device='cpu')
        output_module_15 = self.module_15(data=0.20000000298023224, dtype=torch.float, device='cpu')
        output_module_16 = self.module_16(data=0.20000000298023224, dtype=torch.float, device='cpu')
        output_module_17 = self.module_17(data=0.20000000298023224, dtype=torch.float, device='cpu')
        output_module_18 = self.module_18(data=0.20000000298023224, dtype=torch.float, device='cpu')
        output_module_19 = self.module_19(data=0.20000000298023224, dtype=torch.float, device='cpu')
        output_module_20 = self.module_20(data=1.0, dtype=torch.float, device='cpu')
        output_module_21 = self.module_21(input=args[0])
        output_module_21 = self.module_22(output_module_21)
        output_module_21 = self.module_23(output_module_21)
        output_module_21 = self.module_24(output_module_21)
        output_module_21 = self.module_25(output_module_21)
        output_module_21 = self.module_26(output_module_21)
        output_module_21 = self.module_27(output_module_21)
        output_module_21 = self.module_28(output_module_21)
        output_module_21 = self.module_29(output_module_21)
        output_module_21 = self.module_30(output_module_21)
        output_module_21 = self.module_31(output_module_21)
        output_module_21 = self.module_32(output_module_21)
        output_module_21 = self.module_33(output_module_21)
        output_module_21 = self.module_34(output_module_21)
        output_module_35 = self.module_35(output_module_21)
        output_module_35 = self.module_36(output_module_35)
        output_module_37 = self.module_37(output_module_21)
        output_module_37 = self.module_38(output_module_37)
        output_module_37 = self.module_39(output_module_37)
        output_module_37 = self.module_40(output_module_37)
        output_module_41 = self.module_41(output_module_21)
        output_module_41 = self.module_42(output_module_41)
        output_module_41 = self.module_43(output_module_41)
        output_module_41 = self.module_44(output_module_41)
        output_module_41 = self.module_45(output_module_41)
        output_module_41 = self.module_46(output_module_41)
        output_module_35 = self.module_47(dim=1, tensors=[output_module_35,output_module_37,output_module_41])
        output_module_35 = self.module_48(output_module_35)
        output_module_35 = self.module_49(input=output_module_35, other=output_module_0)
        output_module_35 = self.module_50(input=output_module_35, other=output_module_21, alpha=1)
        output_module_35 = self.module_51(output_module_35)
        output_module_52 = self.module_52(output_module_35)
        output_module_52 = self.module_53(output_module_52)
        output_module_54 = self.module_54(output_module_35)
        output_module_54 = self.module_55(output_module_54)
        output_module_54 = self.module_56(output_module_54)
        output_module_54 = self.module_57(output_module_54)
        output_module_58 = self.module_58(output_module_35)
        output_module_58 = self.module_59(output_module_58)
        output_module_58 = self.module_60(output_module_58)
        output_module_58 = self.module_61(output_module_58)
        output_module_58 = self.module_62(output_module_58)
        output_module_58 = self.module_63(output_module_58)
        output_module_52 = self.module_64(dim=1, tensors=[output_module_52,output_module_54,output_module_58])
        output_module_52 = self.module_65(output_module_52)
        output_module_52 = self.module_66(input=output_module_52, other=output_module_1)
        output_module_52 = self.module_67(input=output_module_52, other=output_module_35, alpha=1)
        output_module_52 = self.module_68(output_module_52)
        output_module_69 = self.module_69(output_module_52)
        output_module_69 = self.module_70(output_module_69)
        output_module_71 = self.module_71(output_module_52)
        output_module_71 = self.module_72(output_module_71)
        output_module_71 = self.module_73(output_module_71)
        output_module_71 = self.module_74(output_module_71)
        output_module_75 = self.module_75(output_module_52)
        output_module_75 = self.module_76(output_module_75)
        output_module_75 = self.module_77(output_module_75)
        output_module_75 = self.module_78(output_module_75)
        output_module_75 = self.module_79(output_module_75)
        output_module_75 = self.module_80(output_module_75)
        output_module_69 = self.module_81(dim=1, tensors=[output_module_69,output_module_71,output_module_75])
        output_module_69 = self.module_82(output_module_69)
        output_module_69 = self.module_83(input=output_module_69, other=output_module_2)
        output_module_69 = self.module_84(input=output_module_69, other=output_module_52, alpha=1)
        output_module_69 = self.module_85(output_module_69)
        output_module_86 = self.module_86(output_module_69)
        output_module_86 = self.module_87(output_module_86)
        output_module_88 = self.module_88(output_module_69)
        output_module_88 = self.module_89(output_module_88)
        output_module_88 = self.module_90(output_module_88)
        output_module_88 = self.module_91(output_module_88)
        output_module_92 = self.module_92(output_module_69)
        output_module_92 = self.module_93(output_module_92)
        output_module_92 = self.module_94(output_module_92)
        output_module_92 = self.module_95(output_module_92)
        output_module_92 = self.module_96(output_module_92)
        output_module_92 = self.module_97(output_module_92)
        output_module_86 = self.module_98(dim=1, tensors=[output_module_86,output_module_88,output_module_92])
        output_module_86 = self.module_99(output_module_86)
        output_module_86 = self.module_100(input=output_module_86, other=output_module_3)
        output_module_86 = self.module_101(input=output_module_86, other=output_module_69, alpha=1)
        output_module_86 = self.module_102(output_module_86)
        output_module_103 = self.module_103(output_module_86)
        output_module_103 = self.module_104(output_module_103)
        output_module_105 = self.module_105(output_module_86)
        output_module_105 = self.module_106(output_module_105)
        output_module_105 = self.module_107(output_module_105)
        output_module_105 = self.module_108(output_module_105)
        output_module_109 = self.module_109(output_module_86)
        output_module_109 = self.module_110(output_module_109)
        output_module_109 = self.module_111(output_module_109)
        output_module_109 = self.module_112(output_module_109)
        output_module_109 = self.module_113(output_module_109)
        output_module_109 = self.module_114(output_module_109)
        output_module_103 = self.module_115(dim=1, tensors=[output_module_103,output_module_105,output_module_109])
        output_module_103 = self.module_116(output_module_103)
        output_module_103 = self.module_117(input=output_module_103, other=output_module_4)
        output_module_103 = self.module_118(input=output_module_103, other=output_module_86, alpha=1)
        output_module_103 = self.module_119(output_module_103)
        output_module_120 = self.module_120(output_module_103)
        output_module_120 = self.module_121(output_module_120)
        output_module_122 = self.module_122(output_module_103)
        output_module_122 = self.module_123(output_module_122)
        output_module_122 = self.module_124(output_module_122)
        output_module_122 = self.module_125(output_module_122)
        output_module_122 = self.module_126(output_module_122)
        output_module_122 = self.module_127(output_module_122)
        output_module_128 = self.module_128(output_module_103)
        output_module_120 = self.module_129(dim=1, tensors=[output_module_120,output_module_122,output_module_128])
        output_module_130 = self.module_130(output_module_120)
        output_module_130 = self.module_131(output_module_130)
        output_module_132 = self.module_132(output_module_120)
        output_module_132 = self.module_133(output_module_132)
        output_module_132 = self.module_134(output_module_132)
        output_module_132 = self.module_135(output_module_132)
        output_module_132 = self.module_136(output_module_132)
        output_module_132 = self.module_137(output_module_132)
        output_module_130 = self.module_138(dim=1, tensors=[output_module_130,output_module_132])
        output_module_130 = self.module_139(output_module_130)
        output_module_130 = self.module_140(input=output_module_130, other=output_module_5)
        output_module_130 = self.module_141(input=output_module_130, other=output_module_120, alpha=1)
        output_module_130 = self.module_142(output_module_130)
        output_module_143 = self.module_143(output_module_130)
        output_module_143 = self.module_144(output_module_143)
        output_module_145 = self.module_145(output_module_130)
        output_module_145 = self.module_146(output_module_145)
        output_module_145 = self.module_147(output_module_145)
        output_module_145 = self.module_148(output_module_145)
        output_module_145 = self.module_149(output_module_145)
        output_module_145 = self.module_150(output_module_145)
        output_module_143 = self.module_151(dim=1, tensors=[output_module_143,output_module_145])
        output_module_143 = self.module_152(output_module_143)
        output_module_143 = self.module_153(input=output_module_143, other=output_module_6)
        output_module_143 = self.module_154(input=output_module_143, other=output_module_130, alpha=1)
        output_module_143 = self.module_155(output_module_143)
        output_module_156 = self.module_156(output_module_143)
        output_module_156 = self.module_157(output_module_156)
        output_module_158 = self.module_158(output_module_143)
        output_module_158 = self.module_159(output_module_158)
        output_module_158 = self.module_160(output_module_158)
        output_module_158 = self.module_161(output_module_158)
        output_module_158 = self.module_162(output_module_158)
        output_module_158 = self.module_163(output_module_158)
        output_module_156 = self.module_164(dim=1, tensors=[output_module_156,output_module_158])
        output_module_156 = self.module_165(output_module_156)
        output_module_156 = self.module_166(input=output_module_156, other=output_module_7)
        output_module_156 = self.module_167(input=output_module_156, other=output_module_143, alpha=1)
        output_module_156 = self.module_168(output_module_156)
        output_module_169 = self.module_169(output_module_156)
        output_module_169 = self.module_170(output_module_169)
        output_module_171 = self.module_171(output_module_156)
        output_module_171 = self.module_172(output_module_171)
        output_module_171 = self.module_173(output_module_171)
        output_module_171 = self.module_174(output_module_171)
        output_module_171 = self.module_175(output_module_171)
        output_module_171 = self.module_176(output_module_171)
        output_module_169 = self.module_177(dim=1, tensors=[output_module_169,output_module_171])
        output_module_169 = self.module_178(output_module_169)
        output_module_169 = self.module_179(input=output_module_169, other=output_module_8)
        output_module_169 = self.module_180(input=output_module_169, other=output_module_156, alpha=1)
        output_module_169 = self.module_181(output_module_169)
        output_module_182 = self.module_182(output_module_169)
        output_module_182 = self.module_183(output_module_182)
        output_module_184 = self.module_184(output_module_169)
        output_module_184 = self.module_185(output_module_184)
        output_module_184 = self.module_186(output_module_184)
        output_module_184 = self.module_187(output_module_184)
        output_module_184 = self.module_188(output_module_184)
        output_module_184 = self.module_189(output_module_184)
        output_module_182 = self.module_190(dim=1, tensors=[output_module_182,output_module_184])
        output_module_182 = self.module_191(output_module_182)
        output_module_182 = self.module_192(input=output_module_182, other=output_module_9)
        output_module_182 = self.module_193(input=output_module_182, other=output_module_169, alpha=1)
        output_module_182 = self.module_194(output_module_182)
        output_module_195 = self.module_195(output_module_182)
        output_module_195 = self.module_196(output_module_195)
        output_module_197 = self.module_197(output_module_182)
        output_module_197 = self.module_198(output_module_197)
        output_module_197 = self.module_199(output_module_197)
        output_module_197 = self.module_200(output_module_197)
        output_module_197 = self.module_201(output_module_197)
        output_module_197 = self.module_202(output_module_197)
        output_module_195 = self.module_203(dim=1, tensors=[output_module_195,output_module_197])
        output_module_195 = self.module_204(output_module_195)
        output_module_195 = self.module_205(input=output_module_195, other=output_module_10)
        output_module_195 = self.module_206(input=output_module_195, other=output_module_182, alpha=1)
        output_module_195 = self.module_207(output_module_195)
        output_module_208 = self.module_208(output_module_195)
        output_module_208 = self.module_209(output_module_208)
        output_module_210 = self.module_210(output_module_195)
        output_module_210 = self.module_211(output_module_210)
        output_module_210 = self.module_212(output_module_210)
        output_module_210 = self.module_213(output_module_210)
        output_module_210 = self.module_214(output_module_210)
        output_module_210 = self.module_215(output_module_210)
        output_module_208 = self.module_216(dim=1, tensors=[output_module_208,output_module_210])
        output_module_208 = self.module_217(output_module_208)
        output_module_208 = self.module_218(input=output_module_208, other=output_module_11)
        output_module_208 = self.module_219(input=output_module_208, other=output_module_195, alpha=1)
        output_module_208 = self.module_220(output_module_208)
        output_module_221 = self.module_221(output_module_208)
        output_module_221 = self.module_222(output_module_221)
        output_module_223 = self.module_223(output_module_208)
        output_module_223 = self.module_224(output_module_223)
        output_module_223 = self.module_225(output_module_223)
        output_module_223 = self.module_226(output_module_223)
        output_module_223 = self.module_227(output_module_223)
        output_module_223 = self.module_228(output_module_223)
        output_module_221 = self.module_229(dim=1, tensors=[output_module_221,output_module_223])
        output_module_221 = self.module_230(output_module_221)
        output_module_221 = self.module_231(input=output_module_221, other=output_module_12)
        output_module_221 = self.module_232(input=output_module_221, other=output_module_208, alpha=1)
        output_module_221 = self.module_233(output_module_221)
        output_module_234 = self.module_234(output_module_221)
        output_module_234 = self.module_235(output_module_234)
        output_module_236 = self.module_236(output_module_221)
        output_module_236 = self.module_237(output_module_236)
        output_module_236 = self.module_238(output_module_236)
        output_module_236 = self.module_239(output_module_236)
        output_module_236 = self.module_240(output_module_236)
        output_module_236 = self.module_241(output_module_236)
        output_module_234 = self.module_242(dim=1, tensors=[output_module_234,output_module_236])
        output_module_234 = self.module_243(output_module_234)
        output_module_234 = self.module_244(input=output_module_234, other=output_module_13)
        output_module_234 = self.module_245(input=output_module_234, other=output_module_221, alpha=1)
        output_module_234 = self.module_246(output_module_234)
        output_module_247 = self.module_247(output_module_234)
        output_module_247 = self.module_248(output_module_247)
        output_module_249 = self.module_249(output_module_234)
        output_module_249 = self.module_250(output_module_249)
        output_module_249 = self.module_251(output_module_249)
        output_module_249 = self.module_252(output_module_249)
        output_module_249 = self.module_253(output_module_249)
        output_module_249 = self.module_254(output_module_249)
        output_module_247 = self.module_255(dim=1, tensors=[output_module_247,output_module_249])
        output_module_247 = self.module_256(output_module_247)
        output_module_247 = self.module_257(input=output_module_247, other=output_module_14)
        output_module_247 = self.module_258(input=output_module_247, other=output_module_234, alpha=1)
        output_module_247 = self.module_259(output_module_247)
        output_module_260 = self.module_260(output_module_247)
        output_module_260 = self.module_261(output_module_260)
        output_module_260 = self.module_262(output_module_260)
        output_module_260 = self.module_263(output_module_260)
        output_module_264 = self.module_264(output_module_247)
        output_module_264 = self.module_265(output_module_264)
        output_module_264 = self.module_266(output_module_264)
        output_module_264 = self.module_267(output_module_264)
        output_module_268 = self.module_268(output_module_247)
        output_module_268 = self.module_269(output_module_268)
        output_module_268 = self.module_270(output_module_268)
        output_module_268 = self.module_271(output_module_268)
        output_module_268 = self.module_272(output_module_268)
        output_module_268 = self.module_273(output_module_268)
        output_module_274 = self.module_274(output_module_247)
        output_module_260 = self.module_275(dim=1, tensors=[output_module_260,output_module_264,output_module_268,output_module_274])
        output_module_276 = self.module_276(output_module_260)
        output_module_276 = self.module_277(output_module_276)
        output_module_278 = self.module_278(output_module_260)
        output_module_278 = self.module_279(output_module_278)
        output_module_278 = self.module_280(output_module_278)
        output_module_278 = self.module_281(output_module_278)
        output_module_278 = self.module_282(output_module_278)
        output_module_278 = self.module_283(output_module_278)
        output_module_276 = self.module_284(dim=1, tensors=[output_module_276,output_module_278])
        output_module_276 = self.module_285(output_module_276)
        output_module_276 = self.module_286(input=output_module_276, other=output_module_15)
        output_module_276 = self.module_287(input=output_module_276, other=output_module_260, alpha=1)
        output_module_276 = self.module_288(output_module_276)
        output_module_289 = self.module_289(output_module_276)
        output_module_289 = self.module_290(output_module_289)
        output_module_291 = self.module_291(output_module_276)
        output_module_291 = self.module_292(output_module_291)
        output_module_291 = self.module_293(output_module_291)
        output_module_291 = self.module_294(output_module_291)
        output_module_291 = self.module_295(output_module_291)
        output_module_291 = self.module_296(output_module_291)
        output_module_289 = self.module_297(dim=1, tensors=[output_module_289,output_module_291])
        output_module_289 = self.module_298(output_module_289)
        output_module_289 = self.module_299(input=output_module_289, other=output_module_16)
        output_module_289 = self.module_300(input=output_module_289, other=output_module_276, alpha=1)
        output_module_289 = self.module_301(output_module_289)
        output_module_302 = self.module_302(output_module_289)
        output_module_302 = self.module_303(output_module_302)
        output_module_304 = self.module_304(output_module_289)
        output_module_304 = self.module_305(output_module_304)
        output_module_304 = self.module_306(output_module_304)
        output_module_304 = self.module_307(output_module_304)
        output_module_304 = self.module_308(output_module_304)
        output_module_304 = self.module_309(output_module_304)
        output_module_302 = self.module_310(dim=1, tensors=[output_module_302,output_module_304])
        output_module_302 = self.module_311(output_module_302)
        output_module_302 = self.module_312(input=output_module_302, other=output_module_17)
        output_module_302 = self.module_313(input=output_module_302, other=output_module_289, alpha=1)
        output_module_302 = self.module_314(output_module_302)
        output_module_315 = self.module_315(output_module_302)
        output_module_315 = self.module_316(output_module_315)
        output_module_317 = self.module_317(output_module_302)
        output_module_317 = self.module_318(output_module_317)
        output_module_317 = self.module_319(output_module_317)
        output_module_317 = self.module_320(output_module_317)
        output_module_317 = self.module_321(output_module_317)
        output_module_317 = self.module_322(output_module_317)
        output_module_315 = self.module_323(dim=1, tensors=[output_module_315,output_module_317])
        output_module_315 = self.module_324(output_module_315)
        output_module_315 = self.module_325(input=output_module_315, other=output_module_18)
        output_module_315 = self.module_326(input=output_module_315, other=output_module_302, alpha=1)
        output_module_315 = self.module_327(output_module_315)
        output_module_328 = self.module_328(output_module_315)
        output_module_328 = self.module_329(output_module_328)
        output_module_330 = self.module_330(output_module_315)
        output_module_330 = self.module_331(output_module_330)
        output_module_330 = self.module_332(output_module_330)
        output_module_330 = self.module_333(output_module_330)
        output_module_330 = self.module_334(output_module_330)
        output_module_330 = self.module_335(output_module_330)
        output_module_328 = self.module_336(dim=1, tensors=[output_module_328,output_module_330])
        output_module_328 = self.module_337(output_module_328)
        output_module_328 = self.module_338(input=output_module_328, other=output_module_19)
        output_module_328 = self.module_339(input=output_module_328, other=output_module_315, alpha=1)
        output_module_328 = self.module_340(output_module_328)
        output_module_341 = self.module_341(output_module_328)
        output_module_341 = self.module_342(output_module_341)
        output_module_343 = self.module_343(output_module_328)
        output_module_343 = self.module_344(output_module_343)
        output_module_343 = self.module_345(output_module_343)
        output_module_343 = self.module_346(output_module_343)
        output_module_343 = self.module_347(output_module_343)
        output_module_343 = self.module_348(output_module_343)
        output_module_341 = self.module_349(dim=1, tensors=[output_module_341,output_module_343])
        output_module_341 = self.module_350(output_module_341)
        output_module_341 = self.module_351(input=output_module_341, other=output_module_20)
        output_module_341 = self.module_352(input=output_module_341, other=output_module_328, alpha=1)
        output_module_341 = self.module_353(output_module_341)
        output_module_354 = self.module_354(input=output_module_341, dim=0)
        output_module_355 = self.module_355(input=output_module_341, shape=[output_module_354,-1])
        output_module_355 = self.module_356(output_module_355)
        output_module_355 = self.module_357(output_module_355)
        return output_module_355
