package main
import (
	"database/sql"
	"github.com/go-redis/redis"
	"github.com/lib/pq"
	"log"

	"strings"

	"strconv"
)
//DELETE FROM products;
//SELECT * FROM b ORDER BY height DESC
func main() {

	client := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password set
		DB:       0,  // use default DB
	})


	connStr := "dbname=simple_db user=postgres password=12eX12EJwSkTR8twwZbVusHLPYRbobbfpa sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}






	for jj:= 0;jj<10000000;jj++{
		txn, err := db.Begin()
		if err != nil {
			log.Fatal(err)
		}

		stmt, err := txn.Prepare(pq.CopyIn("b", "height", "txid", "hex"))
		if err != nil {
			log.Fatal(err)
		}

		for i := 0; i < 500; i++ {

			val, err := client.RPop("heighttxhex").Result()
			log.Printf("")
			if err != nil {
				panic(err)
			}
			a := strings.Split(val, ":")

			stoi, err := strconv.Atoi(a[0])

			if err != nil {

			}

			_, err = stmt.Exec(stoi, a[1], a[2])
			if err != nil {
				log.Fatal(err)
			}
		}

		_, err = stmt.Exec()
		if err != nil {
			log.Fatal(err)
		}

		err = stmt.Close()
		if err != nil {
			log.Fatal(err)
		}

		err = txn.Commit()
		if err != nil {
			log.Fatal(err)
		}
	}

}

/*
-- Table: public."100000"

-- DROP TABLE public."100000";

CREATE TABLE public."100000"
(
height integer NOT NULL,
txid text COLLATE pg_catalog."default" NOT NULL,
hex text COLLATE pg_catalog."default" NOT NULL,
CONSTRAINT "100000_pkey" PRIMARY KEY (height)
)
WITH (
OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."100000"
OWNER to postgres;
*/