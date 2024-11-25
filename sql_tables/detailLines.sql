CREATE TABLE detailLines (
    detailLineId SERIAL PRIMARY KEY,
    guestCheckId BIGINT,
    lineNum INT,
    menuItemId INT,
    FOREIGN KEY (guestCheckId) REFERENCES guestChecks(guestCheckId)
);
