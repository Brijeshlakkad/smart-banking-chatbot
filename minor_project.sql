-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 15, 2018 at 10:00 AM
-- Server version: 5.6.38
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `minor_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `acc_id` int(10) NOT NULL,
  `c_id` int(10) NOT NULL,
  `acc_name` varchar(30) NOT NULL,
  `acc_type` varchar(10) NOT NULL,
  `balance` varchar(100) NOT NULL DEFAULT '0',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `passcode` varchar(6) NOT NULL DEFAULT '-99',
  `acc_no` varchar(12) NOT NULL,
  `status` int(1) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`acc_id`, `c_id`, `acc_name`, `acc_type`, `balance`, `created_time`, `passcode`, `acc_no`, `status`) VALUES
(4, 70, 'Brijesh Rameshbhai Lakkad', 'saving', '0', '2018-08-01 20:24:57', '123456', '007046167267', 1),
(16, 1, 'Brijesh Rameshbhai Lakkad', 'saving', '0', '2018-08-06 17:33:32', '-99', '007046167268', 1),
(19, 100, 'Sanket Patel', 'saving', '0', '2018-08-20 15:44:59', '123456', '007046167290', 1),
(20, 101, 'Brijesh Rameshbhai Lakkad', 'saving', '0', '2018-08-20 16:15:47', '683249', '007046167255', 1);

-- --------------------------------------------------------

--
-- Table structure for table `bank_atm`
--

CREATE TABLE `bank_atm` (
  `bid` int(10) NOT NULL,
  `area` varchar(10) NOT NULL,
  `city` varchar(10) NOT NULL,
  `state` varchar(10) NOT NULL,
  `country` varchar(10) NOT NULL,
  `branch_atm` varchar(30) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `cards`
--

CREATE TABLE `cards` (
  `card_id` int(30) NOT NULL,
  `c_id` int(10) NOT NULL,
  `acc_id` int(10) NOT NULL,
  `holder_name` varchar(30) NOT NULL,
  `till_month` varchar(10) NOT NULL,
  `till_year` varchar(10) NOT NULL,
  `csv` varchar(4) NOT NULL,
  `card_type` varchar(10) NOT NULL,
  `card_no` varchar(16) NOT NULL,
  `status` int(1) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cards`
--

INSERT INTO `cards` (`card_id`, `c_id`, `acc_id`, `holder_name`, `till_month`, `till_year`, `csv`, `card_type`, `card_no`, `status`) VALUES
(10, 70, 4, 'Brijesh Rameshbhai Lakkad', '08', '19', '494', 'Mastercard', '2685498962451745', 1),
(38, 100, 19, 'Sanket Patel', '10', '19', '656', 'Mastercard', '5743344187443345', 1),
(44, 101, 20, 'Brijesh Rameshbhai Lakkad', '10', '19', '970', 'Mastercard', '2428205825599963', 0);

-- --------------------------------------------------------

--
-- Table structure for table `chats`
--

