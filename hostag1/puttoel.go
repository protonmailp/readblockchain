package main

import (
	"github.com/olivere/elastic"
	"fmt"
	"context"

)




type Tweet struct {
	User     string                `json:"user"`
	Message  string                `json:"message"`
	Retweets int                   `json:"retweets"`
}


func main(){

	client, err := elastic.NewClient()
	if err != nil {
		// Handle error
		panic(err)
	}

	esversion, err := client.ElasticsearchVersion("http://127.0.0.1:9200")
	if err != nil {
		// Handle error
		panic(err)
	}
	fmt.Printf("Elasticsearch version %s\n", esversion)


	// Index a tweet (using JSON serialization)
	tweet1 := Tweet{User: "olivere", Message: "Take Five", Retweets: 0}
	put1, err := client.Index().
		Index("bitcoin").
		Type("doc").
		Id("1").
		BodyJson(tweet1).
		Do(context.Background())
	if err != nil {
		// Handle error
		panic(err)
	}
	fmt.Printf("Indexed tweet %s to index %s, type %s\n", put1.Id, put1.Index, put1.Type)



	for i:=0;i<1000000000;i++ {

		// Index a tweet (using JSON serialization)
		tweet1 := Tweet{User: "olivere", Message: "Take Five", Retweets: i}
		_, err := client.Index().
			Index("bitcoin").
			Type("doc").
			Id(string(i)).
			BodyJson(tweet1).
			Do(context.Background())
		if err != nil {
			// Handle error
			panic(err)
		}
	//	fmt.Printf("Indexed tweet %s to index %s, type %s\n", put1.Id, put1.Index, put1.Type)





	}



}