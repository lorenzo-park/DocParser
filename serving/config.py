from docparser.utils.data_utils import DocsDataset
from docparser.utils.experiment_utils import DocparserDefaultConfig

import os


# keras model file path
WEIGHT_PATH = '/root/DocParser/serving/model/docparser.h5'
MODEL_DIR = os.path.dirname(WEIGHT_PATH)

# Path where the Frozen PB will be save
FROZEN_PB_DIR = '/root/DocParser/serving/frozen_model/'

# Name for the Frozen PB name
FROZEN_NAME = 'mask_frozen_graph.pb'

# PATH where to save serving model
SERVING_MODEL_PATH = '/root/DocParser/serving/serving_model'

# Version of the serving model
VERSION_NUMBER = 1


class InferenceConfig(DocparserDefaultConfig):
    NAME = 'docparser_inference'
    DETECTION_MAX_INSTANCES = 200
    IMAGE_RESIZE_MODE = "square"
    NUM_CLASSES = len(DocsDataset.ALL_CLASSES) + 1
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
