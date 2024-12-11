-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 11, 2024 at 05:00 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cesfam_bd`
--
CREATE DATABASE IF NOT EXISTS `cesfam_bd` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `cesfam_bd`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add evento', 7, 'add_evento'),
(26, 'Can change evento', 7, 'change_evento'),
(27, 'Can delete evento', 7, 'delete_evento'),
(28, 'Can view evento', 7, 'view_evento'),
(29, 'Can add oirs', 8, 'add_oirs'),
(30, 'Can change oirs', 8, 'change_oirs'),
(31, 'Can delete oirs', 8, 'delete_oirs'),
(32, 'Can view oirs', 8, 'view_oirs'),
(33, 'Can add trabaja con nosotros', 9, 'add_trabajaconnosotros'),
(34, 'Can change trabaja con nosotros', 9, 'change_trabajaconnosotros'),
(35, 'Can delete trabaja con nosotros', 9, 'delete_trabajaconnosotros'),
(36, 'Can view trabaja con nosotros', 9, 'view_trabajaconnosotros'),
(37, 'Can add noticia', 10, 'add_noticia'),
(38, 'Can change noticia', 10, 'change_noticia'),
(39, 'Can delete noticia', 10, 'delete_noticia'),
(40, 'Can view noticia', 10, 'view_noticia'),
(41, 'Can add captcha store', 11, 'add_captchastore'),
(42, 'Can change captcha store', 11, 'change_captchastore'),
(43, 'Can delete captcha store', 11, 'delete_captchastore'),
(44, 'Can view captcha store', 11, 'view_captchastore');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$jAXz2g816V73ckf2ECIFld$UCMYPePqeqCDzEy5GGsBz84+Rbaz/Z35a6I+2y8jRxo=', '2024-12-11 03:13:21.931634', 1, 'cesfam', '', '', 'cesfam@cesfam.cl', 1, 1, '2024-12-11 03:13:07.954357');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `captcha_captchastore`
--

CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `captcha_captchastore`
--

INSERT INTO `captcha_captchastore` (`id`, `challenge`, `response`, `hashkey`, `expiration`) VALUES
(1, 'GOWK', 'gowk', '1f63cb9b1e897acef613882c9158d1a7790f04b4', '2024-12-11 03:26:49.272028'),
(2, 'XMFK', 'xmfk', 'b06f68a66ee1bc04bccc42ae3cc655753d6c5a8d', '2024-12-11 03:27:45.113076'),
(3, 'ARXI', 'arxi', '7a0faf2375471ac7970039acce0202292f38b345', '2024-12-11 03:27:45.792077'),
(4, 'KIPM', 'kipm', 'ec75d99cba834c4188d88d10fd694f1f79c17096', '2024-12-11 03:27:46.873913'),
(5, 'UVPW', 'uvpw', '5f701d71813d383fcde1d8486238d4bcc1ec74aa', '2024-12-11 03:28:04.013345'),
(6, 'SZOY', 'szoy', '20cf676a30136c0947540daff919a6dff2915d98', '2024-12-11 03:28:04.564261'),
(7, 'XUBN', 'xubn', '20642aa12ea36e4b4366814db5698b34e3713477', '2024-12-11 03:28:05.008513'),
(8, 'NPAI', 'npai', '3ff55ebf9eea5a6e5b99960860af4341dafd1009', '2024-12-11 03:28:05.337776'),
(9, 'VQPI', 'vqpi', '095992138250bf91c5e4a947cf22dbc428311676', '2024-12-11 03:28:05.629980'),
(10, 'FMAJ', 'fmaj', 'b1b3be85d49592303484b9f6d3ad174de985b197', '2024-12-11 03:28:05.867411'),
(11, 'EQAY', 'eqay', '833a8abb5979671a56505fce64e341df25f7f825', '2024-12-11 03:28:06.188224'),
(12, 'RJEM', 'rjem', '1a08254df274817c35c826caa50fd1feaefec312', '2024-12-11 03:28:06.445587'),
(13, 'EBEY', 'ebey', 'd4d3c7bf1d706532757c9890bec1a68ee7168d99', '2024-12-11 03:28:06.700905'),
(14, 'JLRG', 'jlrg', 'df721d98246981a169f2917172cf79322414675f', '2024-12-11 03:28:07.025530'),
(15, 'VGXT', 'vgxt', 'c7c71072dbdd10fed27ebc598d04cd2705259f26', '2024-12-11 03:28:07.286778'),
(16, 'POZZ', 'pozz', 'f05dc32f876ffe936d5f94a04a85ea27041e50ee', '2024-12-11 03:28:07.456850'),
(17, 'LRWM', 'lrwm', 'ff9751ee0342caadaaed01b1a274f5c880f18e08', '2024-12-11 03:28:07.721347'),
(18, 'IKTE', 'ikte', '78aea7ca7391dd63c691610f4bc891e0bee6e7d6', '2024-12-11 03:28:07.917628'),
(19, 'IGXT', 'igxt', '60e99769157c53bf70954232845d1f34a83fdce0', '2024-12-11 03:28:08.117695'),
(20, 'RNTV', 'rntv', '8fb03e2ee3a1d9c8793ce1feb12255c74d48a470', '2024-12-11 03:28:51.860351'),
(21, 'FAVQ', 'favq', 'da3ec6c5c1acafd8aea9a02cc540ee5f2a47c8ad', '2024-12-11 03:30:02.848222'),
(22, 'ZKCV', 'zkcv', '553c4e5a56b81be73c91a7158ec1d65657856d3a', '2024-12-11 03:30:03.077770'),
(23, 'ETLA', 'etla', '85275162ac8baab3af1ac2baae4cd8689477f1bc', '2024-12-11 03:30:03.260376'),
(24, 'PDQO', 'pdqo', 'bdd3b2840b2bb6f8704846a4484994fb133bb6ba', '2024-12-11 03:30:32.276867'),
(25, 'IQVB', 'iqvb', '345416ade21b0c2321f36e314542e6173942b85d', '2024-12-11 03:30:35.762617'),
(26, 'XTNW', 'xtnw', '3b7a1a95493adf240ec0bfa835c26261ba9f66ce', '2024-12-11 03:30:53.832203'),
(27, 'LWWS', 'lwws', '606adb7f28837465a9d518ad1fe448862b4825cc', '2024-12-11 03:35:10.880428'),
(28, 'JBAE', 'jbae', 'bc2a13cbe0570d15f30b03b8d82185963e9cc55b', '2024-12-11 03:35:12.909810'),
(29, 'BNUS', 'bnus', '006055cbcc0506eb3a25c91f00a4da6bdabcc66e', '2024-12-11 03:38:56.869443'),
(30, 'SMJS', 'smjs', 'f2a32cc577f3db488bf0da48f71915decddd3f54', '2024-12-11 03:38:58.606163'),
(31, 'UUJN', 'uujn', '3af33a978d239a8492e295cf86be492c1bc57129', '2024-12-11 03:38:59.544611');

-- --------------------------------------------------------

--
-- Table structure for table `cesfampage_evento`
--

CREATE TABLE `cesfampage_evento` (
  `id` bigint(20) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_termino` date NOT NULL,
  `descripcion` longtext NOT NULL,
  `tipo_evento` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cesfampage_noticia`
--

CREATE TABLE `cesfampage_noticia` (
  `id` bigint(20) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `evento_relacionado_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cesfampage_oirs`
--

CREATE TABLE `cesfampage_oirs` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `motivo` varchar(50) NOT NULL,
  `mensaje` longtext NOT NULL,
  `fecha_envio` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cesfampage_trabajaconnosotros`
