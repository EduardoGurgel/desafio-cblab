CREATE TABLE guestChecks (
    guestCheckId BIGINT PRIMARY KEY,
    chkNum INT,
    opnBusDt DATE,
    clsdBusDt DATE,
    clsdFlag BOOLEAN,
    gstCnt INT,
    subTtl FLOAT,
    chkTtl FLOAT,
    payTtl FLOAT
);
