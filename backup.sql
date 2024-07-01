--
-- PostgreSQL database dump
--

-- Dumped from database version 13.15 (Debian 13.15-1.pgdg120+1)
-- Dumped by pg_dump version 13.15 (Debian 13.15-1.pgdg120+1)

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

--
-- Name: my_schema; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA my_schema;


ALTER SCHEMA my_schema OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: table_count_data; Type: TABLE; Schema: my_schema; Owner: postgres
--

CREATE TABLE my_schema.table_count_data (
    id_count_data integer NOT NULL,
    counter_data bigint NOT NULL,
    date date NOT NULL,
    description text
);


ALTER TABLE my_schema.table_count_data OWNER TO postgres;

--
-- Name: table_count_data_id_count_data_seq; Type: SEQUENCE; Schema: my_schema; Owner: postgres
--

CREATE SEQUENCE my_schema.table_count_data_id_count_data_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE my_schema.table_count_data_id_count_data_seq OWNER TO postgres;

--
-- Name: table_count_data_id_count_data_seq; Type: SEQUENCE OWNED BY; Schema: my_schema; Owner: postgres
--

ALTER SEQUENCE my_schema.table_count_data_id_count_data_seq OWNED BY my_schema.table_count_data.id_count_data;


--
-- Name: table_picture_counter_data; Type: TABLE; Schema: my_schema; Owner: postgres
--

CREATE TABLE my_schema.table_picture_counter_data (
    id_picture integer NOT NULL,
    name_of_picture text NOT NULL,
    id_count_data integer NOT NULL,
    refer_mongo_entry text,
    additional_info text
);


ALTER TABLE my_schema.table_picture_counter_data OWNER TO postgres;

--
-- Name: table_picture_counter_data_id_picture_seq; Type: SEQUENCE; Schema: my_schema; Owner: postgres
--

CREATE SEQUENCE my_schema.table_picture_counter_data_id_picture_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE my_schema.table_picture_counter_data_id_picture_seq OWNER TO postgres;

--
-- Name: table_picture_counter_data_id_picture_seq; Type: SEQUENCE OWNED BY; Schema: my_schema; Owner: postgres
--

ALTER SEQUENCE my_schema.table_picture_counter_data_id_picture_seq OWNED BY my_schema.table_picture_counter_data.id_picture;


--
-- Name: table_count_data id_count_data; Type: DEFAULT; Schema: my_schema; Owner: postgres
--

ALTER TABLE ONLY my_schema.table_count_data ALTER COLUMN id_count_data SET DEFAULT nextval('my_schema.table_count_data_id_count_data_seq'::regclass);


--
-- Name: table_picture_counter_data id_picture; Type: DEFAULT; Schema: my_schema; Owner: postgres
--

ALTER TABLE ONLY my_schema.table_picture_counter_data ALTER COLUMN id_picture SET DEFAULT nextval('my_schema.table_picture_counter_data_id_picture_seq'::regclass);


--
-- Data for Name: table_count_data; Type: TABLE DATA; Schema: my_schema; Owner: postgres
--

COPY my_schema.table_count_data (id_count_data, counter_data, date, description) FROM stdin;
1	326079	2023-02-14	Feb 14 2024
2	331293	2024-03-23	Mar 23 2024
3	334031	2024-04-05	
4	334128	2024-04-06	
5	334434	2024-04-08	
7	336231	2024-04-23	
8	338405	2024-05-08	
9	339243	2024-05-16	
10	339630	2024-05-19	May
41	334939	2024-04-11	restored
42	341775	2024-06-01	June 2024
43	343138	2024-06-11	
\.


--
-- Data for Name: table_picture_counter_data; Type: TABLE DATA; Schema: my_schema; Owner: postgres
--

COPY my_schema.table_picture_counter_data (id_picture, name_of_picture, id_count_data, refer_mongo_entry, additional_info) FROM stdin;
1	picture_001.jpg	1	mongo_entry_123	The fist picture with data lectro counter
23		41		
24		42		
25		43		
\.


--
-- Name: table_count_data_id_count_data_seq; Type: SEQUENCE SET; Schema: my_schema; Owner: postgres
--

SELECT pg_catalog.setval('my_schema.table_count_data_id_count_data_seq', 44, true);


--
-- Name: table_picture_counter_data_id_picture_seq; Type: SEQUENCE SET; Schema: my_schema; Owner: postgres
--

SELECT pg_catalog.setval('my_schema.table_picture_counter_data_id_picture_seq', 26, true);


--
-- Name: table_count_data table_count_data_pkey; Type: CONSTRAINT; Schema: my_schema; Owner: postgres
--

ALTER TABLE ONLY my_schema.table_count_data
    ADD CONSTRAINT table_count_data_pkey PRIMARY KEY (id_count_data);


--
-- Name: table_picture_counter_data table_picture_counter_data_pkey; Type: CONSTRAINT; Schema: my_schema; Owner: postgres
--

ALTER TABLE ONLY my_schema.table_picture_counter_data
    ADD CONSTRAINT table_picture_counter_data_pkey PRIMARY KEY (id_picture);


--
-- Name: table_picture_counter_data table_picture_counter_data_id_count_data_fkey; Type: FK CONSTRAINT; Schema: my_schema; Owner: postgres
--

ALTER TABLE ONLY my_schema.table_picture_counter_data
    ADD CONSTRAINT table_picture_counter_data_id_count_data_fkey FOREIGN KEY (id_count_data) REFERENCES my_schema.table_count_data(id_count_data);


--
-- PostgreSQL database dump complete
--

