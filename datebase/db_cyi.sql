/*
Navicat MySQL Data Transfer

Source Server         : CYI
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : db_cyi

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2024-03-12 17:32:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_tg
-- ----------------------------
DROP TABLE IF EXISTS `tb_tg`;
CREATE TABLE `tb_tg` (
  `团员姓名` varchar(10) NOT NULL,
  `团员性别` char(2) NOT NULL,
  `团员年龄` int(3) NOT NULL,
  `团员所属组织` varchar(30) NOT NULL,
  `入团时间` varchar(20) NOT NULL,
  `团员职位` varchar(20) NOT NULL,
  PRIMARY KEY (`团员姓名`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_tg
-- ----------------------------
INSERT INTO `tb_tg` VALUES ('宁立', '女', '20', '清华大学共青团', '2017', '团员');
INSERT INTO `tb_tg` VALUES ('张三', '男', '19', '中山大学共青团', '2016', '团委书记');
INSERT INTO `tb_tg` VALUES ('张二', '女', '20', '中山大学共青团', '2018', '副书记');
INSERT INTO `tb_tg` VALUES ('张文康', '男', '20', '清华大学共青团', '2016', '副书记');
INSERT INTO `tb_tg` VALUES ('李宫', '女', '21', '清华大学共青团', '2015', '团员');
INSERT INTO `tb_tg` VALUES ('李胜男', '女', '21', '清华大学共青团', '2015', '团委书记');
INSERT INTO `tb_tg` VALUES ('柳儿', '女', '19', '北京大学共青团', '2017', '团委书记');
INSERT INTO `tb_tg` VALUES ('秦理倪', '男', '20', '中山大学共青团', '2018', '团员');
INSERT INTO `tb_tg` VALUES ('谷农', '男', '21', '清华大学共青团', '2015', '宣传部长');
INSERT INTO `tb_tg` VALUES ('陈靓瑄', '女', '18', '北京大学共青团', '2016', '副书记');

-- ----------------------------
-- Table structure for tb_ty
-- ----------------------------
DROP TABLE IF EXISTS `tb_ty`;
CREATE TABLE `tb_ty` (
  `团员姓名` varchar(10) NOT NULL,
  `团员性别` char(2) NOT NULL,
  `团员年龄` int(3) NOT NULL,
  `团员所属组织` varchar(30) NOT NULL,
  `入团时间` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_ty
-- ----------------------------
INSERT INTO `tb_ty` VALUES ('张厉', '男', '19', '中山大学共青团', '2016年');
INSERT INTO `tb_ty` VALUES ('李米理', '女', '20', '中山大学共青团', '2018年');
INSERT INTO `tb_ty` VALUES ('柳柯文', '男', '19', '北京大学共青团', '2017年');
INSERT INTO `tb_ty` VALUES ('陈拉卡', '女', '18', '北京大学共青团', '2016年');
INSERT INTO `tb_ty` VALUES ('李安', '男', '21', '清华大学共青团', '2015年');
INSERT INTO `tb_ty` VALUES ('张菈', '女', '20', '清华大学共青团', '2016年');
INSERT INTO `tb_ty` VALUES ('唐零零', '女', '21', '中山大学共青团', '2019年');
INSERT INTO `tb_ty` VALUES ('何琴', '女', '22', '北京大学共青团', '2017年');
INSERT INTO `tb_ty` VALUES ('赵恩', '男', '20', '清华大学共青团', '2018年');
INSERT INTO `tb_ty` VALUES ('艾恺尼', '男', '19', '中山大学共青团', '2016年');

-- ----------------------------
-- Table structure for tb_tzzcx
-- ----------------------------
DROP TABLE IF EXISTS `tb_tzzcx`;
CREATE TABLE `tb_tzzcx` (
  `团组织名称` varchar(255) NOT NULL,
  `负责人` varchar(255) NOT NULL,
  `总人数` int(11) NOT NULL,
  `新增人数` int(11) NOT NULL,
  `转出人数` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_tzzcx
-- ----------------------------
INSERT INTO `tb_tzzcx` VALUES ('中山大学共青团', '张三', '3000', '651', '456');
INSERT INTO `tb_tzzcx` VALUES ('北京大学共青团', '李四', '1565', '198', '32');
INSERT INTO `tb_tzzcx` VALUES ('清华大学共青团', '王五', '8912', '123', '154');

-- ----------------------------
-- Table structure for tb_username
-- ----------------------------
DROP TABLE IF EXISTS `tb_username`;
CREATE TABLE `tb_username` (
  `用户名称` varchar(10) NOT NULL,
  `密码` varchar(20) NOT NULL,
  `类型` varchar(10) NOT NULL,
  PRIMARY KEY (`用户名称`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_username
-- ----------------------------
INSERT INTO `tb_username` VALUES ('test', '1234', '普通用户');
INSERT INTO `tb_username` VALUES ('user01', '1234', '普通用户');
INSERT INTO `tb_username` VALUES ('user02', '1111', '管理员');
INSERT INTO `tb_username` VALUES ('user3', '1111', '管理员');
INSERT INTO `tb_username` VALUES ('徐启杰', '1234', '管理员');
INSERT INTO `tb_username` VALUES ('管理员', '1234', '管理员');
