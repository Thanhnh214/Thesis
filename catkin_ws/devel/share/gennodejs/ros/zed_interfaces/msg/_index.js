
"use strict";

let RGBDSensors = require('./RGBDSensors.js');
let Skeleton3D = require('./Skeleton3D.js');
let Keypoint2Di = require('./Keypoint2Di.js');
let Keypoint3D = require('./Keypoint3D.js');
let Skeleton2D = require('./Skeleton2D.js');
let BoundingBox3D = require('./BoundingBox3D.js');
let PosTrackStatus = require('./PosTrackStatus.js');
let Object = require('./Object.js');
let PlaneStamped = require('./PlaneStamped.js');
let BoundingBox2Di = require('./BoundingBox2Di.js');
let BoundingBox2Df = require('./BoundingBox2Df.js');
let ObjectsStamped = require('./ObjectsStamped.js');
let Keypoint2Df = require('./Keypoint2Df.js');

module.exports = {
  RGBDSensors: RGBDSensors,
  Skeleton3D: Skeleton3D,
  Keypoint2Di: Keypoint2Di,
  Keypoint3D: Keypoint3D,
  Skeleton2D: Skeleton2D,
  BoundingBox3D: BoundingBox3D,
  PosTrackStatus: PosTrackStatus,
  Object: Object,
  PlaneStamped: PlaneStamped,
  BoundingBox2Di: BoundingBox2Di,
  BoundingBox2Df: BoundingBox2Df,
  ObjectsStamped: ObjectsStamped,
  Keypoint2Df: Keypoint2Df,
};
