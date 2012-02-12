CREATE TABLE T_GEND_UBIGEO_INB
(
  ID_UBIGEO_INEI  CHAR(6 BYTE),
  POBLACION       NUMBER(10)                    NOT NULL,
  INB             NUMBER(17,16)                 NOT NULL
)
TABLESPACE TS_DATA
PCTUSED    0
PCTFREE    10
INITRANS   1
MAXTRANS   255
STORAGE    (
            INITIAL          128K
            MINEXTENTS       1
            MAXEXTENTS       UNLIMITED
            PCTINCREASE      0
            BUFFER_POOL      DEFAULT
           )
LOGGING 
NOCOMPRESS 
NOCACHE
NOPARALLEL
MONITORING;


CREATE UNIQUE INDEX P_ID_UBIGEO_INEI ON T_GEND_UBIGEO_INB
(ID_UBIGEO_INEI)
LOGGING
TABLESPACE TS_IDX
PCTFREE    10
INITRANS   2
MAXTRANS   255
STORAGE    (
            INITIAL          128K
            MINEXTENTS       1
            MAXEXTENTS       UNLIMITED
            PCTINCREASE      0
            BUFFER_POOL      DEFAULT
           )
NOPARALLEL;


ALTER TABLE T_GEND_UBIGEO_INB ADD (
  CONSTRAINT P_ID_UBIGEO_INEI
 PRIMARY KEY
 (ID_UBIGEO_INEI)
    USING INDEX 
    TABLESPACE TS_IDX
    PCTFREE    10
    INITRANS   2
    MAXTRANS   255
    STORAGE    (
                INITIAL          128K
                MINEXTENTS       1
                MAXEXTENTS       UNLIMITED
                PCTINCREASE      0
               ));

GRANT SELECT ON T_GEND_UBIGEO_INB TO CONSULTA;

GRANT DELETE, INSERT, REFERENCES, SELECT, UPDATE ON T_GEND_UBIGEO_INB TO DESA WITH GRANT OPTION;

GRANT SELECT ON T_GEND_UBIGEO_INB TO R_INACC_CONSULTA;

GRANT DELETE, INSERT, SELECT, UPDATE ON T_GEND_UBIGEO_INB TO R_SIG_EDITOR;

GRANT SELECT ON T_GEND_UBIGEO_INB TO R_SIG_EDITOR_DGAAM;

GRANT SELECT ON T_GEND_UBIGEO_INB TO R_SIG_EDITOR_DGE;

GRANT SELECT ON T_GEND_UBIGEO_INB TO R_SIG_EDITOR_DGH;

GRANT SELECT ON T_GEND_UBIGEO_INB TO R_SIG_EDITOR_DGM;

GRANT SELECT ON T_GEND_UBIGEO_INB TO R_SIMEM_CONSULTA;

GRANT DELETE, INSERT, SELECT, UPDATE ON T_GEND_UBIGEO_INB TO R_SIMEM_MNTO;