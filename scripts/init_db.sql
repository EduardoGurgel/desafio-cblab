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

CREATE TABLE taxes (
    taxId SERIAL PRIMARY KEY,
    guestCheckId BIGINT,
    taxNum INT,
    taxRate FLOAT,
    taxCollTtl FLOAT,
    FOREIGN KEY (guestCheckId) REFERENCES guestChecks(guestCheckId)
);

CREATE TABLE detailLines (
    detailLineId SERIAL PRIMARY KEY,
    guestCheckId BIGINT,
    lineNum INT,
    menuItemId INT,
    FOREIGN KEY (guestCheckId) REFERENCES guestChecks(guestCheckId)
);

CREATE TABLE menuItem (
    menuItemId INT PRIMARY KEY,
    inclTax FLOAT,
    activeTaxes TEXT
);
