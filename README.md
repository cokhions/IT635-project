# IT635-project
CREATE DATABASE fashion_item;
CREATE USER fashion_item WITH PASSWORD 'testing';
GRANT ALL PRIVILEGES ON DATABASE fashion_item to fashion_item;
\c fashion_item

CREATE TABLE manufacturers (
  designer_id INTEGER NOT NULL,
  name            VARCHAR(128) NOT NULL,
  street_address  VARCHAR(256) NOT NULL,
  city            VARCHAR(64) NOT NULL,
  state           VARCHAR(32) NOT NULL,
  zip             VARCHAR(16) NOT NULL,
  phone           VARCHAR(16) NOT NULL,
  PRIMARY KEY     ( designer_id )
);

CREATE TABLE customers (
  customer_id     INTEGER NOT NULL,
  name            VARCHAR(128) NOT NULL,
  street_address  VARCHAR(256) NOT NULL,
  city            VARCHAR(64) NOT NULL,
  state           VARCHAR(32) NOT NULL,
  zip             VARCHAR(16) NOT NULL,
  phone           VARCHAR(16) NOT NULL,
  PRIMARY KEY     ( customer_id )
);

CREATE TABLE parts (
  item_id         INTEGER NOT NULL,
  name            VARCHAR(128) NOT NULL,
  description     TEXT NOT NULL,
  designer_id INTEGER NOT NULL,
  PRIMARY KEY ( item_id ),
  CONSTRAINT fk_manufacturer FOREIGN KEY (designer_id) REFERENCES manufacturers(designer_id)
);

CREATE TABLE orders (
  order_id        INTEGER NOT NULL,
  item_id         INTEGER NOT NULL,
  customer_id     INTEGER NOT NULL,
  quantity        INTEGER NOT NULL,
  PRIMARY KEY ( order_id, customer_id, item_id ),
  CONSTRAINT fk_part FOREIGN KEY (item_id) REFERENCES parts(item_id), 
  CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

GRANT ALL PRIVILEGES ON manufacturers, customers, parts, orders TO fashion_item;
