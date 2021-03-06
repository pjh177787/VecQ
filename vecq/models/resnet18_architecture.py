# Architecture reconstruction
import keras
import sys
sys.path.append('../')
from ..quantize_layers import Conv2D_Q, Dense_Q, DepthwiseConv2D_Q
def ResNet18(kq=None,
		bq=None,
		aq=None,
		activation=None,
		after_activation=None):
	inputs=keras.layers.Input(shape=(224,224,3))
	x0=keras.layers.normalization.BatchNormalization(name='bn_data',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=False,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(inputs)
	x1=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_1',
		trainable=True,
		padding=((3, 3), (3, 3)),
		data_format='channels_last')(x0)
	x2=Conv2D_Q(name='conv0',
		trainable=True,
		filters=64,
		kernel_size=(7, 7),
		strides=(2, 2),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x1)
	x3=keras.layers.normalization.BatchNormalization(name='bn0',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x2)
	x4=keras.layers.core.Activation(name='relu0',
		trainable=True,
		activation='relu')(x3)
	x5=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_2',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x4)
	x6=keras.layers.pooling.MaxPooling2D(name='pooling0',
		trainable=True,
		pool_size=(3, 3),
		padding='valid',
		strides=(2, 2),
		data_format='channels_last')(x5)
	x7=keras.layers.normalization.BatchNormalization(name='stage1_unit1_bn1',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x6)
	x8=keras.layers.core.Activation(name='stage1_unit1_relu1',
		trainable=True,
		activation='relu')(x7)
	x9=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_3',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x8)
	x10=Conv2D_Q(name='stage1_unit1_conv1',
		trainable=True,
		filters=64,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x9)
	x11=keras.layers.normalization.BatchNormalization(name='stage1_unit1_bn2',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x10)
	x12=keras.layers.core.Activation(name='stage1_unit1_relu2',
		trainable=True,
		activation='relu')(x11)
	x13=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_4',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x12)
	x14=Conv2D_Q(name='stage1_unit1_conv2',
		trainable=True,
		filters=64,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x13)
	x15=Conv2D_Q(name='stage1_unit1_sc',
		trainable=True,
		filters=64,
		kernel_size=(1, 1),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x8)
	x16=keras.layers.merge.Add(name='add_1',
		trainable=True)([x14,x15])
	x17=keras.layers.normalization.BatchNormalization(name='stage1_unit2_bn1',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x16)
	x18=keras.layers.core.Activation(name='stage1_unit2_relu1',
		trainable=True,
		activation='relu')(x17)
	x19=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_5',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x18)
	x20=Conv2D_Q(name='stage1_unit2_conv1',
		trainable=True,
		filters=64,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x19)
	x21=keras.layers.normalization.BatchNormalization(name='stage1_unit2_bn2',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x20)
	x22=keras.layers.core.Activation(name='stage1_unit2_relu2',
		trainable=True,
		activation='relu')(x21)
	x23=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_6',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x22)
	x24=Conv2D_Q(name='stage1_unit2_conv2',
		trainable=True,
		filters=64,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x23)
	x25=keras.layers.merge.Add(name='add_2',
		trainable=True)([x24,x16])
	x26=keras.layers.normalization.BatchNormalization(name='stage2_unit1_bn1',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x25)
	x27=keras.layers.core.Activation(name='stage2_unit1_relu1',
		trainable=True,
		activation='relu')(x26)
	x28=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_7',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x27)
	x29=Conv2D_Q(name='stage2_unit1_conv1',
		trainable=True,
		filters=128,
		kernel_size=(3, 3),
		strides=(2, 2),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x28)
	x30=keras.layers.normalization.BatchNormalization(name='stage2_unit1_bn2',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x29)
	x31=keras.layers.core.Activation(name='stage2_unit1_relu2',
		trainable=True,
		activation='relu')(x30)
	x32=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_8',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x31)
	x33=Conv2D_Q(name='stage2_unit1_conv2',
		trainable=True,
		filters=128,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x32)
	x34=Conv2D_Q(name='stage2_unit1_sc',
		trainable=True,
		filters=128,
		kernel_size=(1, 1),
		strides=(2, 2),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x27)
	x35=keras.layers.merge.Add(name='add_3',
		trainable=True)([x33,x34])
	x36=keras.layers.normalization.BatchNormalization(name='stage2_unit2_bn1',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x35)
	x37=keras.layers.core.Activation(name='stage2_unit2_relu1',
		trainable=True,
		activation='relu')(x36)
	x38=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_9',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x37)
	x39=Conv2D_Q(name='stage2_unit2_conv1',
		trainable=True,
		filters=128,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x38)
	x40=keras.layers.normalization.BatchNormalization(name='stage2_unit2_bn2',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x39)
	x41=keras.layers.core.Activation(name='stage2_unit2_relu2',
		trainable=True,
		activation='relu')(x40)
	x42=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_10',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x41)
	x43=Conv2D_Q(name='stage2_unit2_conv2',
		trainable=True,
		filters=128,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x42)
	x44=keras.layers.merge.Add(name='add_4',
		trainable=True)([x43,x35])
	x45=keras.layers.normalization.BatchNormalization(name='stage3_unit1_bn1',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x44)
	x46=keras.layers.core.Activation(name='stage3_unit1_relu1',
		trainable=True,
		activation='relu')(x45)
	x47=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_11',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x46)
	x48=Conv2D_Q(name='stage3_unit1_conv1',
		trainable=True,
		filters=256,
		kernel_size=(3, 3),
		strides=(2, 2),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x47)
	x49=keras.layers.normalization.BatchNormalization(name='stage3_unit1_bn2',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x48)
	x50=keras.layers.core.Activation(name='stage3_unit1_relu2',
		trainable=True,
		activation='relu')(x49)
	x51=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_12',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x50)
	x52=Conv2D_Q(name='stage3_unit1_conv2',
		trainable=True,
		filters=256,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x51)
	x53=Conv2D_Q(name='stage3_unit1_sc',
		trainable=True,
		filters=256,
		kernel_size=(1, 1),
		strides=(2, 2),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x46)
	x54=keras.layers.merge.Add(name='add_5',
		trainable=True)([x52,x53])
	x55=keras.layers.normalization.BatchNormalization(name='stage3_unit2_bn1',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x54)
	x56=keras.layers.core.Activation(name='stage3_unit2_relu1',
		trainable=True,
		activation='relu')(x55)
	x57=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_13',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x56)
	x58=Conv2D_Q(name='stage3_unit2_conv1',
		trainable=True,
		filters=256,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x57)
	x59=keras.layers.normalization.BatchNormalization(name='stage3_unit2_bn2',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x58)
	x60=keras.layers.core.Activation(name='stage3_unit2_relu2',
		trainable=True,
		activation='relu')(x59)
	x61=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_14',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x60)
	x62=Conv2D_Q(name='stage3_unit2_conv2',
		trainable=True,
		filters=256,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x61)
	x63=keras.layers.merge.Add(name='add_6',
		trainable=True)([x62,x54])
	x64=keras.layers.normalization.BatchNormalization(name='stage4_unit1_bn1',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x63)
	x65=keras.layers.core.Activation(name='stage4_unit1_relu1',
		trainable=True,
		activation='relu')(x64)
	x66=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_15',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x65)
	x67=Conv2D_Q(name='stage4_unit1_conv1',
		trainable=True,
		filters=512,
		kernel_size=(3, 3),
		strides=(2, 2),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x66)
	x68=keras.layers.normalization.BatchNormalization(name='stage4_unit1_bn2',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x67)
	x69=keras.layers.core.Activation(name='stage4_unit1_relu2',
		trainable=True,
		activation='relu')(x68)
	x70=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_16',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x69)
	x71=Conv2D_Q(name='stage4_unit1_conv2',
		trainable=True,
		filters=512,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x70)
	x72=Conv2D_Q(name='stage4_unit1_sc',
		trainable=True,
		filters=512,
		kernel_size=(1, 1),
		strides=(2, 2),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x65)
	x73=keras.layers.merge.Add(name='add_7',
		trainable=True)([x71,x72])
	x74=keras.layers.normalization.BatchNormalization(name='stage4_unit2_bn1',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x73)
	x75=keras.layers.core.Activation(name='stage4_unit2_relu1',
		trainable=True,
		activation='relu')(x74)
	x76=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_17',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x75)
	x77=Conv2D_Q(name='stage4_unit2_conv1',
		trainable=True,
		filters=512,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x76)
	x78=keras.layers.normalization.BatchNormalization(name='stage4_unit2_bn2',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x77)
	x79=keras.layers.core.Activation(name='stage4_unit2_relu2',
		trainable=True,
		activation='relu')(x78)
	x80=keras.layers.convolutional.ZeroPadding2D(name='zero_padding2d_18',
		trainable=True,
		padding=((1, 1), (1, 1)),
		data_format='channels_last')(x79)
	x81=Conv2D_Q(name='stage4_unit2_conv2',
		trainable=True,
		filters=512,
		kernel_size=(3, 3),
		strides=(1, 1),
		padding='valid',
		data_format='channels_last',
		dilation_rate=(1, 1),
		activation=activation,
		use_bias=False,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x80)
	x82=keras.layers.merge.Add(name='add_8',
		trainable=True)([x81,x73])
	x83=keras.layers.normalization.BatchNormalization(name='bn1',
		trainable=True,
		axis=3,
		momentum=0.99,
		epsilon=2e-05,
		center=True,
		scale=True,
		beta_initializer={'class_name': 'Zeros', 'config': {}},
		gamma_initializer={'class_name': 'Ones', 'config': {}},
		moving_mean_initializer={'class_name': 'Zeros', 'config': {}},
		moving_variance_initializer={'class_name': 'Ones', 'config': {}},
		beta_regularizer=None,
		gamma_regularizer=None,
		beta_constraint=None,
		gamma_constraint=None)(x82)
	x84=keras.layers.core.Activation(name='relu1',
		trainable=True,
		activation='relu')(x83)
	x85=keras.layers.pooling.GlobalAveragePooling2D(name='pool1',
		trainable=True,
		data_format='channels_last')(x84)
	x86=Dense_Q(name='fc1',
		trainable=True,
		units=1000,
		activation=activation,
		use_bias=True,
		kernel_regularizer=None,
		bias_regularizer=None,
		activity_regularizer=None,
		kernel_constraint=None,
		bias_constraint=None,
		kq=kq,
		bq=bq,
		aq=aq,
		after_activation=after_activation)(x85)
	x87=keras.layers.core.Activation(name='softmax',
		trainable=True,
		activation='softmax')(x86)
	model=keras.models.Model(inputs,x87)
	return model