CREATE TABLE `chats` (
  `chat_id` int(10) NOT NULL,
  `from_id` int(10) NOT NULL,
  `to_id` int(10) NOT NULL,
  `text` varchar(100) NOT NULL,
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `chats`
--

INSERT INTO `chats` (`chat_id`, `from_id`, `to_id`, `text`, `created_time`) VALUES
(1, 14, 0, 'hey', '2018-07-28 21:11:04'),
(4, 0, 19, 'Hello, i m Jon', '2018-07-28 21:39:33'),
(8, 14, 0, 'Hey again', '2018-07-29 00:03:52'),
(11, 14, 0, 'final', '2018-07-29 00:05:53'),
(12, 19, 0, 'Hey', '2018-07-30 09:19:55'),
(13, 19, 0, 'I want help', '2018-07-30 09:20:37'),
(14, 0, 19, 'I m listening', '2018-07-30 09:21:02'),
(15, 70, 0, 'hey', '2018-08-01 20:04:28'),
(16, 70, 0, 'Hello', '2018-08-02 20:27:14'),
(17, 101, 0, 'Hey, Jon', '2018-08-20 16:31:17'),
(18, 0, 101, 'Hello, i m Jon. How can i help you?', '2018-07-28 21:39:33'),
(19, 106, 0, 'Hi', '2018-08-23 00:50:48'),
(20, 107, 0, 'hii', '2018-08-23 09:42:52');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `cid` int(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `fname` varchar(15) NOT NULL,
  `lname` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `postal_add` varchar(40) DEFAULT NULL,
  `perm_add` varchar(50) DEFAULT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `country` varchar(20) DEFAULT NULL,
  `middle_name` varchar(10) DEFAULT NULL,
  `pincode` varchar(6) NOT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(7) DEFAULT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `jon` int(1) DEFAULT '0',
  `hasAcc` int(11) NOT NULL DEFAULT '0',
  `last_otp` varchar(6) DEFAULT '-99'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`cid`, `username`, `fname`, `lname`, `email`, `password`, `contact`, `postal_add`, `perm_add`, `city`, `state`, `country`, `middle_name`, `pincode`, `dob`, `gender`, `time`, `created_time`, `jon`, `hasAcc`, `last_otp`) VALUES
(1, 'brijeshlakkad22222', 'Brijesh', 'Lakkad', 'lakkadbrijesh@gmail.com', '12345b', '7046167268', 'xyz', 'xyz', 'surat', 'gujarat', 'india', 'Rameshbhai', '395006', NULL, 'Male', '2018-07-27 08:56:55', '2018-07-27 16:33:37', 0, 1, '-99'),
(70, 'Brijesh', 'Brijesh', 'Lakkad', 'brij79lakkad@gmail.com', '123456bB', '7046167267', '205, Nanddham Apartment', 'Near Ashok Vatika Society, L.H.Road', 'Surat', 'Gujarat', 'India', 'Rameshbhai', '395008', '2018-07-03', 'Male', '2018-07-31 13:44:07', '2018-07-31 13:44:07', 1, 1, '-99'),
(100, 'sanketpatel2', 'Sanket', 'Patel', 'patelsanket864@gmail.com', '123456bB', '7046167290', '205, Nanddham Apartment', 'Near Ashok Vatika Society, L.H.Road', 'Surat', 'Gujarat', 'India', 'J', '395006', '2018-08-08', 'Male', '2018-08-20 15:13:11', '2018-08-20 15:13:11', 1, 0, '-99'),
(101, 'brijeshlakkad', 'Brijesh', 'Lakkad', 'brijeshlakkad22@gmail.com', '123456bb', '1010101010', 'line 2, line 3', 'Near Ashok Vatika Society, L.H.Road', 'Surat', 'Gujarat', 'India', 'R', '395006', '2018-08-08', 'Male', '2018-08-20 16:12:13', '2018-08-20 16:12:13', 1, 1, '469819');

-- --------------------------------------------------------

--
-- Table structure for table `feedbacks`
--

CREATE TABLE `feedbacks` (
  `f_id` int(10) NOT NULL,
  `email` varchar(30) NOT NULL,
  `f_text` varchar(50) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `feedbacks`
--

INSERT INTO `feedbacks` (`f_id`, `email`, `f_text`, `time`) VALUES
(1, 'brij79lakkad@gmail.com', '123', '2018-07-27 08:58:56'),
(3, 'brij79lakkad@gmail.com', '123', '2018-07-27 09:03:50'),
(4, 'brij79lakkad@gmail.com', '1234', '2018-07-27 09:24:41'),
(5, 'brijeshlakkad22@gmail.com', 'Ickdsbkdbs', '2018-08-20 16:27:55'),
(6, 'brij79lakkad@gmail.com', 'dlsjdsldlsk', '2018-08-23 00:58:33');

-- --------------------------------------------------------

--
-- Table structure for table `requests`
--

CREATE TABLE `requests` (
  `r_id` int(10) NOT NULL,
  `acc_id` int(10) NOT NULL,
  `card_loan` varchar(4) NOT NULL,
  `status_bit` varchar(5) NOT NULL,
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `requests`
--

INSERT INTO `requests` (`r_id`, `acc_id`, `card_loan`, `status_bit`, `created_time`) VALUES
(1, 4, 'card', '1', '2018-08-05 12:27:35'),
(2, 19, 'card', '1', '2018-08-20 15:49:11'),
(4, 20, 'card', '1', '2018-08-22 16:20:18');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `t_id` int(10) NOT NULL,
  `from_acc` int(10) NOT NULL,
  `to_acc` int(10) NOT NULL,
  `amount` int(10) NOT NULL,
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`acc_id`),
  ADD KEY `c_id` (`c_id`);

--
-- Indexes for table `bank_atm`
--
ALTER TABLE `bank_atm`
  ADD PRIMARY KEY (`area`),
  ADD UNIQUE KEY `bid` (`bid`);

--
-- Indexes for table `cards`
--
ALTER TABLE `cards`
  ADD PRIMARY KEY (`card_id`),
  ADD KEY `c_id` (`c_id`),
  ADD KEY `acc_id` (`acc_id`);

--
-- Indexes for table `chats`
--
ALTER TABLE `chats`
  ADD PRIMARY KEY (`chat_id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`cid`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `contact` (`contact`);

--
-- Indexes for table `feedbacks`
--
ALTER TABLE `feedbacks`
  ADD UNIQUE KEY `f_id` (`f_id`);

--
-- Indexes for table `requests`
--
ALTER TABLE `requests`
  ADD PRIMARY KEY (`r_id`),
  ADD KEY `acc_id` (`acc_id`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`t_id`),
  ADD KEY `from_acc` (`from_acc`),
  ADD KEY `to_acc` (`to_acc`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `acc_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `bank_atm`
--
ALTER TABLE `bank_atm`
  MODIFY `bid` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cards`
--
ALTER TABLE `cards`
  MODIFY `card_id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `chats`
--
ALTER TABLE `chats`
  MODIFY `chat_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `cid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT for table `feedbacks`
--
ALTER TABLE `feedbacks`
  MODIFY `f_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `requests`
--
ALTER TABLE `requests`
  MODIFY `r_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `t_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `accounts_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `customers` (`cid`);

--
-- Constraints for table `cards`
--
ALTER TABLE `cards`
  ADD CONSTRAINT `cards_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `customers` (`cid`),
  ADD CONSTRAINT `cards_ibfk_2` FOREIGN KEY (`acc_id`) REFERENCES `accounts` (`acc_id`);

--
-- Constraints for table `requests`
--
ALTER TABLE `requests`
  ADD CONSTRAINT `requests_ibfk_1` FOREIGN KEY (`acc_id`) REFERENCES `accounts` (`acc_id`);

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`from_acc`) REFERENCES `accounts` (`acc_id`),
  ADD CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`to_acc`) REFERENCES `accounts` (`acc_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