--

CREATE TABLE `cesfampage_trabajaconnosotros` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `area_postulacion` varchar(50) NOT NULL,
  `curriculum` varchar(100) DEFAULT NULL,
  `mensaje` longtext NOT NULL,
  `fecha_envio` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(11, 'captcha', 'captchastore'),
(7, 'Cesfampage', 'evento'),
(10, 'Cesfampage', 'noticia'),
(8, 'Cesfampage', 'oirs'),
(9, 'Cesfampage', 'trabajaconnosotros'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Cesfampage', '0001_initial', '2024-12-11 03:12:40.502061'),
(2, 'contenttypes', '0001_initial', '2024-12-11 03:12:40.580633'),
(3, 'auth', '0001_initial', '2024-12-11 03:12:41.333737'),
(4, 'admin', '0001_initial', '2024-12-11 03:12:41.502427'),
(5, 'admin', '0002_logentry_remove_auto_add', '2024-12-11 03:12:41.511603'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2024-12-11 03:12:41.522641'),
(7, 'contenttypes', '0002_remove_content_type_name', '2024-12-11 03:12:41.696700'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-12-11 03:12:41.791486'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-12-11 03:12:41.813172'),
(10, 'auth', '0004_alter_user_username_opts', '2024-12-11 03:12:41.825243'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-12-11 03:12:41.895068'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-12-11 03:12:41.899067'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-12-11 03:12:41.910137'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-12-11 03:12:41.936339'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-12-11 03:12:41.953968'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-12-11 03:12:41.975413'),
(17, 'auth', '0011_update_proxy_permissions', '2024-12-11 03:12:41.990470'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-12-11 03:12:42.010047'),
(19, 'captcha', '0001_initial', '2024-12-11 03:12:42.047908'),
(20, 'captcha', '0002_alter_captchastore_id', '2024-12-11 03:12:42.055132'),
(21, 'sessions', '0001_initial', '2024-12-11 03:12:42.104101');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4hsw4mvhhd7qjwajgu4knz0oquhredw0', '.eJxVjj1TxCAURf-Kk9Zdhs8QKO23s2ce8LJBYxgD2Dj-d8mYwm3vvee89z04aHVxreDuUhzswIbL_8xDeMftKOIbbPdMQt7qnjw5JuRsC7nliOvLuX0QLFCWTk-MCSlwNGaeYJSgRwzS-6j0xEMAJaSfPM4zcmli0D5EDCzwMEfTY9Bd-vfAoc5uzffcqluhVLfjZ8NS-xFOubwyfmXslQqrJis50YIKo54ptZR2SVtr-gD3lUqq8IA8HYi2ghKq2Ej5ifz8Apv5Woo:1tLDs2:6ZqiD5PXNfWbz5y_ylhM7LpEJoSB6umkvZaM9HcGoDY', '2024-12-11 04:28:42.731900');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `captcha_captchastore`
--
ALTER TABLE `captcha_captchastore`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `hashkey` (`hashkey`);

--
-- Indexes for table `cesfampage_evento`
--
ALTER TABLE `cesfampage_evento`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cesfampage_noticia`
--
ALTER TABLE `cesfampage_noticia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Cesfampage_noticia_evento_relacionado_i_f9a3808f_fk_Cesfampag` (`evento_relacionado_id`);

--
-- Indexes for table `cesfampage_oirs`
--
ALTER TABLE `cesfampage_oirs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cesfampage_trabajaconnosotros`
--
ALTER TABLE `cesfampage_trabajaconnosotros`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `captcha_captchastore`
--
ALTER TABLE `captcha_captchastore`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `cesfampage_evento`
--
ALTER TABLE `cesfampage_evento`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cesfampage_noticia`
--
ALTER TABLE `cesfampage_noticia`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cesfampage_oirs`
--
ALTER TABLE `cesfampage_oirs`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cesfampage_trabajaconnosotros`
--
ALTER TABLE `cesfampage_trabajaconnosotros`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `cesfampage_noticia`
--
ALTER TABLE `cesfampage_noticia`
  ADD CONSTRAINT `Cesfampage_noticia_evento_relacionado_i_f9a3808f_fk_Cesfampag` FOREIGN KEY (`evento_relacionado_id`) REFERENCES `cesfampage_evento` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
