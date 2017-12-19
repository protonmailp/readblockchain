// Copyright (c) 2014-2017 The btcsuite developers
// Use of this source code is governed by an ISC
// license that can be found in the LICENSE file.

package main

import (
	"log"

	"github.com/btcsuite/btcd/rpcclient"
	"fmt"


)

type network struct {
	host string
	totalblock int64
	totaltransactions int64
}

func main() {
	network :=network{"localhost:18332",1200000,300000000}
	// Connect to local bitcoin core RPC server using HTTP POST mode.
	yourrpcuser := "admin"
	yourrpcpass:="admin"
	connCfg := &rpcclient.ConnConfig{
		Host:         network.host,
		User:         yourrpcuser,
		Pass:         yourrpcpass,
		HTTPPostMode: true, // Bitcoin core only supports HTTP POST mode
		DisableTLS:   true, // Bitcoin core does not provide TLS by default
	}
	// Notice the notification parameter is nil since notifications are
	// not supported in HTTP POST mode.
	client, err := rpcclient.New(connCfg, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Shutdown()

    cq :=make(chan int ,1)
	cheight :=make(chan int64,network.totalblock)


	for i:=int64(0);i<network.totalblock ;i++  {
		        cheight<-i

	}

	ctransactions := make(chan string,network.totaltransactions)
	getTxToChan := func(cheight chan int64,ctransactions chan string){
		for {
			height := <-cheight
			blockhash, err := client.GetBlockHash(height)

			if err != nil {
				log.Fatal(err)
			}

			tx, err := client.GetBlockVerbose(blockhash)
			if err != nil {
				log.Fatal(err)
			}
			for _, v := range tx.Tx {
				ctransactions <- v
				fmt.Println(height, v)
			}
			if height > network.totalblock-2 {
				cq <- 1

			}
		}

	}

	go getTxToChan(cheight,ctransactions)
	 go getTxToChan(cheight,ctransactions)
	go getTxToChan(cheight,ctransactions)
	go getTxToChan(cheight,ctransactions)
	go getTxToChan(cheight,ctransactions)
	go getTxToChan(cheight,ctransactions)

	<-cq

	for elem := range ctransactions {
		fmt.Println(elem)
	}


  fmt.Println("ok")

}