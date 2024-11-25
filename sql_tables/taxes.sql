CREATE TABLE taxes (
    taxId SERIAL PRIMARY KEY,
    guestCheckId BIGINT,
    taxNum INT,
    taxRate FLOAT,
    taxCollTtl FLOAT,
    FOREIGN KEY (guestCheckId) REFERENCES guestChecks(guestCheckId)
);
