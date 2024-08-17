
"use strict";

let GetPlan = require('./GetPlan.js')
let GetNodesInRadius = require('./GetNodesInRadius.js')
let GetNodeData = require('./GetNodeData.js')
let AddLink = require('./AddLink.js')
let CleanupLocalGrids = require('./CleanupLocalGrids.js')
let PublishMap = require('./PublishMap.js')
let RemoveLabel = require('./RemoveLabel.js')
let SetLabel = require('./SetLabel.js')
let DetectMoreLoopClosures = require('./DetectMoreLoopClosures.js')
let SetGoal = require('./SetGoal.js')
let GetMap = require('./GetMap.js')
let LoadDatabase = require('./LoadDatabase.js')
let GetMap2 = require('./GetMap2.js')
let GlobalBundleAdjustment = require('./GlobalBundleAdjustment.js')
let ResetPose = require('./ResetPose.js')
let ListLabels = require('./ListLabels.js')

module.exports = {
  GetPlan: GetPlan,
  GetNodesInRadius: GetNodesInRadius,
  GetNodeData: GetNodeData,
  AddLink: AddLink,
  CleanupLocalGrids: CleanupLocalGrids,
  PublishMap: PublishMap,
  RemoveLabel: RemoveLabel,
  SetLabel: SetLabel,
  DetectMoreLoopClosures: DetectMoreLoopClosures,
  SetGoal: SetGoal,
  GetMap: GetMap,
  LoadDatabase: LoadDatabase,
  GetMap2: GetMap2,
  GlobalBundleAdjustment: GlobalBundleAdjustment,
  ResetPose: ResetPose,
  ListLabels: ListLabels,
};
