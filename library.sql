-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2018-07-08 14:38:15
-- 服务器版本： 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- 表的结构 `14`
--

CREATE TABLE `14` (
  `no` varchar(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `total_book_num` int(10) DEFAULT NULL,
  `like_book_type` varchar(5) DEFAULT NULL,
  `like_book_type_num` int(10) DEFAULT NULL,
  `longest_book` varchar(100) DEFAULT NULL,
  `longest_book_day` int(10) DEFAULT NULL,
  `most_book_date` varchar(13) DEFAULT NULL,
  `most_book_num` int(10) DEFAULT NULL,
  `library_count` int(10) DEFAULT NULL,
  `earliest_date` varchar(13) DEFAULT NULL,
  `earliest_time` varchar(6) DEFAULT NULL,
  `night_day` int(10) NOT NULL,
  `daying_page` int(10) NOT NULL,
  `fuying_page` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `15`
--

CREATE TABLE `15` (
  `no` varchar(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `total_book_num` int(10) DEFAULT NULL,
  `like_book_type` varchar(5) DEFAULT NULL,
  `like_book_type_num` int(10) DEFAULT NULL,
  `longest_book` varchar(100) DEFAULT NULL,
  `longest_book_day` int(10) DEFAULT NULL,
  `most_book_date` varchar(13) DEFAULT NULL,
  `most_book_num` int(10) DEFAULT NULL,
  `library_count` int(10) DEFAULT NULL,
  `earliest_date` varchar(13) DEFAULT NULL,
  `earliest_time` varchar(6) DEFAULT NULL,
  `night_day` int(10) NOT NULL,
  `daying_page` int(10) NOT NULL,
  `fuying_page` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `16`
--

CREATE TABLE `16` (
  `no` varchar(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `total_book_num` int(10) DEFAULT NULL,
  `like_book_type` varchar(5) DEFAULT NULL,
  `like_book_type_num` int(10) DEFAULT NULL,
  `longest_book` varchar(100) DEFAULT NULL,
  `longest_book_day` int(10) DEFAULT NULL,
  `most_book_date` varchar(13) DEFAULT NULL,
  `most_book_num` int(10) DEFAULT NULL,
  `library_count` int(10) DEFAULT NULL,
  `earliest_date` varchar(13) DEFAULT NULL,
  `earliest_time` varchar(6) DEFAULT NULL,
  `night_day` int(10) NOT NULL,
  `daying_page` int(10) NOT NULL,
  `fuying_page` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `17`
--

CREATE TABLE `17` (
  `no` varchar(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `total_book_num` int(10) DEFAULT NULL,
  `like_book_type` varchar(5) DEFAULT NULL,
  `like_book_type_num` int(10) DEFAULT NULL,
  `longest_book` varchar(100) DEFAULT NULL,
  `longest_book_day` int(10) DEFAULT NULL,
  `most_book_date` varchar(13) DEFAULT NULL,
  `most_book_num` int(10) DEFAULT NULL,
  `library_count` int(10) DEFAULT NULL,
  `earliest_date` varchar(13) DEFAULT NULL,
  `earliest_time` varchar(6) DEFAULT NULL,
  `night_day` int(10) NOT NULL,
  `daying_page` int(10) NOT NULL,
  `fuying_page` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `14`
--
ALTER TABLE `14`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `15`
--
ALTER TABLE `15`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `16`
--
ALTER TABLE `16`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `17`
--
ALTER TABLE `17`
  ADD PRIMARY KEY (`no`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
