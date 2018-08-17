from unittest import TestCase
import numpy as np
import os

import sangarak

fixtures = "sangarak/tests/fixtures/"

class TestDistributedMatrix(TestCase):
    def test_16x16_matrix(self):
        path = os.path.abspath(fixtures + "/16x16_8x8_2x2/") + "/"
        matrix = np.array([
            [5383., 886., 777., 915., 383., 886., 777., 915., 793.,  335., 386.,  492.,  793.,  335.,  386.,  492.],
            [ 649., 5421.,362.,  27.,  649.,  421.,  362.,   27.,  690.,   59.,  763.,  926.,  690.,   59.,  763.,  926.],
            [ 540., 426., 5172., 736.,  540.,  426.,  172.,  736.,  211.,  368.,  567. , 429.,  211.,  368.,  567., 429.],
            [ 782., 530., 862., 5123.,  782.,  530.,  862.,  123.,   67.,  135.,  929.,  802.,   67.,  135.,  929.,  802.],
            [ 383., 886., 777., 915., 5383.,  886.,  777.,  915.,  793.,  335.,  386.,  492.,  793.,  335.,  386.,  492.],
            [ 649., 421., 362., 27.,  649., 5421.,  362.,   27.,  690. ,  59. , 763. , 926. , 690. ,  59. , 763. , 926.],
            [ 540., 426., 172., 736.,  540.,  426., 5172.,  736.,  211.,  368.,  567.,  429.,  211.,  368.,  567.,  429.],
            [ 782., 530., 862., 123.,  782.,  530.,  862., 5123.,   67.,  135.,  929.,  802.,   67.,  135.,  929.,  802.],
            [  22., 58.,  69.,  167.,   22.,   58.,   69.,  167., 5393.,  456.,   11.,   42.,  393.,  456.,   11.,   42.],
            [ 229., 373., 421., 919.,  229.,  373.,  421.,  919.,  784., 5537.,  198.,  324.,  784.,  537.,  198.,  324.],
            [ 315., 370., 413., 526.,  315., 370.,  413.,  526.,   91.,  980., 5956. , 873. ,  91.,  980. , 956.,  873.],
            [ 862., 170., 996., 281.,  862.,  170.,  996.,  281.,  305.,  925.,   84., 5327.,  305.,  925.,   84.,  327.],
            [  22., 58.,  69.,  167.,   22.,   58.,   69.,  167.,  393.,  456.,   11.,   42., 5393.,  456.,   11.,   42.],
            [ 229., 373., 421., 919.,  229.,  373.,  421.,  919.,  784.,  537.,  198.,  324.,  784., 5537.,  198.,  324.],
            [ 315., 370., 413., 526.,  315.,  370.,  413.,  526. ,  91. , 980. , 956. , 873. ,  91.,  980., 5956.,  873.],
            [ 862., 170., 996., 281.,  862.,  170.,  996.,  281.,  305., 925. ,  84.,  327. , 305.,  925. ,  84., 5327.]
            ]            
        )

        files = {
            0: path + "0input.txt",
            1: path + "1input.txt",
            2: path + "2input.txt",
            3: path + "3input.txt"
        }
        n = 16
        nb = 8
        pb = 2
        num_procs = 4

        m = sangarak.read_matrix(files, "row", n, nb, pb, num_procs)
        print(m)
        
        self.assertTrue(np.array_equal(matrix, m))