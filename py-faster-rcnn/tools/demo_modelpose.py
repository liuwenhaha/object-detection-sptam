#!/usr/bin/env python

# --------------------------------------------------------
# Faster R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""
Demo script showing detections in sample images.

See README.md for installation instructions before running.
"""

import _init_paths
from fast_rcnn.config import cfg
from fast_rcnn.test import im_detect
from fast_rcnn.nms_wrapper import nms
from utils.timer import Timer
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe, os, sys, cv2
import argparse
import math
import random

CLASSES = ('__background__',
           'bathtub', 'bed', 'chair', 'desk',
           'dresser', 'monitor', 'night_stand', 'sofa', 'table',
           'toilet')


NETS = {'vgg16': ('VGG16', 'pose_coco_Allconst_iter16000.caffemodel')}
#                  'pose_cls_15k_15kcls_pose__iter_230000.caffemodel')}


def vis_detections(im, class_name, dets,th_scores,th_sincos,size_deltas,cls_ind,thresh=0.5):
    """Draw detected bounding boxes."""
     ##print(dets[:,-1])
       
    inds = np.where(dets[:, -1] >= thresh)[0]
    if len(inds) == 0:
        ## print(len(inds))
        return

    im = im[:, :, (2, 1, 0)]
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(im, aspect='equal')
    for i in inds:
        bbox = dets[i, :4]
        score = dets[i, -1]
        bin_scores = th_scores[i,:]
        bin = np.argmax(bin_scores)
        binplus = (bin + 1) % 8
        binminus = (bin + 7) % 8
        bin2 = binminus
        if (th_scores[i,binplus] > th_scores[i,binminus]):
           bin2 = binplus
 
        ### 
        angle1 = bin  * (2*math.pi / 8.0) + math.atan2(th_sincos[i,bin *2],th_sincos[i,bin *2+1])
        angle2 = bin2 * (2*math.pi / 8.0) + math.atan2(th_sincos[i,bin2*2],th_sincos[i,bin2*2+1])
       
        mean = cfg.SIZE_MEANS[cls_ind]
        dimX = size_deltas[i,0] + mean[0]
        dimY = size_deltas[i,1] + mean[1]
        dimZ = size_deltas[i,2] + mean[2]
        ###
        ax.add_patch(
            plt.Rectangle((bbox[0], bbox[1]),
                          bbox[2] - bbox[0],
                          bbox[3] - bbox[1], fill=False,
                          edgecolor='red', linewidth=3.5)
            )
        ax.text(bbox[0], bbox[1] - 2,
                '{:.3f} {:s} | {:s}{:s} {:.3f} {:.3f} | {:.2f}x{:.2f}y{:.2f}z'.format(score,class_name,str(bin),str(bin2), angle1, angle2,dimX,dimY,dimZ),
                bbox=dict(facecolor='blue', alpha=0.5),
                fontsize=14, color='white')

    ax.set_title(('{} detections with '
                  'p({} | box) >= {:.1f}').format(class_name, class_name,
                                                  thresh),
                  fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.draw()

def demo(net, image_name):
    """Detect object classes in an image using pre-computed object proposals."""

    # Load the demo image
    ##im_file = os.path.join(cfg.DATA_DIR, 'modelnet_demo','room1k', image_name)
    im_file = os.path.join(cfg.DATA_DIR, 'modelnet_demo', image_name)
    #im_file = os.path.join(cfg.DATA_DIR, 'modelnet_devkit', 'room25kp','Images',image_name) #data/modelnet_devkit/room25kp/Images/
    im = cv2.imread(im_file)

    # Detect all object classes and regress object bounds
    timer = Timer()
    timer.tic()
    scores, boxes, delta_th,bin_scores,size_deltas = im_detect(net, im)
    timer.toc()
    print ('Detection took {:.3f}s for '
           '{:d} object proposals').format(timer.total_time, boxes.shape[0])

    ##iri = random.randint(0,len(bin_scores)-1) 
    ##print('{:.3f} {:.3f} {:.3f} {:.3f} {:.3f} {:.3f} {:d} {:d}').format(bin_scores[0,0],bin_scores[0,1],bin_scores[0,2],bin_scores[0,3],bin_scores[iri,0],bin_scores[iri,1],len(bin_scores),len(boxes))
    ##print('{:.3f} {:.3f} {:.3f}').format(scores[iri,0],scores[iri,1],scores[iri,2])  

    # Visualize detections for each class
    CONF_THRESH = 0.7
    NMS_THRESH = 0.3
    for cls_ind, cls in enumerate(CLASSES[1:]):
        cls_ind += 1 # because we skipped background 
        cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)] 

        cls_scores = scores[:, cls_ind]
        dets = np.hstack((cls_boxes,
                          cls_scores[:, np.newaxis])).astype(np.float32)
        keep = nms(dets, NMS_THRESH)
        ##print(len(keep))
        dets = dets[keep, :]
        th_scores = bin_scores[keep, 8*cls_ind : 8*(cls_ind+1) ]
        th_sincos = delta_th[keep,  16*cls_ind : 16*(cls_ind+1)]
        sizeD = size_deltas[keep,    3*cls_ind : 3*(cls_ind+1) ]
        vis_detections(im, cls, dets,th_scores,th_sincos,sizeD,cls_ind, thresh=CONF_THRESH)

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Faster R-CNN demo')
    parser.add_argument('--gpu', dest='gpu_id', help='GPU device id to use [0]',
                        default=0, type=int)
    parser.add_argument('--cpu', dest='cpu_mode',
                        help='Use CPU mode (overrides --gpu)',
                        action='store_true')
    parser.add_argument('--net', dest='demo_net', help='Network to use [vgg16]',
                        choices=NETS.keys(), default='vgg16')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    cfg.TEST.HAS_RPN = True  # Use RPN for proposals
    cfg.TEST.HAS_POSE = True ##POSE

    args = parse_args()

    ##prototxt = os.path.join(cfg.MODELS_DIR, 'modelpose', NETS[args.demo_net][0],
    ##                            'faster_rcnn_end2end', 'test.final.prototxt')
    prototxt = '/data/ondeloc/models_trained/modelpose/VGG16/faster_rcnn_end2end/test.final.prototxt'	  

    ## caffemodel = os.path.join(cfg.ROOT_DIR, 'output','faster_rcnn_end2end','train',
    ##                          NETS[args.demo_net][1])

    ##caffemodel = '/state/partition1/javier/output/faster_rcnn_end2end/coco_2014_train/coco_15kr_50ks__iter_15000.caffemodel'
    ##caffemodel = '/state/partition1/javier/output/faster_rcnn_end2end/train/pose_cls_15k_40kcls_230kopose_p+c+r_iter_200000.caffemodel'

    caffemodel = '~/caffeModels/pose_coco_Allconst_iter16000.caffemodel'
#    caffemodel = '/data/caffeModels/pose_coco_Allconst_iter16000.caffemodel'

    if not os.path.isfile(caffemodel):
        raise IOError(('{:s} not found.\nDid you run ./data/script/'
                       'fetch_faster_rcnn_models.sh?').format(caffemodel))

    if args.cpu_mode:
        caffe.set_mode_cpu()
    else:
        caffe.set_mode_gpu()
        caffe.set_device(args.gpu_id)
        cfg.GPU_ID = args.gpu_id
    net = caffe.Net(prototxt, caffemodel, caffe.TEST)

    print '\n\nLoaded network {:s}'.format(caffemodel)

    # Warmup on a dummy image
    im = 128 * np.ones((300, 500, 3), dtype=np.uint8)
    for i in xrange(2):
        _, _, _,_,_  = im_detect(net, im, None)

    im_names_real = ['real01.jpg','real02.jpg','real03.jpg','real04.jpg','real05.jpg','real06.jpg','real07.jpg','real08.jpg','real09.jpg','real10.jpg','real11.jpg','real12.jpg','real13.jpg','real14.jpg','real15.jpg','real16.jpg','real17.jpg','real18.jpg','real19.jpg','real20.jpg','real21.jpg','real22.jpg','real23.jpg','real24.jpg','real25.jpg','real26.jpg','frame0.jpg','bedroom_01.jpeg','cluter1.jpg','dresser1.jpg','dresser2.jpg','monitor1.jpg']
    im_names_gen = ['p277_1_0.jpg','p274_1_0.jpg','t69_1_0.jpg','t71_1_0.jpg','t92_1_0.jpg','t82_1_0.jpg','t83_1_0.jpg','t116_1_0.jpg','t114_1_0.jpg','t113_1_0.jpg','t94_1_0.jpg','t89_1_0.jpg','t76_1_0.jpg','t74_1_0.jpg','t48_1_0.jpg','t33_1_0.jpg']
    im_names_room = ['v1_1_0.jpg','v2_1_0.jpg','v3_1_0.jpg','v4_1_0.jpg','v5_1_0.jpg','v6_1_0.jpg','v7_1_0.jpg','v8_1_0.jpg','v9_1_0.jpg','v10_1_0.jpg','v11_1_0.jpg','v12_1_0.jpg','v14_1_0.jpg','v117_1_0.jpg']
    im_demo_images = ['livingroom1.jpg','chair1.jpg'] 
    #testfile = os.path.join(cfg.DATA_DIR, 'modelnet_devkit', 'room25kp','ImageSets','minitest.txt')
    #with open(testfile) as f:
    #   test_lines = f.read().splitlines()
    #im_names_test = [s + '.jpg' for s in test_lines]
    #im_names = im_names_test
    im_names = ['/data/ondeloc/py-faster-rcnn/tools/demo_images/'+s  for s in im_demo_images]
    for im_name in im_names:
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'Demo for data/demo/{}'.format(im_name)
        demo(net, im_name)

    ## plt.show()
    from matplotlib.backends.backend_pdf import PdfPages
    pp = PdfPages('demo_out.pdf')

#    pp = PdfPages('~/multi.pdf')


    for i in plt.get_fignums():
	plt.figure(i)
	pp.savefig()
        #plt.savefig('/home/javier/rcnn/py-faster-rcnn/output/demo/figure%d.png' % i)
    pp.close()
