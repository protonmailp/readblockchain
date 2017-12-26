package main

import (
	"github.com/syndtr/goleveldb/leveldb"
	"fmt"
)

func main(){




	db, err := leveldb.OpenFile("./height", nil)
	if err != nil{
		fmt.Println(err)
	}
	defer db.Close()



	iter := db.NewIterator(nil, nil)
	for iter.Next() {
		// Remember that the contents of the returned slice should not be modified, and
		// only valid until the next call to Next.
		key := string(iter.Key())
		value := string(iter.Value())
		fmt.Println(key,value)
	}
	iter.Release()
	err = iter.Error()


}
