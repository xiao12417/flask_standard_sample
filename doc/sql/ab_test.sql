/*
Navicat MySQL Data Transfer

Source Server         : 开发服10.246.14.121
Source Server Version : 50544
Source Host           : 10.246.14.121:3306
Source Database       : ab_test

Target Server Type    : MYSQL
Target Server Version : 50544
File Encoding         : 65001

Date: 2015-08-21 17:52:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `abtest_apps`
-- ----------------------------
DROP TABLE IF EXISTS `abtest_apps`;
CREATE TABLE `abtest_apps` (
  `app_id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(50) NOT NULL COMMENT '游戏名称',
  `app_adduser_id` int(11) DEFAULT NULL COMMENT 'app创建人',
  `app_group_id` int(11) DEFAULT NULL,
  `app_platform` int(11) DEFAULT NULL COMMENT '游戏支持平台',
  `app_author` varchar(100) DEFAULT NULL COMMENT '开发商',
  `app_icon` varchar(100) DEFAULT NULL COMMENT '图标',
  `app_screenshots` varchar(500) DEFAULT NULL COMMENT '截屏数组',
  `app_description` blob COMMENT '游戏内容提要',
  `app_price` float DEFAULT NULL COMMENT '游戏价格',
  `app_inapp_purchase` tinyint(1) DEFAULT NULL COMMENT '是否App内购买',
  `app_video` varchar(500) DEFAULT NULL COMMENT '视屏链接',
  `app_star` float DEFAULT NULL COMMENT '游戏星级，五星为满分',
  `app_reviews` int(11) DEFAULT NULL COMMENT '评论数',
  `app_update_info` varchar(1000) DEFAULT NULL COMMENT '更新信息',
  `app_website` varchar(100) DEFAULT NULL,
  `app_pubdate` datetime DEFAULT NULL,
  `app_category` varchar(100) DEFAULT NULL COMMENT '类别，领域',
  `app_version` varchar(30) DEFAULT NULL COMMENT '版本号',
  `app_size` varchar(30) DEFAULT NULL COMMENT '游戏大小',
  `app_rate` varchar(50) DEFAULT NULL COMMENT '游戏分级',
  `app_compatibility` varchar(100) DEFAULT NULL COMMENT '游戏兼容性',
  `app_copyright` varchar(100) DEFAULT NULL COMMENT '版权所属',
  `app_languages` varchar(50) DEFAULT NULL COMMENT '语言',
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`app_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of abtest_apps
-- ----------------------------

-- ----------------------------
-- Table structure for `abtest_group_user`
-- ----------------------------
DROP TABLE IF EXISTS `abtest_group_user`;
CREATE TABLE `abtest_group_user` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_type` int(11) DEFAULT NULL COMMENT '用户在小组中的类型',
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of abtest_group_user
-- ----------------------------

-- ----------------------------
-- Table structure for `abtest_groups`
-- ----------------------------
DROP TABLE IF EXISTS `abtest_groups`;
CREATE TABLE `abtest_groups` (
  `group_id` int(11) DEFAULT NULL,
  `group_name` varchar(50) DEFAULT NULL COMMENT '组名称',
  `group_description` varchar(1000) DEFAULT NULL COMMENT '组介绍',
  `group_admin_id` int(11) DEFAULT NULL COMMENT '组管理员',
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of abtest_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `abtest_indicators`
-- ----------------------------
DROP TABLE IF EXISTS `abtest_indicators`;
CREATE TABLE `abtest_indicators` (
  `indicators_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '统计指标',
  `indicators_name` varchar(100) NOT NULL COMMENT '统计指标名称',
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`indicators_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of abtest_indicators
-- ----------------------------

-- ----------------------------
-- Table structure for `abtest_plans`
-- ----------------------------
DROP TABLE IF EXISTS `abtest_plans`;
CREATE TABLE `abtest_plans` (
  `plan_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL COMMENT '方案所属实验',
  `app_id` int(11) NOT NULL COMMENT '方案所属app',
  `plan_name` varchar(100) DEFAULT NULL COMMENT '方案名称',
  `plan_item_name` varchar(50) DEFAULT NULL COMMENT '方案测试条目名称',
  `plan_item_content` varchar(1000) DEFAULT NULL COMMENT '方案测试具体内容',
  `plan_probability` float DEFAULT NULL COMMENT '方案概率',
  `plan_get_url` varchar(100) DEFAULT NULL COMMENT '方案所对应的下载页面网址',
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`plan_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of abtest_plans
-- ----------------------------

-- ----------------------------
-- Table structure for `abtest_statisitics`
-- ----------------------------
DROP TABLE IF EXISTS `abtest_statisitics`;
CREATE TABLE `abtest_statisitics` (
  `statistics_id` int(11) NOT NULL AUTO_INCREMENT,
  `statisitics_test_id` int(11) DEFAULT NULL COMMENT '所属实验id',
  `statisitics_plan_id` int(11) DEFAULT NULL COMMENT '所属方案id',
  `statisitics_item_id` int(11) DEFAULT NULL COMMENT '统计指标id',
  `statisitics_item_num` int(11) DEFAULT NULL COMMENT '相应指标的统计数目',
  `statisitics_interval` int(11) DEFAULT NULL COMMENT '统计事件间隔',
  `statisitics_timestamp` timestamp NULL DEFAULT NULL COMMENT '统计事件戳',
  `statisitics_date` datetime DEFAULT NULL COMMENT '统计数据日期',
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`statistics_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of abtest_statisitics
-- ----------------------------

-- ----------------------------
-- Table structure for `abtest_tests`
-- ----------------------------
DROP TABLE IF EXISTS `abtest_tests`;
CREATE TABLE `abtest_tests` (
  `test_id` int(11) NOT NULL AUTO_INCREMENT,
  `test_name` varchar(50) NOT NULL COMMENT '实验名称',
  `test_app_id` int(11) NOT NULL COMMENT '测试游戏app ID',
  `test_author_id` int(11) NOT NULL,
  `test_group_id` int(11) DEFAULT NULL COMMENT '实验所属项目组',
  `test_url` varchar(100) DEFAULT NULL COMMENT '实验生成的产品页面网址',
  `test_plan_num` int(11) NOT NULL DEFAULT '0' COMMENT '实验的方案数',
  `test_plan_ids` varchar(1000) DEFAULT NULL COMMENT '实验相关方案的id数组',
  `test_status` int(11) DEFAULT NULL COMMENT '实验状态',
  `test_item` varchar(50) DEFAULT NULL COMMENT '测试内容',
  `test_platform` int(11) DEFAULT NULL COMMENT '测试平台',
  `test_expired_time` int(11) DEFAULT NULL COMMENT '有效期，单位天',
  `test_publish_time` datetime DEFAULT NULL COMMENT '测试发布日期',
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of abtest_tests
-- ----------------------------

-- ----------------------------
-- Table structure for `abtest_users`
-- ----------------------------
DROP TABLE IF EXISTS `abtest_users`;
CREATE TABLE `abtest_users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_type` int(11) NOT NULL DEFAULT '0',
  `user_name` varchar(50) DEFAULT NULL,
  `user_nickname` varchar(50) DEFAULT NULL,
  `user_personal_signature` varchar(500) DEFAULT NULL,
  `user_mail` varchar(50) DEFAULT NULL,
  `user_password` varchar(50) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of abtest_users
-- ----------------------------
INSERT INTO `abtest_users` VALUES ('1', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('2', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('3', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('4', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('5', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('6', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('7', '6', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('8', '7', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('9', '8', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('10', '9', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('11', '0', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('12', '1', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('13', '2', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('14', '3', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('15', '4', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('16', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('17', '6', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('18', '7', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('19', '8', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('20', '9', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('21', '0', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('22', '1', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('23', '2', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('24', '3', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('25', '4', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('26', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('27', '6', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('28', '7', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('29', '8', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('30', '9', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('31', '0', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('32', '1', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('33', '2', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('34', '3', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('35', '4', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('36', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('37', '6', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('38', '7', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('39', '8', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('40', '9', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('41', '0', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('42', '1', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('43', '2', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('44', '3', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('45', '4', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('46', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('47', '6', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('48', '7', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('49', '8', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('50', '9', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('51', '0', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('52', '1', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('53', '2', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('54', '3', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('55', '4', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('56', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('57', '6', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('58', '7', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('59', '8', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('60', '9', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('61', '0', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('62', '1', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('63', '2', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('64', '3', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('65', '4', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('66', '5', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('67', '6', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('68', '7', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('69', '8', null, null, null, null, null, null);
INSERT INTO `abtest_users` VALUES ('70', '9', null, null, null, null, null, null);
