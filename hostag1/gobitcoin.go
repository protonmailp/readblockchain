package main

import (
//"github.com/btcsuite/btcd/chaincfg"
"github.com/btcsuite/btcd/rpcclient"
//"github.com/btcsuite/btcutil"
"log"

)

func main() {









	// create new client instance
	client, err := rpcclient.New(&rpcclient.ConnConfig{
		HTTPPostMode: true,
		DisableTLS:   true,
		Host:         "127.0.0.1:8332",
		User:         "admin",
		Pass:         "admin",
	}, nil)
	if err != nil {
		log.Fatalf("error creating new btc client: %v", err)
	}



	blockhash ,err := client.GetBlockHash(481199)
	if err != nil {

	}
	log.Printf("blockchain : %s",blockhash)


	block ,err :=client.GetBlock(blockhash)


	if err != nil {

	}

	  hashs,err := block.TxHashes()

	  for k,v := range hashs {

	  	log.Printf("%d,%v",k,v.String())

	  	rtv,err :=client.GetRawTransactionVerbose(&v)


	  	if err != nil {

		}
		log.Printf("%v",rtv.Hex)





	  }





	var i int64
	for i=0;i<2;i++ {
		blockhash ,err := client.GetBlockHash(i)
		if err != nil {
			log.Printf("err: %s",err)
		}


		log.Printf("%d blockchain : %s",i,blockhash)




	}


}
