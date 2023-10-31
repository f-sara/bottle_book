--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Homebrew)
-- Dumped by pg_dump version 15.4

-- Started on 2023-10-31 20:34:59 JST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16390)
-- Name: book_user; Type: TABLE; Schema: public; Owner: book_user
--

CREATE TABLE public.book_user (
    user_id character varying(255) NOT NULL,
    passwd character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    user_shi character varying(255),
    user_mei character varying(255),
    del boolean
);


ALTER TABLE public.book_user OWNER TO book_user;

--
-- TOC entry 3607 (class 0 OID 16390)
-- Dependencies: 214
-- Data for Name: book_user; Type: TABLE DATA; Schema: public; Owner: book_user
--

COPY public.book_user (user_id, passwd, email, user_shi, user_mei, del) FROM stdin;
testtest	1234	test@gmail.com	test	test	f
testtest2	1234	test2@gmail.com	テスト	テスト	f
\.


--
-- TOC entry 3464 (class 2606 OID 16396)
-- Name: book_user book_user_pkey; Type: CONSTRAINT; Schema: public; Owner: book_user
--

ALTER TABLE ONLY public.book_user
    ADD CONSTRAINT book_user_pkey PRIMARY KEY (user_id);


-- Completed on 2023-10-31 20:34:59 JST

--
-- PostgreSQL database dump complete
--

