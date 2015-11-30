#!/usr/bin/env python
# Copyright (C) 2015 Swift Navigation Inc.
# Contact: Bhaskar Mookerji <mookerji@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.

import numpy as np
import swiftnav.ephemeris as e
import swiftnav.gpstime as g

tol = 1e-10

def test_sat_state():
  eph = e.Ephemeris(**{'toe': { 'wn': 1867, 'tow': 518400.0,},
                       'sid': {'sat': 17, 'band': 0, 'constellation': 0},
                       'valid': 1,
                       'healthy': 1,
                       'kepler': {'crs': 25.125,
                                  'inc_dot': 3.78944355982045e-10,
                                  'tgd': -1.1175870895385742e-08,
                                  'crc': 106.65625,
                                  'ecc': 0.016364791779778898,
                                  'omegadot': -8.013190924423338e-09,
                                  'inc': 0.9253317285121154,
                                  'cuc': 1.255422830581665e-06,
                                  'omega0': 2.7384009602031045,
                                  'cus': 1.280754804611206e-05,
                                  'm0': -2.057975194561658,
                                  'toc': {'tow': 518400.0, 'wn': 21845,},
                                  'dn': 5.035924052164783e-09,
                                  'cic': 2.7194619178771973e-07,
                                  'sqrta': 5153.647108078003,
                                  'cis': 9.313225746154785e-09,
                                  'iode': 50,
                                  'iodc': 21845,
                                  'crc': 49614,
                                  'w': -1.9329047030450934,
                                  'af0': 0.0004458986222743988,
                                  'af1': 3.637978807091713e-12,
                                  'af2': 0.0}})
  assert eph.good(g.GpsTime(**{ 'wn': 1867, 'tow': 518400.0,}))
  time = g.GpsTime(**{ 'wn': 1867, 'tow': 518400.0,})
  pos, vel, clock_err, clock_rate_err =  eph.calc_sat_state(time)
  assert np.allclose(pos, [  8939514.51292471, -19122117.65874583,  16447534.13118957])
  assert np.allclose(vel, [ 1892.86704302,  -765.38725981, -1985.61338019])
  assert clock_err - 0.00336435649383 < tol
  assert clock_rate_err - 3.63797880709e-12 < tol
  assert not eph.good(g.GpsTime(**{ 'wn': 1866, 'tow': 518400.0,}))
  assert not eph.good(g.GpsTime(**{ 'wn': 1867, 'tow': 518400.0 + 3600.*4}))
  assert eph.good(g.GpsTime(**{ 'wn': 1867, 'tow': 518400.0 + 3600.*2}))
  assert not eph.good(g.GpsTime(**{ 'wn': 1868, 'tow': 518400.0,}))
  assert len(eph.to_dict()) == 6
  assert repr(eph)
